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
    topic_suggestions: str = Field(default="", description="AI生成的选题建议")
    selected_topic: str = Field(default="", description="选中的核心选题")
    
    # 深度分析结果
    deep_analysis: str = Field(default="", description="深度分析内容")
    
    # 报告生成结果
    report_url: str = Field(default="", description="生成的报告URL")
    
    # 知识库存储结果
    knowledge_ids: List[str] = Field(default=[], description="存储到知识库的文档ID列表")


class GraphInput(BaseModel):
    """工作流的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题，例如：人工智能、量子计算、新能源汽车等")


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


# ==================== 节点2: 选题生成 ====================
class TopicGenerationInput(BaseModel):
    """选题生成节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    search_results: str = Field(..., description="热点搜索结果摘要")
    search_details: List[Dict] = Field(default=[], description="搜索结果详情列表")


class TopicGenerationOutput(BaseModel):
    """选题生成节点的输出"""
    topic_suggestions: str = Field(..., description="AI生成的选题建议")
    selected_topic: str = Field(..., description="选中的核心选题")


# ==================== 节点3: 深度分析 ====================
class DeepAnalysisInput(BaseModel):
    """深度分析节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    selected_topic: str = Field(..., description="选中的核心选题")
    search_details: List[Dict] = Field(default=[], description="搜索结果详情列表")


class DeepAnalysisOutput(BaseModel):
    """深度分析节点的输出"""
    deep_analysis: str = Field(..., description="深度分析内容")


# ==================== 节点4: 报告生成 ====================
class ReportGenerationInput(BaseModel):
    """报告生成节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    selected_topic: str = Field(..., description="选中的核心选题")
    topic_suggestions: str = Field(..., description="AI生成的选题建议")
    deep_analysis: str = Field(..., description="深度分析内容")


class ReportGenerationOutput(BaseModel):
    """报告生成节点的输出"""
    report_url: str = Field(..., description="生成的报告下载URL")


# ==================== 节点5: 知识存储 ====================
class KnowledgeStorageInput(BaseModel):
    """知识存储节点的输入"""
    industry_keyword: str = Field(..., description="行业关键词或主题")
    selected_topic: str = Field(..., description="选中的核心选题")
    topic_suggestions: str = Field(..., description="AI生成的选题建议")
    deep_analysis: str = Field(..., description="深度分析内容")
    search_details: List[Dict] = Field(default=[], description="搜索结果详情列表")


class KnowledgeStorageOutput(BaseModel):
    """知识存储节点的输出"""
    knowledge_ids: List[str] = Field(default=[], description="存储到知识库的文档ID列表")
