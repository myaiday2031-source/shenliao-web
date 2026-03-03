"""
客户邀约邮件生成节点：生成向客户发送的邀约邮件
"""
import os
import json
from jinja2 import Template
from typing import List, Dict
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from langchain_core.messages import HumanMessage, SystemMessage
from coze_coding_dev_sdk import LLMClient
from graphs.state import ClientInvitationInput, ClientInvitationOutput


def client_invitation_node(state: ClientInvitationInput, config: RunnableConfig, runtime: Runtime[Context]) -> ClientInvitationOutput:
    """
    title: 客户邀约邮件生成
    desc: 生成向客户发送的邀约邮件，邀请客户参加线下研讨会或一对一交流，询问购买意愿和重点关注的专家/话题
    integrations: 大语言模型
    """
    ctx = runtime.context
    
    try:
        # 读取模型配置文件
        cfg_file = os.path.join(os.getenv("COZE_WORKSPACE_PATH"), config['metadata']['llm_cfg'])
        with open(cfg_file, 'r', encoding='utf-8') as fd:
            _cfg = json.load(fd)
        
        llm_config = _cfg.get("config", {})
        sp = _cfg.get("sp", "")
        up = _cfg.get("up", "")
        
        # 整理专家列表为文本
        expert_list_text = ""
        for idx, expert in enumerate(state.expert_candidates[:5], 1):
            expert_list_text += f"{idx}. {expert.get('name', '专家姓名')}"
            if expert.get('institution'):
                expert_list_text += f" - {expert['institution']}"
            if expert.get('specialty'):
                expert_list_text += f"（{expert['specialty']}）"
            expert_list_text += "\n"
        
        # 使用jinja2模板渲染提示词
        up_tpl = Template(up)
        user_prompt_content = up_tpl.render({
            "industry_keyword": state.industry_keyword,
            "final_topic": state.final_topic,
            "expert_list_text": expert_list_text,
            "expert_count": len(state.expert_candidates)
        })
        
        # 初始化LLM客户端
        client = LLMClient(ctx=ctx)
        
        # 构建消息
        messages = [
            SystemMessage(content=sp),
            HumanMessage(content=user_prompt_content)
        ]
        
        # 调用大模型
        response = client.invoke(
            messages=messages,
            model=llm_config.get("model", "doubao-seed-1-8-251228"),
            temperature=llm_config.get("temperature", 0.7),
            top_p=llm_config.get("top_p", 0.7),
            max_completion_tokens=llm_config.get("max_completion_tokens", 1500)
        )
        
        # 提取响应内容
        response_text = response.content
        if isinstance(response_text, list):
            text_parts = []
            for item in response_text:
                if isinstance(item, dict) and item.get("type") == "text":
                    text_parts.append(item.get("text", ""))
            response_text = " ".join(text_parts)
        elif not isinstance(response_text, str):
            response_text = str(response_text)
        
        return ClientInvitationOutput(
            client_invitation_email=response_text
        )
        
    except Exception as e:
        raise Exception(f"客户邀约邮件生成失败: {str(e)}")
