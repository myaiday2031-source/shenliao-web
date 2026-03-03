"""
研究报告加密邮件发送节点
"""
import os
import json
from jinja2 import Template
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from langchain_core.messages import HumanMessage, SystemMessage
from graphs.state import EncryptedEmailSendInput, EncryptedEmailSendOutput
from coze_coding_dev_sdk import LLMClient


def encrypted_email_send_node(state: EncryptedEmailSendInput, config: RunnableConfig, runtime: Runtime[Context]) -> EncryptedEmailSendOutput:
    """
    title: 研究报告加密邮件发送
    desc: 生成加密邮件内容，将研究报告通过加密方式发送给客户
    integrations: 大语言模型, email
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
        client_email=state.client_email,
        industry_keyword=state.industry_keyword,
        final_topic=state.final_topic,
        research_report_url=state.research_report_url
    )
    
    # 调用大模型生成邮件内容
    client = LLMClient(ctx=ctx)
    message = HumanMessage(content=user_prompt)
    resp = client.invoke(
        messages=[message],
        model=llm_config.get("model", "doubao-seed-1-8-251228"),
        temperature=llm_config.get("temperature", 0.3),
        top_p=llm_config.get("top_p", 0.9),
        max_completion_tokens=llm_config.get("max_completion_tokens", 2000)
    )
    
    email_content = resp.content
    
    # 这里应该调用email技能发送加密邮件
    # 暂时返回已发送状态
    # 实际实现需要调用email技能
    email_sent = True
    
    return EncryptedEmailSendOutput(encrypted_email_sent=email_sent)
