"""
主图编排：基于AI的主动式行业智库平台工作流（两阶段模式）
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
from graphs.nodes.manual_expert_import_node import manual_expert_import_node
from graphs.nodes.expert_list_merge_node import expert_list_merge_node
from graphs.nodes.client_invitation_node import client_invitation_node
from graphs.nodes.communication_table_node import communication_table_node
from graphs.nodes.interview_plan_node import interview_plan_node
from graphs.nodes.interview_minutes_upload_node import interview_minutes_upload_node
from graphs.nodes.deep_analysis_node import deep_analysis_node
from graphs.nodes.research_report_node import research_report_node
from graphs.nodes.news_article_node import news_article_node
from graphs.nodes.news_video_generation_node import news_video_generation_node
from graphs.nodes.encrypted_email_send_node import encrypted_email_send_node
from graphs.nodes.news_article_publish_node import news_article_publish_node
from graphs.nodes.news_video_publish_node import news_video_publish_node
from graphs.nodes.knowledge_storage_node import knowledge_storage_node


# 创建状态图，指定工作流的入参和出参
builder = StateGraph(GlobalState, input_schema=GraphInput, output_schema=GraphOutput)

# ==================== 阶段1：访谈准备阶段 ====================
# 添加节点
builder.add_node("hotspot_scan", hotspot_scan_node)
builder.add_node("topic_suggestion_generation", topic_suggestion_generation_node, 
                 metadata={"type": "agent", "llm_cfg": "config/topic_generation_llm_cfg.json"})
builder.add_node("topic_confirmation", topic_confirmation_node)
builder.add_node("expert_matching", expert_matching_node,
                 metadata={"type": "agent", "llm_cfg": "config/expert_matching_llm_cfg.json"})
builder.add_node("manual_expert_import", manual_expert_import_node)
builder.add_node("expert_list_merge", expert_list_merge_node)
builder.add_node("client_invitation", client_invitation_node,
                 metadata={"type": "agent", "llm_cfg": "config/client_invitation_llm_cfg.json"})
builder.add_node("communication_table", communication_table_node,
                 metadata={"type": "agent", "llm_cfg": "config/communication_table_llm_cfg.json"})
builder.add_node("interview_plan", interview_plan_node,
                 metadata={"type": "agent", "llm_cfg": "config/interview_plan_llm_cfg.json"})

# ==================== 阶段2：访谈执行与产出阶段 ====================
# 添加节点
builder.add_node("interview_minutes_upload", interview_minutes_upload_node)
builder.add_node("deep_analysis", deep_analysis_node,
                 metadata={"type": "agent", "llm_cfg": "config/deep_analysis_llm_cfg.json"})
builder.add_node("research_report", research_report_node,
                 metadata={"type": "agent", "llm_cfg": "config/research_report_llm_cfg.json"})
builder.add_node("news_article", news_article_node,
                 metadata={"type": "agent", "llm_cfg": "config/news_article_llm_cfg.json"})
builder.add_node("news_video_generation", news_video_generation_node,
                 metadata={"type": "agent", "llm_cfg": "config/news_video_generation_llm_cfg.json"})
builder.add_node("encrypted_email_send", encrypted_email_send_node,
                 metadata={"type": "agent", "llm_cfg": "config/encrypted_email_send_llm_cfg.json"})
builder.add_node("news_article_publish", news_article_publish_node,
                 metadata={"type": "agent", "llm_cfg": "config/news_article_publish_llm_cfg.json"})
builder.add_node("news_video_publish", news_video_publish_node,
                 metadata={"type": "agent", "llm_cfg": "config/news_video_publish_llm_cfg.json"})
builder.add_node("knowledge_storage", knowledge_storage_node)


# ==================== 设置入口点和边 ====================
# 设置入口点
builder.set_entry_point("hotspot_scan")

# 阶段1的边（线性工作流）
builder.add_edge("hotspot_scan", "topic_suggestion_generation")
builder.add_edge("topic_suggestion_generation", "topic_confirmation")
builder.add_edge("topic_confirmation", "expert_matching")
builder.add_edge("expert_matching", "manual_expert_import")
builder.add_edge("manual_expert_import", "expert_list_merge")
builder.add_edge("expert_list_merge", "client_invitation")
builder.add_edge("client_invitation", "communication_table")
builder.add_edge("communication_table", "interview_plan")

# 阶段1到阶段2的过渡（人工上传访谈纪要后继续）
builder.add_edge("interview_plan", "interview_minutes_upload")

# 阶段2的边
builder.add_edge("interview_minutes_upload", "deep_analysis")

# 并行分支1：研究报告和新闻稿生成
builder.add_edge("deep_analysis", "research_report")
builder.add_edge("deep_analysis", "news_article")

# 并行分支2：新闻稿视频生成（依赖新闻稿）和加密邮件发送（依赖研究报告）
builder.add_edge("news_article", "news_video_generation")

# 并行分支3：发布节点
builder.add_edge("research_report", "encrypted_email_send")
builder.add_edge("news_article", "news_article_publish")
builder.add_edge("news_video_generation", "news_video_publish")

# 汇聚到知识存储节点
builder.add_edge(["encrypted_email_send", "news_article_publish", "news_video_publish"], "knowledge_storage")
builder.add_edge("knowledge_storage", END)

# 编译图
main_graph = builder.compile()
