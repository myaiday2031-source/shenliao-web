"""
项目状态更新节点
"""
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from graphs.state import ProjectUpdateStatusInput, ProjectUpdateStatusOutput
from storage.database.supabase_client import get_supabase_client


def project_update_status_node(state: ProjectUpdateStatusInput, config: RunnableConfig, runtime: Runtime[Context]) -> ProjectUpdateStatusOutput:
    """
    title: 项目状态更新
    desc: 更新项目的状态和相关信息
    integrations: supabase
    """
    ctx = runtime.context
    
    try:
        # 获取数据库客户端
        client = get_supabase_client()
        
        # 构建更新数据
        update_data = {
            "status": state.status
        }
        
        if state.current_stage is not None:
            update_data["current_stage"] = state.current_stage
        
        if state.final_topic is not None:
            update_data["final_topic"] = state.final_topic
        
        # 更新项目状态
        response = client.table('projects').update(update_data).eq('id', state.project_id).execute()
        
        success = response.data is not None
        
        return ProjectUpdateStatusOutput(success=success)
    
    except Exception as e:
        raise Exception(f"项目状态更新失败: {str(e)}")
