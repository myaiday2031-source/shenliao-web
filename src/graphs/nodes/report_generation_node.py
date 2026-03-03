"""
报告生成节点：使用document-generation技能生成研究报告
"""
from coze_coding_dev_sdk import DocumentGenerationClient
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from graphs.state import ReportGenerationInput, ReportGenerationOutput


def report_generation_node(state: ReportGenerationInput, config: RunnableConfig, runtime: Runtime[Context]) -> ReportGenerationOutput:
    """
    title: 报告生成
    desc: 将选题建议和深度分析内容整合成专业的Markdown格式研究报告，并生成PDF文档
    integrations: document-generation
    """
    ctx = runtime.context
    
    try:
        # 初始化文档生成客户端
        client = DocumentGenerationClient()
        
        # 构建Markdown格式的报告内容
        markdown_content = f"""# {state.final_topic}

## 行业关键词
{state.industry_keyword}

---

## 一、选题建议

{state.topic_suggestions}

---

## 二、深度分析

### 2.1 市场分析

### 2.2 技术趋势

### 2.3 竞争格局

### 2.4 发展前景

### 详细分析内容

{state.deep_analysis}

---

## 三、结论与建议

### 3.1 核心观点

### 3.2 行动建议

### 3.3 风险提示

---

## 附录

- 生成时间：自动生成
- 数据来源：网络搜索与AI分析
- 报告版本：V1.0

---

*本报告由"深聊"智库平台AI自动生成，仅供参考。*
"""
        
        # 生成PDF报告（使用英文标题）
        safe_title = "industry_research_report"
        
        url = client.create_pdf_from_markdown(markdown_content, safe_title)
        
        return ReportGenerationOutput(
            report_url=url
        )
        
    except Exception as e:
        raise Exception(f"报告生成失败: {str(e)}")
