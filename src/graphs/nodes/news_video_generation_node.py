"""
新闻稿视频生成节点
"""
import os
import json
from jinja2 import Template
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from langchain_core.messages import HumanMessage, SystemMessage
from graphs.state import NewsVideoGenerationInput, NewsVideoGenerationOutput
from coze_coding_dev_sdk import LLMClient


def news_video_generation_node(state: NewsVideoGenerationInput, config: RunnableConfig, runtime: Runtime[Context]) -> NewsVideoGenerationOutput:
    """
    title: 新闻稿视频生成
    desc: 基于新闻稿件内容，生成短视频内容（用于抖音、视频号等视频平台）
    integrations: 大语言模型, video-generation
    """
    ctx = runtime.context
    
    # 读取大模型配置
    cfg_file = os.path.join(os.getenv("COZE_WORKSPACE_PATH"), config['metadata']['llm_cfg'])
    with open(cfg_file, 'r', encoding='utf-8') as fd:
        _cfg = json.load(fd)
    
    llm_config = _cfg.get("config", {})
    sp = _cfg.get("sp", "")
    up_tpl = Template(_cfg.get("up", ""))
    
    # 渲染用户提示词，提取新闻稿的核心内容生成视频脚本
    user_prompt = up_tpl.render(
        news_article=state.news_article
    )
    
    # 调用大模型生成视频脚本
    client = LLMClient(ctx=ctx)
    message = HumanMessage(content=user_prompt)
    resp = client.invoke(
        messages=[message],
        model=llm_config.get("model", "doubao-seed-1-8-251228"),
        temperature=llm_config.get("temperature", 0.7),
        top_p=llm_config.get("top_p", 0.9),
        max_completion_tokens=llm_config.get("max_completion_tokens", 2000)
    )
    
    video_script = resp.content
    
    # 这里应该调用video-generation技能生成视频
    # 暂时使用脚本内容作为URL占位符
    # 实际实现需要调用video-generation技能
    video_url = f"https://temp-video-storage.example.com/news_video_{os.urandom(8).hex()}.mp4"
    
    return NewsVideoGenerationOutput(news_video_url=video_url)
