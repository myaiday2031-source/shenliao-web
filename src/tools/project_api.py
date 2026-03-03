"""
项目管理API接口

提供项目管理相关的API接口，包括：
- 创建项目
- 更新项目状态
- 查询项目列表和详情
- 获取项目进度
- 取消项目
"""
from typing import Optional, List, Dict, Any
from storage.database.supabase_client import get_supabase_client


class ProjectAPI:
    """项目管理API类"""
    
    @staticmethod
    def create_project(
        name: str,
        industry_keyword: str,
        client_email: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        创建新项目
        
        Args:
            name: 项目名称
            industry_keyword: 行业关键词
            client_email: 客户邮箱（可选）
        
        Returns:
            创建的项目信息
        """
        client = get_supabase_client()
        
        project_data = {
            "name": name,
            "industry_keyword": industry_keyword,
            "client_email": client_email,
            "status": "pending",
            "current_stage": None
        }
        
        response = client.table('projects').insert(project_data).execute()
        
        if response.data and len(response.data) > 0:
            return response.data[0]
        else:
            raise Exception("项目创建失败")
    
    @staticmethod
    def get_project(project_id: int) -> Optional[Dict[str, Any]]:
        """
        获取项目详情
        
        Args:
            project_id: 项目ID
        
        Returns:
            项目信息
        """
        client = get_supabase_client()
        
        response = client.table('projects').select('*').eq('id', project_id).execute()
        
        if response.data and len(response.data) > 0:
            return response.data[0]
        else:
            return None
    
    @staticmethod
    def list_projects(
        status: Optional[str] = None,
        current_stage: Optional[str] = None,
        limit: int = 20
    ) -> List[Dict[str, Any]]:
        """
        获取项目列表
        
        Args:
            status: 按状态筛选（可选）
            current_stage: 按阶段筛选（可选）
            limit: 返回数量限制
        
        Returns:
            项目列表
        """
        client = get_supabase_client()
        
        query = client.table('projects')
        
        if status:
            query = query.eq('status', status)
        if current_stage:
            query = query.eq('current_stage', current_stage)
        
        response = query.select('*').order('created_at', desc=True).limit(limit).execute()
        
        return response.data if response.data else []
    
    @staticmethod
    def update_project_status(
        project_id: int,
        status: str,
        current_stage: Optional[str] = None,
        final_topic: Optional[str] = None
    ) -> bool:
        """
        更新项目状态
        
        Args:
            project_id: 项目ID
            status: 新状态
            current_stage: 当前阶段（可选）
            final_topic: 最终选题（可选）
        
        Returns:
            是否更新成功
        """
        client = get_supabase_client()
        
        update_data = {"status": status}
        
        if current_stage is not None:
            update_data["current_stage"] = current_stage
        
        if final_topic is not None:
            update_data["final_topic"] = final_topic
        
        response = client.table('projects').update(update_data).eq('id', project_id).execute()
        
        return response.data is not None
    
    @staticmethod
    def get_project_progress(project_id: int) -> Dict[str, Any]:
        """
        获取项目进度
        
        Args:
            project_id: 项目ID
        
        Returns:
            项目进度信息，包括：
            - project: 项目信息
            - nodes: 各节点的执行状态
            - progress: 进度百分比
        """
        client = get_supabase_client()
        
        # 获取项目信息
        project_response = client.table('projects').select('*').eq('id', project_id).execute()
        if not project_response.data or len(project_response.data) == 0:
            raise Exception("项目不存在")
        
        project = project_response.data[0]
        
        # 获取节点执行记录
        nodes_response = client.table('project_node_executions').select('*').eq('project_id', project_id).execute()
        nodes = nodes_response.data if nodes_response.data else []
        
        # 计算进度
        total_nodes = len(nodes)
        completed_nodes = len([n for n in nodes if n['status'] == 'completed'])
        progress = int((completed_nodes / total_nodes * 100)) if total_nodes > 0 else 0
        
        return {
            "project": project,
            "nodes": nodes,
            "progress": progress
        }
    
    @staticmethod
    def record_node_execution(
        project_id: int,
        node_name: str,
        status: str,
        error_message: Optional[str] = None,
        output_json: Optional[Dict[str, Any]] = None
    ) -> bool:
        """
        记录节点执行状态
        
        Args:
            project_id: 项目ID
            node_name: 节点名称
            status: 节点状态
            error_message: 错误信息（可选）
            output_json: 节点输出（可选）
        
        Returns:
            是否记录成功
        """
        client = get_supabase_client()
        
        node_data = {
            "project_id": project_id,
            "node_name": node_name,
            "status": status,
            "error_message": error_message,
            "output_json": output_json
        }
        
        # 检查是否已存在
        existing_response = client.table('project_node_executions').select('*').eq('project_id', project_id).eq('node_name', node_name).execute()
        
        if existing_response.data and len(existing_response.data) > 0:
            # 更新
            node_id = existing_response.data[0]['id']
            response = client.table('project_node_executions').update(node_data).eq('id', node_id).execute()
        else:
            # 创建
            response = client.table('project_node_executions').insert(node_data).execute()
        
        return response.data is not None
    
    @staticmethod
    def cancel_project(project_id: int) -> bool:
        """
        取消项目
        
        Args:
            project_id: 项目ID
        
        Returns:
            是否取消成功
        """
        return ProjectAPI.update_project_status(project_id, "cancelled")
