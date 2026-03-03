"""
项目查询节点
"""
from typing import Optional
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from graphs.state import ProjectQueryInput, ProjectQueryOutput
from storage.database.supabase_client import get_supabase_client


def project_query_node(state: ProjectQueryInput, config: RunnableConfig, runtime: Runtime[Context]) -> ProjectQueryOutput:
    """
    title: 项目查询
    desc: 查询项目列表和详情
    integrations: supabase
    """
    ctx = runtime.context
    
    try:
        # 获取数据库客户端
        client = get_supabase_client()
        
        # 构建查询
        query = client.table('projects')
        
        if state.project_id:
            # 查询单个项目
            response = query.select('*').eq('id', state.project_id).execute()
            projects = response.data if response.data else []
            total = len(projects)
        else:
            # 查询项目列表
            if state.status:
                query = query.eq('status', state.status)
            if state.current_stage:
                query = query.eq('current_stage', state.current_stage)
            
            response = query.select('*').order('created_at', desc=True).limit(state.limit).execute()
            projects = response.data if response.data else []
            total = len(projects)
        
        return ProjectQueryOutput(
            projects=projects,
            total=total
        )
    
    except Exception as e:
        raise Exception(f"项目查询失败: {str(e)}")
