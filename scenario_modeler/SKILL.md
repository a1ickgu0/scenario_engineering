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
version: "0.5.0"
---

# Scenario Modeler SKILL

## Overview

This SKILL synthesizes and abstracts structured models from multiple `scenario_analyzer` analysis outputs. It transforms individual case-level analyses into cross-case inductive models that reveal patterns, commonalities, and variations across industries, stakeholders, and purchase decisions.

**Primary Outputs**:
1. **Industry Model**: Industry patterns, challenges, stakeholder distributions, solution preferences
2. **Stakeholder Model**: Two-layer structure (Category Layer + Role Layer) with mappings
3. **Purchase Factor Model**: Hierarchical structure (Business Driver + Technical Implementation + Quantified Metrics)

**Supporting Models for OpenSCENARIO Preparation**:
4. **Lifecycle Model**: Scenario phases, triggers, actions, completion criteria
5. **State Model**: Stakeholder/system/organization states and transitions
6. **Environment Model**: Industry constraints, regional characteristics, organizational context
7. **Entity Model**: Organizations, systems, external entities with attributes
8. **Relationship Model**: Hierarchical, collaborative, conflicting, dependency relations
9. **Interaction Sequence Model**: Actor-to-actor action flows with triggers and conditions
10. **Parameterization Model**: Configurable parameters for metrics, roles, scenarios, constraints

---

## Quality Requirements

**IMPORTANT**: All model synthesis must strictly follow the requirements below to ensure content completeness and analysis quality.

### Mandatory Quality Standards

| Quality Dimension | Requirement Standard | Acceptance Method |
|-------------------|---------------------|-------------------|
| **Completeness** | Three core models must be fully generated, each model contains all required sections | Output checklist verification |
| **Traceability** | Each model conclusion must annotate customer name - original quote (source case ID - original content) | Citation format check |
| **Accuracy** | Aggregated conclusions must accurately reflect source case content, frequency statistics must be precise | Source case cross-reference verification |
| **Structure** | Matrix tables must be complete, tree structures must have clear hierarchy, hierarchical relationships complete | Format compliance check |
| **Criticality** | Each model must contain critical analysis chapter, conclusion credibility rating must be annotated | Critical chapter check |

### Output Completeness Checklist

Each model output must contain all of the following sections:

**Industry Model Completeness Check**:
```
## 1. Industry Classification ✓/✗
## 2. Regional Distribution ✓/✗
## 3. Typical Challenges by Industry ✓/✗
## 4. Stakeholder Distribution ✓/✗
## 5. Solution Preferences ✓/✗
## 6. Purchase Factor Synthesis per Industry ✓/✗
## 7. Key Insights ✓/✗
## 8. Traceability Summary ✓/✗
## 9. Critical Analysis ✓/✗
```

**Stakeholder Model Completeness Check**:
```
## Part A: Category Layer ✓/✗
  - Category Definitions ✓/✗
  - Category × Industry Matrix ✓/✗
  - Category Typical Expectations ✓/✗
  - Category Influence Distribution ✓/✗

## Part B: Role Layer ✓/✗
  - Master Role Catalog ✓/✗
  - Category → Role Hierarchy ✓/✗
  - Role × Industry Matrix ✓/✗
  - Role Detailed Attributes ✓/✗

## Part C: Key Insights ✓/✗
## Part D: Traceability Summary ✓/✗
## Part E: Critical Analysis ✓/✗
```

**Purchase Factor Model Completeness Check**:
```
## 1. Business Driver Layer ✓/✗
## 2. Technical Implementation Layer ✓/✗
## 3. Quantified Metrics Layer ✓/✗
## 4. Industry × Business Driver Matrix ✓/✗
## 5. Solution Chain ✓/✗
## 6. Stakeholder × Driver Mapping ✓/✗
## 7. Key Insights ✓/✗
## 8. Traceability Summary ✓/✗
## 9. Critical Analysis ✓/✗
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
- **当前完成率**: Z/3 %

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
├── cross_analysis/
│   └ cross_analysis_matrix.md
└── validation/
    ├── completeness_check.md
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

Step 2: Model Completeness Verification
├── Check Industry Model 9 sections completeness
├── Check Stakeholder Model 5 Parts completeness
├── Check Purchase Factor Model 9 sections completeness
├── Verify traceability citation format
└── Confirm critical analysis chapter exists

Step 3: Data Quality Verification
├── Frequency statistics accuracy verification
├── Customer name - original quote consistency verification
├── Credibility rating rationality verification
└── Critical analysis logic completeness verification

Step 4: Issue List Generation
├── Uncited source case list
├── Missing sections list
├── Incomplete traceability list
└── Missing credibility rating list
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

## Model Completeness Verification Results
| Model Name | Required Sections | Completed Sections | Missing Sections | Completeness | Critical Analysis |
|------------|------------------|-------------------|-----------------|--------------|-------------------|
| Industry Model | 9 | 9 | 0 | ✓ | ✓ Contains credibility rating |
| Stakeholder Model | 5 | 5 | 0 | ✓ | ✓ Contains credibility rating |
| Purchase Factor Model | 9 | 9 | 0 | ✓ | ✓ Contains credibility rating |

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

## Output Requirements

### Industry Model Output Structure

The Industry Model output must include the following sections:

1. **Industry Classification**: Primary and secondary industry taxonomy with case counts
2. **Regional Distribution**: Region × Industry matrix with concentration analysis
3. **Typical Challenges by Industry**: Challenge types with frequency and original quotes
4. **Stakeholder Distribution**: Industry × Stakeholder category matrix
5. **Solution Preferences**: Cross-industry and industry-specific solution patterns
6. **Purchase Factor Synthesis per Industry**: **MANDATORY** - Each industry must have 3-5 purchase factors with:
   - Ranking and business importance
   - Typical expressions from source documents
   - **Customer name attribution** (e.g., "Aberdeen City Council")
   - **Original quote reference** (e.g., Page number or line number)
7. **Key Insights**: Pattern discoveries with traceability
8. **Traceability Summary**: Enhanced traceability tables with customer names and original quotes
9. **Critical Analysis**: **MANDATORY** - Independent chapter addressing:
   - Data source limitations (supplier bias, survivorship bias)
   - Objective correction of industry insights
   - Technical solution objective assessment
   - Market distribution objective interpretation
   - Data usage recommendations
   - Conclusion credibility rating

### Stakeholder Model Output Structure

The Stakeholder Model output must include the following sections:

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

### Purchase Factor Model Output Structure

**CRITICAL**: Purchase Factor Model must follow "Business Intent Priority" principle. All analyses center on customer's business value propositions, NOT products/technologies.

The Purchase Factor Model output must include the following sections:

1. **Business Driver Layer Frequency Distribution**: Purchase factors (business intents) frequency distribution, including:
   - Frequency statistics (customer uniqueness principle)
   - Supplementary explanation (specific manifestations, quantified metrics, business value)
   - Top 5 customer original quotes

2. **Technical Implementation Layer Frequency Distribution**: Technical solutions purchased to achieve purchase factors, with explicit linkage to business drivers

3. **Quantified Metrics Layer Frequency Distribution**: Quantified measurement indicator type statistics

4. **Industry × Purchase Factor Priority Matrix**: Industry × purchase factor priority matrix

5. **Purchase Factor → Technical Implementation Chain**: Purchase factor → technical implementation mapping chain

6. **Quantified Dimensions Analysis (NEW - MANDATORY)**:
   - Decompose quantifiable dimensions for each purchase factor
   - List cases providing quantified data with their quantified values
   - Classify quantified dimension types (efficiency improvement, cost savings, coverage rate, time reduction, certification achievement, etc.)

   **Quantified Dimensions Analysis Table Format**:
   ```
   | Purchase Factor | Quantified Dimension | Quantified Cases | Representative Cases (Values) | Original Quote |
   |-----------------|---------------------|------------------|------------------------------|----------------|
   | Operations efficiency | Ticket reduction rate | 25 cases | Austrian Red Cross(30%); Aberdeen(70%); Cheval(90%) | "operations simplified 30%" |
   | Operations efficiency | Deployment time reduction | 18 cases | Grove City(30min); Cheval(90%); Flintshire(hours→days) | "deployment completed in 30min" |
   | Security compliance | Certification achievement | 12 cases | Amiri(HIMSS Level 5); ADA(ISO 27001); Schnellecke(TISAX) | "HIMSS Level 5 certified" |
   | Cost efficiency | Cost savings percentage | 15 cases | CELSA(40%); Hindalco(30%); Cairo Amman(50%) | "MPLS cost 40% reduction" |
   ```

7. **Lead User Identification (NEW - MANDATORY)**:
   - Identify lead users/customers for each purchase factor
   - Lead user definition: Customers representing purchase factor development direction, having innovative procurement motivation, leading industry trends
   - Lead user identification criteria:
     - **Time Leadership**: First to propose or achieve the purchase factor (e.g., Golden State Warriors proposing WiFi 6E need in 2021)
     - **Quantification Leadership**: Achieved most challenging quantified goals (e.g., University of Illinois 100GbE research competitiveness)
     - **Industry Benchmark**: Having demonstration effect within industry (e.g., Amiri Hospital HIMSS Level 5 first in Kuwait)
     - **Innovation Motivation**: Having innovative business drivers rather than following needs (e.g., Nobu Hotels AI-driven hyper-personalized experience)

   **Lead User Identification Table Format**:
   ```
   | Purchase Factor | Lead User | Leadership Type | Leadership Reason | Industry Impact |
   |-----------------|-----------|-----------------|-------------------|-----------------|
   | WiFi innovation experience | Golden State Warriors(2022) | Time+Benchmark | First WiFi 6E venue in North America, leading industry by 2 years in 2022, fan experience innovation driven | Sports entertainment WiFi 6E benchmark |
   | Research competitiveness | University of Illinois(2024) | Quantification+Benchmark | 100GbE fabric research competitiveness, grant winning capability, research university benchmark | Higher education HPC benchmark |
   | Smart hospital certification | Amiri Hospital(2021) | Benchmark+Quantification | HIMSS Level 5 first in Kuwait, Level 6 target, smart hospital benchmark | Healthcare HIMSS certification benchmark |
   | Cost efficiency | CELSA Group(2022) | Quantification+Benchmark | MPLS→SD-WAN 40% cost savings, 70 European locations unified management, manufacturing benchmark | Manufacturing SD-WAN benchmark |
   | Hyper-personalized experience | Nobu Hotels(2024) | Innovation+Benchmark | AI-driven concierge service, Zero Trust+IoT combination, hospitality innovation pioneer | Hospitality AI experience benchmark |
   ```

8. **Purchase Factor Year Evolution Analysis (NEW - MANDATORY)**:
   - Focus on listing purchase factor changes across different years
   - List emerging/strengthened/evolving purchase factors for each year
   - Provide evidence (lead user cases + original quotes)

   **Purchase Factor Year Evolution Table Format**:
   ```
   | Year | Emerging Purchase Factors | Strengthened Purchase Factors | Evolving Purchase Factors | Lead User Evidence |
   |------|---------------------------|------------------------------|---------------------------|--------------------|
   | 2021 | Remote healthcare support | Security compliance certification | - | Amiri: "400 remote consultations"(emerging); HIMSS Level 5(strengthened) |
   | 2022 | WiFi 6E innovation experience | Cost efficiency optimization | Operations efficiency→AIOps | GSW: "WiFi 6E North America first"(emerging); CELSA: "40% cost reduction"(strengthened) |
   | 2023 | IoT smart building | Zero Trust architecture | WiFi 6→WiFi 6E | Nobu: "IoT smart room"(emerging); Rotana: "Zero Trust"(strengthened) |
   | 2024 | Research competitiveness(HPC) | SASE/ZTNA | SD-WAN→SASE | UI: "100GbE research competitiveness"(emerging); Schnellecke: "ZTNA"(strengthened) |
   | 2025 | Edge AI prediction | Hyper-personalized experience | Zero Trust→SASE | Bosch: "30-60 day prediction"(emerging); Gloria: "AI-driven experience"(strengthened) |
   | 2026 | WiFi 7 readiness | NaaS subscription model | WiFi 6E→WiFi 7 | Al-Nassr: "WiFi 7 readiness"(emerging); Grove City: "NaaS"(strengthened) |
   ```

9. **Stakeholder × Purchase Factor Mapping**: Stakeholder category × purchase factor mapping matrix

10. **Key Insights**: Pattern discoveries, including:
    - Purchase factor evolution trend insights
    - Lead user driving pattern insights
    - Industry differentiated purchase factor insights

11. **Traceability Summary**: Purchase factor traceability summary, including:
    - Quantified dimensions traceability table
    - Lead user traceability table
    - Year evolution traceability table

12. **Critical Analysis (MANDATORY)**:
    - Data source limitations assessment
    - Objective purchase factor correction
    - Lead user identification credibility assessment
    - Year evolution evidence completeness assessment
    - Data usage recommendations
    - Conclusion credibility rating

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

1. **Input Collection**: Gather multiple `-analysis.md` documents
2. **Document Parsing**: Extract structured fields from each document
3. **Dimension Extraction**: Extract industry, stakeholders, purchase factors, etc.
4. **Cross-Case Aggregation**: Group and count patterns across documents
5. **Model Synthesis**: Generate synthesis models with frequency and traceability
6. **Critical Analysis**: Apply objective correction and credibility assessment
7. **Cross-Analysis Generation**: Build cross-dimension matrixes
8. **Output Formatting**: Format outputs using defined templates

---

## Version History

- **0.5.0** (2026-04-14): Major enhancement - **Purchase Factor Definition Clarification**: Purchase factors are business intents/value propositions, NOT products/technologies purchased; Added three MANDATORY new sections to Purchase Factor Model: (1) **Quantified Dimensions Analysis** - decompose quantifiable dimensions for each purchase factor with case data; (2) **Lead User Identification** - identify customers representing purchase factor development direction with leadership criteria (time leadership, quantification leadership, industry benchmark, innovation motivation); (3) **Purchase Factor Year Evolution Analysis** - track purchase factor changes across years with lead user evidence. All analyses must follow "Business Intent Priority" principle.
- **0.4.0** (2026-04-14): Added Statistical Conclusion Standards - Customer uniqueness principle (each customer counts once in frequency statistics), Multi-customer citation requirements (list top 3-5 important customers with original quotes), Business driver/purchase element elaboration requirements (each item needs supplementary explanation with specific manifestations, quantified metrics, implementation methods, business value), Analysis table synthesis requirements (each table needs synthesis and elaboration section covering core findings, distribution patterns, anomalies, business implications, data limitations)
- **0.3.0** (2026-04-14): Major enhancement - Added Quality Requirements section with mandatory quality standards and output completeness checklist for all three models; Added Parallel Processing Strategy for multi-Agent efficiency optimization based on input volume; Added Processing Progress Report for real-time progress tracking during model synthesis; Added Post-Analysis Validation process with source case coverage verification, completeness check, and problem data identification
- **0.2.0** (2026-04-12): Added enhanced output requirements for all three models: Industry Model (purchase factors per industry), Stakeholder Model (category + role layer with critical analysis), Purchase Factor Model (three-layer structure with critical analysis). All models now require customer name attribution, original quotes, and critical analysis chapter with credibility ratings
- **0.1.0** (2026-04-11): Initial scenario_modeler SKILL draft with OpenSCENARIO preparation support