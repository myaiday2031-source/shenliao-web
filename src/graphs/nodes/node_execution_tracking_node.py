"""
节点执行追踪节点
"""
from typing import Optional
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from graphs.state import NodeExecutionTrackingInput, NodeExecutionTrackingOutput
from storage.database.supabase_client import get_supabase_client


def node_execution_tracking_node(state: NodeExecutionTrackingInput, config: RunnableConfig, runtime: Runtime[Context]) -> NodeExecutionTrackingOutput:
    """
    title: 节点执行追踪
    desc: 记录节点执行状态和输出
    integrations: supabase
    """
    ctx = runtime.context
    
    try:
        # 获取数据库客户端
        client = get_supabase_client()
        
        # 构建节点执行记录数据
        node_data = {
            "project_id": state.project_id,
            "node_name": state.node_name,
            "status": state.status,
            "error_message": state.error_message,
            "output_json": state.output_json
        }
        
        # 检查是否已存在该节点的执行记录
        existing_response = client.table('project_node_executions').select('*').eq('project_id', state.project_id).eq('node_name', state.node_name).execute()
        
        if existing_response.data and len(existing_response.data) > 0:
            # 更新现有记录
            node_id = existing_response.data[0]['id']
            response = client.table('project_node_executions').update(node_data).eq('id', node_id).execute()
        else:
            # 创建新记录
            response = client.table('project_node_executions').insert(node_data).execute()
        
        success = response.data is not None
        
        return NodeExecutionTrackingOutput(success=success)
    
    except Exception as e:
        raise Exception(f"节点执行追踪失败: {str(e)}")
