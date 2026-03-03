## 项目概述
- **名称**: 基于AI的主动式行业智库平台"深聊"
- **功能**: 这是一个AI驱动的行业智库平台工作流，通过自动化的热点扫描、选题生成、深度分析、报告生成和知识存储，实现从信息采集到知识沉淀的完整闭环。

### 节点清单
| 节点名 | 文件位置 | 类型 | 功能描述 | 分支逻辑 | 配置文件 |
|-------|---------|------|---------|---------|---------|
| hotspot_scan | `nodes/hotspot_scan_node.py` | task | 热点扫描 | - | - |
| topic_generation | `nodes/topic_generation_node.py` | agent | 选题生成 | - | `config/topic_generation_llm_cfg.json` |
| deep_analysis | `nodes/deep_analysis_node.py` | agent | 深度分析 | - | `config/deep_analysis_llm_cfg.json` |
| report_generation | `nodes/report_generation_node.py` | task | 报告生成 | - | - |
| knowledge_storage | `nodes/knowledge_storage_node.py` | task | 知识存储 | - | - |

**类型说明**: task(task节点) / agent(大模型) / condition(条件分支) / looparray(列表循环) / loopcond(条件循环)

## 子图清单
无子图（本工作流为线性流程，无需子图）

## 技能使用
- 节点 `hotspot_scan` 使用技能 `web-search`：扫描行业热点信息
- 节点 `topic_generation` 使用技能 `llm`：生成选题建议
- 节点 `deep_analysis` 使用技能 `llm`：进行深度行业分析
- 节点 `report_generation` 使用技能 `document-generation`：生成PDF报告
- 节点 `knowledge_storage` 使用技能 `knowledge`：存储内容到知识库

## 工作流说明

### 工作流架构
本工作流实现了"深聊"智库平台的核心功能，通过5个线性节点完成从信息采集到知识沉淀的全过程：

1. **热点扫描 (hotspot_scan)**:
   - 输入：行业关键词
   - 功能：使用web-search技能搜索该行业的最新热点、技术难点、政策关注点
   - 输出：搜索结果摘要和详情列表

2. **选题生成 (topic_generation)**:
   - 输入：行业关键词、搜索结果
   - 功能：使用LLM分析搜索结果，生成高质量的选题建议（包括核心选题和备选选题）
   - 输出：选题建议和选中的核心选题

3. **深度分析 (deep_analysis)**:
   - 输入：行业关键词、核心选题、搜索详情
   - 功能：使用LLM对核心选题进行深度分析，包括市场分析、技术趋势、竞争格局、发展前景等
   - 输出：深度分析内容

4. **报告生成 (report_generation)**:
   - 输入：行业关键词、核心选题、选题建议、深度分析
   - 功能：使用document-generation技能生成专业的Markdown格式PDF报告
   - 输出：报告下载URL

5. **知识存储 (knowledge_storage)**:
   - 输入：行业关键词、核心选题、选题建议、深度分析、搜索详情
   - 功能：使用knowledge技能将内容存储到知识库，便于后续检索和复用
   - 输出：存储的文档ID列表

### 输入输出
- **输入 (GraphInput)**:
  - `industry_keyword`: 行业关键词或主题（必填）

- **输出 (GraphOutput)**:
  - `topic_suggestions`: AI生成的选题建议
  - `deep_analysis`: 深度分析内容
  - `report_url`: 生成的报告下载URL

### 使用场景
- 智库研究和内容策划
- 行业深度分析报告生成
- 知识库内容沉淀
- 行业趋势跟踪和热点发现

### 技术特点
- 全流程自动化，从信息采集到报告生成无需人工干预
- 基于AI的智能选题和分析，确保内容的专业性和深度
- 知识自动沉淀，支持后续检索和复用
- 支持PDF报告生成，便于分享和归档
