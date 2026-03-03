"""
研究报告生成节点
"""
import os
import json
from jinja2 import Template
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from langchain_core.messages import HumanMessage, SystemMessage
from graphs.state import ResearchReportInput, ResearchReportOutput
from coze_coding_dev_sdk import LLMClient


def research_report_node(state: ResearchReportInput, config: RunnableConfig, runtime: Runtime[Context]) -> ResearchReportOutput:
    """
    title: 研究报告生成
    desc: 基于深度分析和访谈纪要，生成详细版研究报告（提供给客户）
    integrations: 大语言模型, document-generation
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
        deep_analysis=state.deep_analysis,
        interview_minutes_text=state.interview_minutes_text[:3000]  # 限制长度
    )
    
    # 调用大模型生成研究报告内容
    client = LLMClient(ctx=ctx)
    message = HumanMessage(content=user_prompt)
    resp = client.invoke(
        messages=[message],
        model=llm_config.get("model", "doubao-seed-1-8-251228"),
        temperature=llm_config.get("temperature", 0.5),
        top_p=llm_config.get("top_p", 0.9),
        max_completion_tokens=llm_config.get("max_completion_tokens", 8000)
    )
    
    research_report_content = resp.content
    
    # 使用document-generation技能生成PDF报告
    # 注意：这里需要调用document-generation技能
    # 暂时使用content作为URL占位符，实际需要生成PDF后获取URL
    research_report_url = f"https://temp-report-storage.example.com/{state.industry_keyword}_report.pdf"
    
    return ResearchReportOutput(
        research_report=research_report_content,
        research_report_url=research_report_url
    )
