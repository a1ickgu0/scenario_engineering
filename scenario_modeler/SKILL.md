---
name: scenario_modeler
description: "Scenario modeling SKILL for synthesizing and abstracting Industry Model, Stakeholder Model, and Purchase Factor Model from multiple scenario_analyzer analysis outputs. Prepares structured inputs for OpenSCENARIO DSL modeling with lifecycle, state, environment, entity, relationship, and parameterization models."
tags:
  - scenario-modeling
  - synthesis-analysis
  - industry-model
  - stakeholder-model
  - purchase-factor
  - openscenario-preparation
  - cross-case-analysis
version: "0.9.0"
---

# Scenario Modeler SKILL

## Overview

This SKILL synthesizes and abstracts structured models from multiple `scenario_analyzer` analysis outputs. It transforms individual case-level analyses into cross-case inductive models that reveal patterns, commonalities, and variations across industries, stakeholders, and purchase decisions.

**Primary Outputs**:
1. **Industry Model**: Industry patterns, challenges, stakeholder distributions, solution preferences
2. **Stakeholder Model**: Two-layer structure (Category Layer + Role Layer) with mappings
3. **Purchase Factor Model**: Hierarchical structure (Business Driver + Technical Implementation + Quantified Metrics)

**Strategic Market Advisory Outputs (Gartner-style)**:
4. **Use Case Fit Model**: Which use cases fit which customer segments, triggers, and solution patterns
5. **Critical Capability Model**: Which capabilities are table stakes, differentiators, emerging differentiators, or optional enhancers by use case
6. **Buying Committee Model**: Who approves, blocks, validates, operates, funds, and uses the solution, and what proof each role needs
7. **Competitive Positioning Model**: Market boundary, alternatives, differentiators, table stakes, proof burden, and positioning risks

**Supporting Models for OpenSCENARIO Preparation**:
8. **Lifecycle Model**: Scenario phases, triggers, actions, completion criteria
9. **State Model**: Stakeholder/system/organization states and transitions
10. **Environment Model**: Industry constraints, regional characteristics, organizational context
11. **Entity Model**: Organizations, systems, external entities with attributes
12. **Relationship Model**: Hierarchical, collaborative, conflicting, dependency relations
13. **Interaction Sequence Model**: Actor-to-actor action flows with triggers and conditions
14. **Parameterization Model**: Configurable parameters for metrics, roles, scenarios, constraints

---

## Quality Requirements

**IMPORTANT**: All model synthesis must strictly follow the requirements below to ensure content completeness and analysis quality.

### Mandatory Quality Standards

| Quality Dimension | Requirement Standard | Acceptance Method |
|-------------------|---------------------|-------------------|
| **Completeness** | Three core models must be fully generated, each model contains all required sections | Output checklist verification |
| **Traceability** | Each model conclusion must annotate customer name - original quote - Chinese translation (for non-Chinese sources) | Citation format check |
| **Accuracy** | Aggregated conclusions must accurately reflect source case content, frequency statistics must be precise | Source case cross-reference verification |
| **Structure** | Matrix tables must be complete, tree structures must have clear hierarchy, hierarchical relationships complete | Format compliance check |
| **Criticality** | Each model must contain critical analysis chapter, conclusion credibility rating must be annotated | Critical chapter check |
| **Confidence** | All inferred information must have explicit confidence level (HIGH/MEDIUM/LOW) and basis category | Confidence level check |
| **MoE Credibility** | All quantified metrics must have MoE indicators with source traceability and credibility assessment | MoE indicator check |
| **Business Priority** | Analysis must follow business-first principle: business background and business drivers analyzed before technical implementation | Analysis order verification |
| **Business Insight Quality** | Primary models must explain context, pressure, stakeholder tension, purchase factor, capability, measurable outcome, counter-evidence, and recommended action before inventory tables | Business Insight Quality Framework check |
| **Template Conformance** | Every output must follow its bound template exactly: required sections, section order, table schemas, and completion placeholders must be preserved or filled | Template compliance check |
| **Strategic Market Advisory Quality** | Gartner-style outputs must define market/use-case boundary, critical capabilities, buying committee, competitive alternatives, proof burden, evidence strength, and scenario implication | Gartner-style strategic modeling check |

### Mandatory Template Output Rules

**CRITICAL**: `scenario_modeler` is a template-driven SKILL. Free-form model reports are invalid even when their content is analytically correct.

#### TR-01 Template Binding

Before generating any model output, bind the target output to its template file and read the template structure.

| Output | Required Template |
|--------|-------------------|
| Industry Model | `assets/templates/industry-model-template.md` |
| Stakeholder Model | `assets/templates/stakeholder-model-template.md` |
| Purchase Factor Model | `assets/templates/purchase-factor-template.md` |
| Use Case Fit Model | `assets/templates/use-case-fit-model-template.md` |
| Critical Capability Model | `assets/templates/critical-capability-model-template.md` |
| Buying Committee Model | `assets/templates/buying-committee-model-template.md` |
| Competitive Positioning Model | `assets/templates/competitive-positioning-model-template.md` |
| Cross Analysis | `assets/templates/cross-analysis-template.md` |
| Lifecycle Model | `assets/templates/lifecycle-model-template.md` |
| State Model | `assets/templates/state-model-template.md` |
| Environment Model | `assets/templates/environment-model-template.md` |
| Entity Model | `assets/templates/entity-model-template.md` |
| Relationship Model | `assets/templates/relationship-model-template.md` |
| Interaction Sequence Model | `assets/templates/interaction-sequence-template.md` |
| Parameterization Model | `assets/templates/parameterization-template.md` |
| Stakeholder Category Model | `assets/templates/stakeholder-category-template.md` |
| Stakeholder Role Model | `assets/templates/stakeholder-role-template.md` |
| Solution Preference Model | `assets/templates/solution-preference-template.md` |
| Conflict Pattern Model | `assets/templates/conflict-pattern-template.md` |
| Template Compliance Check Report | `assets/templates/template-compliance-check-template.md` |

#### TR-02 No Section Dropping or Merging

All headings from the bound template must appear in the generated output in the same order. Do not drop, rename, merge, or reorder template sections. If evidence is missing, keep the section and mark it as `No direct evidence found` with a limitation note and recommended validation question.

#### TR-03 Table Schema Preservation

All template tables must preserve their required columns. Columns may be filled, expanded with additional rows, or supplemented with extra columns only when needed, but required columns must not be removed or renamed.

#### TR-04 Placeholder Completion

Template placeholders such as `[INSIGHT]`, `[CASE_IDS]`, `[CUSTOMER_NAME]`, `[QUOTE]`, `[HIGH/MEDIUM/LOW]`, and `TBD` must be replaced with case-grounded content. If the source data does not support a field, fill it with a clear evidence-gap statement instead of leaving the placeholder.

#### TR-05 Template Deviation Control

Any deviation from the bound template must be listed in the final validation report with:
- Deviated section or table
- Reason for deviation
- Risk to downstream use
- Corrective action or explicit user approval requirement

Unexplained template deviation is a blocking defect.

### Output Completeness Checklist

Each model output must contain all of the following sections:

**Template Compliance Check (applies to every output file)**:
```
Bound template file declared ✓/✗
All template headings present ✓/✗
Template heading order preserved ✓/✗
Required table columns preserved ✓/✗
All placeholders replaced or explicitly marked as evidence gaps ✓/✗
No free-form replacement of template structure ✓/✗
Deviation log present when deviations exist ✓/✗
```

**Industry Model Completeness Check**:
```
## Document Information ✓/✗
## 0. Executive Industry Insight Summary ✓/✗
## 1. Industry Classification ✓/✗
## 2. Regional Distribution ✓/✗
## 3. Typical Challenges by Industry (Enhanced Traceability) ✓/✗
## 4. Stakeholder Distribution by Industry ✓/✗
## 5. Solution Preference by Industry (Enhanced Traceability) ✓/✗
## 6. Purchase Factor Synthesis per Industry (MANDATORY - 3-5 items each) ✓/✗
## 7. Key Insights (Enhanced Traceability) ✓/✗
## 8. Traceability Summary (Enhanced - 4 Sub-tables) ✓/✗
## 9. Critical Analysis (MANDATORY) ✓/✗
## 10. Notes ✓/✗
```

**Stakeholder Model Completeness Check**:
```
## Document Information ✓/✗
## Part 0: Stakeholder Decision System ✓/✗
## Part A: Category Layer (类别层) ✓/✗
  - Category Definitions ✓/✗
  - Category × Industry Matrix ✓/✗
  - Category Typical Expectations ✓/✗
  - Category Influence Distribution ✓/✗

## Part B: Role Layer (角色层) ✓/✗
  - Master Role Catalog ✓/✗
  - Category → Role Hierarchy ✓/✗
  - Role × Industry Matrix ✓/✗
  - Role Detailed Attributes ✓/✗

## Part C: Key Insights (Enhanced Traceability) ✓/✗
## Part D: Traceability Summary (Enhanced - 4 Sub-tables) ✓/✗
## Part E: Critical Analysis (MANDATORY) ✓/✗
## Part F: Notes ✓/✗
```

**Purchase Factor Model Completeness Check**:
```
## Document Information ✓/✗
## 0. Executive Business Insight Summary ✓/✗
## 1. Business Driver Layer Frequency Distribution ✓/✗
## 2. Technical Implementation Layer Frequency Distribution ✓/✗
## 3. Quantified Metric Patterns ✓/✗
## 4. Industry × Business Driver Priority Matrix ✓/✗
## 5. Business Driver → Technical Implementation → Solution Chain ✓/✗
## 6. Purchase Factor Detailed Analysis Table (Enhanced Traceability) ✓/✗
## 7. Stakeholder × Driver Mapping ✓/✗
## 8. Key Insights (Enhanced Traceability) ✓/✗
## 9. Traceability Summary (Enhanced - 4 Sub-tables) ✓/✗
## 10. Critical Analysis (MANDATORY) ✓/✗
## 11. Notes ✓/✗
```

**Cross Analysis Completeness Check**:
```
## Document Information ✓/✗
## 0. Strategic Cross-Model Insight Summary ✓/✗
## 1. Industry × Stakeholder Category Matrix ✓/✗
## 2. Industry × Stakeholder Role Matrix (Top Roles) ✓/✗
## 3. Industry × Business Driver Matrix ✓/✗
## 4. Stakeholder Category × Business Driver Matrix ✓/✗
## 5. Stakeholder Role × Business Driver Matrix (Top Roles) ✓/✗
## 6. Stakeholder Category × Conflict Matrix ✓/✗
## 7. Key Cross-Dimension Insights ✓/✗
## 8. Traceability Summary ✓/✗
## Notes ✓/✗
```

**Use Case Fit Model Completeness Check**:
```
## Document Information ✓/✗
## 0. Executive Use-Case Fit Summary ✓/✗
## 1. Market and Use-Case Definition ✓/✗
## 2. Use Case × Industry Fit Matrix ✓/✗
## 3. Use Case Decision Logic ✓/✗
## 4. Adoption Trigger and Barrier Analysis ✓/✗
## 5. Use Case Fit Scoring ✓/✗
## 6. Traceability Summary ✓/✗
## 7. Strategic Insights ✓/✗
## 8. Notes ✓/✗
```

**Critical Capability Model Completeness Check**:
```
## Document Information ✓/✗
## 0. Executive Capability Summary ✓/✗
## 1. Capability Taxonomy ✓/✗
## 2. Capability × Use Case Criticality Matrix ✓/✗
## 3. Table Stakes vs Differentiator Analysis ✓/✗
## 4. Capability Weighting by Industry ✓/✗
## 5. Capability Proof Burden ✓/✗
## 6. Capability-to-Scenario Mapping ✓/✗
## 7. Traceability Summary ✓/✗
## 8. Strategic Insights ✓/✗
## 9. Notes ✓/✗
```

**Buying Committee Model Completeness Check**:
```
## Document Information ✓/✗
## 0. Executive Buying Committee Summary ✓/✗
## 1. Buying Committee Role Taxonomy ✓/✗
## 2. Role × Use Case Influence Matrix ✓/✗
## 3. Buying Journey Decision Map ✓/✗
## 4. Stakeholder Proof Burden ✓/✗
## 5. Buying Committee Archetypes ✓/✗
## 6. Engagement Playbook ✓/✗
## 7. Traceability Summary ✓/✗
## 8. Strategic Insights ✓/✗
## 9. Notes ✓/✗
```

**Competitive Positioning Model Completeness Check**:
```
## Document Information ✓/✗
## 0. Executive Competitive Positioning Summary ✓/✗
## 1. Market Definition and Boundary ✓/✗
## 2. Competitive Alternative Map ✓/✗
## 3. Vendor Narrative vs Customer Evidence ✓/✗
## 4. Differentiator vs Table Stakes Matrix ✓/✗
## 5. Positioning by Use Case ✓/✗
## 6. Competitive Risk and Objection Analysis ✓/✗
## 7. Proof Burden and Validation Plan ✓/✗
## 8. Scenario Modeling Implications ✓/✗
## 9. Traceability Summary ✓/✗
## 10. Strategic Insights ✓/✗
## 11. Notes ✓/✗
```

### Traceability Requirements

Each model conclusion must include:
- **Source Case ID**: Annotate contributing case list (e.g., "Aberdeen City Council, Southern Sun, Chase Center")
- **Frequency Statistics**: Annotate pattern occurrence frequency (e.g., "53.3% frequency, 65 mentions")
- **Customer Name**: Annotate specific customer name for key conclusions
- **Original Quote**: Retain key expressions from source cases (e.g., "Guest experience is everything")
- **Quote Location**: Source file page, paragraph or line number annotation

Example format:
```
| Pattern Discovery | Frequency | Customer Name | Original Quote | Source Cases |
|-------------------|-----------|---------------|----------------|--------------|
| Operations efficiency is primary driver | 53.3% | Austrian Red Cross, Aberdeen City Council | "Operations simplified 30%" / "AIOps reduces burden 70%" | 65 cases |
```

---

### Statistical Conclusion Standards

**IMPORTANT**: All statistical conclusions in model synthesis must follow these standards to ensure accuracy and completeness.

#### 1. Customer Statistics Uniqueness Principle

**Rule**: Each customer can only count as 1 in frequency statistics, even if the source case mentions the same pattern multiple times.

| Statistics Type | Correct Practice | Wrong Practice | Explanation |
|-----------------|------------------|----------------|-------------|
| Frequency Statistics | Customer A appears 1 time | Customer A appears 3 times | Even if source case mentions 3 times, count only 1 time in statistics |
| Original Quote | "Operations simplified 30%" (mentioned 3 times, lines 15/25/35) | Only annotate line 15 | Annotate customer mention count and all locations |
| Source Case Count | 65 cases (65 customers) | 65 mentions (possibly fewer than 65 customers) | Frequency = Source Case Count = Customer Count |

**Example**:
```
| Business Driver | Frequency (Customer Count) | Percentage | Main Customers (3-5) | Original Quote |
|----------|--------------|------|-----------------|----------|
| 运维效率优化 | 65次(65个客户) | 53.3% | Austrian Red Cross, Aberdeen City Council, University of Illinois | "运维简化30%" (ARC, 提及2次); "AIOps减负70%" (Aberdeen, 提及1次) |
```

#### 2. 多客户原文引用规范

**规则**: 统计结果涉及多客户时，必须列出多客户的原文引用；客户数>5时，列出最重要的3-5个。

| 客户数量 | 引用要求 | 重要性判断标准 |
|----------|----------|----------------|
| 1个客户 | 列出该客户的完整引用 | N/A |
| 2-5个客户 | 列出所有客户的原文引用 | 全部列出 |
| >5个客户 | 列出最重要的3-5个客户原文 | 量化明确、表述典型、行业代表、时间新颖 |

**重要性判断标准**:
1. **量化表达明确**: 有具体数字（如"70%"、"30天→3天"）
2. **原文表达典型**: 表述清晰、可直接引用、代表性强
3. **行业代表性**: 代表主要行业（教育/医疗/酒店/制造）或典型场景
4. **时间新颖性**: 近期案例优先（2024-2026年优先于2021-2022年）

**示例**:
```
| 业务驱动 | 频率 | 占比 | 主要客户(Top 5) | 原文引用 |
|----------|------|------|-----------------|----------|
| 运维效率优化 | 65次 | 53.3% | Austrian Red Cross(2024), Aberdeen City Council(2026), University of Illinois(2024), Grove City College(2025), Cheval Collection(2024) | "运维简化30%" (ARC); "AIOps减负70%" (Aberdeen); "troubleshooting days→hours" (UI); "部署速度显著提升" (Grove City); "部署时间减少90%" (Cheval) |
| 安全合规需求 | 48次 | 39.3% | Australian Defence Apparel(2025), Amiri Hospital(2021), Waldkliniken Eisenberg(2023), Royal Devon Healthcare(2024), Schnellecke Logistics(2025) | "ISO 27001 compliant" (ADA); "HIMSS Level 5认证" (Amiri); "患者数据保护" (Waldkliniken); "零信任安全" (Schnellecke) |
```

#### 3. 业务驱动/购买要素补充说明规范

**规则**: 每个业务驱动或购买要素不能仅用单词语表达，必须增加补充说明。

| 内容类型 | 要求格式 | 补充说明内容要求 |
|----------|----------|------------------|
| 业务驱动 | **标题**: 补充说明 | 具体表现、量化指标、实现方式、业务价值 |
| 购买要素 | **标题**: 补充说明 | 技术方案、量化效果、业务重要性、实现路径 |
| 技术能力 | **标题**: 补充说明 | 功能描述、业务驱动链接、典型行业、部署方式 |

**补充说明内容框架**:
```
**业务驱动/购买要素**: [标题]
├── **具体表现**: 该驱动/要素的具体表现形式
├── **量化指标**: 相关的量化数据（如有）
├── **实现方式**: 通过何种技术或方案实现
├── **业务价值**: 对客户业务的实际价值
└── **典型行业**: 该驱动最突出的行业分布
```

**示例**:
```
| 业务驱动 | 频率 | 补充说明 | 主要行业 | 源案例 |
|----------|------|----------|----------|--------|
| **运维效率优化**: 网络运维负担减轻，从被动响应转为主动预防，Central云管理+AIOps自动化实现运维减负 | 65次 | 具体表现: 运维简化、工单减少、故障自愈; 量化: 30%效率提升、70%减负、100%工单减少; 实现: Central云管理+AIOps; 价值: IT团队战略聚焦 | 教育、医疗、酒店 | Austrian Red Cross, Aberdeen City Council, University of Illinois |
| **安全合规需求**: ISO 27001/HIMSS合规认证，零信任架构实现访问控制，监管约束是硬性不可妥协要求 | 48次 | 具体表现: 认证达成、零信任架构、数据保护; 量化: ISO认证、HIMSS Level 5、100%数据安全; 实现: ClearPass+Zero Trust; 价值: 合规通过、供应链准入 | 医疗、政府、金融 | Australian Defence Apparel, Amiri Hospital, Schnellecke Logistics |
```

#### 4. 分析表综述说明规范

**规则**: 每个分析表格输出后，必须补充一段综述说明，对表中内容进行综述及展开说明。

**综述说明结构**:
```
[表格输出]

**综述说明**:

**核心发现**: 表格中最重要的模式或结论（1-2项）
- 描述最重要的发现及其统计支持

**分布特征**: 各项的分布规律和集中趋势
- 分布集中度、头部模式占比、尾部分布特征

**异常观察**: 特殊情况或异常数据点
- 异常高/低频率、行业特定异常、时间趋势异常

**业务含义**: 对客户决策或业务的影响
- 驱动优先级含义、行业差异含义、时间演变含义

**数据限制**: 数据来源限制或可信度说明
- 供应商偏差影响、覆盖不足影响、量化缺失影响
```

**示例**:
```
## 1. Business Driver Layer 频率分布

| 业务驱动 | 频率 | 占比 | 补充说明 | 主要客户(Top 5) | 原文引用 |
|----------|------|------|----------|-----------------|----------|
| **运维效率优化** | 65次 | 53.3% | 网络运维负担减轻... | ARC, Aberdeen... | ... |
| **安全合规需求** | 48次 | 39.3% | ISO/HIMSS合规认证... | ADA, Amiri... | ... |
| **用户体验提升** | 45次 | 36.9% | 无缝连接、数字体验... | Gloria, Chase... | ... |
| ... | ... | ... | ... | ... | ... |

**综述说明**:

**核心发现**:
- 运维效率优化是跨行业首要业务驱动（53.3%），反映网络运维负担是普遍痛点
- 安全合规需求虽频率较低（39.3%），但在医疗和政府行业是首要驱动（60%+），是硬性不可妥协要求

**分布特征**:
- 运维效率、安全合规、用户体验三大驱动占总驱动的89.5%（129/143），形成核心驱动三角
- 成本优化在制造业优先级最高（CELSA 40%成本节约典型），但在教育行业优先级较低（$200K savings仅1例）
- 频率分布呈长尾形态，前3驱动占89.5%，后5驱动仅占10.5%

**异常观察**:
- IoT/智能建筑驱动频率仅12.3%，但在酒店行业2025-2026案例中提及率上升至25%，呈新兴趋势
- 可持续发展驱动仅6.6%（8次），全部集中在欧洲制造业案例（CELSA, Bosch），反映区域行业特征
- 业务扩张驱动在酒店业高频出现（Premier Inn 90%部署减少），但在医疗行业几乎不出现

**业务含义**:
- 运维效率驱动反映IT团队资源约束普遍存在，运维自动化成为跨行业共同诉求
- 安全合规驱动反映行业监管强化趋势，医疗行业HIMSS认证、制造业ISO 27001成为准入门槛
- 用户体验驱动上升反映消费者级体验期望渗透到企业网络，酒店业"Guest experience is everything"成为典型表达

**数据限制**:
- 所有案例来自供应商发布，运维效率驱动频率可能反映供应商推广重点而非客户实际决策优先级
- 部分驱动量化表达不完整（仅30%案例有量化数据），频率统计准确性受影响
- 需独立验证客户实际决策优先级，可信度评级: ★★★☆☆（中等可信，供应商视角偏差）
```

---

### Critical Analysis Requirements (批判性分析要求)

每个模型必须包含批判性分析章节，内容包括：
- **数据来源限制评估**: 供应商视角偏差、幸存者偏差、量化数据来源限制
- **客观校正**: 原始结论 vs 客观校正对比表
- **技术方案评估**: 供应商声称效果 vs 客户验证状态 vs 客观评估
- **结论可信度评级**: 星级评分（★☆☆☆☆ to ★★★★☆）

---

## Parallel Processing Strategy (多 Agent 并行策略)

**IMPORTANT**: When quality requirements are satisfied, use parallel agents to maximize efficiency based on model complexity and input volume.

### Parallel Agent Deployment Matrix

| 输入规模 | 并行策略 | 推荐Agent数量 | 效率预期 |
|----------|----------|---------------|----------|
| 1-30 个源案例 | 单Agent串行处理 | 1 | 逐个模型合成，质量优先 |
| 31-60 个源案例 | 小规模并行 | 2-3 | 各模型独立Agent处理 |
| 61-100 个源案例 | 中规模并行 | 3-4 | Industry/Stakeholder/Purchase并行 |
| 101-150 个源案例 | 大规模并行 | 4-5 | 模型并行+跨分析并行 |
| 150+ 个源案例 | 批量并行处理 | 5-6 | 最大化吞吐量 |

### Parallel Processing Workflow

```
Phase 1: 数据准备与分发
├── 收集所有 scenario_analyzer 分析输出
├── 统计源案例数量和行业分布
├── 按模型类型创建Agent任务包
│   ├── Agent-Industry: 行业模型合成
│   ├── Agent-Stakeholder: 利益相关者模型合成
│   ├── Agent-Purchase: 购买因素模型合成
│   └── Agent-CrossAnalysis: 跨维度矩阵生成
└── 启动并行Agent处理

Phase 2: 并行模型合成
├── Agent-Industry: 处理行业分布、挑战、解决方案偏好
│   ├── 行业分类统计
│   ├── 区域分布矩阵
│   ├── 典型挑战频率表
│   └── 解决方案偏好分析
├── Agent-Stakeholder: 处理类别层和角色层
│   ├── 类别定义和频率统计
│   ├── 角色-类别映射
│   ├── 影响力分布
│   └── 共现模式识别
├── Agent-Purchase: 处理三层结构
│   ├── 业务驱动频率统计
│   ├── 技术实现映射
│   ├── 量化指标模式
│   └── 解决方案链
└── Agent-CrossAnalysis: 处理跨维度矩阵
    ├── Industry × Role 矩阵
    ├── Industry × Purchase Factor 矩阵
    └── Role × Purchase Factor 矩阵

Phase 3: 结果整合与验证
├── 收集所有Agent输出结果
├── 执行模型完整性检查
├── 整合批判性分析章节
├── 生成追溯性汇总表
├── 输出处理报告
└── 验证可信度评级标注
```

### Agent Task Package Structure

每个并行Agent任务包应包含：
- **源案例范围**: 明确分配的分析案例范围（如按行业分组）
- **输出模型**: 指定的模型输出类型（Industry/Stakeholder/Purchase）
- **质量检查**: 内置的输出完整性自检机制
- **追溯要求**: 强制包含客户名-原文引用格式
- **批判分析**: 内置批判性分析模板

---

## Processing Progress Report (处理过程进展报告)

**IMPORTANT**: During parallel model synthesis, generate real-time progress reports to track execution status and identify issues promptly.

### Progress Report Requirements

进展报告应在以下时机生成：
- **每个Agent任务开始时**: 记录模型合成启动信息
- **每个模型章节完成后**: 更新进度统计
- **遇到数据缺失时**: 实时记录问题
- **所有模型完成时**: 生成最终汇总报告

### Progress Report Output Structure

```
# Scenario Modeler Processing Progress Report

## 任务执行概况
- **任务启动时间**: YYYY-MM-DD HH:MM:SS
- **预计完成时间**: YYYY-MM-DD HH:MM:SS
- **当前执行阶段**: Phase 1/2/3
- **并行Agent数量**: X 个
- **源案例总数**: Y 个

## 实时进度统计
- **输入源案例总数**: X 个
- **正在处理模型**: Y 个 (当前Agent任务)
- **已完成模型**: Z 个
- **问题模型**: W 个
- **当前完成率**: Z/7 % (3 primary models + 4 strategic market advisory models)

## Agent 任务状态追踪
| Agent ID | 分配模型 | 源案例数 | 已完成章节 | 缺失章节 | 状态 | 开始时间 |
|----------|----------|----------|------------|----------|------|----------|
| Agent-Industry | Industry Model | 122 | 9/9 | 0 | 已完成 | 10:00:00 |
| Agent-Stakeholder | Stakeholder Model | 122 | 5/5 | 0 | 进行中 | 10:00:00 |
| Agent-Purchase | Purchase Factor Model | 122 | 7/9 | 2 | 进行中 | 10:00:00 |
| Agent-CrossAnalysis | Cross-Analysis | 122 | 2/4 | 2 | 待启动 | - |

## 当前模型合成详情
### Industry Model 进度
| 章节 | 状态 | 源案例覆盖 | 追溯性标注 | 批判分析 |
|------|------|------------|------------|----------|
| 1. Industry Classification | ✓ 完成 | 122/122 | ✓ | N/A |
| 2. Regional Distribution | ✓ 完成 | 122/122 | ✓ | N/A |
| 3. Typical Challenges | ✓ 完成 | 100/122 | ✓ | N/A |
| 4. Stakeholder Distribution | ✓ 完成 | 122/122 | ✓ | N/A |
| 5. Solution Preferences | ✓ 完成 | 98/122 | ✓ | N/A |
| 6. Purchase Factor Synthesis | ✓ 完成 | 85/122 | ✓ | ✓ |
| 7. Key Insights | ✓ 完成 | 122/122 | ✓ | N/A |
| 8. Traceability Summary | ✓ 完成 | 122/122 | ✓ | N/A |
| 9. Critical Analysis | ✓ 完成 | N/A | N/A | ✓ |

### Stakeholder Model 进度
| 章节 | 状态 | 源案例覆盖 | 追溯性标注 | 批判分析 |
|------|------|------------|------------|----------|
| Part A: Category Layer | ✓ 完成 | 122/122 | ✓ | N/A |
| Part B: Role Layer | ✓ 完成 | 122/122 | ✓ | N/A |
| Part C: Key Insights | ✓ 完成 | 122/122 | ✓ | N/A |
| Part D: Traceability | ✓ 完成 | 122/122 | ✓ | N/A |
| Part E: Critical Analysis | ○ 进行中 | N/A | N/A | ○ |

### Purchase Factor Model 进度
| 章节 | 状态 | 源案例覆盖 | 追溯性标注 | 批判分析 |
|------|------|------------|------------|----------|
| 1. Business Driver Layer | ✓ 完成 | 122/122 | ✓ | N/A |
| 2. Technical Implementation | ✓ 完成 | 122/122 | ✓ | N/A |
| 3. Quantified Metrics | ✓ 完成 | 46/122 | ✓ | N/A |
| 4. Industry × Driver Matrix | ✓ 完成 | 122/122 | ✓ | N/A |
| 5. Solution Chain | ✓ 完成 | 122/122 | ✓ | N/A |
| 6. Stakeholder × Driver | ✓ 完成 | 122/122 | ✓ | N/A |
| 7. Key Insights | ○ 进行中 | 122/122 | ○ | N/A |
| 8. Traceability Summary | ○ 待开始 | N/A | N/A | N/A |
| 9. Critical Analysis | ○ 待开始 | N/A | N/A | ○ |

## 数据缺失问题记录
| 序号 | 模型章节 | 缺失类型 | 影响案例数 | 处理建议 |
|------|----------|----------|------------|----------|
| 1 | Quantified Metrics | 部分案例无量化数据 | 76个案例 | 标注为"量化表达不完整" |
| 2 | Purchase Factor Synthesis | 部分行业案例不足 | 3个行业 | 基于现有案例推断，可信度降级 |

## 预计剩余时间
- **剩余模型数量**: X 个
- **剩余章节数量**: Y 个
- **预计剩余时间**: Z 分钟
- **预计完成时间**: HH:MM:SS

## 异常告警
- [!] Agent-Purchase 处理进度落后，量化数据提取复杂度高
- [ ] Purchase Factor Model 缺失2个章节，需要补充
- [ ] 76个案例无量化数据，需标注可信度降级

## 下一步行动
- [ ] 完成 Agent-Stakeholder 批判分析章节
- [ ] 完成 Agent-Purchase Key Insights 和 Traceability 章节
- [ ] 启动 Agent-CrossAnalysis 跨维度矩阵生成
- [ ] 整合所有模型输出并验证完整性
```

### Progress Report Storage Location

进展报告应存储在指定目录：
```
/output_directory/
├── progress/
│   ├── progress_YYYYMMDD_HHMMSS_phase1.md  (任务启动报告)
│   ├── progress_YYYYMMDD_HHMMSS_phase2.md  (模型合成进展)
│   ├── progress_YYYYMMDD_HHMMSS_final.md   (最终汇总报告)
├── models/
│   ├── industry_model.md
│   ├── stakeholder_model.md
│   └── purchase_factor_model.md
├── strategic_models/
│   ├── use_case_fit_model.md
│   ├── critical_capability_model.md
│   ├── buying_committee_model.md
│   └── competitive_positioning_model.md
├── cross_analysis/
│   └ cross_analysis_matrix.md
└── validation/
    ├── template_compliance_check.md
    ├── completeness_check.md
    ├── business_insight_check.md
    └── credibility_ratings.md
```

---

## Post-Analysis Validation

**IMPORTANT**: After all model synthesis complete, perform comprehensive validation in the following order:

### Validation Process

```
Step 0: Data Consistency Validation (NEW - Must execute first)
├── Baseline Data Confirmation
│   ├── Input source case total: N
│   ├── Stakeholder entry total: M (from stakeholder_model.md)
│   └── Average stakeholders per case: M/N
│
├── Case Count Unit Verification
│   ├── Industry × Year Matrix year total verification
│   ├── Industry × Year Matrix industry total verification
│   ├── Year × Region Matrix year total verification
│   ├── Year × Region Matrix region total verification
│   └── Verification formula: Σ(total) = N ✓
│
├── Stakeholder Entry Count Verification
│   ├── Industry × Role Matrix role total verification
│   ├── Industry × Role Matrix industry total verification
│   └── Verification formula: Σ(total) ≈ M (allow ±5% variance)
│
├── Multi-dimensional Unit Confirmation
│   ├── Industry × Purchase Factor: total > N, explained ✓
│   ├── Purchase Factor × Year: total > N, explained ✓
│   ├── Role × Purchase Factor: total >> N, explained ✓
│   ├── Solution × Industry: total > N, explained ✓
│
├── Unit Annotation Completeness Check
│   ├── Check each matrix has statistical unit annotation
│   ├── Check each matrix has total row/column
│   ├── Check each matrix has verification note
│   └── Check multi-dimensional matrices have "one case multiple X" explanation
│
└── Generate Data Consistency Validation Report

Step 1: Source Case Coverage Verification
├── Input source case total statistics
├── Each model's source case citation statistics
├── Identify uncited source cases
└── Calculate coverage rate

Step 2: Template Compliance Verification
├── Confirm each output declares or maps to the required template
├── Compare generated headings against template headings
├── Verify heading order is unchanged
├── Verify required table columns are present and not renamed
├── Detect unresolved placeholders: [.*], TBD, TODO, N/A without evidence-gap note
├── Identify sections replaced by generic summaries
└── Generate Template Compliance Check Report

Step 3: Model Completeness Verification
├── Check Industry Model 11 template sections completeness
├── Check Stakeholder Model 7 template sections completeness
├── Check Purchase Factor Model 12 template sections completeness
├── Check Use Case Fit Model 10 template sections completeness
├── Check Critical Capability Model 11 template sections completeness
├── Check Buying Committee Model 11 template sections completeness
├── Check Competitive Positioning Model 13 template sections completeness
├── Check Cross Analysis template sections completeness
├── Verify traceability citation format
└── Confirm critical analysis chapter exists

Step 4: Data Quality Verification
├── Frequency statistics accuracy verification
├── Customer name - original quote consistency verification
├── Credibility rating rationality verification
└── Critical analysis logic completeness verification

Step 5: Business Insight Quality Verification
├── Executive insight summary presence verification
├── Business reasoning chain completeness verification
├── Product-as-factor guard verification
├── Counter-evidence and measurement gap verification
└── Recommended action specificity verification

Step 6: Strategic Market Advisory Verification
├── Use case boundary and fit scoring verification
├── Critical capability classification verification
├── Buying committee proof-burden verification
├── Competitive alternative and differentiator verification
├── Scenario modeling implication verification
└── Gartner-style framework compliance verification

Step 7: Issue List Generation
├── Uncited source case list
├── Missing sections list
├── Incomplete traceability list
├── Missing credibility rating list
├── Template deviation list
├── Strategic advisory gap list
└── Unresolved placeholder list
```

### Processing Report Output Structure

After model synthesis completion, must generate processing report:

```
# Scenario Modeler Processing Report

## Execution Summary
- **Input source case total**: X
- **Successfully synthesized models**: Y (Industry/Stakeholder/Purchase)
- **Problem model count**: Z
- **Synthesis success rate**: 100% (all core models must complete)

## Source Case Coverage Verification
| Model Name | Cited Cases | Coverage Rate | Uncited Cases | Status |
|------------|-------------|---------------|---------------|--------|
| Industry Model | 122/122 | 100% | 0 | ✓ Complete |
| Stakeholder Model | 122/122 | 100% | 0 | ✓ Complete |
| Purchase Factor Model | 46/122 | 37.7% | 76 | ○ Quantified data insufficient |

## Template Compliance Verification Results
| Output File | Bound Template | Heading Match | Heading Order | Required Columns | Placeholder Resolution | Deviations | Status |
|-------------|----------------|---------------|---------------|------------------|------------------------|------------|--------|
| industry_model.md | industry-model-template.md | 11/11 | ✓ | ✓ | ✓ | 0 | ✓ Pass |
| stakeholder_model.md | stakeholder-model-template.md | 7/7 | ✓ | ✓ | ✓ | 0 | ✓ Pass |
| purchase_factor_model.md | purchase-factor-template.md | 12/12 | ✓ | ✓ | ✓ | 0 | ✓ Pass |
| use_case_fit_model.md | use-case-fit-model-template.md | 10/10 | ✓ | ✓ | ✓ | 0 | ✓ Pass |
| critical_capability_model.md | critical-capability-model-template.md | 11/11 | ✓ | ✓ | ✓ | 0 | ✓ Pass |
| buying_committee_model.md | buying-committee-model-template.md | 11/11 | ✓ | ✓ | ✓ | 0 | ✓ Pass |
| competitive_positioning_model.md | competitive-positioning-model-template.md | 13/13 | ✓ | ✓ | ✓ | 0 | ✓ Pass |
| cross_analysis_matrix.md | cross-analysis-template.md | 10/10 | ✓ | ✓ | ✓ | 0 | ✓ Pass |

## Model Completeness Verification Results
| Model Name | Required Sections | Completed Sections | Missing Sections | Completeness | Critical Analysis |
|------------|------------------|-------------------|-----------------|--------------|-------------------|
| Industry Model | 11 | 11 | 0 | ✓ | ✓ Contains credibility rating |
| Stakeholder Model | 7 | 7 | 0 | ✓ | ✓ Contains credibility rating |
| Purchase Factor Model | 12 | 12 | 0 | ✓ | ✓ Contains credibility rating |
| Use Case Fit Model | 10 | 10 | 0 | ✓ | N/A |
| Critical Capability Model | 11 | 11 | 0 | ✓ | N/A |
| Buying Committee Model | 11 | 11 | 0 | ✓ | N/A |
| Competitive Positioning Model | 13 | 13 | 0 | ✓ | N/A |
| Cross Analysis | 10 | 10 | 0 | ✓ | N/A |

## Traceability Verification Results
| Model Name | Customer Name Annotation | Original Quote | Quote Location | Status |
|------------|-------------------------|----------------|----------------|--------|
| Industry Model | ✓ 100% | ✓ 100% | ✓ 85% | ✓ Qualified |
| Stakeholder Model | ✓ 100% | ✓ 100% | ✓ 90% | ✓ Qualified |
| Purchase Factor Model | ✓ 100% | ✓ 100% | ✓ 80% | ✓ Qualified |

## Credibility Rating Verification Results
| Model Name | Rating Chapter | Rating Dimensions | Missing Dimensions | Status |
|------------|---------------|-------------------|-------------------|--------|
| Industry Model | ✓ | 6 | 0 | ✓ Complete |
| Stakeholder Model | ✓ | 6 | 0 | ✓ Complete |
| Purchase Factor Model | ✓ | 5 | 0 | ✓ Complete |

## Data Quality Issue List
| ID | Issue Type | Impact Scope | Affected Model | Resolution |
|----|-----------|--------------|----------------|------------|
| 1 | Quantified data missing | 76 cases without quantified indicators | Purchase Factor Model | Mark credibility downgrade, retain existing data |
| 2 | Insufficient industry cases | 3 industries <5 cases | Industry Model | Infer from existing cases, annotate data limitations |
| 3 | Template deviation | Any missing heading, reordered section, removed required column, or unresolved placeholder | Any output | Blocking defect; repair output before final delivery |

## Recommendations and Follow-up Actions
- [ ] Supplement quantified data extraction for 76 cases
- [ ] Increase case collection for data-insufficient industries
- [ ] Verify credibility rating rationality for all models
- [ ] Generate supplementary cross-industry year evolution analysis chapter
```

### Problem Data Categories

| Issue Type | Definition | Resolution Recommendation |
|-----------|------------|---------------------------|
| **Insufficient source case citation** | Model does not cite some source cases | Check omissions, supplement citations or annotate data limitations |
| **Quantified data missing** | Large number of source cases without quantified indicators | Mark credibility downgrade, retain existing data completeness |
| **Incomplete traceability** | Missing customer name or original quote | Supplement traceability information, ensure format compliance |
| **Missing critical analysis** | Missing critical analysis chapter or credibility rating | Supplement critical analysis, annotate credibility rating |
| **Missing sections** | Model missing required sections | Supplement missing sections, ensure completeness |

---

## When to Use

- **Cross-case synthesis**: When you have multiple scenario_analyzer analysis outputs and need to identify patterns
- **Industry modeling**: When you need to understand industry-specific characteristics and commonalities
- **Stakeholder abstraction**: When you need to generalize stakeholder roles across cases
- **Purchase decision analysis**: When you need to identify common buying motivations and quantification patterns
- **OpenSCENARIO preparation**: When preparing structured inputs for DSL-based scenario modeling
- **Pattern discovery**: When searching for recurring themes, conflicts, or solution preferences

## Input Requirements

**Source Documents**: Multiple `-analysis.md` files generated by `scenario_analyzer` SKILL

**Required Fields per Document**:
- Customer basic information (industry, country, company, year)
- Purchase elements (ranked list with business value and metrics)
- Stakeholder listing (roles, expectations, influence, value/risk)
- Conflicts and priorities
- Operational scenarios
- Products and solutions

**Document Format**: Markdown with structured tables and traceability references

## Analysis Dimensions

### 1. Industry Model

| Dimension | Description | Output |
|-----------|-------------|--------|
| Industry Classification | Primary and secondary industry taxonomy | Industry hierarchy tree |
| Regional Distribution | Geographic patterns per industry | Region × Industry matrix |
| Typical Challenges | Common pain points per industry | Challenge frequency table |
| Stakeholder Distribution | Typical stakeholder roles per industry | Industry × Role matrix |
| Solution Preferences | Common product/solution combinations | Solution frequency table |

### 2. Stakeholder Model

**Two-Layer Structure**:

| Layer | Content | Purpose |
|-------|---------|---------|
| Category Layer | Abstract classifications (Decision Maker, IT Lead, Operator, User, Regulator, Partner) | Generalization for cross-industry comparison |
| Role Layer | Concrete roles extracted from cases (CEO, CIO, IT Director, Teacher, Student, etc.) | Specific instantiation for actual scenarios |
| Mapping | Category → Role mappings with frequency and industry context | Traceability and pattern recognition |

**Category Definitions**:

| Category | Definition | Typical Traits |
|----------|------------|----------------|
| Decision Maker | Final decision authority or budget approval | High influence, strategic view, ROI focus |
| IT Lead | Technical architecture and operations lead | High influence, technical view, feasibility focus |
| Operator | Daily operations and execution | Medium-high influence, execution view, efficiency focus |
| User | Direct system users | Medium influence, experience view, usability focus |
| Regulator | Policy, compliance, industry oversight | High constraint, compliance view, risk focus |
| Partner | External support and service providers | Medium influence, service view, collaboration focus |

### 3. Purchase Factor Model

**CRITICAL DEFINITION - Purchase Factor Clarification**:

**Purchase Factors are articulated from the customer/user's business value perspective, NOT the products/technologies they purchase.**

| Layer | Definition | Examples | Wrong Understanding |
|------|------|------|----------|
| **Purchase Factor** | Customer's business intent, value proposition, strategic goal | "30% operations efficiency improvement", "student wireless-first experience", "HIMSS Level 5 certification" | ❌ "Wi-Fi 6E APs", "Aruba Central" |
| **Technical Implementation** | Specific products/technologies purchased to achieve purchase factors | Wi-Fi 6/6E, Central cloud management, ClearPass NAC | ✓ This is technical implementation, NOT purchase factor |

**Purchase Factor vs Technical Implementation Comparison**:
```
Purchase Factor (Business Intent)    →    Technical Implementation (Product Purchased)
─────────────────────────────────────────────────────────────────────────────────────
Operations efficiency 30%            →    Central cloud management + AIOps
Security compliance (HIMSS Level 5)  →    ClearPass + Zero Trust architecture
Student wireless-first experience    →    Wi-Fi 6E full coverage
Cost efficiency 40% savings          →    SD-WAN replacing MPLS
Fan immersive experience             →    Wi-Fi 6E + Indoor Location
```

**Hierarchical Structure**:

| Level | Content | Examples |
|-------|---------|----------|
| Business Driver Layer (Purchase Factor Layer) | Why buy - business intent/value proposition/strategic goals | Operations efficiency improvement, security compliance certification, user experience enhancement, cost efficiency optimization, digital transformation, sustainability |
| Technical Implementation Layer | What capabilities to buy - products/technologies purchased to achieve purchase factors | Wi-Fi 6/6E coverage, Central cloud management, ClearPass NAC, SD-WAN, CX switches |
| Quantified Metrics Layer | How to measure success - quantified indicators measuring purchase factor achievement | Operations efficiency 30% improvement, HIMSS Level 5 certification, 100% user coverage, cost 40% savings |

### 4. Lifecycle Model

**Storyboard Structure**:

```
Scenario Lifecycle
├── Init
│   ├── Stakeholder initial state
│   ├── System initial state (pre-deployment)
│   └── Environment initial conditions
├── Phases
│   ├── Need Identification
│   ├── Evaluation & Selection
│   ├── Purchase Decision
│   ├── Deployment
│   ├── Acceptance
│   └── Operations
├── StartTrigger
│   └── Entry conditions for each phase
├── Actions
│   ├── Stakeholder actions
│   ├── System actions
│   └── Interaction actions
└── StopTrigger
    └── Completion criteria per phase
```

### 5. State Model

| State Type | States | Transition Triggers |
|------------|--------|---------------------|
| Stakeholder State | Need Identification → Evaluation → Decision → Acceptance → Operations → Satisfied/Dissatisfied | Phase completion, decision events, acceptance events |
| System State | Not Deployed → Deploying → Running → Upgrading → Fault → Recovered | Deployment start, acceptance pass, fault events |
| Organization State | Problem Identified → Solution Seeking → Procurement → Implementation → Normal Operation | Problem confirmed, contract signed, acceptance completed |

### 6. Environment Model

| Dimension | Elements | Examples |
|-----------|----------|----------|
| Industry Environment | Regulations, standards, compliance | HIPAA (healthcare), GDPR (Europe), 1:1 device policy (education) |
| Regional Environment | National regulations, cultural traits, market maturity | UK/US/Japan data compliance differences |
| Organizational Environment | Scale, architecture type, budget constraints | 67 schools, 26,500 students, public/private budget |
| Technical Environment | Tech stack, existing systems, integration constraints | Cloud transition, legacy network architecture |

### 7. Entity Model

| Entity Type | Definition | Attributes |
|-------------|------------|------------|
| Organization Entity | Companies, departments, teams, project groups | Name, scale, hierarchy, function |
| System Entity | Products, solutions, components, services | Name, version, function, state |
| External Entity | Suppliers, regulators, partners | Name, role, relationship, constraints |

### 8. Relationship Model

| Relation Type | Definition | Examples |
|---------------|------------|----------|
| Hierarchical | Superior-subordinate, management | CEO → CIO → IT Director |
| Collaborative | Joint participation, cooperation | IT Team ↔ Supplier |
| Conflicting | Conflict, competition | Cost Optimization ↔ Quality Improvement |
| Dependency | Pre/post dependency | Deployment Phase → Acceptance Phase |

### 9. Interaction Sequence Model

**Structure**:

```
Interaction Sequence
├── Trigger
├── Actor Actions
│   ├── Actor1 → Action1
│   ├── Actor2 → Action2
│   └── ...
├── Conditions
└── Result → State Transition
```

### 10. Parameterization Model

| Parameter Type | Definition | Examples |
|----------------|------------|----------|
| Metric Parameters | Performance, efficiency indicators | `fault_ticket_reduction: 100%`, `coverage_increase: 2x` |
| Role Attribute Parameters | Influence, priority, participation phase | `influence_level: high`, `priority: 1` |
| Scenario Parameters | Deployment time, coverage scale, user count | `deploy_time: 30min`, `user_count: 26500` |
| Constraint Parameters | Budget limit, time constraints, compliance | `budget_limit: X`, `compliance: HIPAA` |

## Cross-Analysis Matrixes

| Matrix | Dimensions | Purpose |
|--------|------------|---------|
| Industry × Role | Which roles are more common in which industries | Stakeholder distribution patterns |
| Industry × Purchase Factor | Which factors have higher priority in which industries | Purchase motivation patterns |
| Role × Purchase Factor | Which roles care about which factors | Stakeholder expectation patterns |
| Role × Conflict | Which roles are involved in which conflicts | Conflict stakeholder patterns |

## Strategic Market Advisory Models

These Gartner-style models are mandatory when the user requests market, industry, competitive, sales, or strategic analysis. They are also recommended for vendor case-study corpora in data communication, networking, and cybersecurity domains.

| Model | Purpose | Required Framework |
|-------|---------|--------------------|
| Use Case Fit Model | Determine which customer use cases fit which segments, adoption triggers, barriers, and scenario implications | `gartner-style-modeling-framework.md` |
| Critical Capability Model | Identify capability criticality, table-stakes vs differentiator status, proof burden, and scenario parameters | `gartner-style-modeling-framework.md` |
| Buying Committee Model | Model approval, blocking, validation, operation, funding, and user influence across the buying journey | `gartner-style-modeling-framework.md` |
| Competitive Positioning Model | Define market boundary, alternatives, vendor narrative vs customer evidence, differentiators, and proof burden | `gartner-style-modeling-framework.md` |

## Output Requirements

### Template-First Output Contract

Every output file must be generated from the corresponding template in `assets/templates/`. Treat the template as the output contract, not as a loose example.

For each generated file:
1. Declare the bound template at the top of the output or in the processing report.
2. Preserve every template heading in the same order.
3. Preserve required table columns from the template.
4. Fill all placeholder cells with source-grounded content or explicit evidence-gap text.
5. Do not replace a detailed template section with a summary paragraph.
6. After generation, run the Template Compliance Check and include the result in `validation/template_compliance_check.md` or the final processing report.

### Industry Model Output Structure

The Industry Model output must follow `industry-model-template.md` exactly and include the following sections in template order:

0. **Executive Industry Insight Summary**: Industry business thesis and cross-industry differentiation before inventory tables
1. **Industry Classification**: Primary and secondary industry taxonomy with case counts
2. **Regional Distribution**: Region × Industry matrix with concentration analysis
3. **Typical Challenges by Industry (Enhanced Traceability)**: Challenge types with frequency and original quotes
4. **Stakeholder Distribution by Industry**: Industry × Stakeholder category matrix
5. **Solution Preference by Industry (Enhanced Traceability)**: Cross-industry and industry-specific solution patterns
6. **Purchase Factor Synthesis per Industry (MANDATORY - 3-5 items each)**: **MANDATORY** - Each industry must have 3-5 purchase factors with:
   - Ranking and business importance
   - Typical expressions from source documents
   - **Customer name attribution** (e.g., "Aberdeen City Council")
   - **Original quote reference** (e.g., Page number or line number)
7. **Key Insights (Enhanced Traceability)**: Pattern discoveries with traceability, confidence, counter-evidence, and recommended action
8. **Traceability Summary (Enhanced - 4 Sub-tables)**: Enhanced traceability tables with customer names and original quotes
9. **Critical Analysis (MANDATORY)**: **MANDATORY** - Independent chapter addressing:
   - Data source limitations (supplier bias, survivorship bias)
   - Objective correction of industry insights
   - Technical solution objective assessment
   - Market distribution objective interpretation
   - Data usage recommendations
   - Conclusion credibility rating
10. **Notes**: Standardization notes, limitations, and follow-up actions

### Stakeholder Model Output Structure

The Stakeholder Model output must follow `stakeholder-model-template.md` exactly and include the following sections in template order:

**Part 0: Stakeholder Decision System**
1. **Decision System Map**: Decision owner, evidence owner, risk/compliance owner, affected user, delivery owner, decision tension, and required evidence
2. **Stakeholder Engagement Playbook**: Business question, proof need, objection, purchase factor strengthened, recommended engagement action, and confidence

**Part A: Category Layer**
1. **Category Definitions**: Six standard categories with definitions, traits, frequency, and source cases
2. **Category × Industry Distribution Matrix**: Distribution across 9+ industries with dominant category identification
3. **Industry Category Patterns**: High-frequency (>50%) and low-frequency (<20%) categories per industry
4. **Category Typical Expectations**: **Enhanced** - Each category expectation must include:
   - Customer name attribution (e.g., "Aberdeen City Council", "Southern Sun")
   - Original quote reference (Page number or line number)
   - Source case IDs
5. **Category Participation Phase Matrix**: Phase participation (✓/○) with source case attribution
6. **Category Influence Distribution**: Influence level distribution with source cases

**Part B: Role Layer**
1. **Master Role Catalog**: All roles with category mapping, frequency, industries, and source cases
2. **Category → Role Hierarchy**: Complete hierarchical tree structure
3. **Role × Industry Matrix**: Role distribution across industries with counts
4. **Industry-Specific Roles**: Industry-specific vs cross-industry role classification with notes
5. **Role Detailed Attributes**: **Enhanced** - Key roles must include:
   - Customer name attribution for each attribute
   - Original quote reference (Page number)
   - Source case IDs
6. **Role Co-occurrence Patterns**: Role pair frequency with customer name and original quote

**Part C: Key Insights**
- Pattern discoveries with **customer name**, **original quote**, **business implication**, and **source cases**

**Part D: Traceability Summary (Enhanced - 4 Sub-tables)**
1. **Category Traceability**: Source cases, frequency, customer name, original quote
2. **Role Traceability**: Source cases, frequency, customer name, original quote
3. **Industry Role Pattern Traceability**: Industry pattern with customer attribution
4. **Co-occurrence Pattern Traceability**: Role pairs with customer attribution

**Part E: Critical Analysis (MANDATORY)**
1. **Data Source Limitations Assessment**: Supplier bias, role overrepresentation, user scale variations, role definition variance
2. **Objective Stakeholder Correction**: Original vs objective correction for each major industry
3. **Role Influence Objective Assessment**: Supplier perspective vs objective assessment for key roles
4. **Stakeholder Distribution Objective Interpretation**: Supplier vs objective interpretation
5. **Data Usage Recommendations**: Guidance for stakeholder engagement, role mapping, influence assessment
6. **Conclusion Credibility Rating**: Star-based rating (★☆☆☆☆ to ★★★★☆) for:
   - Category definition credibility
   - IT Lead universality credibility
   - User role distribution credibility
   - Role influence level credibility
   - Industry role pattern credibility
   - Co-occurrence pattern credibility

**Part F: Notes**
- Category standardization notes
- Role standardization notes
- Data limitations
- Recommended follow-up

### Purchase Factor Model Output Structure

**CRITICAL**: Purchase Factor Model must follow "Business Intent Priority" principle. All analyses center on customer's business value propositions, NOT products/technologies.

The Purchase Factor Model output must follow `purchase-factor-template.md` exactly and include the following sections in template order:

0. **Executive Business Insight Summary**: Top business conclusions, business reasoning chain, and decision implication map before frequency tables

1. **Business Driver Layer Frequency Distribution**: Purchase factors (business intents) frequency distribution, including:
   - Frequency statistics (customer uniqueness principle)
   - Supplementary explanation (specific manifestations, quantified metrics, business value)
   - Top 5 customer original quotes

2. **Technical Implementation Layer Frequency Distribution**: Technical solutions purchased to achieve purchase factors, with explicit linkage to business drivers

3. **Quantified Metric Patterns**: Quantified measurement indicator type statistics and detailed metric evidence

4. **Industry × Purchase Factor Priority Matrix**: Industry × purchase factor priority matrix

5. **Business Driver → Technical Implementation → Solution Chain**: purchase factor → capability → solution mapping chain

6. **Purchase Factor Detailed Analysis Table (Enhanced Traceability)**: Detailed factor-level evidence, mechanism, customer quotes, metric gaps, and confidence

7. **Stakeholder × Driver Mapping**: Stakeholder category × driver mapping matrix and driver-stakeholder matrix

8. **Key Insights (Enhanced Traceability)**: Pattern discoveries with causal mechanism, segmentation, stakeholder implication, metric gaps, counter-evidence, confidence, and recommended action

9. **Traceability Summary (Enhanced - 4 Sub-tables)**: Business driver, technical implementation, quantified metric, and industry driver pattern traceability

10. **Critical Analysis (MANDATORY)**:
    - Data source limitations assessment
    - Objective purchase factor correction
    - Lead user identification credibility assessment
    - Year evolution evidence completeness assessment
    - Data usage recommendations
    - Conclusion credibility rating

11. **Notes**: Factor standardization notes, layer mapping notes, limitations, and recommended follow-up

### Gartner-Style Strategic Market Advisory Output Structure

All four strategic advisory outputs must follow `gartner-style-modeling-framework.md` and their bound templates exactly. They translate the primary models into market-facing guidance.

#### Use Case Fit Model

The Use Case Fit Model must follow `use-case-fit-model-template.md` exactly and include:
1. Market and use-case boundary
2. Use case × industry fit matrix
3. Decision logic by use case
4. Adoption trigger and barrier analysis
5. Fit scoring
6. Traceability and strategic insights
7. Scenario modeling implications

#### Critical Capability Model

The Critical Capability Model must follow `critical-capability-model-template.md` exactly and include:
1. Capability taxonomy for data communication domains
2. Capability × use case criticality matrix
3. Table stakes vs differentiator classification
4. Capability weighting by industry
5. Proof burden, MoE/KPI, and measurement gaps
6. Capability-to-scenario mapping
7. Traceability and strategic insights

#### Buying Committee Model

The Buying Committee Model must follow `buying-committee-model-template.md` exactly and include:
1. Buying committee role taxonomy
2. Role × use case influence matrix
3. Buying journey decision map
4. Stakeholder proof burden
5. Buying committee archetypes
6. Engagement playbook
7. Traceability and strategic insights

#### Competitive Positioning Model

The Competitive Positioning Model must follow `competitive-positioning-model-template.md` exactly and include:
1. Market definition and boundary
2. Competitive alternative map
3. Vendor narrative vs customer evidence
4. Differentiator vs table stakes matrix
5. Positioning by use case
6. Competitive risk and objection analysis
7. Proof burden and validation plan
8. Scenario modeling implications
9. Traceability and strategic insights

### Traceability Requirements (Enhanced)

Each model conclusion must include:
- **Source Cases**: List of case IDs that contributed to the conclusion
- **Frequency/Weight**: How often the pattern appears (e.g., "appears in 80% of Education cases")
- **Customer Name**: Specific customer attribution (e.g., "Aberdeen City Council", "Southern Sun")
- **Original Quote**: Key original wording with reference (e.g., Page number, line number, or paragraph)
- **Variations**: Exceptions or variations across cases

### Critical Analysis Requirements

The Critical Analysis chapter must address:

| Aspect | Required Content |
|--------|------------------|
| Data Source Limitations | Supplier perspective bias, survivorship bias, quantified data source concerns |
| Objective Industry Correction | Original conclusion vs objective correction for each major industry |
| Technical Solution Assessment | Supplier claimed effects vs customer verification status vs objective evaluation |
| Market Distribution Interpretation | Supplier perspective vs objective interpretation for regional patterns |
| Data Usage Recommendations | Guidance for different usage scenarios (market analysis, ROI calculation, risk assessment) |
| Conclusion Credibility Rating | Star-based rating (★☆☆☆☆ to ★★★★☆) for each conclusion type |

---

## Traceability Requirements

Each model conclusion must include:
- **Source Cases**: List of case IDs that contributed to the conclusion
- **Frequency/Weight**: How often the pattern appears (e.g., "appears in 80% of Education cases")
- **Customer Name**: Specific customer attribution for key conclusions
- **Original Quote**: Key original wording with reference (Page/Line number)
- **Variations**: Exceptions or variations across cases

---

## Data Consistency Validation (数据一致性检测)

**IMPORTANT**: After all model synthesis and cross-analysis matrix generation, perform comprehensive data consistency validation to ensure all statistics align with defined statistical口径.

### Statistical口径定义 (统计口径定义)

所有矩阵和表格必须明确标注统计口径，确保读者理解数据来源和计数规则：

| 统计口径类型 | 定义 | 基准数量 | 适用矩阵 |
|-------------|------|---------|----------|
| **案例数 (Case Count)** | 每个分析文件计1个 | **输入源案例总数N** | Industry × Year, Year × Region, Industry × Solution (如按案例计数) |
| **利益相关者条目数 (Stakeholder Entry Count)** | 每条stakeholder记录计1个 | **N × 平均利益相关者数** | Industry × Role, Role × Conflict |
| **购买因素提及次数 (Purchase Factor Mention Count)** | 每次购买因素被提及计1次 | **> N** (一案多因素) | Industry × Purchase Factor, Purchase Factor × Year |
| **角色×因素交叉数 (Role × Factor Cross Count)** | 角色-因素配对计数 | **利益相关者数 × 平均因素数** | Role × Purchase Factor |
| **解决方案提及次数 (Solution Mention Count)** | 每次解决方案被提及计1次 | **> N** (一案多方案) | Solution × Industry |

### Mandatory Consistency Checks (强制一致性检查)

**Phase 1: 案例数口径检查**

以下矩阵合计必须等于输入源案例总数：

| 矩阵 | 检查项 | 公式 | 预期结果 |
|------|--------|------|----------|
| Industry × Year Matrix | 年度合计 | Σ(各年度合计) | = N |
| Industry × Year Matrix | 行业合计 | Σ(各行业合计) | = N |
| Year × Region Matrix | 年度合计 | Σ(各年度合计) | = N |
| Year × Region Matrix | 区域合计 | Σ(各区域合计) | = N |

**验证示例**:
```
Industry × Year Matrix:
| 2019 | 2020 | 2021 | ... | 合计 |
|------|------|------|------|------|
| 21 | 24 | 29 | ... | N |

验证: 21 + 24 + 29 + ... = N ✓
```

**Phase 2: 利益相关者口径检查**

以下矩阵合计应与 stakeholder_model.md 中记录的利益相关者总数一致：

| 矩阵 | 检查项 | 公式 | 预期结果 |
|------|--------|------|----------|
| Industry × Role Matrix | 角色合计 | Σ(各角色合计) | ≈ 利益相关者总数 |
| Industry × Role Matrix | 行业合计 | Σ(各行业合计) | ≈ 利益相关者总数 |

**允许误差**: ±5%差异（因角色映射规则可能略有差异）

**Phase 3: 多维度口径说明**

以下矩阵合计**不应**等于案例数，必须在表格后明确说明：

| 矩阵 | 说明内容 | 示例 |
|------|----------|------|
| Industry × Purchase Factor | "一个案例可涉及多个购买因素，合计(XXX)大于案例数(N)" | 合计695 > 案例数167 |
| Purchase Factor × Year | "一个案例可涉及多个购买因素，年度合计大于各年度案例数" | 2021年合计142 > 2021年案例数29 |
| Role × Purchase Factor | "这是角色×购买因素交叉计数，合计(XXX)远大于案例数" | 合计4714 > 案例数167 |
| Solution × Industry | "一个案例可涉及多个解决方案，合计(XXX)大于案例数(N)" | 合计386 > 案例数167 |

### Output Format Requirements (输出格式要求)

**每个矩阵必须包含**:

1. **统计口径说明**: 在矩阵标题下方标注统计口径
   ```
   > **统计口径**: 案例数（总计167个案例）
   ```

2. **行/列合计**: 每个矩阵必须有行合计和列合计
   ```
   | 行业 | 2019 | 2020 | ... | **行业合计** |
   |------|------|------|------|------|
   | 教育 | 5 | 4 | ... | 26 |
   | **年度合计** | 21 | 24 | ... | **167** |
   ```

3. **数据核对注释**: 在矩阵后添加核对注释
   ```
   > **数据核对**: 年度合计21+24+...+20=167 ✓ 与案例总数一致
   ```

4. **多维度说明**: 对于多维度计数矩阵，添加说明
   ```
   > **数据说明**: 一个案例可涉及多个购买因素，合计(695)大于案例数(167)。
   ```

### Consistency Validation Report Structure (一致性验证报告结构)

验证报告必须包含以下内容：

```
# Data Consistency Validation Report

## 基准数据
- **输入源案例总数**: N = 167
- **利益相关者总条目**: M = 1069
- **平均利益相关者数/案例**: 6.4

## 案例数口径验证
| 矩阵名称 | 计算合计 | 基准N | 差异 | 状态 |
|----------|----------|-------|------|------|
| Industry × Year (年度合计) | 167 | 167 | 0 | ✓ 一致 |
| Industry × Year (行业合计) | 167 | 167 | 0 | ✓ 一致 |
| Year × Region (年度合计) | 167 | 167 | 0 | ✓ 一致 |
| Year × Region (区域合计) | 167 | 167 | 0 | ✓ 一致 |

## 利益相关者口径验证
| 矩阵名称 | 计算合计 | 基准M | 差异 | 状态 |
|----------|----------|-------|------|------|
| Industry × Role (角色合计) | 1074 | 1069 | +5 | ✓ 允许误差内(±5%) |
| Industry × Role (行业合计) | 1074 | 1069 | +5 | ✓ 允许误差内 |

## 多维度口径确认
| 矩阵名称 | 合计值 | 案例数N | 说明 | 状态 |
|----------|--------|--------|------|------|
| Industry × Purchase Factor | 695 | 167 | 一案多因素，已说明 | ✓ 已说明 |
| Purchase Factor × Year | 695 | 167 | 一案多因素，已说明 | ✓ 已说明 |
| Role × Purchase Factor | 4714 | 167 | 多维度交叉，已说明 | ✓ 已说明 |
| Solution × Industry | 386 | 167 | 一案多方案，已说明 | ✓ 已说明 |

## 口径说明完整性检查
| 矩阵名称 | 口径说明 | 合计列 | 核对注释 | 状态 |
|----------|----------|--------|----------|------|
| Industry × Year | ✓ | ✓ | ✓ | ✓ 完整 |
| Year × Region | ✓ | ✓ | ✓ | ✓ 完整 |
| Industry × Role | ✓ | ✓ | ✓ | ✓ 完整 |
| Industry × Purchase Factor | ✓ | ✓ | ✓ | ✓ 完整 |
| Purchase Factor × Year | ✓ | ✓ | ✓ | ✓ 完整 |
| Role × Purchase Factor | ✓ | ✓ | ✓ | ✓ 完整 |
| Role × Conflict | ✓ | ✓ | ✓ | ✓ 完整 |
| Solution × Industry | ✓ | ✓ | ✓ | ✓ 完整 |

## 问题清单
| 序号 | 问题类型 | 影响矩阵 | 描述 | 处理方式 |
|------|----------|----------|------|----------|
| 1 | 合计不一致 | XX Matrix | 计算合计≠基准 | 修正统计逻辑 |

## 验证结论
- **案例数口径验证**: ✓ 全部通过
- **利益相关者口径验证**: ✓ 全部通过（允许误差内）
- **多维度口径说明**: ✓ 全部已说明
- **口径说明完整性**: ✓ 全部完整

**整体一致性评级**: ★★★★☆ (高度一致)
```

### Common Consistency Errors (常见一致性错误)

| 错误类型 | 描述 | 修正方法 |
|----------|------|----------|
| **合计列缺失** | 矩阵缺少行/列合计 | 添加合计行/列 |
| **口径未标注** | 矩阵未说明统计口径 | 在标题下添加口径说明 |
| **核对注释缺失** | 矩阵后无数据核对说明 | 添加核对注释 |
| **合计不等于基准** | 案例数口径矩阵合计≠N | 修正统计逻辑或标注差异原因 |
| **多维度未说明** | 多维度计数矩阵未说明合计>N的原因 | 添加"一案多X"说明 |

---

## Workflow

### Phase 0: Preparation and Validation

1. **Input Collection**: Gather multiple `-analysis.md` documents
2. **Input Validation**: Apply Input Validation Framework to validate all inputs
3. **Document Parsing**: Extract structured fields from each document

### Phase 1: Business-First Analysis (MANDATORY)

4. **Business Background Analysis**: Extract and document industry, organizational, operational, and strategic context (see Business Background Driver Priority Framework)
5. **Business Driver Identification**: Identify and prioritize business drivers with quantified business value
6. **Business Impact Assessment**: Document impact of inaction and define success criteria

### Phase 2: Confidence and Credibility Assessment

7. **Confidence Assignment**: Assign confidence levels (HIGH/MEDIUM/LOW) and basis categories to all inferred information (see Confidence Level Framework)
8. **MoE Indicator Extraction**: Extract and document all quantified metrics with source traceability and credibility assessment (see MoE Indicators Framework)

### Phase 3: Dimension Extraction

9. **Stakeholder Analysis**: Extract stakeholders with three-level role hierarchy classification (Category → Subcategory → Concrete Role)
10. **Dimension Extraction**: Extract industry, purchase factors, operational scenarios, etc.
11. **Cross-Case Aggregation**: Group and count patterns across documents

### Phase 4: Model Synthesis

12. **Template Binding**: Bind every target output to its required template and extract required headings/tables before writing
13. **Business Insight Chain Generation**: Apply Business Insight Quality Framework to convert major patterns into context -> pressure -> stakeholder tension -> purchase factor -> capability -> measurable outcome -> risk -> recommended action chains
14. **Template-Based Model Generation**: Generate synthesis models by filling the bound templates section-by-section; do not skip sections with sparse evidence
15. **Critical Analysis**: Apply objective correction, counter-evidence, and credibility assessment inside the template's required critical-analysis section
16. **Strategic Advisory Model Generation**: Apply `assets/prompts/strategic-advisory.prompt.md` and Gartner-Style Strategic Modeling Framework to generate Use Case Fit, Critical Capability, Buying Committee, and Competitive Positioning models
17. **Cross-Analysis Generation**: Build cross-dimension matrixes with strategic cross-model insight summary using `cross-analysis-template.md`

### Phase 5: Validation and Formatting

18. **Template Compliance Validation**: Verify heading presence/order, table schemas, placeholder resolution, and deviation log before other quality checks
19. **Consistency Validation**: Apply Cross-Model Consistency Framework
20. **Business Insight Validation**: Run Business Insight Quality Framework gate before finalizing primary models
21. **Strategic Advisory Validation**: Verify use-case boundary, capability classification, buying committee proof burden, competitive alternative, and scenario implication completeness
22. **Automated Validation**: Run Automated Validation Framework checks
23. **Output Formatting**: Format outputs using defined templates with all quality requirements

---

## Version History

- **0.9.0** (2026-05-09): Gartner-style strategic market modeling enhancement - Added four mandatory strategic advisory model templates for data communication and cybersecurity market analysis: Use Case Fit Model, Critical Capability Model, Buying Committee Model, and Competitive Positioning Model. Added Gartner-Style Strategic Modeling Framework, template bindings, completeness checks, output directory support, workflow generation step, and validation requirements for market/use-case boundary, table-stakes vs differentiator classification, proof burden, competitive alternatives, and scenario modeling implications.
- **0.8.1** (2026-05-09): Template conformance hardening - Added mandatory template binding for every output file, no section dropping/merging rules, table schema preservation rules, placeholder completion rules, and deviation logging. Post-analysis validation now includes Template Compliance Verification before completeness and quality checks, with required reporting for heading match, heading order, required columns, unresolved placeholders, and template deviations.
- **0.8.0** (2026-05-09): Business insight quality enhancement - Added mandatory Business Insight Quality Framework integration for primary models. Industry, Stakeholder, Purchase Factor, and Cross-Analysis outputs now start with executive insight summaries before inventory tables; major conclusions must include business context, trigger or pressure, stakeholder decision tension, purchase factor, capability, measurable outcome or gap, counter-evidence, confidence, and recommended action. Templates and validation flow now explicitly guard against generic conclusions and product-name-as-driver outputs.
- **0.7.0** (2026-05-07): Major analysis quality enhancements - Added five comprehensive analysis quality frameworks based on user optimization requirements: (1) **Business Background Driver Priority Framework** - establishes business-first analysis order requiring business background and business driver analysis before technical implementation; (2) **Confidence Level Framework** - defines three-level confidence system (HIGH/MEDIUM/LOW) with explicit basis categories (Explicit Statement, Direct Citation, Multiple Source Agreement, Industry Standard, Contextual Inference, Quantitative Support, Expert Judgment, Speculative Inference) and mandatory confidence assignment for all inferred information; (3) **MoE Indicators Framework** - establishes Metrics of Effectiveness indicator standards with mandatory source traceability, credibility requirements, and quantified metric verification; defines five source types (Direct Measurement, Vendor Claim, Customer Statement, Industry Benchmark, Calculated/Inferred) with credibility assessment; (4) **Stakeholder Role Hierarchy Framework** - defines three-level stakeholder classification (Category Layer → Subcategory Layer → Concrete Role Layer) with complete hierarchy trees for all six standard categories and 60+ concrete roles across industries; (5) **Bilingual Quote Reference Framework** - mandates bilingual quote requirements for all non-Chinese sources with translation quality standards (accuracy, completeness, terminology consistency, readability) and comprehensive implementation guidelines. All frameworks integrate with existing validation and consistency frameworks for end-to-end quality assurance.
- **0.5.0** (2026-04-14): Major enhancement - **Purchase Factor Definition Clarification**: Purchase factors are business intents/value propositions, NOT products/technologies purchased; Added three MANDATORY new sections to Purchase Factor Model: (1) **Quantified Dimensions Analysis** - decompose quantifiable dimensions for each purchase factor with case data; (2) **Lead User Identification** - identify customers representing purchase factor development direction with leadership criteria (time leadership, quantification leadership, industry benchmark, innovation motivation); (3) **Purchase Factor Year Evolution Analysis** - track purchase factor changes across years with lead user evidence. All analyses must follow "Business Intent Priority" principle.
- **0.4.0** (2026-04-14): Added Statistical Conclusion Standards - Customer uniqueness principle (each customer counts once in frequency statistics), Multi-customer citation requirements (list top 3-5 important customers with original quotes), Business driver/purchase element elaboration requirements (each item needs supplementary explanation with specific manifestations, quantified metrics, implementation methods, business value), Analysis table synthesis requirements (each table needs synthesis and elaboration section covering core findings, distribution patterns, anomalies, business implications, data limitations)
- **0.3.0** (2026-04-14): Major enhancement - Added Quality Requirements section with mandatory quality standards and output completeness checklist for all three models; Added Parallel Processing Strategy for multi-Agent efficiency optimization based on input volume; Added Processing Progress Report for real-time progress tracking during model synthesis; Added Post-Analysis Validation process with source case coverage verification, completeness check, and problem data identification
- **0.2.0** (2026-04-12): Added enhanced output requirements for all three models: Industry Model (purchase factors per industry), Stakeholder Model (category + role layer with critical analysis), Purchase Factor Model (three-layer structure with critical analysis). All models now require customer name attribution, original quotes, and critical analysis chapter with credibility ratings
- **0.1.0** (2026-04-11): Initial scenario_modeler SKILL draft with OpenSCENARIO preparation support
