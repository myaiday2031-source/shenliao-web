"""
状态定义：基于AI的主动式行业智库平台工作流
"""
from typing import List, Dict, Optional
from pydantic import BaseModel, Field
from utils.file.file import File


class GlobalState(BaseModel):
    """全局状态定义"""
    # 输入数据
    industry_keyword: str = Field(default="", description="行业关键词或主题")
    client_email: str = Field(default="", description="客户邮箱地址")
    
    # 热点扫描结果
    search_results: str = Field(default="", description="热点搜索结果摘要")
    search_details: List[Dict] = Field(default=[], description="搜索结果详情列表")
    
    # 选题生成结果
    topic_suggestions: str = Field(default="", description="AI生成的选题建议（包含多个备选选题）")
    ai_recommended_topic: str = Field(default="", description="AI推荐的选题（供专家参考）")
    expert_confirmed_topic: str = Field(default="", description="专家最终确认的选题（人工输入）")
    expert_review_comment: Optional[str] = Field(default=None, description="专家的审核意见（可选）")
    
    # 专家资源匹配结果
    ai_matched_experts: List[Dict] = Field(default=[], description="AI匹配的8-10位专家人选列表")
    manual_expert_list: List[Dict] = Field(default=[], description="人工导入的专家列表")
    final_expert_list: List[Dict] = Field(default=[], description="最终确定的专家列表（AI匹配+人工导入）")
    
    # 客户邀约邮件
    client_invitation_email: str = Field(default="", description="向客户发送的邀约邮件内容")
    
    # 专家沟通表
    expert_communication_table: str = Field(default="", description="与专家的沟通表内容（时间、主题、薪酬等）")
    
    # 访谈/会议方案
    interview_plan: str = Field(default="", description="访谈/会议方案")
    
    # 访谈纪要
    interview_minutes: Optional[File] = Field(default=None, description="访谈纪要文件（人工上传）")
    interview_minutes_text: str = Field(default="", description="访谈纪要文本内容")
    
    # 深度分析结果
    deep_analysis: str = Field(default="", description="深度分析内容")
    
    # 双产出物
    research_report: str = Field(default="", description="详细版研究报告内容")
    research_report_url: str = Field(default="", description="研究报告PDF下载URL")
    news_article: str = Field(default="", description="简报版新闻稿件内容")
    news_video: Optional[File] = Field(default=None, description="新闻稿视频文件")
    news_video_url: str = Field(default="", description="新闻稿视频URL")
    
    # 分发状态
    encrypted_email_sent: bool = Field(default=False, description="研究报告加密邮件是否已发送")
    news_article_published: bool = Field(default=False, description="新闻稿件是否已发布（微信、微博、知乎）")
    news_video_published: bool = Field(default=False, description="新闻稿视频是否已发布（抖音、视频号）")
    
    # 知识库存储结果
    knowledge_ids: List[str] = Field(default=[], description="存储到知识库的文档ID列表")


class GraphInput(BaseModel):
    """工作流的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题，例如：人工智能、量子计算、新能源汽车等")
    client_email: Optional[str] = Field(default=None, description="客户邮箱地址（用于发送研究报告）")
    expert_confirmed_topic: Optional[str] = Field(default=None, description="专家最终确认的选题（可选，如果不提供，将使用AI推荐或等待专家输入）")
    expert_review_comment: Optional[str] = Field(default=None, description="专家的审核意见（可选）")
    manual_expert_list: Optional[File] = Field(default=None, description="人工导入的专家列表（Excel格式，可选）")
    interview_minutes: Optional[File] = Field(default=None, description="访谈纪要文件（人工上传，可选，两阶段模式中使用）")
    
    # 项目管理相关
    project_name: Optional[str] = Field(default=None, description="项目名称（可选，如果不提供将自动生成）")
    project_id: Optional[int] = Field(default=None, description="项目ID（用于继续执行已存在的项目）")


class GraphOutput(BaseModel):
    """工作流的输出"""
    topic_suggestions: str = Field(..., description="AI生成的选题建议")
    interview_plan: str = Field(default="", description="访谈/会议方案（阶段1输出）")
    deep_analysis: str = Field(..., description="深度分析内容")
    research_report_url: str = Field(..., description="详细版研究报告下载URL")
    news_article: str = Field(..., description="简报版新闻稿件内容")
    news_video_url: str = Field(default="", description="新闻稿视频URL")
    encrypted_email_sent: bool = Field(default=False, description="研究报告加密邮件是否已发送")
    news_article_published: bool = Field(default=False, description="新闻稿件是否已发布")
    news_video_published: bool = Field(default=False, description="新闻稿视频是否已发布")


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


# ==================== 节点5: 客户邀约邮件生成（更新） ====================
class ClientInvitationInput(BaseModel):
    """客户邀约邮件生成节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    final_topic: str = Field(..., description="最终确定的选题")
    final_expert_list: List[Dict] = Field(..., description="最终确定的专家列表")


class ClientInvitationOutput(BaseModel):
    """客户邀约邮件生成节点的输出"""
    client_invitation_email: str = Field(..., description="向客户发送的邀约邮件内容")


class KnowledgeStorageInput(BaseModel):
    """知识存储节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    final_topic: str = Field(..., description="最终确定的选题")
    topic_suggestions: str = Field(..., description="AI生成的选题建议")
    deep_analysis: str = Field(..., description="深度分析内容")
    search_details: List[Dict] = Field(default=[], description="搜索结果详情列表")
    expert_review_comment: Optional[str] = Field(default=None, description="专家的审核意见")
    interview_plan: str = Field(default="", description="访谈/会议方案")
    interview_minutes_text: str = Field(default="", description="访谈纪要文本内容")
    research_report: str = Field(default="", description="详细版研究报告内容")
    news_article: str = Field(default="", description="简报版新闻稿件内容")


class KnowledgeStorageOutput(BaseModel):
    """知识存储节点的输出"""
    knowledge_ids: List[str] = Field(default=[], description="存储到知识库的文档ID列表")


# ==================== 节点4-1: 人工专家导入 ====================
class ManualExpertImportInput(BaseModel):
    """人工专家导入节点的输入"""
    manual_expert_list: Optional[File] = Field(default=None, description="人工导入的专家列表（Excel格式）")


class ManualExpertImportOutput(BaseModel):
    """人工专家导入节点的输出"""
    manual_expert_list: List[Dict] = Field(default=[], description="解析出的专家列表")


# ==================== 节点7: 专家沟通表 ====================
class CommunicationTableInput(BaseModel):
    """沟通表生成节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    final_topic: str = Field(..., description="最终确定的选题")
    final_expert_list: List[Dict] = Field(..., description="最终确定的专家列表")


class CommunicationTableOutput(BaseModel):
    """沟通表生成节点的输出"""
    expert_communication_table: str = Field(..., description="与专家的沟通表内容（时间、主题、薪酬等）")


# ==================== 节点8: 访谈/会议方案生成 ====================
class InterviewPlanInput(BaseModel):
    """访谈/会议方案生成节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    final_topic: str = Field(..., description="最终确定的选题")
    final_expert_list: List[Dict] = Field(..., description="最终确定的专家列表")
    expert_communication_table: str = Field(..., description="与专家的沟通表内容")


class InterviewPlanOutput(BaseModel):
    """访谈/会议方案生成节点的输出"""
    interview_plan: str = Field(..., description="访谈/会议方案")


# ==================== 节点9: 访谈纪要上传 ====================
class InterviewMinutesUploadInput(BaseModel):
    """访谈纪要上传节点的输入"""
    interview_minutes: Optional[File] = Field(default=None, description="访谈纪要文件（人工上传）")


class InterviewMinutesUploadOutput(BaseModel):
    """访谈纪要上传节点的输出"""
    interview_minutes_text: str = Field(..., description="访谈纪要文本内容")


# ==================== 节点10: 深度分析 ====================
class DeepAnalysisInput(BaseModel):
    """深度分析节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    final_topic: str = Field(..., description="最终确定的选题")
    search_details: List[Dict] = Field(default=[], description="搜索结果详情列表")
    interview_minutes_text: str = Field(..., description="访谈纪要文本内容")


class DeepAnalysisOutput(BaseModel):
    """深度分析节点的输出"""
    deep_analysis: str = Field(..., description="深度分析内容")


# ==================== 节点11-1: 研究报告生成 ====================
class ResearchReportInput(BaseModel):
    """研究报告生成节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    final_topic: str = Field(..., description="最终确定的选题")
    topic_suggestions: str = Field(..., description="AI生成的选题建议")
    deep_analysis: str = Field(..., description="深度分析内容")
    interview_minutes_text: str = Field(..., description="访谈纪要文本内容")


class ResearchReportOutput(BaseModel):
    """研究报告生成节点的输出"""
    research_report: str = Field(..., description="详细版研究报告内容")
    research_report_url: str = Field(..., description="研究报告PDF下载URL")


# ==================== 节点11-2: 新闻稿件生成 ====================
class NewsArticleInput(BaseModel):
    """新闻稿件生成节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    final_topic: str = Field(..., description="最终确定的选题")
    deep_analysis: str = Field(..., description="深度分析内容")
    interview_minutes_text: str = Field(..., description="访谈纪要文本内容")


class NewsArticleOutput(BaseModel):
    """新闻稿件生成节点的输出"""
    news_article: str = Field(..., description="简报版新闻稿件内容")


# ==================== 节点12-2: 新闻稿视频生成 ====================
class NewsVideoGenerationInput(BaseModel):
    """新闻稿视频生成节点的输入"""
    news_article: str = Field(..., description="新闻稿件内容")


class NewsVideoGenerationOutput(BaseModel):
    """新闻稿视频生成节点的输出"""
    news_video_url: str = Field(..., description="新闻稿视频URL")


# ==================== 节点13-1: 研究报告加密邮件发送 ====================
class EncryptedEmailSendInput(BaseModel):
    """研究报告加密邮件发送节点的输入"""
    client_email: str = Field(..., description="客户邮箱地址")
    industry_keyword: str = Field(..., description="行业关键词或主题")
    final_topic: str = Field(..., description="最终确定的选题")
    research_report_url: str = Field(..., description="研究报告PDF下载URL")


class EncryptedEmailSendOutput(BaseModel):
    """研究报告加密邮件发送节点的输出"""
    encrypted_email_sent: bool = Field(..., description="研究报告加密邮件是否已发送")


# ==================== 节点13-2: 新闻稿件发布 ====================
class NewsArticlePublishInput(BaseModel):
    """新闻稿件发布节点的输入"""
    news_article: str = Field(..., description="新闻稿件内容")
    industry_keyword: str = Field(..., description="行业关键词或主题")


class NewsArticlePublishOutput(BaseModel):
    """新闻稿件发布节点的输出"""
    news_article_published: bool = Field(..., description="新闻稿件是否已发布（微信、微博、知乎）")


# ==================== 节点13-3: 新闻稿视频发布 ====================
class NewsVideoPublishInput(BaseModel):
    """新闻稿视频发布节点的输入"""
    news_video_url: str = Field(..., description="新闻稿视频URL")
    industry_keyword: str = Field(..., description="行业关键词或主题")


class NewsVideoPublishOutput(BaseModel):
    """新闻稿视频发布节点的输出"""
    news_video_published: bool = Field(..., description="新闻稿视频是否已发布（抖音、视频号）")


# ==================== 节点4: 专家资源匹配（更新） ====================
class ExpertMatchingInput(BaseModel):
    """专家资源匹配节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    final_topic: str = Field(..., description="最终确定的选题")
    search_details: List[Dict] = Field(default=[], description="搜索结果详情列表")


class ExpertMatchingOutput(BaseModel):
    """专家资源匹配节点的输出"""
    ai_matched_experts: List[Dict] = Field(..., description="AI匹配的8-10位专家人选列表")


# ==================== 节点4-2: 专家列表合并 ====================
class ExpertListMergeInput(BaseModel):
    """专家列表合并节点的输入"""
    ai_matched_experts: List[Dict] = Field(default=[], description="AI匹配的专家列表")
    manual_expert_list: List[Dict] = Field(default=[], description="人工导入的专家列表")


class ExpertListMergeOutput(BaseModel):
    """专家列表合并节点的输出"""
    final_expert_list: List[Dict] = Field(..., description="合并后的专家列表")


# ==================== 项目管理相关节点 ====================

class ProjectCreateInput(BaseModel):
    """项目创建节点的输入"""
    project_name: Optional[str] = Field(default=None, description="项目名称（可选，如果不提供将自动生成）")
    industry_keyword: str = Field(..., description="行业关键词")


class ProjectCreateOutput(BaseModel):
    """项目创建节点的输出"""
    project_id: int = Field(..., description="创建的项目ID")
    project_name: str = Field(..., description="项目名称")


class ProjectUpdateStatusInput(BaseModel):
    """项目状态更新节点的输入"""
    project_id: int = Field(..., description="项目ID")
    status: str = Field(..., description="新的项目状态")
    current_stage: Optional[str] = Field(default=None, description="当前阶段（可选）")
    final_topic: Optional[str] = Field(default=None, description="最终选题（可选）")


class ProjectUpdateStatusOutput(BaseModel):
    """项目状态更新节点的输出"""
    success: bool = Field(..., description="是否更新成功")


class NodeExecutionTrackingInput(BaseModel):
    """节点执行追踪节点的输入"""
    project_id: int = Field(..., description="项目ID")
    node_name: str = Field(..., description="节点名称")
    status: str = Field(..., description="节点状态：pending, in_progress, completed, failed, skipped")
    error_message: Optional[str] = Field(default=None, description="错误信息（可选）")
    output_json: Optional[dict] = Field(default=None, description="节点输出（可选）")


class NodeExecutionTrackingOutput(BaseModel):
    """节点执行追踪节点的输出"""
    success: bool = Field(..., description="是否更新成功")


class ProjectQueryInput(BaseModel):
    """项目查询节点的输入"""
    project_id: Optional[int] = Field(default=None, description="项目ID（查询单个项目）")
    status: Optional[str] = Field(default=None, description="按状态筛选（可选）")
    current_stage: Optional[str] = Field(default=None, description="按阶段筛选（可选）")
    limit: int = Field(default=10, description="返回数量限制")


class ProjectQueryOutput(BaseModel):
    """项目查询节点的输出"""
    projects: List[Dict] = Field(default=[], description="项目列表")
    total: int = Field(default=0, description="总数")
