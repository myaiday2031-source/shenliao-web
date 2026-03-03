"""
深度分析节点：使用大语言模型对选中的选题进行深度分析
"""
import os
import json
from jinja2 import Template
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from langchain_core.messages import HumanMessage, SystemMessage
from coze_coding_dev_sdk import LLMClient
from graphs.state import DeepAnalysisInput, DeepAnalysisOutput


def deep_analysis_node(state: DeepAnalysisInput, config: RunnableConfig, runtime: Runtime[Context]) -> DeepAnalysisOutput:
    """
    title: 深度分析
    desc: 对选中的核心选题进行深度分析，包括市场分析、技术趋势、竞争格局、发展前景等维度
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
        
        # 整理搜索详情为文本
        search_details_text = ""
        for idx, item in enumerate(state.search_details[:5], 1):
            search_details_text += f"{idx}. {item['title']}\n"
            search_details_text += f"   来源：{item['site_name']}\n"
            search_details_text += f"   摘要：{item['summary']}\n\n"
        
        # 使用jinja2模板渲染提示词
        up_tpl = Template(up)
        user_prompt_content = up_tpl.render({
            "industry_keyword": state.industry_keyword,
            "selected_topic": state.selected_topic,
            "search_details": search_details_text
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
            max_completion_tokens=llm_config.get("max_completion_tokens", 4000)
        )
        
        # 提取响应内容
        response_text = response.content
        if isinstance(response_text, list):
            # 处理多模态响应
            text_parts = []
            for item in response_text:
                if isinstance(item, dict) and item.get("type") == "text":
                    text_parts.append(item.get("text", ""))
            response_text = " ".join(text_parts)
        elif not isinstance(response_text, str):
            response_text = str(response_text)
        
        return DeepAnalysisOutput(
            deep_analysis=response_text
        )
        
    except Exception as e:
        raise Exception(f"深度分析失败: {str(e)}")
