## 项目概述
- **名称**: 基于AI的主动式行业智库平台"深聊"
- **功能**: 这是一个AI驱动的行业智库平台工作流，通过自动化的热点扫描、AI生成选题建议、专家确认选题、深度分析、报告生成和知识存储，实现从信息采集到知识沉淀的完整闭环。**支持人机协作的选题决策流程**。

### 节点清单
| 节点名 | 文件位置 | 类型 | 功能描述 | 分支逻辑 | 配置文件 |
|-------|---------|------|---------|---------|---------|
| hotspot_scan | `nodes/hotspot_scan_node.py` | task | 热点扫描 | - | - |
| topic_suggestion_generation | `nodes/topic_suggestion_generation_node.py` | agent | AI选题建议生成 | - | `config/topic_generation_llm_cfg.json` |
| topic_confirmation | `nodes/topic_confirmation_node.py` | task | 专家选题确认 | - | - |
| deep_analysis | `nodes/deep_analysis_node.py` | agent | 深度分析 | - | `config/deep_analysis_llm_cfg.json` |
| report_generation | `nodes/report_generation_node.py` | task | 报告生成 | - | - |
| knowledge_storage | `nodes/knowledge_storage_node.py` | task | 知识存储 | - | - |

**类型说明**: task(task节点) / agent(大模型) / condition(条件分支) / looparray(列表循环) / loopcond(条件循环)

## 子图清单
无子图（本工作流为线性流程，无需子图）

## 技能使用
- 节点 `hotspot_scan` 使用技能 `web-search`：扫描行业热点信息
- 节点 `topic_suggestion_generation` 使用技能 `llm`：生成选题建议（不做最终决策）
- 节点 `deep_analysis` 使用技能 `llm`：进行深度行业分析
- 节点 `report_generation` 使用技能 `document-generation`：生成PDF报告
- 节点 `knowledge_storage` 使用技能 `knowledge`：存储内容到知识库

## 工作流说明

### 工作流架构（支持人机协作）
本工作流实现了"深聊"智库平台的核心功能，通过6个节点完成从信息采集到知识沉淀的全过程。**特别强调：选题采用人机协作模式，AI生成建议，专家最终决策**。

1. **热点扫描 (hotspot_scan)**:
   - 输入：行业关键词
   - 功能：使用web-search技能搜索该行业的最新热点、技术难点、政策关注点
   - 输出：搜索结果摘要和详情列表

2. **AI选题建议生成 (topic_suggestion_generation)**:
   - 输入：行业关键词、搜索结果
   - 功能：使用LLM分析搜索结果，生成高质量的选题建议（包括推荐选题和多个备选选题）
   - 输出：选题建议和AI推荐的选题（供专家参考）
   - **特点**：AI明确标注这是建议，不做最终决策

3. **专家选题确认 (topic_confirmation)**:
   - 输入：AI推荐的选题、专家确认的选题（可选）、专家审核意见（可选）
   - 功能：接收专家最终确认的选题。如果专家提供了选题，使用专家的选题；如果未提供，使用AI推荐的选题
   - 输出：最终确定的选题（用于后续深度分析）
   - **人机协作核心节点**：专家可以直接接受AI建议、修改建议、或提供全新的选题

4. **深度分析 (deep_analysis)**:
   - 输入：行业关键词、最终确定的选题、搜索详情
   - 功能：使用LLM对最终确定的选题进行深度分析，包括市场分析、技术趋势、竞争格局、发展前景等
   - 输出：深度分析内容

5. **报告生成 (report_generation)**:
   - 输入：行业关键词、最终确定的选题、选题建议、深度分析
   - 功能：使用document-generation技能生成专业的Markdown格式PDF报告
   - 输出：报告下载URL

6. **知识存储 (knowledge_storage)**:
   - 输入：行业关键词、最终确定的选题、选题建议、深度分析、搜索详情、专家审核意见
   - 功能：使用knowledge技能将内容存储到知识库，便于后续检索和复用
   - 输出：存储的文档ID列表

### 输入输出
- **输入 (GraphInput)**:
  - `industry_keyword`: 行业关键词或主题（必填）
  - `expert_confirmed_topic`: 专家最终确认的选题（可选，如果不提供，将使用AI推荐）
  - `expert_review_comment`: 专家的审核意见（可选）

- **输出 (GraphOutput)**:
  - `topic_suggestions`: AI生成的选题建议
  - `deep_analysis`: 深度分析内容
  - `report_url`: 生成的报告下载URL

### 人机协作流程
本工作流支持两种使用模式：

**模式1：专家完全采纳AI建议**
```
专家输入：行业关键词
  ↓
AI生成选题建议
  ↓
专家确认节点：专家未提供选题，自动使用AI推荐
  ↓
继续深度分析...
```

**模式2：专家自定义选题**
```
专家输入：行业关键词 + 专家确认的选题 + 审核意见
  ↓
AI生成选题建议（供参考）
  ↓
专家确认节点：使用专家提供的选题
  ↓
继续深度分析...
```

### 使用场景
- 智库研究和内容策划
- 行业深度分析报告生成
- 知识库内容沉淀
- 行业趋势跟踪和热点发现
- **专家与AI协作进行选题决策**

### 技术特点
- 全流程自动化，从信息采集到报告生成
- **人机协作的选题决策机制**：AI生成建议，专家最终决策
- 基于AI的智能分析，确保内容的专业性和深度
- 知识自动沉淀，支持后续检索和复用
- 支持PDF报告生成，便于分享和归档
- 灵活的选题机制，支持专家自主选择或自定义选题
