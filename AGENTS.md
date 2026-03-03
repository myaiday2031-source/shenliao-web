## 项目概述
- **名称**: 基于AI的主动式行业智库平台"深聊"（两阶段工作流+项目管理）
- **功能**: 这是一个AI驱动的行业智库平台工作流，通过自动化的热点扫描、AI生成选题建议、专家确认选题、专家资源匹配、客户邀约、专家沟通表生成、访谈方案生成、人工执行访谈、访谈纪要上传、深度分析、双产出物生成（研究报告+新闻稿）、多渠道分发，实现从信息采集到知识沉淀的完整闭环。**支持人机协作的选题决策流程、专家主动访谈准备，以及多项目并行管理和实时进度监控**。

### 节点清单
| 节点名 | 文件位置 | 类型 | 功能描述 | 分支逻辑 | 配置文件 |
|-------|---------|------|---------|---------|---------|
| hotspot_scan | `nodes/hotspot_scan_node.py` | agent | 行业热点扫描 | - | `config/hotspot_scan_llm_cfg.json` |
| topic_suggestion_generation | `nodes/topic_suggestion_generation_node.py` | agent | AI选题建议生成 | - | `config/topic_generation_llm_cfg.json` |
| topic_confirmation | `nodes/topic_confirmation_node.py` | task | 专家选题确认 | - | - |
| expert_matching | `nodes/expert_matching_node.py` | agent | 专家资源匹配（AI） | - | `config/expert_matching_llm_cfg.json` |
| manual_expert_import | `nodes/manual_expert_import_node.py` | task | 人工专家导入（Excel） | - | - |
| expert_list_merge | `nodes/expert_list_merge_node.py` | task | 专家列表合并 | - | - |
| client_invitation | `nodes/client_invitation_node.py` | agent | 客户邀约邮件生成 | - | `config/client_invitation_llm_cfg.json` |
| communication_table | `nodes/communication_table_node.py` | agent | 专家沟通表生成 | - | `config/communication_table_llm_cfg.json` |
| interview_plan | `nodes/interview_plan_node.py` | agent | 访谈/会议方案生成 | - | `config/interview_plan_llm_cfg.json` |
| interview_minutes_upload | `nodes/interview_minutes_upload_node.py` | task | 访谈纪要上传 | - | - |
| deep_analysis | `nodes/deep_analysis_node.py` | agent | 深度分析 | - | `config/deep_analysis_llm_cfg.json` |
| research_report | `nodes/research_report_node.py` | agent | 研究报告生成（详细版） | - | `config/research_report_llm_cfg.json` |
| news_article | `nodes/news_article_node.py` | agent | 新闻稿件生成（简报版） | - | `config/news_article_llm_cfg.json` |
| news_video_generation | `nodes/news_video_generation_node.py` | agent | 新闻稿视频生成 | - | `config/news_video_generation_llm_cfg.json` |
| encrypted_email_send | `nodes/encrypted_email_send_node.py` | agent | 研究报告加密邮件发送 | - | `config/encrypted_email_send_llm_cfg.json` |
| news_article_publish | `nodes/news_article_publish_node.py` | agent | 新闻稿件发布（微信、微博、知乎） | - | `config/news_article_publish_llm_cfg.json` |
| news_video_publish | `nodes/news_video_publish_node.py` | agent | 新闻稿视频发布（抖音、视频号） | - | `config/news_video_publish_llm_cfg.json` |
| knowledge_storage | `nodes/knowledge_storage_node.py` | agent | 知识存储 | - | `config/knowledge_storage_llm_cfg.json` |
| project_create | `nodes/project_create_node.py` | task | 创建新项目 | - | - |
| project_update_status | `nodes/project_update_status_node.py` | task | 更新项目状态 | - | - |
| node_execution_tracking | `nodes/node_execution_tracking_node.py` | task | 追踪节点执行状态 | - | - |
| project_query | `nodes/project_query_node.py` | task | 查询项目进度 | - | - |

**类型说明**: task(task节点) / agent(大模型) / condition(条件分支) / looparray(列表循环) / loopcond(条件循环)

## 子图清单
无子图（本工作流为线性流程，无需子图）

## 技能使用
- 节点 `hotspot_scan` 使用技能 `web-search`：扫描行业热点信息
- 节点 `topic_suggestion_generation` 使用技能 `llm`：生成选题建议（不做最终决策）
- 节点 `expert_matching` 使用技能 `llm`：根据选题匹配专家资源
- 节点 `manual_expert_import` 使用技能 `pandas`：读取Excel格式的专家列表
- 节点 `client_invitation` 使用技能 `llm`：生成客户邀约邮件
- 节点 `communication_table` 使用技能 `llm`：生成专家沟通表
- 节点 `interview_plan` 使用技能 `llm`：生成访谈/会议方案
- 节点 `interview_minutes_upload` 使用技能 `FileOps`：读取访谈纪要文件
- 节点 `deep_analysis` 使用技能 `llm`：进行深度行业分析
- 节点 `research_report` 使用技能 `llm` + `document-generation`：生成详细版研究报告
- 节点 `news_article` 使用技能 `llm`：生成简报版新闻稿件
- 节点 `news_video_generation` 使用技能 `llm` + `video-generation`：生成新闻稿视频
- 节点 `encrypted_email_send` 使用技能 `llm` + `email`：生成并发送加密邮件
- 节点 `news_article_publish` 使用技能 `llm` + `wechat-official-account` + `weibo` + `zhihu`：发布新闻稿到文字平台
- 节点 `news_video_publish` 使用技能 `llm` + `douyin` + `video-account`：发布视频到视频平台
- 节点 `knowledge_storage` 使用技能 `knowledge`：存储内容到知识库

## 工作流说明

### 工作流架构（两阶段模式）
本工作流实现了"深聊"智库平台的核心功能，通过17个节点完成从信息采集到知识沉淀的全过程。**采用两阶段模式，阶段1生成访谈准备方案，阶段2基于访谈纪要生成双产出物并分发**。

#### 阶段1：访谈准备阶段
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
   - 输出：最终确定的选题（用于后续流程）
   - **人机协作核心节点**：专家可以直接接受AI建议、修改建议、或提供全新的选题

4. **专家资源匹配 (expert_matching)**:
   - 输入：行业关键词、最终确定的选题
   - 功能：使用LLM根据选题方向，智能匹配8-10位相关的专家人选
   - 输出：AI匹配的专家候选人列表

5. **人工专家导入 (manual_expert_import)**:
   - 输入：人工导入的专家列表（Excel格式，可选）
   - 功能：从Excel文件中读取专家列表
   - 输出：解析出的专家列表

6. **专家列表合并 (expert_list_merge)**:
   - 输入：AI匹配的专家列表、人工导入的专家列表
   - 功能：合并两个专家列表，去重后形成最终专家列表
   - 输出：最终确定的专家列表

7. **客户邀约邮件生成 (client_invitation)**:
   - 输入：行业关键词、最终确定的选题、最终专家列表
   - 功能：使用LLM生成专业的客户邀约邮件
   - 输出：客户邀约邮件内容

8. **专家沟通表生成 (communication_table)**:
   - 输入：行业关键词、最终确定的选题、最终专家列表
   - 功能：使用LLM生成详细的专家访谈沟通表
   - 输出：专家访谈沟通表（Markdown格式）

9. **访谈/会议方案生成 (interview_plan)**:
   - 输入：行业关键词、最终确定的选题、最终专家列表、专家沟通表
   - 功能：使用LLM生成详细的访谈或线下研讨会方案
   - 输出：访谈/会议方案
   - **阶段1结束**：输出方案后，工作流暂停，等待人工执行访谈

#### 阶段2：访谈执行与产出阶段
10. **访谈纪要上传 (interview_minutes_upload)**:
    - 输入：访谈纪要文件（人工上传）
    - 功能：接收人工上传的访谈纪要，提取文本内容
    - 输出：访谈纪要文本内容
    - **阶段2开始**：人工执行访谈后，重新运行工作流并上传纪要

11. **深度分析 (deep_analysis)**:
    - 输入：行业关键词、最终确定的选题、搜索详情、访谈纪要
    - 功能：使用LLM基于访谈纪要对最终确定的选题进行深度分析
    - 输出：深度分析内容

12. **双路径并行：双产出物生成**:
    - **研究报告生成 (research_report)**:
        - 输入：行业关键词、最终确定的选题、深度分析、访谈纪要
        - 功能：使用LLM生成详细版研究报告，并转换为PDF
        - 输出：研究报告内容和PDF下载URL
    
    - **新闻稿件生成 (news_article)**:
        - 输入：行业关键词、最终确定的选题、深度分析、访谈纪要
        - 功能：使用LLM生成简报版新闻稿件
        - 输出：新闻稿件内容

13. **双路径并行：视频生成与邮件发送**:
    - **新闻稿视频生成 (news_video_generation)**（依赖news_article）:
        - 输入：新闻稿件内容
        - 功能：使用LLM生成视频脚本，调用video-generation技能生成视频
        - 输出：新闻稿视频URL
    
    - **研究报告加密邮件发送 (encrypted_email_send)**（依赖research_report）:
        - 输入：客户邮箱、行业关键词、最终确定的选题、研究报告URL
        - 功能：生成加密邮件内容，调用email技能发送
        - 输出：加密邮件发送状态

14. **双路径并行：多渠道发布**:
    - **新闻稿件发布 (news_article_publish)**（依赖news_article）:
        - 输入：新闻稿件内容、行业关键词
        - 功能：调用wechat-official-account、微博、知乎等技能发布到文字平台
        - 输出：新闻稿件发布状态
    
    - **新闻稿视频发布 (news_video_publish)**（依赖news_video）:
        - 输入：新闻稿视频URL、行业关键词
        - 功能：调用抖音、视频号等技能发布到视频平台
        - 输出：新闻稿视频发布状态

15. **知识存储 (knowledge_storage)**:
    - 输入：所有阶段产生的关键内容
    - 功能：使用knowledge技能将内容存储到知识库
    - 输出：存储的文档ID列表

### 输入输出
- **输入 (GraphInput)**:
  - `industry_keyword`: 行业关键词或主题（必填）
  - `client_email`: 客户邮箱地址（可选，用于发送研究报告）
  - `expert_confirmed_topic`: 专家最终确认的选题（可选）
  - `expert_review_comment`: 专家的审核意见（可选）
  - `manual_expert_list`: 人工导入的专家列表（Excel格式，可选）
  - `interview_minutes`: 访谈纪要文件（可选，两阶段模式中使用）

- **输出 (GraphOutput)**:
  - `topic_suggestions`: AI生成的选题建议
  - `interview_plan`: 访谈/会议方案（阶段1输出）
  - `deep_analysis`: 深度分析内容
  - `research_report_url`: 详细版研究报告下载URL
  - `news_article`: 简报版新闻稿件内容
  - `news_video_url`: 新闻稿视频URL
  - `encrypted_email_sent`: 研究报告加密邮件是否已发送
  - `news_article_published`: 新闻稿件是否已发布
  - `news_video_published`: 新闻稿视频是否已发布

### 两阶段工作流模式

#### 阶段1：访谈准备
```
专家输入：行业关键词（可选：客户邮箱、专家确认选题、专家列表Excel）
  ↓
热点扫描 → AI选题建议 → 专家选题确认 → 专家匹配（AI）
  ↓
人工导入专家（可选）→ 专家列表合并 → 客户邀约 → 沟通表 → 访谈方案
  ↓
【输出访谈方案，工作流暂停】
```

#### 阶段2：访谈执行与产出
```
【人工执行访谈，生成访谈纪要】
  ↓
重新运行工作流，输入：行业关键词 + 访谈纪要文件
  ↓
访谈纪要上传 → 深度分析
  ↓
【并行】：
  ├─ 研究报告生成 → 加密邮件发送
  └─ 新闻稿生成 → 新闻稿视频生成 → 视频发布
  └─ 新闻稿发布（微信、微博、知乎）
  ↓
知识存储
  ↓
【输出双产出物和分发状态】
```

### 使用场景
- 智库研究和内容策划
- 行业深度分析报告生成
- 专家访谈准备与执行
- 知识库内容沉淀
- 行业趋势跟踪和热点发现
- **专家与AI协作进行选题决策**
- **多渠道内容分发（研究报告+新闻稿）**

### 技术特点
- **两阶段工作流**：阶段1生成访谈方案，阶段2基于访谈纪要生成双产出物
- **人机协作**：AI生成建议，专家最终决策；人工导入专家列表与AI推荐结合
- **双产出物系统**：详细版研究报告（客户）+ 简报版新闻稿（宣传）
- **智能分发**：加密邮件发送 + 多媒体渠道发布（微信、微博、知乎、抖音、视频号）
- **并行处理**：研究报告和新闻稿生成与分发采用并行架构
- 基于AI的智能分析，确保内容的专业性和深度
- 知识自动沉淀，支持后续检索和复用
- 灵活的选题机制，支持专家自主选择或自定义选题

### 注意事项
1. **两阶段执行**：工作流需要分两次运行，第一次生成访谈方案，第二次基于访谈纪要生成产出物
2. **技能配置**：部分节点（如video-generation、email、wechat-official-account、douyin等）需要配置相应的技能集成
3. **专家导入格式**：人工导入专家时，Excel文件应包含姓名、机构、专业领域、研究方向等字段
4. **访谈纪要格式**：访谈纪要可以是PDF、DOCX、TXT等格式，系统会自动提取文本内容
5. **客户邮箱必填**：如需发送研究报告加密邮件，必须在输入中提供客户邮箱

---

## 项目管理功能

### 项目管理概述
为支持多个选题并行执行和实时监控项目进度，系统提供了完整的项目管理功能。通过数据库持久化存储项目信息和节点执行状态，可以实现：
- **多项目并行**：同时运行多个研究项目，互不干扰
- **实时监控**：查看各项目的执行状态和进度
- **进度追踪**：追踪每个节点的执行情况
- **历史记录**：保留完整的项目执行历史

### 数据库表结构

#### 项目表（projects）
| 字段 | 类型 | 说明 |
|-----|------|-----|
| id | int | 项目ID（主键） |
| name | string | 项目名称 |
| industry_keyword | string | 行业关键词 |
| final_topic | text | 最终选题 |
| client_email | string | 客户邮箱 |
| status | string | 项目状态 |
| current_stage | string | 当前阶段 |
| created_at | datetime | 创建时间 |
| updated_at | datetime | 更新时间 |
| completed_at | datetime | 完成时间 |
| metadata_json | json | 附加信息 |

#### 节点执行记录表（project_node_executions）
| 字段 | 类型 | 说明 |
|-----|------|-----|
| id | int | 记录ID（主键） |
| project_id | int | 项目ID（外键） |
| node_name | string | 节点名称 |
| status | string | 节点状态 |
| started_at | datetime | 开始执行时间 |
| completed_at | datetime | 完成时间 |
| error_message | text | 错误信息 |
| output_json | json | 节点输出 |
| created_at | datetime | 记录创建时间 |
| updated_at | datetime | 记录更新时间 |

### 项目状态定义

#### 项目状态（status）
- **pending**: 待启动
- **stage1_in_progress**: 阶段1进行中（访谈准备）
- **stage1_completed**: 阶段1完成（等待访谈）
- **stage2_in_progress**: 阶段2进行中（产出生成）
- **stage2_completed**: 阶段2完成（已完成）
- **cancelled**: 已取消

#### 节点状态（status）
- **pending**: 待执行
- **in_progress**: 执行中
- **completed**: 已完成
- **failed**: 失败
- **skipped**: 跳过

### 项目管理API使用

#### 创建项目
```python
from tools.project_api import ProjectAPI

project = ProjectAPI.create_project(
    name="人工智能行业研究报告",
    industry_keyword="人工智能",
    client_email="client@example.com"
)

print(f"项目ID: {project['id']}")
```

#### 查询项目
```python
# 查询单个项目
project = ProjectAPI.get_project(project_id=1)

# 查询项目列表
projects = ProjectAPI.list_projects(
    status="stage1_in_progress",  # 按状态筛选
    limit=20
)
```

#### 更新项目状态
```python
# 更新项目状态为阶段1进行中
ProjectAPI.update_project_status(
    project_id=1,
    status="stage1_in_progress",
    current_stage="stage1"
)

# 更新项目状态为阶段2进行中，并设置最终选题
ProjectAPI.update_project_status(
    project_id=1,
    status="stage2_in_progress",
    current_stage="stage2",
    final_topic="人工智能在医疗领域的应用研究"
)
```

#### 记录节点执行
```python
# 记录节点开始执行
ProjectAPI.record_node_execution(
    project_id=1,
    node_name="hotspot_scan",
    status="in_progress"
)

# 记录节点执行完成
ProjectAPI.record_node_execution(
    project_id=1,
    node_name="hotspot_scan",
    status="completed",
    output_json={"search_results": "..."}
)

# 记录节点执行失败
ProjectAPI.record_node_execution(
    project_id=1,
    node_name="expert_matching",
    status="failed",
    error_message="专家匹配服务不可用"
)
```

#### 获取项目进度
```python
progress = ProjectAPI.get_project_progress(project_id=1)

print(f"项目名称: {progress['project']['name']}")
print(f"项目状态: {progress['project']['status']}")
print(f"进度: {progress['progress']}%")
print(f"节点执行情况:")
for node in progress['nodes']:
    print(f"  - {node['node_name']}: {node['status']}")
```

#### 取消项目
```python
ProjectAPI.cancel_project(project_id=1)
```

### 工作流集成项目管理

#### 方式1：使用项目管理节点
工作流中提供了以下项目管理节点，可以直接在工作流中使用：
- **project_create**: 创建新项目
- **project_update_status**: 更新项目状态
- **node_execution_tracking**: 追踪节点执行
- **project_query**: 查询项目

#### 方式2：在节点中集成项目管理
在每个节点函数中调用ProjectAPI记录节点执行状态：

```python
from tools.project_api import ProjectAPI

def hotspot_scan_node(state: HotspotScanInput, config: RunnableConfig, runtime: Runtime[Context]) -> HotspotScanOutput:
    """热点扫描节点"""
    ctx = runtime.context
    
    # 获取项目ID（从runtime或state中）
    project_id = ctx.get('project_id', 1)
    
    # 记录节点开始执行
    ProjectAPI.record_node_execution(
        project_id=project_id,
        node_name="hotspot_scan",
        status="in_progress"
    )
    
    try:
        # 执行节点逻辑
        result = execute_hotspot_scan(state)
        
        # 记录节点执行完成
        ProjectAPI.record_node_execution(
            project_id=project_id,
            node_name="hotspot_scan",
            status="completed",
            output_json={"search_results": result}
        )
        
        return HotspotScanOutput(**result)
    
    except Exception as e:
        # 记录节点执行失败
        ProjectAPI.record_node_execution(
            project_id=project_id,
            node_name="hotspot_scan",
            status="failed",
            error_message=str(e)
        )
        raise
```

### 多项目并行监控

#### 查看所有进行中的项目
```python
# 查看所有正在执行的项目（阶段1和阶段2）
in_progress_projects = ProjectAPI.list_projects(
    status="stage1_in_progress",
    limit=50
)

# 查看所有已完成的项目
completed_projects = ProjectAPI.list_projects(
    status="stage2_completed",
    limit=50
)
```

#### 项目监控面板
可以基于ProjectAPI构建一个项目监控面板，实时显示：
- 项目列表
- 每个项目的状态
- 每个项目的进度百分比
- 节点执行情况
- 预计完成时间

### 项目生命周期示例

```
1. 创建项目
   └─ status: pending
   └─ current_stage: null

2. 开始阶段1
   └─ status: stage1_in_progress
   └─ current_stage: stage1
   └─ 执行节点: hotspot_scan → topic_suggestion → ... → interview_plan

3. 阶段1完成
   └─ status: stage1_completed
   └─ current_stage: stage1
   └─ 等待人工执行访谈

4. 开始阶段2
   └─ status: stage2_in_progress
   └─ current_stage: stage2
   └─ 执行节点: interview_minutes_upload → deep_analysis → ... → knowledge_storage

5. 项目完成
   └─ status: stage2_completed
   └─ current_stage: stage2
   └─ completed_at: [完成时间]

6. 取消项目（可选）
   └─ status: cancelled
```
