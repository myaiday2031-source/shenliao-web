"""
主图编排：基于AI的主动式行业智库平台工作流（支持人机协作）
"""
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from graphs.state import (
    GlobalState,
    GraphInput,
    GraphOutput
)

# 导入所有节点函数
from graphs.nodes.hotspot_scan_node import hotspot_scan_node
from graphs.nodes.topic_suggestion_generation_node import topic_suggestion_generation_node
from graphs.nodes.topic_confirmation_node import topic_confirmation_node
from graphs.nodes.expert_matching_node import expert_matching_node
from graphs.nodes.client_invitation_node import client_invitation_node
from graphs.nodes.communication_table_node import communication_table_node
from graphs.nodes.deep_analysis_node import deep_analysis_node
from graphs.nodes.report_generation_node import report_generation_node
from graphs.nodes.knowledge_storage_node import knowledge_storage_node


# 创建状态图，指定工作流的入参和出参
builder = StateGraph(GlobalState, input_schema=GraphInput, output_schema=GraphOutput)

# 添加节点
builder.add_node("hotspot_scan", hotspot_scan_node)
builder.add_node("topic_suggestion_generation", topic_suggestion_generation_node, 
                 metadata={"type": "agent", "llm_cfg": "config/topic_generation_llm_cfg.json"})
builder.add_node("topic_confirmation", topic_confirmation_node)
builder.add_node("expert_matching", expert_matching_node,
                 metadata={"type": "agent", "llm_cfg": "config/expert_matching_llm_cfg.json"})
builder.add_node("client_invitation", client_invitation_node,
                 metadata={"type": "agent", "llm_cfg": "config/client_invitation_llm_cfg.json"})
builder.add_node("communication_table", communication_table_node,
                 metadata={"type": "agent", "llm_cfg": "config/communication_table_llm_cfg.json"})
builder.add_node("deep_analysis", deep_analysis_node,
                 metadata={"type": "agent", "llm_cfg": "config/deep_analysis_llm_cfg.json"})
builder.add_node("report_generation", report_generation_node)
builder.add_node("knowledge_storage", knowledge_storage_node)

# 设置入口点
builder.set_entry_point("hotspot_scan")

# 添加边（线性工作流）
builder.add_edge("hotspot_scan", "topic_suggestion_generation")
builder.add_edge("topic_suggestion_generation", "topic_confirmation")
builder.add_edge("topic_confirmation", "expert_matching")
builder.add_edge("expert_matching", "client_invitation")
builder.add_edge("client_invitation", "communication_table")
builder.add_edge("communication_table", "deep_analysis")
builder.add_edge("deep_analysis", "report_generation")
builder.add_edge("report_generation", "knowledge_storage")
builder.add_edge("knowledge_storage", END)

# 编译图
main_graph = builder.compile()
