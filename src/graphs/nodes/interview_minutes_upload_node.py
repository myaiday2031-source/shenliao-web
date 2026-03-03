"""
访谈纪要上传节点
"""
import os
from typing import Optional
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from utils.file.file import FileOps
from graphs.state import InterviewMinutesUploadInput, InterviewMinutesUploadOutput


def interview_minutes_upload_node(state: InterviewMinutesUploadInput, config: RunnableConfig, runtime: Runtime[Context]) -> InterviewMinutesUploadOutput:
    """
    title: 访谈纪要上传
    desc: 接收人工上传的访谈纪要文件，提取文本内容
    integrations: 
    """
    ctx = runtime.context
    
    # 如果没有上传访谈纪要，返回空文本
    if state.interview_minutes is None:
        return InterviewMinutesUploadOutput(interview_minutes_text="")
    
    try:
        # 提取文件文本内容
        interview_minutes_text = FileOps.extract_text(state.interview_minutes)
        
        return InterviewMinutesUploadOutput(interview_minutes_text=interview_minutes_text)
    
    except Exception as e:
        # 读取失败时返回空文本
        print(f"读取访谈纪要文件失败: {str(e)}")
        return InterviewMinutesUploadOutput(interview_minutes_text="")
