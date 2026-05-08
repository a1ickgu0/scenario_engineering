---
name: scenario_analyzer
description: "INCOSE requirements engineering SKILL for analyzing extracted customer data from scenario_parser outputs (MD + JSON). Generates structured 12-section analysis reports with stakeholder analysis, ConOps-grounded state models, environment models, entity hierarchies, bilingual traceability support, MoE analysis, and parameterization. Designed for downstream analysis generation, outputs structured for OpenSCENARIO DSL preparation."
tags:
  - incose
  - requirements-engineering
  - analysis-generation
  - stakeholder-analysis
  - state-model
  - traceability
  - openscenario-preparation
version: "0.7.1"
---

# Scenario Analyzer SKILL

## Overview

This SKILL performs INCOSE requirements engineering analysis on **extracted data from scenario_parser**. It reads intermediate files (MD + JSON) and generates structured 12-section analysis reports.

**Input Sources**:
| Source | Format | Purpose |
|--------|--------|---------|
| Parser Output MD | `*-extracted.md` | Context verification, human review |
| Parser Output JSON | `*-extracted.json` | Structured data input |

**Primary Goals**:
1. Analyze stakeholder information and generate structured tables
2. Build ConOps-grounded state/environment/entity/lifecycle models
3. Construct operational scenarios with triggers/transitions
4. Generate parameterization and MoE analysis for OpenSCENARIO DSL

**Output**: 12-section analysis report with full traceability

**Note**: This SKILL now requires scenario_parser output as input. For direct PDF processing, use scenario_parser first.

## Input Requirements

### Required Input Files

| File | Required | Purpose |
|------|----------|---------|
| `{customer}-extracted.md` | Yes | Context verification, reference checking |
| `{customer}-extracted.json` | Yes | Structured data for analysis generation |

### JSON Input Structure

Analyzer expects JSON with these sections (from scenario_parser):
- `document_meta` - Source file metadata
- `content_extract` - Customer basic information and identity basis
- `initial_state` - Problem context before solution
- `final_state` - Outcome after solution
- `stakeholder_mentions` - Raw stakeholder information with layer/title hints
- `pain_points_mentions` - Extracted pain points
- `product_mentions` - Product/solution information
- `metrics_mentions` - Quantified metrics, before/after comparison, MoE hints
- `environment_mentions` - Environment constraints
- `raw_quotes` - Original quotes with speakers and language

### Direct Input Mode (Legacy)

For backward compatibility, direct text/PDF input is still supported but requires in-SKILL extraction:
- Input: Raw text or narrative document
- Processing: Perform extraction internally before analysis
- Note: Recommended to use scenario_parser first for better quality

### Input Validation (NEW - Required Before Analysis)

**IMPORTANT**: Before generating analysis, validate Parser output.

| Validation Type | Check Method | Fail Condition | Recovery Action |
|---------------|-------------|---------------|---------------|
| **File Pair Exists** | Both MD and JSON present | One missing | Skip analysis, report missing file |
| **JSON Valid** | Parse JSON | JSON parse error | Report error, skip to next document |
| **MD Exists** | Check MD file | MD missing | Proceed with JSON-only (warning) |
| **File Consistency** | Base name match | Mismatched names | Identify correct pair manually |
| **Reference Integrity** | MD references map to JSON | Broken references | Flag for review |

**Validation Checklist**:
```
Before Analysis:
- [ ] extracted.md exists
- [ ] extracted.json exists and is parseable
- [ ] File base names match
- [ ] Required JSON fields present
- [ ] Reference markers in MD exist
```

## Quality Requirements (质量要求)

**IMPORTANT**: All analyses must strictly follow the requirements below to ensure content completeness and analysis quality.

### Mandatory Quality Standards

| 质量维度 | 要求标准 | 验收方法 |
|----------|----------|----------|
| **完整性** | 所有12个输出章节必须完整生成，不得遗漏任何章节 | 输出检查清单验证 |
| **追溯性** | 每个分析结论必须标注原文引用（客户名-原文内容） | 引用格式检查 |
| **准确性** | 提取的信息必须准确反映原文内容，不得臆造或推测 | 原文对照验证 |
| **结构化** | 表格必须包含所有要求的列，树状结构必须完整展示 | 格式规范检查 |
| **痛点准确性** | 痛点提取必须准确反映原文中各角色面临的具体困难，不得臆造 | 原文对照验证 |
| **层级拆分** | 利益相关者必须拆分层级与角色名，不得混写 | 表格字段检查 |
| **MoE 完整性** | 关键效果必须包含 MoE、来源、论据、依据 | MoE 表检查 |
| **ConOps 有效性** | 状态模型必须基于真实运行线程，不得套泛化占位状态 | ConOps 审核 |

### Output Completeness Checklist (输出完整性检查清单)

每个分析报告必须包含以下全部章节：

```
## 0. 客户基本信息 ✓/✗
## 1. 购买要素 ✓/✗
## 1.1 MoE 指标分析 ✓/✗
## 2. 利益相关者清单 ✓/✗
## 2.1 痛点提取完整性 ✓/✗
## 3. 冲突与优先级 ✓/✗
## 4. 基于 ConOps 的状态模型 ✓/✗
## 5. 环境模型 ✓/✗
## 6. 实体层级模型 ✓/✗
## 7. 生命周期阶段 ✓/✗
## 8. 运行场景 ✓/✗
## 9. 承诺与参与建议 ✓/✗
## 10. 产品与解决方案 ✓/✗
## 11. 参数化模型 ✓/✗
## 12. 追溯与备注 ✓/✗
```

### Output Validation (NEW - Required After Analysis)

**IMPORTANT**: After generating analysis, validate output quality.

| Validation Type | Check Method | Fail Condition | Recovery Action |
|---------------|-------------|---------------|---------------|
| **Section Presence** | 12 section scan | Missing section | Regenerate missing section |
| **Table Structure** | Table format check | Violates template | Reformat to template |
| **Traceability** | Reference scan | Missing references | Add reference markers |
| **Consistency** | Cross-field verify | Inconsistent data | Investigate and correct |
| **Language** | Language uniformity | Mixed languages | Normalize to primary |

**Validation Checklist**:
```
After Analysis:
- [ ] All 12 sections present
- [ ] Tables follow template format
- [ ] Each key point has source reference
- [ ] Stakeholder counts are consistent
- [ ] Language is uniform
- [ ] No critical data missing
```

### Traceability Requirements (追溯性要求)

每个分析项必须包含：
- **客户名称**: 标注具体客户名（如 "Southern Sun", "Aberdeen City Council"）
- **原文引用**: 保留原文关键表述（如 "Guest experience is everything"）
- **引用位置**: 页码、段落或行号标注（如 "Page 3, paragraph 2" 或 "第15行"）
- **非中文双语支持**: 对于非中文原文引用，必须保留原文并补充简明中文释义

示例格式：
```
| 利益相关者 | 期望 | 影响力 | 客户名 | 原文引用 |
|------------|------|--------|--------|----------|
| Guests | 无缝连接体验 | 高 | Southern Sun | "Guest experience is everything" / 中文释义: 客户体验至上 (第18行) |
```

---

### Statistical Conclusion Standards (统计类结论规范)

**IMPORTANT**: All statistical conclusions must follow these standards to ensure accuracy and completeness.

#### 1. 客户统计唯一性原则

**规则**: 每个客户在频率统计中最多只计为1次，即使原文多次提及同一模式。

| 统计类型 | 正确做法 | 错误做法 | 说明 |
|----------|----------|----------|------|
| 频率统计 | 客户A出现1次 | 客户A出现3次 | 即使原文提及3次，统计时仅计1次 |
| 原文引用 | "运维简化30%" (提及3次，第15/25/35行) | 仅标注第15行 | 说明客户提及次数和所有位置 |

**示例**:
```
| 业务驱动 | 频率 | 客户名 | 原文引用 |
|----------|------|--------|----------|
| 运维效率优化 | 65次 | Austrian Red Cross | "运维简化30%" (提及3次: 第15/25/35行) |
```

#### 2. 多客户原文引用规范

**规则**: 统计结果涉及多客户时，必须列出多客户的原文引用；客户数>5时，列出最重要的3-5个。

| 客户数量 | 引用要求 | 示例 |
|----------|----------|------|
| 1个客户 | 列出该客户的完整引用 | "运维简化30%" (Austrian Red Cross, 第15行) |
| 2-5个客户 | 列出所有客户的原文引用 | "运维简化30%" (ARC, 第15行); "AIOps减负70%" (Aberdeen, 第35行) |
| >5个客户 | 列出最重要的3-5个客户原文 | 重要案例: ARC, Aberdeen, Illinois... (共12个客户) |

**重要性判断标准**:
1. **量化表达明确**: 有具体数字（如"70%"、"30天→3天"）
2. **原文表达典型**: 表述清晰、可直接引用
3. **行业代表性**: 代表主要行业或典型场景
4. **时间新颖性**: 近期案例优先（2024-2026年）

**示例**:
```
| 业务驱动 | 频率 | 主要客户(3-5个) | 原文引用 |
|----------|------|-----------------|----------|
| 运维效率优化 | 65次(65个客户) | Austrian Red Cross, Aberdeen City Council, University of Illinois, Austrian Red Cross, Grove City College | "运维简化30%" (ARC, 第15行); "AIOps减负70%" (Aberdeen, 第35行); "troubleshooting days→hours" (UI, 第45行); "部署速度显著提升" (Grove City, 第30行) |
```

#### 3. 业务驱动/购买要素补充说明规范

**规则**: 每个业务驱动或购买要素不能仅用单词语表达，必须增加补充说明。

| 内容类型 | 要求格式 | 示例 |
|----------|----------|------|
| 业务驱动 | 标题 + 补充说明 | **运维效率优化**: 网络运维负担减轻，从被动响应转为主动预防，AIOps自动化减负 |
| 购买要素 | 标题 + 量化说明 | **运维简化**: Central云管理平台实现远程统一管理，运维效率提升30%，工单减少100% |

**补充说明内容要求**:
- **具体表现**: 该驱动/要素的具体表现形式
- **量化指标**: 相关的量化数据（如有）
- **实现方式**: 通过何种技术或方案实现
- **业务价值**: 对客户业务的实际价值

**示例**:
```
| 排序 | 购买要素 | 补充说明 | 量化表达 | 客户名 | 原文引用 |
|------|----------|----------|----------|--------|----------|
| 1 | **运维简化** | Central云管理平台实现单一仪表板远程管理，IT团队从运维负担转向战略聚焦，BYOD认证自动化 | 30%效率提升，100%工单减少 | Austrian Red Cross | "运维简化30%"; "BYOD头痛问题解决" (第15/35行) |
| 2 | **AIOps自动化** | AI-native网络实现预测性运维，从被动响应转为主动预防，故障自愈能力 | 70%运维减负 | Aberdeen City Council | "AIOps自动化运维减负70%" (第35行) |
```

#### 4. 分析表综述说明规范

**规则**: 每个分析表格输出后，必须补充一段综述说明，对表中内容进行综述及展开说明。

**综述说明结构**:
```
[表格输出]

**综述说明**:
1. **核心发现**: 表格中最重要的模式或结论
2. **分布特征**: 各项的分布规律和集中趋势
3. **异常观察**: 特殊情况或异常数据点
4. **业务含义**: 对客户决策或业务的影响
5. **数据限制**: 数据来源限制或可信度说明
```

**示例**:
```
| 业务驱动 | 频率 | 占比 | 主要客户 | 原文引用 |
|----------|------|------|----------|----------|
| 运维效率优化 | 65次 | 53.3% | Austrian Red Cross, Aberdeen City Council... | ... |
| 安全合规需求 | 48次 | 39.3% | Australian Defence Apparel, Amiri Hospital... | ... |
| ... | ... | ... | ... | ... |

**综述说明**:

**核心发现**: 运维效率优化是跨行业首要业务驱动，出现在53.3%的案例中，反映了网络运维负担是普遍痛点。安全合规需求在医疗和政府行业优先级更高（60%+），是硬性不可妥协要求。

**分布特征**: 运维效率、安全合规、用户体验三大驱动占总驱动的89.5%，形成核心驱动三角。成本优化在制造业优先级最高（40%成本节约典型），但在教育行业优先级较低。

**异常观察**: IoT/智能建筑驱动频率仅12.3%，但在酒店行业呈现新兴趋势，2025-2026案例中提及率上升至25%。可持续发展驱动仅6.6%，集中在欧洲制造业案例。

**业务含义**: 运维效率驱动反映IT团队资源约束普遍存在，安全合规驱动反映行业监管强化趋势。用户体验驱动上升反映消费者级体验期望渗透到企业网络。

**数据限制**: 所有案例来自供应商发布，运维效率驱动频率可能反映供应商推广重点而非客户实际优先级。需独立验证客户实际决策优先级。
```

---

## Parallel Processing Strategy (多 Agent 并行策略)

**IMPORTANT**: When quality requirements are satisfied, use parallel agents to maximize efficiency based on task volume.

### Parallel Agent Deployment Matrix

| 任务数量 | 并行策略 | 推荐Agent数量 | 效率预期 |
|----------|----------|---------------|----------|
| 1-5 个文档 | 单Agent串行处理 | 1 | 逐个分析，质量优先 |
| 6-15 个文档 | 小规模并行 | 2-3 | 50-70%效率提升 |
| 16-30 个文档 | 中规模并行 | 4-5 | 200-300%效率提升 |
| 31-50 个文档 | 大规模并行 | 6-8 | 400-600%效率提升 |
| 50+ 个文档 | 批量并行处理 | 8-10 | 最大化吞吐量 |

### Parallel Processing Workflow

```
Phase 1: 任务分发
├── 识别待分析文档列表
├── 按行业/年份/规模分组
├── 创建并行Agent任务包
└── 启动并行Agent处理

Phase 2: 并行执行
├── Agent 1: 处理文档组 A (如教育行业)
├── Agent 2: 处理文档组 B (如医疗行业)
├── Agent 3: 处理文档组 C (如酒店行业)
├── ...
└── 各Agent独立生成分析报告

Phase 3: 结果整合
├── 收集所有Agent输出结果
├── 执行完整性检查验证
├── 生成问题文档清单
└── 输出处理报告汇总
```

### Agent Task Package Structure

每个并行Agent任务包应包含：
- **文档列表**: 明确分配的分析文档路径
- **输出目录**: 指定的输出结果存放位置
- **质量检查**: 内置的输出完整性自检机制
- **异常处理**: 遇到无法分析的文档时的处理流程

---

## Processing Progress Report (处理过程进展报告)

**IMPORTANT**: During parallel processing, generate real-time progress reports to track execution status and identify issues promptly.

### Progress Report Requirements

进展报告应在以下时机生成：
- **每个Agent任务开始时**: 记录任务启动信息
- **每批次文档处理完成后**: 更新进度统计
- **遇到问题文档时**: 实时记录问题
- **所有任务完成时**: 生成最终汇总报告

### Progress Report Output Structure

```
# Scenario Engine Processing Progress Report

## 任务执行概况
- **任务启动时间**: YYYY-MM-DD HH:MM:SS
- **预计完成时间**: YYYY-MM-DD HH:MM:SS
- **当前执行阶段**: Phase 1/2/3
- **并行Agent数量**: X 个

## 实时进度统计
- **输入文档总数**: X 个
- **正在处理文档**: Y 个 (当前Agent任务)
- **已完成文档**: Z 个
- **问题文档**: W 个
- **当前完成率**: Z/X %

## Agent 任务状态追踪
| Agent ID | 分配文档数 | 已完成数 | 问题数 | 状态 | 开始时间 | 预计完成 |
|----------|------------|----------|--------|------|----------|----------|
| Agent-1 | 10 | 8 | 0 | 进行中 | 10:00:00 | 10:30:00 |
| Agent-2 | 10 | 10 | 1 | 已完成 | 10:00:00 | 10:25:00 |
| Agent-3 | 10 | 5 | 0 | 进行中 | 10:00:00 | 10:35:00 |
| ... | ... | ... | ... | ... | ... | ... |

## 当批处理详情
### 本批次成功文档
| 序号 | 文档名 | 客户名 | 行业 | 处理时长 | 输出文件 | 完整性检查 |
|------|--------|--------|------|----------|----------|------------|
| 1 | doc-001.pdf | Customer A | 教育 | 5min | output-001.md | ✓ 12章节完整 |
| 2 | doc-002.pdf | Customer B | 医疗 | 4min | output-002.md | ✓ 12章节完整 |
| ... | ... | ... | ... | ... | ... | ... |

### 本批次问题文档
| 序号 | 文档名 | 问题类型 | 发现时间 | Agent ID | 处理建议 |
|------|--------|----------|----------|----------|----------|
| 1 | doc-003.pdf | PDF损坏 | 10:15:00 | Agent-2 | 重新获取原始文档 |
| ... | ... | ... | ... | ... | ... |

## 预计剩余时间
- **剩余文档数量**: X 个
- **预计剩余时间**: Y 分钟
- **预计完成时间**: HH:MM:SS

## 异常告警
- [!] Agent-2 遇到PDF损坏文档，已跳过继续处理
- [!] Agent-4 处理进度落后，预计延迟10分钟
- [!] 整体完成率低于预期，建议增加Agent数量

## 下一步行动
- [ ] 继续处理剩余 X 个文档
- [ ] 处理已识别的 Y 个问题文档
- [ ] 等待所有Agent完成任务
```

### Progress Report Update Frequency

| 执行阶段 | 更新频率 | 更新内容 |
|----------|----------|----------|
| **Phase 1 任务分发** | 任务启动时 | Agent分配、文档分组、预计时间 |
| **Phase 2 并行执行** | 每批次完成后 | 进度统计、问题文档、Agent状态 |
| **Phase 3 结果整合** | 所有任务完成时 | 最终汇总、完整性验证结果 |

### Progress Report Storage Location

进展报告应存储在指定目录：
```
/output_directory/
├── progress/
│   ├── progress_YYYYMMDD_HHMMSS_phase1.md  (任务启动报告)
│   ├── progress_YYYYMMDD_HHMMSS_batch1.md  (第一批次进展)
│   ├── progress_YYYYMMDD_HHMMSS_batch2.md  (第二批次进展)
│   ├── ...
│   └── progress_YYYYMMDD_HHMMSS_final.md   (最终汇总报告)
├── analysis/
│   ├── output-001.md
│   ├── output-002.md
│   └── ...
└── problems/
    ├── problem_documents_list.md
    └── incomplete_reports_list.md
```

### Progress Report Usage Scenarios

| 使用场景 | 报告用途 |
|----------|----------|
| **实时监控** | 了解当前处理进度，发现异常及时干预 |
| **问题定位** | 识别问题文档和问题Agent，快速处理 |
| **资源调整** | 根据进度落后情况动态调整Agent数量 |
| **最终验证** | 确认所有文档处理完成，生成最终报告 |

---

## Post-Analysis Validation (分析后完整性检查)

**IMPORTANT**: After all analyses complete, perform comprehensive validation to ensure all documents are processed and identify problematic documents.

### Validation Process

```
Step 1: 文档清单对比
├── 输入文档总数统计
├── 成功分析文档统计
├── 未处理文档识别
└── 问题文档标记

Step 2: 输出完整性验证
├── 检查每个报告的12章节完整性
├── 验证追溯性引用格式
├── 确认量化指标表达规范
└── 标记不完整报告

Step 3: 问题文档清单生成
├── 无法读取的文档（PDF损坏、格式错误）
├── 内容缺失的文档（信息不足、结构混乱）
├── 语言识别困难的文档（多语言混合、翻译质量差）
└── 输出不完整的报告（需补充分析）
```

### Processing Report Output Structure

分析完成后必须生成处理报告：

```
# Scenario Engine Processing Report

## 执行概况
- **输入文档总数**: X 个
- **成功分析文档**: Y 个
- **问题文档数量**: Z 个
- **分析成功率**: Y/X %

## 成功分析文档清单
| 序号 | 文档名 | 行业 | 客户名 | 年份 | 输出文件 |
|------|--------|------|--------|------|----------|
| 1 | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |

## 问题文档清单
| 序号 | 文档名 | 问题类型 | 问题描述 | 建议处理方式 |
|------|--------|----------|----------|--------------|
| 1 | ... | PDF损坏 | 无法提取文本内容 | 重新获取原始文档 |
| 2 | ... | 内容不足 | 缺少客户信息和解决方案描述 | 补充其他来源信息 |
| 3 | ... | 格式错误 | 表格嵌套无法解析 | 手动预处理后重新分析 |
| ... | ... | ... | ... | ... |

## 输出完整性验证结果
| 序号 | 输出文件 | 缺失章节 | 需补充内容 | 状态 |
|------|----------|----------|------------|------|
| ... | ... | ... | ... | 待补充/已完成 |

## 建议与后续行动
- [ ] 处理问题文档清单中的X个文档
- [ ] 补充Y个报告的缺失章节
- [ ] 验证Z个报告的追溯性引用
```

### Problem Document Categories

| 问题类型 | 定义 | 处理建议 |
|----------|------|----------|
| **PDF损坏/无法读取** | PDF文件损坏或格式不兼容 | 重新获取原始文档或使用OCR工具 |
| **内容严重缺失** | 缺少客户基本信息、购买要素等核心内容 | 标记为"信息不足"，尝试补充其他来源 |
| **结构混乱/无法解析** | 文档结构混乱，无法提取结构化信息 | 手动预处理后重新分析 |
| **语言识别困难** | 多语言混合或翻译质量差导致理解困难 | 使用专业翻译工具辅助 |
| **输出不完整** | 分析报告缺失部分章节 | 重新分析补充缺失内容 |

---

## Analyzer Workflow from Parser Data

### Step-by-Step Process

**Based on Parser extracted.json + extracted.md**:

```
Step 1: Load Parser Output
├── Read extracted.json (structured data)
├── Read extracted.md (context verification)
└── Validate input completeness

Step 2: Customer Info Processing (Section 0)
├── Extract from content_extract field
├── Verify company identity basis and filename-not-primary rule
├── Format initial_state from parser
├── Format final_state from parser
└── Generate customer basic info table with before/after comparison

Step 3: Purchase Elements Analysis (Section 1)
├── Analyze metrics_mentions for quantification and before/after deltas
├── Rank purchase factors by strategic intent and business value
├── Build MoE analysis with source, argument, and basis
├── Add supplementary explanations
└── Parameterize each element

Step 4: Stakeholder Analysis (Section 2)
├── Classify stakeholder_mentions by role type
├── Split layer from role title
├── Categorize pain_points_mentions
├── Determine influence levels
├── Map relationships (Hierarchical/Collaborative/Conflicting/Dependency)
├── Generate stakeholder table with synthesis

Step 5: Conflicts & Priority (Section 3)
├── Identify conflicting expectations
├── Analyze stakeholder priorities
├── Recommend resolution approaches

Step 6: State Model Generation (Section 4)
├── Identify ConOps operational threads
├── Build actor states from business operations
├── Build system/solution states from enabling capabilities
├── Link transitions to before/after outcomes and MoE
└── Generate ConOps-grounded transition explanations

Step 7: Environment Model (Section 5)
├── Organize industry constraints from environment_mentions
├── Organize regional constraints
├── Organize organizational constraints
├── Organize technical constraints
└── Generate 4-dimension environment tables

Step 8: Entity Model (Section 6)
├── Build organization hierarchy from stakeholder_mentions
├── Build system hierarchy from product_mentions
├── Identify external entity connections
└── Generate entity tree structures

Step 9: Lifecycle Phases (Section 7)
├── Extract from lifecycle_mentions
├── Define phase triggers/actions/completion criteria
└── Generate phase sequence table

Step 10: Operational Scenarios (Section 8)
├── Build from scenario_mentions
├── Define trigger/condition/transition structure
├── Generate scenario flow tables

Step 11: Engagement & Commitment (Section 9)
├── Recommend stakeholder participation stages
├── Define evaluation focus per stakeholder

Step 12: Products & Solutions (Section 10)
├── Organize product_mentions hierarchy
├── Map products to entity model
├── Generate product table

Step 13: Parameterization Model (Section 11)
├── Collect metrics_mentions
├── Define role attributes
├── Define scenario parameters
├── Define constraint parameters
└── Generate parameterization tables

Step 14: Traceability & Notes (Section 12)
├── Compile all raw_quotes
├── Add Chinese rendering for non-Chinese quotes
├── List inference notes
├── Document analysis methodology
```

### Parser-to-Analyzer Data Mapping

| Parser JSON Field | Analyzer Section | Usage |
|-------------------|------------------|-------|
| `content_extract` | Section 0 | Basic info table and company identity basis |
| `initial_state` | Section 0 | Problem context |
| `final_state` | Section 0 | Outcome summary |
| `stakeholder_mentions` | Section 2 | Stakeholder classification |
| `pain_points_mentions` | Section 2 | Pain point categorization |
| `metrics_mentions` | Section 1, 1.1, 11 | Purchase ranking, MoE, Parameterization |
| `product_mentions` | Section 10 | Products hierarchy |
| `environment_mentions` | Section 5 | 4-dimension model |
| `scenario_mentions` | Section 8 | Operational scenarios |
| `lifecycle_mentions` | Section 7 | Phase sequence |
| `raw_quotes` | Section 12 | Traceability compilation |

---

## When to Use

- **Customer story analysis**: When a vendor customer story is provided in PDF or text form
- **Stakeholder mapping**: When you need to identify users, customers, operators, maintainers, regulators, suppliers, and other stakeholder groups
- **Expectation capture**: When different stakeholder needs, values, risks and conflicts must be surfaced
- **Operational scenarios**: When you want to define how the solution is expected to be used and operated
- **Solution discovery**: When you need to identify actual products, services and technical solutions referenced in the story
- **Generic workflow**: When output should be structured and reusable beyond a single tool or platform
- **Traceability**: When the analysis must be tied back to specific sections or wording from the original story

## Key Capabilities

### Stakeholder Extraction
Identify and classify stakeholder groups, purchase elements, expectations, influences, conflicts, and lifecycle participation.

### Customer Story Traceability
Link each analysis item back to the original customer story text or PDF section, preserving wording and context.

### Operational Scenarios Capture
Produce a structured view of how the customer expects the system to be used, including use contexts, operating scenarios, and success conditions.

### Product & Solution Identification
Extract the product, service, and solution elements that are described or implied by the customer story, and map them to stakeholder needs.

### PDF Processing Tools
When direct PDF reading is not available, use external PDF processing tools to extract text content before analysis. Recommended tools include:
- PDF text extraction utilities (pdftotext, pdf2txt)
- Online PDF converters
- OCR tools for scanned PDFs
- Manual text extraction and copying

## Analysis Requirements

For each customer story, the SKILL should produce:

### Core Information
- **Customer basic information**: document title, country, industry, company name, and document year
- **Initial state description**: problems before solution deployment, organizational context
- **Final state description**: overall benefits and outcomes after solution deployment

### Purchase Analysis
- **Purchase elements**: 3-5 business-level buying factors described in the story, evaluated and ranked by business importance. Prioritize elements that align with the customer's core business needs, strategic objectives, and value propositions. Focus on what drives the fundamental business decisions rather than just technical features. For each purchase element, include quantified assessment information, detailing how the customer quantifies the value of this element across different dimensions, including before-and-after changes (e.g., cost reduction from X to Y, time savings of Z%, efficiency improvements).
- **Strategic and business intent**: For each purchase element, explicitly explain the strategic intent and business intent it serves.
- **MoE analysis**: For each major outcome, identify candidate MoE indicators and explain their source, argument, and evidence basis.

### Stakeholder Analysis
- **Stakeholder listing**: Who the stakeholders are, their organizational layer, and their specific role titles
- **Pain points and challenges**: Specific difficulties each stakeholder faces in current state, including workflow bottlenecks, efficiency obstacles, and experience barriers
- **Expectations/needs**: What each stakeholder expects or requires from the system
- **Influence and value**: How stakeholders influence the system or are affected by it, including value and risk
- **Relationship types**: Hierarchical, Collaborative, Conflicting, or Dependency relationships between stakeholders
- **Priority and conflict**: Conflicting expectations, relative priorities, and potential risks
- **Engagement and commitment**: Suggested stakeholder involvement in decision, evaluation, acceptance, and lifecycle activities

### State Model (for OpenSCENARIO)
- **ConOps operational threads**: Mission/business threads showing who acts, through what capability, toward what outcome
- **Actor and system states**: States must be derived from actual operations and enabling capabilities
- **Before/after outcome linkage**: State transitions should connect pre-deployment problems to post-deployment outcomes
- **State transition triggers**: Conditions that trigger state changes

### Environment Model (for OpenSCENARIO)
- **Industry environment**: Regulations, standards, compliance requirements, industry policies
- **Regional environment**: National regulations, cultural characteristics, market maturity
- **Organizational environment**: Scale, architecture type, budget constraints, strategic direction
- **Technical environment**: Existing tech stack, integration constraints, technical standards

### Entity Model (for OpenSCENARIO)
- **Organization entity hierarchy**: Company → Department → Team → Role tree structure
- **System entity composition**: Solution → Products → Services tree structure
- **External entity connections**: Supplier, Regulator, Partner relationships

### Lifecycle Model (for OpenSCENARIO)
- **Lifecycle phases**: Need Identification → Evaluation → Decision → Deployment → Acceptance → Operations
- **Phase triggers**: Start conditions for each phase
- **Phase actions**: Key activities per phase
- **Phase completion criteria**: End conditions for each phase

### Operational Scenarios
- **Running scenarios**: Key usage flows with trigger conditions, execution conditions, and state transitions
- **Scenario structure**: Trigger → Actions → Conditions → Result (State Transition)
- **Environmental assumptions**: Contextual constraints and prerequisites

### Product/Solution View
- **Product/solution identification**: The products, services, and solution elements referenced or implied
- **Entity mapping**: Map products/solutions to entity hierarchy

### Parameterization Model (for OpenSCENARIO)
- **Metric parameters**: Quantified metrics with name, type, value, unit structure
- **Role attribute parameters**: Influence level, priority, participation phase attributes
- **Scenario parameters**: Deployment time, coverage scale, user count parameters
- **Constraint parameters**: Budget limit, time constraints, compliance requirements

## Required Output Format

The output should be structured with tables as the primary format and supplemental narrative explanation for key findings. Each analysis item should include a reference marker for traceability.

### Output Structure

```
## 0. 客户基本信息
   - 基本信息 table
   - 公司识别依据与置信度
   - 应用产品与方案之前的问题 (Initial State)
   - 整体使用效果/收益综述 (Final State)
   - 部署前后效果对比

## 1. 购买要素 (Purchase Elements with Parameterization)
   - 战略意图 / 业务意图 / 量化表达
   - 1.1 MoE 指标分析

## 2. 利益相关者清单 (Stakeholder List with Pain Points and Relationship Types)
   - 利益相关者表格（必须拆分层级与角色名，包含痛点/困难列）
   - 痛点综述说明

## 3. 冲突与优先级 (Conflicts and Priority)

## 4. 基于 ConOps 的状态模型 (ConOps-Grounded State Model)
   - ConOps 运行线程状态表
   - 角色状态表
   - 系统/方案状态表
   - 状态转换说明

## 5. 环境模型 (Environment Model)
   - 行业环境表
   - 地域环境表
   - 组织环境表
   - 技术环境表

## 6. 实体层级模型 (Entity Model)
   - 组织实体层级树
   - 系统实体组成树
   - 外部实体连接图

## 7. 生命周期阶段 (Lifecycle Phases)
   - 阶段序列表 (触发器/动作/完成标准)

## 8. 运行场景 (Operational Scenarios with Trigger/Transition)

## 9. 承诺与参与建议 (Engagement and Commitment)

## 10. 产品与解决方案 (Products and Solutions)

## 11. 参数化模型 (Parameterization Model)
   - 量化指标参数表
   - 角色属性参数表
   - 场景参数表
   - 约束参数表

## 12. 追溯与备注 (Traceability and Notes)
   - 非中文原文 + 中文释义
```

### Traceability Format

Each analysis item should include a reference marker such as:
- quoted text snippet
- page/section indication
- direct phrasing from the customer story

Example:
- Stakeholder: Operations Team
  - Expectation: "快速完成系统部署" (source: page 4, paragraph 2)

## Workflow Example

1. User provides PDF customer story or extracted text
2. **If PDF format**: Use PDF processing tools to extract readable text content
   - Convert PDF to text using pdftotext, pdf2txt, or online converters
   - Preserve page/section references for traceability
   - Clean extracted text for analysis
3. Use an LLM or analyst process to extract the relevant passages
4. Organize stakeholders and expectations into structured tables
5. Identify conflicting goals and recommend priority
6. Summarize product/solution concepts and usage scenarios

## PDF Processing Integration

### Tool Requirements
- **Text Extraction**: pdftotext, pdf2txt, or online PDF-to-text converters
- **OCR Support**: For scanned PDFs, use OCR tools like tesseract
- **Text Cleaning**: Remove formatting artifacts and preserve readable content

### Processing Steps
1. **Extract Text**: Convert PDF to plain text format
2. **Add References**: Mark page numbers, sections, or paragraph locations
3. **Clean Content**: Remove headers, footers, and formatting noise
4. **Validate**: Ensure extracted text is readable and complete

### Example Commands
```bash
# Using pdftotext (Linux/Mac)
pdftotext -layout input.pdf output.txt

# Using pdf2txt (Python)
pdf2txt.py -o output.txt input.pdf

# With page numbers
pdftotext -f 1 -l 10 input.pdf output.txt
```

### Traceability Preservation
- Include page references: "Page 3, paragraph 2"
- Section markers: "Section 2.1: Customer Challenges"
- Direct quotes with context

```
/scenario_analyzer
# Activate customer-story extraction and stakeholder analysis workflow
```

---

### Traceability Data Quality Rules (追溯数据质量规则)

**IMPORTANT**: All traceability data must follow these rules to ensure data authenticity and verifiability.

#### TR-01: Original Text Priority Principle (原始文本优先原则)

**Rule**: All "Original Quote" (原文引用) fields must extract original text from source files. Translations, paraphrasing, or summarized statements are prohibited.

| Field Type | Correct Practice | Wrong Practice | Explanation |
|------------|------------------|----------------|-------------|
| Original Quote | "Guest experience is everything" (original English) | "客人体验至上" (Chinese translation) | Extract original text as written in source |
| Original Quote | "运维简化30%" (original Chinese if source is Chinese) | "Operations simplified 30%" (English translation) | Maintain source language authenticity |

**Example**:
```
| Customer Name | Core Expectation | Original Quote | Source Case ID |
|---------------|------------------|----------------|----------------|
| Southern Sun | Seamless guest experience | "Guest experience is everything" | analysis_2026_SouthernSun.md |
| Austrian Red Cross | Operations efficiency improvement | "Operations simplified 30%" | analysis_2024_AustrianRedCross.md |
```

#### TR-02: Multi-Language Case Language Rule (多语言案例语言规则)

**Rule**: When source files are primarily in one language (typically English for vendor case studies), original quotes should be extracted in that source language. If the source file itself contains Chinese text, then extract the original Chinese.

| Source Language | Quote Language | Example |
|-----------------|----------------|---------|
| English source (vendor case study) | English quote | "Guest experience is everything" |
| Chinese source | Chinese quote | "运维效率提升30%" |
| Mixed language source | Primary language quote | Use the dominant language in source |

#### TR-03: Quote Source Location Rule (引用来源定位规则)

**Rule**: Original quotes must include precise location markers (line number, page number, or paragraph number) to enable traceability verification.

| Location Format | Example | Usage |
|-----------------|---------|-------|
| Line number | "第15行" or "Line 15" | Text-extracted documents |
| Page + paragraph | "Page 3, paragraph 2" | PDF documents |
| Section reference | "Section 2.1: Customer Challenges" | Structured documents |

---

### Table Format Specification Rules (表格格式规范规则)

**IMPORTANT**: All tables must follow standardized format specifications to ensure consistency and readability.

#### TF-01: Role Detailed Attributes Table Standard Column Order (角色详细属性表标准列顺序)

**Rule**: Role Detailed Attributes tables must follow the fixed column order: `Customer Name | Core Expectation | Original Quote | Source Case ID`

| Standard Order | Column Description | Example |
|-----------------|--------------------|---------|
| 1. Customer Name | Specific customer attribution | Southern Sun |
| 2. Core Expectation | Business-oriented user need | Seamless guest experience |
| 3. Original Quote | Original text from source file | "Guest experience is everything" |
| 4. Source Case ID | Source document reference | analysis_2026_SouthernSun.md |

**Wrong Practice**:
```
| Customer Name | Original Quote | Core Expectation | Source Case ID |  ❌ Wrong order
```

**Correct Practice**:
```
| Customer Name | Core Expectation | Original Quote | Source Case ID |  ✓ Correct order
```

#### TF-02: Business-Oriented Content Rule (业务导向内容规则)

**Rule**: "Core Expectation" (期望核心) fields must describe user needs from business perspective, not technical solution perspective.

| Perspective | Example | Correct/Wrong |
|-------------|---------|---------------|
| Business perspective | Seamless guest experience, operations efficiency improvement | ✓ Correct |
| Technical perspective | Wi-Fi 6E deployment, Central cloud management | ❌ Wrong |

**Transformation Examples**:
| Technical Description | → Business-Oriented Description |
|-----------------------|--------------------------------|
| Wi-Fi 6E deployment | Seamless wireless-first experience |
| Central cloud management | Remote unified management capability |
| ClearPass NAC | Secure BYOD authentication automation |

---

### Role Coverage Completeness Rules (角色覆盖完整性规则)

**IMPORTANT**: Role coverage must ensure comprehensive representation across all significant industries.

#### RC-01: Industry User Role Mandatory Coverage (行业用户角色强制覆盖)

**Rule**: Role Detailed Attributes must cover user roles from all industries with frequency ≥5%. Each qualifying industry must have at least one user role (non-decision-maker/non-IT-lead) detailed attributes section.

| Industry | Frequency Threshold | Required Coverage |
|----------|--------------------|-------------------|
| Higher Education | ≥5% | Student/Faculty user roles required |
| Healthcare | ≥5% | Patient/Medical staff user roles required |
| Hospitality | ≥5% | Guest/Resident user roles required |
| Manufacturing | ≥5% | Production worker user roles required |
| Government/Public | ≥5% | Civil servant/Public service user roles required |
| K-12 Education | ≥5% | Student user roles required |
| Retail | ≥5% | Consumer/Customer user roles required |
| IT Services | ≥5% | Enterprise customer user roles required |

#### RC-02: User Role Classification Completeness (用户角色分类完整性)

**Rule**: Each industry must include at least one industry-specific user role detailed attributes section. User roles are defined as non-managerial, non-IT-lead roles (e.g., Students, Guests, Patients, Production Workers, Consumers).

| Role Category | Examples | Required per Industry |
|---------------|----------|----------------------|
| User Role (End User) | Students, Guests, Patients, Consumers, Production Workers | ≥1 section per qualifying industry |
| Decision Maker | CEO, CIO, IT Director | Covered separately |
| IT Lead | CTO, Network Manager, IT Manager | Covered separately |

#### RC-03: Role Section Numbering Convention (角色章节编号规范)

**Rule**: Role detailed attributes section numbering should follow hierarchical structure: `R-main-number` for primary roles, `R-main-number.sub-number` for role sub-categories.

| Numbering Pattern | Usage | Example |
|-------------------|-------|---------|
| R-01 to R-12 | Primary role categories | R-01 CIO/CTO, R-07 Students |
| R-XX.Y | Role sub-categories within same category | R-09.1 Hotel Guests (sub-category of R-09 Venue Audience) |

---

### Synthesis Update Linkage Rules (综述更新联动规则)

**IMPORTANT**: Synthesis sections must be updated when new role sections are added.

#### SU-01: Synthesis Table Synchronous Update (综述表同步更新)

**Rule**: When new Role Detailed Attributes sections are added, Role Need Synthesis table must synchronously add corresponding role category rows.

| Action Required | Trigger Condition | Example |
|-----------------|-------------------|---------|
| Add synthesis table row | New R-XX section added | Add "Manufacturing Worker" row when R-13 is added |
| Update role count | Multiple new sections added | Update total role count in synthesis |

#### SU-02: Synthesis Description Expansion (综述说明扩展)

**Rule**: Synthesis description section must reflect expectation patterns of newly added role categories.

| Synthesis Element | Update Requirement |
|-------------------|-------------------|
| Role Layer Summary | Add description for new role categories |
| Industry-Specific Patterns | Document industry-specific user expectations |
| Expectation Pattern Analysis | Include new role expectation patterns |

---

### Role Detailed Attributes Completeness Check (新增完整性检查项)

**Part B.5 Role Detailed Attributes Completeness Check**:
```
- [ ] Original Quote Language Correctness: All original quotes are in source file's original language ✓/✗
- [ ] Table Column Order Compliance: All tables follow "Customer Name | Core Expectation | Original Quote | Source Case ID" ✓/✗
- [ ] Core Expectation Business-Oriented: All expectations are business needs, not technical solutions ✓/✗
- [ ] Industry User Role Coverage: All frequency ≥5% industries include ≥1 user role section ✓/✗
- [ ] Synthesis Table Synchronous Update: Synthesis table includes all new role categories ✓/✗
- [ ] Synthesis Description Expansion: Synthesis description reflects new role patterns ✓/✗
```

---

## Version History

- **0.7.0** (2026-04-21):
  - **Architecture Split**: Analyzer now accepts scenario_parser output (MD + JSON) as primary input
  - **Updated Input Requirements**: Added Parser Output input specification with JSON structure requirements
  - **Added Analyzer Workflow from Parser Data**: Step-by-step process for generating analysis from extracted data
  - **Added Parser-to-Analyzer Data Mapping**: Field-to-section mapping table
  - **Updated Description**: Changed from direct PDF processing to downstream analysis generation
  - **Legacy Support**: Direct text/PDF input still supported for backward compatibility

- **0.6.0** (2026-04-16):
  - **Added Stakeholder Pain Points Extraction**: New dimension for extracting role-specific challenges, workflow bottlenecks, efficiency obstacles, and experience barriers before solution deployment
  - **Updated Quality Requirements**: Added pain point accuracy validation requirement with original text verification
  - **Updated Output Completeness Checklist**: Added pain point extraction completeness check (Section 2.1)
  - **Updated Stakeholder Analysis Section**: Pain points now precede expectations to establish problem-to-need causal chain
  - **Updated Output Format**: Section 2 renamed to include "Pain Points" dimension with required synthesis section

- **0.5.0** (2026-04-16):
  - **Added Traceability Data Quality Rules**: TR-01 Original Text Priority Principle, TR-02 Multi-Language Case Language Rule, TR-03 Quote Source Location Rule
  - **Added Table Format Specification Rules**: TF-01 Role Detailed Attributes Table Standard Column Order, TF-02 Business-Oriented Content Rule
  - **Added Role Coverage Completeness Rules**: RC-01 Industry User Role Mandatory Coverage, RC-02 User Role Classification Completeness, RC-03 Role Section Numbering Convention
  - **Added Synthesis Update Linkage Rules**: SU-01 Synthesis Table Synchronous Update, SU-02 Synthesis Description Expansion
  - **Updated Output Completeness Checklist**: Added Role Detailed Attributes Completeness Check (6 items)

- **0.4.0** (2026-04-14): Added Statistical Conclusion Standards - Customer uniqueness principle (each customer counts once in statistics), Multi-customer citation requirements (list top 3-5 important customers), Business driver/purchase element elaboration requirements (each item needs supplementary explanation), Analysis table summary requirements (each table needs synthesis and elaboration section)
- **0.3.0** (2026-04-14): Major enhancement - Added Quality Requirements section with mandatory quality standards and output completeness checklist; Added Parallel Processing Strategy for multi-Agent efficiency optimization based on task volume; Added Processing Progress Report for real-time progress tracking during execution; Added Post-Analysis Validation process with processing report generation and problem document identification
- **0.2.0** (2026-04-11): Added OpenSCENARIO DSL preparation support - State Model, Environment Model, Entity Model, Lifecycle Phases, Parameterization Model, Relationship Types, enhanced Operational Scenarios with trigger/transition
- **0.1.0** (2026-04-10): Initial customer-story based INCOSE requirements engineering SKILL draft
