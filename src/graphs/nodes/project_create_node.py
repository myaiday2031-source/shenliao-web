"""
项目创建节点
"""
import datetime
from typing import Optional
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from graphs.state import ProjectCreateInput, ProjectCreateOutput
from storage.database.supabase_client import get_supabase_client


def project_create_node(state: ProjectCreateInput, config: RunnableConfig, runtime: Runtime[Context]) -> ProjectCreateOutput:
    """
    title: 项目创建
    desc: 创建新的智库研究项目
    integrations: supabase
    """
    ctx = runtime.context
    
    try:
        # 生成项目名称
        if state.project_name:
            project_name = state.project_name
        else:
            project_name = f"{state.industry_keyword}研究项目-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # 获取数据库客户端
        client = get_supabase_client()
        
        # 创建项目
        project_data = {
            "name": project_name,
            "industry_keyword": state.industry_keyword,
            "status": "pending",
            "current_stage": None
        }
        
        response = client.table('projects').insert(project_data).execute()
        
        if response.data and len(response.data) > 0:
            project_id = response.data[0]['id']
        else:
            raise Exception("项目创建失败")
        
        return ProjectCreateOutput(
            project_id=project_id,
            project_name=project_name
        )
    
    except Exception as e:
        raise Exception(f"项目创建失败: {str(e)}")
