"""
专家资源匹配节点：使用大语言模型匹配8-10位合适的专家人选
"""
import os
import json
from jinja2 import Template
from typing import List, Dict, Any
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from langchain_core.messages import HumanMessage, SystemMessage
from graphs.state import ExpertMatchingInput, ExpertMatchingOutput
from coze_coding_dev_sdk import LLMClient


def expert_matching_node(state: ExpertMatchingInput, config: RunnableConfig, runtime: Runtime[Context]) -> ExpertMatchingOutput:
    """
    title: 专家资源匹配
    desc: 根据选题和行业关键词，AI配合匹配8-10位合适的专家人选，包括专家姓名、机构、专业领域、研究方向等
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
        
        # 使用jinja2模板渲染提示词
        up_tpl = Template(up)
        user_prompt_content = up_tpl.render({
            "industry_keyword": state.industry_keyword,
            "final_topic": state.final_topic,
            "search_details": state.search_details
        })
        
        # 初始化LLM
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
        
        # 解析专家列表
        ai_matched_experts: List[Dict[str, Any]] = []
        lines = response_text.split('\n')
        
        current_expert: Dict[str, Any] = {}
        for line in lines:
            line = line.strip()
            if not line:
                if current_expert:
                    ai_matched_experts.append(current_expert)
                    current_expert = {}
                continue
            
            # 尝试解析专家信息
            if line.startswith('专家') or line.startswith('姓名') or line.startswith('1.') or line.startswith('2.') or line.startswith('3.') or line.startswith('4.') or line.startswith('5.') or line.startswith('6.') or line.startswith('7.') or line.startswith('8.') or line.startswith('9.') or line.startswith('10.'):
                if current_expert:
                    ai_matched_experts.append(current_expert)
                current_expert = {"姓名": line.split('.')[-1].strip() if '.' in line else line.strip()}
            elif '机构' in line or '单位' in line:
                current_expert['机构'] = line.split('：')[-1].split(':')[-1].strip()
            elif '专业' in line or '领域' in line:
                current_expert['专业领域'] = line.split('：')[-1].split(':')[-1].strip()
            elif '方向' in line or '研究' in line:
                current_expert['研究方向'] = line.split('：')[-1].split(':')[-1].strip()
        
        # 添加最后一个专家
        if current_expert:
            ai_matched_experts.append(current_expert)
        
        # 如果解析失败，使用原始文本作为单个专家
        if not ai_matched_experts:
            ai_matched_experts = [{"姓名": "待定专家", "信息": response_text}]
        
        # 确保最多10位专家
        ai_matched_experts = ai_matched_experts[:10]
        
        return ExpertMatchingOutput(
            ai_matched_experts=ai_matched_experts
        )
        
    except Exception as e:
        raise Exception(f"专家资源匹配失败: {str(e)}")
