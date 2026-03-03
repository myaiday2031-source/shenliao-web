"""
人工专家导入节点
"""
import os
import pandas as pd
from typing import Optional, List, Dict, Any
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from graphs.state import ManualExpertImportInput, ManualExpertImportOutput


def manual_expert_import_node(state: ManualExpertImportInput, config: RunnableConfig, runtime: Runtime[Context]) -> ManualExpertImportOutput:
    """
    title: 人工专家导入
    desc: 从Excel文件中导入专家列表，与AI推荐的专家合并
    integrations: pandas
    """
    ctx = runtime.context
    
    # 如果没有提供人工导入的专家列表，返回空列表
    if state.manual_expert_list is None:
        return ManualExpertImportOutput(manual_expert_list=[])
    
    try:
        # 下载Excel文件到临时目录
        import tempfile
        from utils.file.file import FileOps
        
        # 获取Excel文件的本地路径或下载
        excel_file_path = state.manual_expert_list.url
        
        # 如果是URL，需要先下载
        if excel_file_path.startswith(("http://", "https://")):
            import requests
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
            response = requests.get(excel_file_path)
            temp_file.write(response.content)
            temp_file.close()
            excel_file_path = temp_file.name
        
        # 读取Excel文件
        df = pd.read_excel(excel_file_path)
        
        # 将DataFrame转换为字典列表
        expert_list: List[Dict[str, Any]] = []
        for _, row in df.iterrows():
            expert: Dict[str, Any] = {}
            for col in df.columns:
                expert[col] = row[col]
            expert_list.append(expert)
        
        # 清理临时文件
        if excel_file_path.startswith("/tmp"):
            import os as os_module
            try:
                os_module.unlink(excel_file_path)
            except:
                pass
        
        return ManualExpertImportOutput(manual_expert_list=expert_list)
    
    except Exception as e:
        # 读取失败时返回空列表，并记录错误
        print(f"读取专家Excel文件失败: {str(e)}")
        return ManualExpertImportOutput(manual_expert_list=[])
