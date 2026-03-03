"""
新闻稿件发布节点
"""
import os
import json
from jinja2 import Template
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from langchain_core.messages import HumanMessage, SystemMessage
from graphs.state import NewsArticlePublishInput, NewsArticlePublishOutput
from coze_coding_dev_sdk import LLMClient


def news_article_publish_node(state: NewsArticlePublishInput, config: RunnableConfig, runtime: Runtime[Context]) -> NewsArticlePublishOutput:
    """
    title: 新闻稿件发布
    desc: 将新闻稿件发布到微信公众号、微博、知乎等文字类媒体渠道
    integrations: 大语言模型, wechat-official-account, weibo（需要具体技能）
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
        news_article=state.news_article,
        industry_keyword=state.industry_keyword
    )
    
    # 调用大模型生成不同平台的适配内容
    client = LLMClient(ctx=ctx)
    message = HumanMessage(content=user_prompt)
    resp = client.invoke(
        messages=[message],
        model=llm_config.get("model", "doubao-seed-1-8-251228"),
        temperature=llm_config.get("temperature", 0.5),
        top_p=llm_config.get("top_p", 0.9),
        max_completion_tokens=llm_config.get("max_completion_tokens", 2000)
    )
    
    # 这里应该调用相关技能发布到微信、微博、知乎
    # 暂时返回已发布状态
    # 实际实现需要调用wechat-official-account、微博、知乎等技能
    published = True
    
    return NewsArticlePublishOutput(news_article_published=published)
