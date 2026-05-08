---
name: customer-story-analysis
description: "Extract stakeholder information, ConOps-grounded operational concepts, and product/solution details from parser outputs or customer narrative text. Preserve original wording, provide Chinese support for non-Chinese quotes, and include traceability references. Output structured for OpenSCENARIO DSL preparation with ConOps state model, environment model, entity model, lifecycle phases, MoE analysis, and parameterization."
---

# Customer Story Analysis Prompt

## Task Description

You are an INCOSE requirements engineering expert. This SKILL defines output requirements and structure for OpenSCENARIO DSL preparation. Extract and structure the following content from the vendor-provided customer story text:

### Core Information
1. **Customer Basic Information**: Document title, country, industry, company name, document year
2. **Customer Identity Basis**: Explicit evidence proving company identity, including confidence and whether filename was only a hint
3. **Initial State**: Problems before solution deployment, organizational context
4. **Final State**: Overall benefits and outcomes after deployment, with before/after comparison

### Purchase Analysis
5. **Purchase Elements**: 3-5 business-level buying factors ranked by importance with strategic intent, business intent, and quantified metrics
6. **MoE Analysis**: Mission/business effectiveness measures, plus source, argument, and evidence basis

### Stakeholder Analysis
7. **Stakeholder List**: Organizational layer, role title, pain points, expectations, influence, value/risk, relationship types, priority
8. **Pain Points Extraction**: Specific difficulties each stakeholder faces in current state (workflow bottlenecks, efficiency obstacles, experience barriers)
9. **Conflicts and Priority**: Conflicting expectations and priority recommendations
10. **Engagement and Commitment**: Lifecycle participation recommendations

### OpenSCENARIO Preparation Models
11. **ConOps State Model**: Operational threads, actor/system states, and transitions grounded in real mission/business use
12. **Environment Model**: Industry, regional, organizational, and technical environment constraints
13. **Entity Model**: Organization hierarchy, system composition, external entity connections
14. **Lifecycle Phases**: Phase sequence with triggers, actions, and completion criteria
15. **Operational Scenarios**: Usage flows with triggers, conditions, and state transitions
16. **Products and Solutions**: Solution mapping to entity hierarchy
17. **Parameterization Model**: Structured parameters for metrics, roles, scenarios, constraints

## PDF Processing Tool Usage

If input is PDF format, first use the following tools to extract text content:

### Recommended Tools
- **pdftotext**: `pdftotext -layout input.pdf output.txt`
- **pdf2txt.py**: `pdf2txt.py -o output.txt input.pdf`
- **Online tools**: Browser PDF-to-text converters

### Processing Requirements
1. Extract plain text content, maintain readability
2. Record page and paragraph locations for traceability
3. Clean formatting noise (headers, footers, etc.)
4. Validate text completeness and accuracy

### Traceability Marker Examples
- "Page 3, paragraph 2: [direct quote]"
- "Section 2.1: [section content]"
- "Customer feedback section: [specific content]"

---

## Output Format Requirements

Output according to the following structure. Use tables primarily, with supplementary explanations after tables.

### 0. 客户基本信息 (Customer Basic Information)

| 文章名 | 国家 | 行业 | 公司名 | 文档年份 | 公司识别依据 | 识别置信度 | 文件名仅作提示? | 来源 |
|--------|------|------|--------|----------|--------------|------------|------------------|------|
| ... | ... | ... | ... | ... | ... | High/Medium/Low | Yes/No | ... |

#### 应用产品与方案之前的问题 (Initial State Description)
Describe the problems before solution deployment:
- Business pain points
- Technical limitations
- Organizational constraints
- Original text reference

#### 整体使用效果/收益综述 (Final State Description)
Describe the outcomes after deployment:
- Quantified benefits
- Business improvements
- Stakeholder satisfaction
- Original text reference

#### 部署前后效果对比 (Before vs After)

| 维度 | 部署前 | 部署后 | 变化 | 证据来源 |
|------|--------|--------|------|----------|
| ... | ... | ... | ... | "..." |

---

### 1. 购买要素 (Purchase Elements)

| 排名 | 购买要素 | 战略意图 | 业务意图 | 业务重要性 | 业务价值 | 量化指标 | 原文引用 |
|------|----------|----------|----------|-----------|----------|----------|----------|
| 1 | Element A | ... | ... | Highest/High/Medium/Low | ... | Before: X, After: Y, Change: Z% | "..." |
| 2 | Element B | ... | ... | ... | ... | ... | "..." |

**购买要素分析要求**:
- 不得只写通用词，必须解释该要素如何服务客户战略或业务意图
- 优先使用原文中明确的前后对比、改善幅度、时间缩短、成本变化、成功率变化
- 若无法量化，必须说明为何无法量化以及可替代证据

#### 1.1 MoE 指标分析

| MoE指标 | 指标类型 | 部署前 | 部署后 | 变化 | 来源 | 论据/业务主张 | 依据/原文证据 |
|---------|----------|--------|--------|------|------|---------------|---------------|
| ... | mission/business/experience/compliance | ... | ... | ... | metric / quote / inferred-with-basis | ... | "..." |

---

### 2. 利益相关者清单 (Stakeholder List with Pain Points)

| 利益相关者 | 层级 | 类型 | 角色名 | 痛点/困难 | 期望/需求 | 影响力 | 价值/风险 | 关系类型 | 优先级 | 原文引用 |
|------------|------|------|--------|----------|----------|--------|----------|----------|--------|----------|
| Stakeholder A | 决策层/管理层/执行层/终端用户/外部伙伴 | 类型 | 角色头衔或岗位名 | Workflow bottlenecks, efficiency obstacles, experience barriers | ... | High/Medium/Low | Value: ...; Risk: ... | Hierarchical/Collaborative/Conflicting/Dependency | 1/2/3 | "..." |

**痛点定义**:
- **Workflow bottlenecks (工作流程瓶颈)**: 影响角色工作效率的流程障碍
- **Efficiency obstacles (效率障碍)**: 导致角色资源浪费的因素
- **Experience barriers (体验障碍)**: 影响角色满意度或用户体验的问题
- **Decision constraints (决策约束)**: 妨碍角色做出有效决策的因素

**痛点提取要求**:
- 痛点必须来自原文描述，标注引用位置
- 区分"痛点"与"期望": 痛点是当前状态的问题，期望是期望状态的解决方案
- 每个利益相关者至少提取一个痛点
- 必须拆分"层级"与"角色名"，例如 `决策层` + `CEO`，不得合并成一个字段
- 如果原文仅给出角色头衔而未直接说明层级，应基于组织语义给出层级并标注为推断

**综述说明** (每个表格后必须包含):
1. **核心痛点**: 各角色面临的最普遍问题
2. **痛点分布**: 不同角色类型的痛点集中区域
3. **痛点-期望关联**: 痛点如何驱动期望的形成

**关系类型定义**:
- **Hierarchical (层级关系)**: 上级-下级, 管理关系
- **Collaborative (协作关系)**: 联合参与, 合作关系
- **Conflicting (对立关系)**: 冲突, 竞争关系
- **Dependency (依赖关系)**: 前后依赖, 支撑关系

---

### 3. 冲突与优先级 (Conflicts and Priority)

| 冲突点 | 相关利益相关者 | 根因 | 优先级建议 | 原文引用 |
|--------|---------------|------|-----------|----------|
| ... | ... | ... | High/Medium/Low: ... | "..." |

---

### 4. 基于 ConOps 的状态模型 (ConOps-Grounded State Model)

**强制要求**:
- 本节必须基于系统工程 ConOps 描述真实业务/任务运行线程，不得输出与原文无关的泛化采购状态占位表。
- 优先描述谁在什么情境下、通过什么系统能力、完成什么任务、达到什么业务结果。
- 若原文没有足够证据支撑某一状态或转换，明确标注“证据不足”，不要套模板补齐。

#### 4.1 ConOps 运行线程状态

| 运行线程 | 参与者/系统 | 前置状态 | 关键动作 | 后置状态 | 触发条件 | 成功准则 | 原文依据 |
|----------|-------------|----------|----------|----------|----------|----------|----------|
| ... | ... | ... | ... | ... | ... | ... | "..." |

#### 4.2 角色状态定义（基于 ConOps）

| 角色/利益相关者 | 状态 | 中文 | 定义 | 转换触发条件 | 原文依据 |
|----------------|------|------|------|-------------|----------|
| ... | ... | ... | ... | ... | "..." |

#### 4.3 系统/方案状态定义（基于 ConOps）

| 系统/方案 | 状态 | 中文 | 定义 | 转换触发条件 | 原文依据 |
|-----------|------|------|------|-------------|----------|
| ... | ... | ... | ... | ... | "..." |

#### 4.4 ConOps 状态转换说明

- 用自然语言总结关键运行线程如何从部署前问题状态转入部署后目标状态
- 明确状态转换与购买要素、MoE、关键利益相关者之间的因果关系
- 若存在多条线程，指出主线程与支撑线程

---

### 5. 环境模型 (Environment Model)

#### 5.1 行业环境

| 环境要素 | 描述 | 具体内容 | 原文依据 |
|----------|------|----------|----------|
| 行业法规 | Industry regulations | HIPAA, GDPR, FERPA, etc. | "..." |
| 行业标准 | Industry standards | ISO 27001, IEEE 802.11, etc. | "..." |
| 合规要求 | Compliance requirements | Specific compliance obligations | "..." |
| 行业政策 | Industry policies | Government or industry mandates | "..." |
| 行业惯例 | Industry practices | Common operational practices | "..." |

#### 5.2 地域环境

| 环境要素 | 描述 | 具体内容 | 原文依据 |
|----------|------|----------|----------|
| 国家法规 | National regulations | Country-specific legal requirements | "..." |
| 文化特性 | Cultural characteristics | Cultural factors affecting adoption | "..." |
| 市场成熟度 | Market maturity | Technology adoption stage | "..." |
| 经济环境 | Economic context | Public/private budget, growth rate | "..." |

#### 5.3 组织环境

| 环境要素 | 描述 | 具体内容 | 原文依据 |
|----------|------|----------|----------|
| 组织规模 | Organizational scale | User count, site count, coverage | "..." |
| 架构类型 | Architecture type | Centralized/Distributed/Federated | "..." |
| 预算约束 | Budget constraints | CapEx/OpEx, approval process | "..." |
| 战略方向 | Strategic direction | Digital transformation, sustainability | "..." |

#### 5.4 技术环境

| 环境要素 | 描述 | 具体内容 | 原文依据 |
|----------|------|----------|----------|
| 现有技术栈 | Existing tech stack | Current infrastructure | "..." |
| 集成约束 | Integration constraints | Existing systems to integrate | "..." |
| 技术标准 | Technical standards | Required specifications | "..." |
| 供应商关系 | Vendor relationships | Existing vendor partnerships | "..." |

---

### 6. 实体层级模型 (Entity Model)

#### 6.1 组织实体层级树

```
Organization: [Company Name]
├── Department: [Department 1]
│   ├── Team: [Team 1]
│   │   └── Role: [Role 1]
│   │   └── Role: [Role 2]
│   └── Team: [Team 2]
├── Department: [Department 2]
│   └── Role: [Role 3]
└── Sites: [Site Count] [Site Type]
    └── User Group: [User Group Name] (Scale: [Count])
```

#### 6.2 系统实体组成树

```
Solution: [Solution Name]
├── Platform: [Platform Name]
│   ├── Service: [Service 1]
│   └── Service: [Service 2]
├── Product: [Product 1] (Type: Hardware/Software)
├── Product: [Product 2] (Type: Hardware/Software)
└── Service: [Support Service]
```

#### 6.3 外部实体连接图

```
Organization: [Company Name]
├── ↔ Supplier: [Vendor Name]
│   ├── Service: [Service Provided]
│   └── Product: [Product Provided]
├── ↔ Regulator: [Regulatory Body]
│   ├── Policy: [Policy Name]
│   └── Compliance: [Compliance Requirement]
└── ↔ Partner: [Partner Name]
    └── Service: [Service Provided]
```

---

### 7. 生命周期阶段 (Lifecycle Phases)

| 阶段 | 中文 | 触发条件 | 主要动作 | 完成标准 | 参与利益相关者 | 原文依据 |
|------|------|----------|----------|----------|---------------|----------|
| Need Identification | 需求识别 | 问题发现事件 | 问题定义、需求收集 | 需求文档完成 | 决策者、用户 | "..." |
| Evaluation | 评估选型 | 需求文档完成 | 方案调研、供应商评估 | 评估报告完成 | IT负责人、决策者 | "..." |
| Decision | 购买决策 | 评估报告完成 | 商务谈判、合同签署 | 合同签署完成 | 决策者、采购方 | "..." |
| Deployment | 部署实施 | 合同签署完成 | 安装配置、系统集成 | 系统可用 | IT团队、供应商 | "..." |
| Acceptance | 验收测试 | 系统可用 | 功能验证、性能测试 | 验收报告通过 | 用户、IT团队 | "..." |
| Operations | 运维运营 | 验收通过 | 日常运维、问题处理 | 持续稳定运行 | 运营方、供应商 | "..." |

---

### 8. 运行场景 (Operational Scenarios)

| 场景 | 描述 | 触发条件 | 执行条件 | 状态转换 | 用户/参与者 | 成功标准 | 原文引用 |
|------|------|----------|----------|----------|------------|----------|----------|
| Scenario A | ... | Trigger event | Preconditions | From: X → To: Y | ... | ... | "..." |

**场景结构要求**:
- 触发条件: 什么事件触发该场景
- 执行条件: 场景执行需要的前置条件
- 状态转换: 场景完成后利益相关者/系统的状态变化

---

### 9. 承诺与参与建议 (Engagement and Commitment)

| 利益相关者 | 参与阶段 | 评价/验收 | 关键关注点 | 原文引用 |
|------------|----------|----------|-----------|----------|
| ... | Need ID/Evaluation/Decision/Deployment/Acceptance/Operations | ... | ... | "..." |

---

### 10. 产品与解决方案 (Products and Solutions)

| 产品/方案 | 类型 | 描述 | 量化收益 | 满足需求 | 实体层级关联 | 原文引用 |
|-----------|------|------|----------|----------|-------------|----------|
| Product A | Hardware/Software/Service | ... | ... | ... | Parent: [Solution] | "..." |

---

### 11. 参数化模型 (Parameterization Model)

#### 11.1 量化指标参数

| 参数名 | 参数类型 | 参数值 | 单位 | 描述 | 原文依据 |
|--------|----------|--------|------|------|----------|
| fault_ticket_reduction | metric | 100 | % | 故障工单减少率 | "..." |
| coverage_increase | metric | 2 | x | 覆盖容量提升倍数 | "..." |
| deploy_time | metric | 30 | minutes | 部署时间 | "..." |

#### 11.2 角色属性参数

| 参数名 | 参数类型 | 参数值 | 描述 | 原文依据 |
|--------|----------|--------|------|----------|
| influence_level | role_attribute | high/medium/low | 影响力等级 | "..." |
| priority | role_attribute | 1/2/3 | 优先级排名 | "..." |
| participation_phase | role_attribute | [phase list] | 参与阶段列表 | "..." |

#### 11.3 场景参数

| 参数名 | 参数类型 | 参数值 | 单位 | 描述 | 原文依据 |
|--------|----------|--------|------|------|----------|
| user_count | scenario | 26500 | users | 用户总数 | "..." |
| site_count | scenario | 67 | sites | 站点数量 | "..." |
| coverage_scale | scenario | 31000 | users | 覆盖规模 | "..." |

#### 11.4 约束参数

| 参数名 | 参数类型 | 参数值 | 描述 | 原文依据 |
|--------|----------|--------|------|----------|
| compliance | constraint | [compliance list] | 合规要求列表 | "..." |
| budget_type | constraint | CapEx/OpEx | 预算类型 | "..." |
| mandate | constraint | [mandate name] | 政策强制要求 | "..." |

---

### 12. 追溯与备注 (Traceability and Notes)

- 本分析基于 `scenario_analyzer/SKILL.md` 的结构要求
- 所有分析项均包含原文引用或来源标记
- 对于推断结论，注明推断来源和原文依据
- 关键指标汇总和战略重点说明
- 对于非中文原文引用，必须同时给出原文和简明中文释义，例如：`"Guest experience is everything"` / `中文释义：客户体验至上`

---

## Processing Approach

1. If input is PDF, first convert key paragraphs to readable text with page references
2. Extract initial state from "problems before solution" descriptions
3. **Extract stakeholder pain points** from problem descriptions at role level:
   - Identify workflow bottlenecks for each role
   - Identify efficiency obstacles and experience barriers
   - Link pain points to specific stakeholders with original quotes
4. Extract final state from "benefits/outcomes" descriptions and build explicit before/after comparison
5. Derive purchase elements from strategic intent, business intent, and quantified value evidence
6. Build MoE analysis with source, argument, and basis
7. Build ConOps threads and derive actor/system states from real operations, not generic placeholders
8. Map environment constraints from industry, region, and organization context
9. Build entity hierarchy from stakeholder roles and organization descriptions
10. Build system composition from products/solutions list
11. Extract lifecycle phases from scenario timeline
12. Parameterize all quantified metrics with structured format
13. For every non-Chinese original quote, provide a concise Chinese rendering alongside the original

## Further Notes

Output reports should use the local language. If local language cannot be determined, default to Chinese.

Every analysis item must include:
- Original text reference (page/section/quote)
- State transition mapping where applicable
- Parameterized format for quantified values
