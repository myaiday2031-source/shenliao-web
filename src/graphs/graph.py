"""
主图编排：基于AI的主动式行业智库平台工作流
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
from graphs.nodes.topic_generation_node import topic_generation_node
from graphs.nodes.deep_analysis_node import deep_analysis_node
from graphs.nodes.report_generation_node import report_generation_node
from graphs.nodes.knowledge_storage_node import knowledge_storage_node


# 创建状态图，指定工作流的入参和出参
builder = StateGraph(GlobalState, input_schema=GraphInput, output_schema=GraphOutput)

# 添加节点
builder.add_node("hotspot_scan", hotspot_scan_node)
builder.add_node("topic_generation", topic_generation_node, 
                 metadata={"type": "agent", "llm_cfg": "config/topic_generation_llm_cfg.json"})
builder.add_node("deep_analysis", deep_analysis_node,
                 metadata={"type": "agent", "llm_cfg": "config/deep_analysis_llm_cfg.json"})
builder.add_node("report_generation", report_generation_node)
builder.add_node("knowledge_storage", knowledge_storage_node)

# 设置入口点
builder.set_entry_point("hotspot_scan")

# 添加边（线性工作流）
builder.add_edge("hotspot_scan", "topic_generation")
builder.add_edge("topic_generation", "deep_analysis")
builder.add_edge("deep_analysis", "report_generation")
builder.add_edge("report_generation", "knowledge_storage")
builder.add_edge("knowledge_storage", END)

# 编译图
main_graph = builder.compile()
