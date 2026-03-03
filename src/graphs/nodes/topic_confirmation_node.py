"""
专家选题确认节点：接收专家最终确认的选题（人机协作）
"""
from typing import Optional
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from graphs.state import TopicConfirmationInput, TopicConfirmationOutput


def topic_confirmation_node(state: TopicConfirmationInput, config: RunnableConfig, runtime: Runtime[Context]) -> TopicConfirmationOutput:
    """
    title: 专家选题确认
    desc: 接收专家最终确认的选题，如果专家未提供，则使用AI推荐的选题。实现人机协作的选题决策流程。
    integrations: 
    """
    ctx = runtime.context
    
    try:
        # 判断专家是否提供了确认的选题
        if state.expert_confirmed_topic and state.expert_confirmed_topic.strip():
            # 专家提供了选题，使用专家的选题
            final_topic = state.expert_confirmed_topic.strip()
            expert_comment = state.expert_review_comment
            
            # 记录日志（可选）
            # ctx.logger.info(f"专家确认选题: {final_topic}")
            
            return TopicConfirmationOutput(
                final_topic=final_topic,
                expert_review_comment=expert_comment
            )
        else:
            # 专家未提供选题，使用AI推荐的选题
            # 可以在这里输出提示，要求专家在下一次运行时提供选题
            final_topic = state.ai_recommended_topic
            expert_comment = state.expert_review_comment or "未提供专家审核意见，使用AI推荐选题"
            
            return TopicConfirmationOutput(
                final_topic=final_topic,
                expert_review_comment=expert_comment
            )
        
    except Exception as e:
        raise Exception(f"专家选题确认失败: {str(e)}")
