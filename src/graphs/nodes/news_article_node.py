"""
新闻稿件生成节点
"""
import os
import json
from jinja2 import Template
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from langchain_core.messages import HumanMessage, SystemMessage
from graphs.state import NewsArticleInput, NewsArticleOutput
from coze_coding_dev_sdk import LLMClient


def news_article_node(state: NewsArticleInput, config: RunnableConfig, runtime: Runtime[Context]) -> NewsArticleOutput:
    """
    title: 新闻稿件生成
    desc: 基于深度分析和访谈纪要，生成简报版新闻稿件（用于新闻宣传）
    integrations: 大语言模型
    """
    ctx = runtime.context
    
    # 读取大模型配置
    cfg_file = os.path.join(os.getenv("COZE_WORKSPACE_PATH"), config['metadata']['llm_cfg'])
    with open(cfg_file, 'r', encoding='utf-8') as fd:
        _cfg = json.load(fd)
    
    llm_config = _cfg.get("config", {})
    sp = _cfg.get("sp", "")
    up_tpl = Template(_cfg.get("up", ""))
    
    # 渲染用户提示词
    user_prompt = up_tpl.render(
        industry_keyword=state.industry_keyword,
        final_topic=state.final_topic,
        deep_analysis=state.deep_analysis[:3000],  # 限制长度
        interview_minutes_text=state.interview_minutes_text[:2000]  # 限制长度
    )
    
    # 调用大模型
    client = LLMClient(ctx=ctx)
    message = HumanMessage(content=user_prompt)
    resp = client.invoke(
        messages=[message],
        model=llm_config.get("model", "doubao-seed-1-8-251228"),
        temperature=llm_config.get("temperature", 0.7),
        top_p=llm_config.get("top_p", 0.9),
        max_completion_tokens=llm_config.get("max_completion_tokens", 3000)
    )
    
    news_article = resp.content
    
    return NewsArticleOutput(news_article=news_article)
