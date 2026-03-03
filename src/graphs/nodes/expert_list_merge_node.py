"""
专家列表合并节点
"""
from typing import List, Dict, Any
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from graphs.state import ExpertListMergeInput, ExpertListMergeOutput


def expert_list_merge_node(state: ExpertListMergeInput, config: RunnableConfig, runtime: Runtime[Context]) -> ExpertListMergeOutput:
    """
    title: 专家列表合并
    desc: 将AI匹配的专家列表和人工导入的专家列表合并，去重后形成最终的专家列表
    integrations: 
    """
    ctx = runtime.context
    
    # 合并两个专家列表
    final_expert_list: List[Dict[str, Any]] = []
    
    # 添加AI匹配的专家
    final_expert_list.extend(state.ai_matched_experts)
    
    # 添加人工导入的专家
    if state.manual_expert_list:
        final_expert_list.extend(state.manual_expert_list)
    
    # 去重（基于姓名）
    unique_experts: List[Dict[str, Any]] = []
    seen_names = set()
    
    for expert in final_expert_list:
        name = expert.get('姓名', expert.get('name', ''))
        if name and name not in seen_names:
            seen_names.add(name)
            unique_experts.append(expert)
        elif not name:
            # 如果没有姓名，直接添加
            unique_experts.append(expert)
    
    return ExpertListMergeOutput(final_expert_list=unique_experts)
