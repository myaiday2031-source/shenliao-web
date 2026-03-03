"""
AI选题建议生成节点：使用大语言模型分析搜索结果，生成选题建议（不做最终决策）
"""
import os
import json
from jinja2 import Template
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from langchain_core.messages import HumanMessage, SystemMessage
from coze_coding_dev_sdk import LLMClient
from graphs.state import TopicSuggestionGenerationInput, TopicSuggestionGenerationOutput


def topic_suggestion_generation_node(state: TopicSuggestionGenerationInput, config: RunnableConfig, runtime: Runtime[Context]) -> TopicSuggestionGenerationOutput:
    """
    title: AI选题建议生成
    desc: 基于热点扫描结果，使用大语言模型生成高质量的选题建议（包含多个备选选题），供专家参考和选择
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
            "search_results": state.search_results,
            "search_details": state.search_details
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
            # 处理多模态响应
            text_parts = []
            for item in response_text:
                if isinstance(item, dict) and item.get("type") == "text":
                    text_parts.append(item.get("text", ""))
            response_text = " ".join(text_parts)
        elif not isinstance(response_text, str):
            response_text = str(response_text)
        
        # 解析响应，提取AI推荐的选题
        # 假设推荐选题以"推荐选题"或"核心选题"开头
        lines = response_text.split('\n')
        ai_recommended_topic = ""
        
        # 尝试找到推荐选题
        for line in lines:
            if "推荐选题" in line or "核心选题" in line or "主选题" in line:
                # 提取选题内容
                topic_text = line.split("：")[-1].split(":")[-1].strip()
                if topic_text and not topic_text.startswith('**'):
                    ai_recommended_topic = topic_text
                elif topic_text.startswith('**'):
                    ai_recommended_topic = topic_text.replace('**', '').strip()
                break
        
        # 如果没有找到明确的核心选题，使用第一个非标题的文本
        if not ai_recommended_topic and lines:
            for line in lines:
                if line.strip() and not line.startswith('#') and not line.startswith('-'):
                    # 移除可能的markdown格式
                    cleaned_line = line.strip()
                    if cleaned_line.startswith('**'):
                        cleaned_line = cleaned_line.replace('**', '').strip()
                    ai_recommended_topic = cleaned_line
                    break
        
        # 如果还是没有，使用行业关键词作为默认
        if not ai_recommended_topic:
            ai_recommended_topic = f"{state.industry_keyword}行业深度研究"
        
        return TopicSuggestionGenerationOutput(
            topic_suggestions=response_text,
            ai_recommended_topic=ai_recommended_topic
        )
        
    except Exception as e:
        raise Exception(f"AI选题建议生成失败: {str(e)}")
