"""
沟通表生成节点：生成与专家沟通的表格（时间、主题、薪酬等）
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
from graphs.state import CommunicationTableInput, CommunicationTableOutput


def communication_table_node(state: CommunicationTableInput, config: RunnableConfig, runtime: Runtime[Context]) -> CommunicationTableOutput:
    """
    title: 沟通表生成
    desc: 生成与专家沟通的表格，包含线下研讨会或一对一交流的时间、主题、薪酬等信息
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
        for idx, expert in enumerate(state.expert_candidates, 1):
            expert_list_text += f"专家{idx}: {expert.get('name', '专家姓名')}"
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
            max_completion_tokens=llm_config.get("max_completion_tokens", 2000)
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
        
        return CommunicationTableOutput(
            expert_communication_table=response_text
        )
        
    except Exception as e:
        raise Exception(f"沟通表生成失败: {str(e)}")
