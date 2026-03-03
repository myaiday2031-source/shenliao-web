"""
知识存储节点：使用knowledge技能将内容存储到知识库
"""
from coze_coding_dev_sdk import KnowledgeClient, KnowledgeDocument, DataSourceType
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from graphs.state import KnowledgeStorageInput, KnowledgeStorageOutput


def knowledge_storage_node(state: KnowledgeStorageInput, config: RunnableConfig, runtime: Runtime[Context]) -> KnowledgeStorageOutput:
    """
    title: 知识存储
    desc: 将选题建议和深度分析内容存储到知识库，便于后续检索和复用
    integrations: knowledge
    """
    ctx = runtime.context
    
    try:
        # 初始化知识库客户端
        client = KnowledgeClient(ctx=ctx)
        
        # 准备要存储的文档内容
        # 1. 选题建议文档
        topic_doc = f"""行业：{state.industry_keyword}

选题建议：
{state.topic_suggestions}

最终选题：{state.final_topic}

专家审核意见：{state.expert_review_comment or '无'}
"""
        
        # 2. 深度分析文档
        analysis_doc = f"""行业：{state.industry_keyword}
选题：{state.final_topic}

深度分析内容：
{state.deep_analysis}

专家审核意见：{state.expert_review_comment or '无'}
"""
        
        # 3. 搜索结果文档（如果有）
        search_doc = ""
        if state.search_details:
            search_doc = f"""行业：{state.industry_keyword}

搜索结果摘要：
{state.search_details}
"""
        
        # 创建文档列表
        documents = []
        
        # 添加选题建议文档
        documents.append(KnowledgeDocument(
            source=DataSourceType.TEXT,
            raw_data=topic_doc
        ))
        
        # 添加深度分析文档
        documents.append(KnowledgeDocument(
            source=DataSourceType.TEXT,
            raw_data=analysis_doc
        ))
        
        # 添加搜索结果文档（如果有）
        if search_doc:
            documents.append(KnowledgeDocument(
                source=DataSourceType.TEXT,
                raw_data=search_doc
            ))
        
        # 将文档添加到知识库
        response = client.add_documents(
            documents=documents,
            table_name="coze_doc_knowledge"
        )
        
        # 提取文档ID
        knowledge_ids = []
        if response.code == 0:
            knowledge_ids = response.doc_ids if response.doc_ids else []
        else:
            raise Exception(f"知识库添加失败: {response.msg}")
        
        return KnowledgeStorageOutput(
            knowledge_ids=knowledge_ids
        )
        
    except Exception as e:
        raise Exception(f"知识存储失败: {str(e)}")
