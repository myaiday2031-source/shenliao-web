"""
状态定义：基于AI的主动式行业智库平台工作流
"""
from typing import List, Dict, Optional
from pydantic import BaseModel, Field


class GlobalState(BaseModel):
    """全局状态定义"""
    # 输入数据
    industry_keyword: str = Field(default="", description="行业关键词或主题")
    
    # 热点扫描结果
    search_results: str = Field(default="", description="热点搜索结果摘要")
    search_details: List[Dict] = Field(default=[], description="搜索结果详情列表")
    
    # 选题生成结果
    topic_suggestions: str = Field(default="", description="AI生成的选题建议（包含多个备选选题）")
    ai_recommended_topic: str = Field(default="", description="AI推荐的选题（供专家参考）")
    expert_confirmed_topic: str = Field(default="", description="专家最终确认的选题（人工输入）")
    expert_review_comment: Optional[str] = Field(default=None, description="专家的审核意见（可选）")
    
    # 专家资源匹配结果
    expert_candidates: List[Dict] = Field(default=[], description="AI匹配的8-10位专家人选列表")
    
    # 客户邀约邮件
    client_invitation_email: str = Field(default="", description="向客户发送的邀约邮件内容")
    
    # 专家沟通表
    expert_communication_table: str = Field(default="", description="与专家的沟通表内容（时间、主题、薪酬等）")
    
    # 深度分析结果
    deep_analysis: str = Field(default="", description="深度分析内容")
    
    # 报告生成结果
    report_url: str = Field(default="", description="生成的报告URL")
    
    # 知识库存储结果
    knowledge_ids: List[str] = Field(default=[], description="存储到知识库的文档ID列表")


class GraphInput(BaseModel):
    """工作流的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题，例如：人工智能、量子计算、新能源汽车等")
    expert_confirmed_topic: Optional[str] = Field(default=None, description="专家最终确认的选题（可选，如果不提供，将使用AI推荐或等待专家输入）")
    expert_review_comment: Optional[str] = Field(default=None, description="专家的审核意见（可选）")


class GraphOutput(BaseModel):
    """工作流的输出"""
    topic_suggestions: str = Field(..., description="AI生成的选题建议")
    deep_analysis: str = Field(..., description="深度分析内容")
    report_url: str = Field(..., description="生成的报告下载URL")


# ==================== 节点1: 热点扫描 ====================
class HotspotScanInput(BaseModel):
    """热点扫描节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")


class HotspotScanOutput(BaseModel):
    """热点扫描节点的输出"""
    search_results: str = Field(..., description="热点搜索结果摘要")
    search_details: List[Dict] = Field(default=[], description="搜索结果详情列表")


# ==================== 节点2: AI选题建议生成 ====================
class TopicSuggestionGenerationInput(BaseModel):
    """AI选题建议生成节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    search_results: str = Field(..., description="热点搜索结果摘要")
    search_details: List[Dict] = Field(default=[], description="搜索结果详情列表")


class TopicSuggestionGenerationOutput(BaseModel):
    """AI选题建议生成节点的输出"""
    topic_suggestions: str = Field(..., description="AI生成的选题建议（包含多个备选选题）")
    ai_recommended_topic: str = Field(..., description="AI推荐的选题（供专家参考）")


# ==================== 节点3: 专家选题确认 ====================
class TopicConfirmationInput(BaseModel):
    """专家选题确认节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    topic_suggestions: str = Field(..., description="AI生成的选题建议")
    ai_recommended_topic: str = Field(..., description="AI推荐的选题")
    # 专家通过GraphInput或人工交互提供的选题
    expert_confirmed_topic: Optional[str] = Field(default=None, description="专家确认的最终选题（如果未提供，使用AI推荐）")
    expert_review_comment: Optional[str] = Field(default=None, description="专家的审核意见（可选）")


class TopicConfirmationOutput(BaseModel):
    """专家选题确认节点的输出"""
    final_topic: str = Field(..., description="最终确定的选题（用于后续深度分析）")
    expert_review_comment: Optional[str] = Field(default=None, description="专家的审核意见")


# ==================== 节点4: 专家资源匹配 ====================
class ExpertMatchingInput(BaseModel):
    """专家资源匹配节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    final_topic: str = Field(..., description="最终确定的选题")
    search_details: List[Dict] = Field(default=[], description="搜索结果详情列表")


class ExpertMatchingOutput(BaseModel):
    """专家资源匹配节点的输出"""
    expert_candidates: List[Dict] = Field(..., description="AI匹配的8-10位专家人选列表")


# ==================== 节点5: 客户邀约邮件生成 ====================
class ClientInvitationInput(BaseModel):
    """客户邀约邮件生成节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    final_topic: str = Field(..., description="最终确定的选题")
    expert_candidates: List[Dict] = Field(..., description="匹配的专家人选列表")


class ClientInvitationOutput(BaseModel):
    """客户邀约邮件生成节点的输出"""
    client_invitation_email: str = Field(..., description="向客户发送的邀约邮件内容")


# ==================== 节点6: 沟通表生成 ====================
class CommunicationTableInput(BaseModel):
    """沟通表生成节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    final_topic: str = Field(..., description="最终确定的选题")
    expert_candidates: List[Dict] = Field(..., description="匹配的专家人选列表")


class CommunicationTableOutput(BaseModel):
    """沟通表生成节点的输出"""
    expert_communication_table: str = Field(..., description="与专家的沟通表内容（时间、主题、薪酬等）")


# ==================== 节点7: 深度分析 ====================
class DeepAnalysisInput(BaseModel):
    """深度分析节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    final_topic: str = Field(..., description="最终确定的选题")
    search_details: List[Dict] = Field(default=[], description="搜索结果详情列表")


class DeepAnalysisOutput(BaseModel):
    """深度分析节点的输出"""
    deep_analysis: str = Field(..., description="深度分析内容")


# ==================== 节点8: 报告生成 ====================
class ReportGenerationInput(BaseModel):
    """报告生成节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    final_topic: str = Field(..., description="最终确定的选题")
    topic_suggestions: str = Field(..., description="AI生成的选题建议")
    deep_analysis: str = Field(..., description="深度分析内容")


class ReportGenerationOutput(BaseModel):
    """报告生成节点的输出"""
    report_url: str = Field(..., description="生成的报告下载URL")


# ==================== 节点9: 知识存储 ====================
class KnowledgeStorageInput(BaseModel):
    """知识存储节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    final_topic: str = Field(..., description="最终确定的选题")
    topic_suggestions: str = Field(..., description="AI生成的选题建议")
    deep_analysis: str = Field(..., description="深度分析内容")
    search_details: List[Dict] = Field(default=[], description="搜索结果详情列表")
    expert_review_comment: Optional[str] = Field(default=None, description="专家的审核意见")


class KnowledgeStorageOutput(BaseModel):
    """知识存储节点的输出"""
    knowledge_ids: List[str] = Field(default=[], description="存储到知识库的文档ID列表")
