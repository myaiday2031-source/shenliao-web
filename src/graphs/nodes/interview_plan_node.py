"""
访谈/会议方案生成节点
"""
import os
import json
from jinja2 import Template
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from langchain_core.messages import HumanMessage, SystemMessage
from graphs.state import InterviewPlanInput, InterviewPlanOutput
from coze_coding_dev_sdk import LLMClient


def interview_plan_node(state: InterviewPlanInput, config: RunnableConfig, runtime: Runtime[Context]) -> InterviewPlanOutput:
    """
    title: 访谈/会议方案生成
    desc: 基于选题和专家列表，生成详细的访谈或线下研讨会方案
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
    
    # 准备专家列表摘要（限制长度）
    expert_summary = ""
    if state.final_expert_list:
        expert_count = len(state.final_expert_list)
        expert_summary = f"共匹配到{expert_count}位专家"
        if expert_count > 0:
            expert_summary += f"，例如：{state.final_expert_list[0].get('姓名', '专家1')}（{state.final_expert_list[0].get('机构', '机构名称')}）"
    
    # 渲染用户提示词
    user_prompt = up_tpl.render(
        industry_keyword=state.industry_keyword,
        final_topic=state.final_topic,
        expert_summary=expert_summary,
        expert_count=len(state.final_expert_list)
    )
    
    # 调用大模型
    client = LLMClient(ctx=ctx)
    message = HumanMessage(content=user_prompt)
    resp = client.invoke(
        messages=[message],
        model=llm_config.get("model", "doubao-seed-1-8-251228"),
        temperature=llm_config.get("temperature", 0.7),
        top_p=llm_config.get("top_p", 0.9),
        max_completion_tokens=llm_config.get("max_completion_tokens", 4000)
    )
    
    interview_plan = resp.content
    
    return InterviewPlanOutput(interview_plan=interview_plan)
