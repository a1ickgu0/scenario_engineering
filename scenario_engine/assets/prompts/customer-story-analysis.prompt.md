---
name: customer-story-analysis
description: "Extract stakeholder information, operational concepts, and product/solution details from a customer story PDF or customer narrative text. Preserve original wording and include traceability references. Output structured for OpenSCENARIO DSL preparation with state model, environment model, entity model, lifecycle phases, and parameterization."
---

# Customer Story Analysis Prompt

## Task Description

You are an INCOSE requirements engineering expert. This SKILL defines output requirements and structure for OpenSCENARIO DSL preparation. Extract and structure the following content from the vendor-provided customer story text:

### Core Information
1. **Customer Basic Information**: Document title, country, industry, company name, document year
2. **Initial State**: Problems before solution deployment, organizational context
3. **Final State**: Overall benefits and outcomes after deployment

### Purchase Analysis
4. **Purchase Elements**: 3-5 business-level buying factors ranked by importance with quantified metrics

### Stakeholder Analysis
5. **Stakeholder List**: Roles, expectations, influence, value/risk, relationship types, priority
6. **Conflicts and Priority**: Conflicting expectations and priority recommendations
7. **Engagement and Commitment**: Lifecycle participation recommendations

### OpenSCENARIO Preparation Models
8. **State Model**: Stakeholder, system, and organization states with transition triggers
9. **Environment Model**: Industry, regional, organizational, and technical environment constraints
10. **Entity Model**: Organization hierarchy, system composition, external entity connections
11. **Lifecycle Phases**: Phase sequence with triggers, actions, and completion criteria
12. **Operational Scenarios**: Usage flows with triggers, conditions, and state transitions
13. **Products and Solutions**: Solution mapping to entity hierarchy
14. **Parameterization Model**: Structured parameters for metrics, roles, scenarios, constraints

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

| 文章名 | 国家 | 行业 | 公司名 | 文档年份 | 来源 |
|--------|------|------|--------|----------|------|
| ... | ... | ... | ... | ... | ... |

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

---

### 1. 购买要素 (Purchase Elements)

| 排名 | 购买要素 | 业务重要性 | 业务价值 | 量化指标 | 原文引用 |
|------|----------|-----------|----------|----------|----------|
| 1 | Element A | Highest/High/Medium/Low | ... | Before: X, After: Y, Change: Z% | "..." |
| 2 | Element B | ... | ... | ... | "..." |

---

### 2. 利益相关者清单 (Stakeholder List)

| 利益相关者 | 类型 | 角色 | 期望/需求 | 影响力 | 价值/风险 | 关系类型 | 优先级 | 原文引用 |
|------------|------|------|----------|--------|----------|----------|--------|----------|
| Stakeholder A | 类型 | 角色 | ... | High/Medium/Low | Value: ...; Risk: ... | Hierarchical/Collaborative/Conflicting/Dependency | 1/2/3 | "..." |

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

### 4. 状态模型 (State Model)

#### 4.1 利益相关者状态定义

| 状态 | 中文 | 定义 | 转换触发条件 | 原文依据 |
|------|------|------|-------------|----------|
| Need Identified | 需求已识别 | Problem recognized, requirements emerging | Problem discovery event | "..." |
| Evaluating | 评估中 | Researching solutions and vendors | Evaluation start trigger | "..." |
| Decision Ready | 决策就绪 | Ready to make purchase decision | Evaluation complete | "..." |
| Decided | 已决策 | Purchase decision made | Decision event | "..." |
| Expecting | 期待部署 | Awaiting deployment completion | Contract signed | "..." |
| Accepting | 验收中 | Testing and validating solution | Deployment complete | "..." |
| Satisfied | 满意 | Solution meets expectations | Acceptance passed | "..." |
| Dissatisfied | 不满意 | Solution fails expectations | Acceptance failed | "..." |

#### 4.2 系统状态定义

| 状态 | 中文 | 定义 | 转换触发条件 | 原文依据 |
|------|------|------|-------------|----------|
| Not Deployed | 未部署 | Solution not yet installed | Initial state | "..." |
| Deploying | 部署中 | Installation and configuration ongoing | Deployment start | "..." |
| Deployed | 已部署 | Installation complete, awaiting acceptance | Deployment complete | "..." |
| Running | 运行中 | Normal operation | Acceptance passed | "..." |
| Upgrading | 升级中 | Version update or enhancement | Upgrade request | "..." |
| Degraded | 降级运行 | Partial functionality available | Issue detected | "..." |
| Fault | 故障 | System failure or error | Fault event | "..." |
| Recovering | 恢复中 | Recovery actions ongoing | Fault detected | "..." |

#### 4.3 组织状态定义

| 状态 | 中文 | 定义 | 转换触发条件 | 原文依据 |
|------|------|------|-------------|----------|
| Problem Identified | 问题已识别 | Issue recognized, seeking solution | Issue discovery | "..." |
| Solution Seeking | 方案寻址 | Researching potential solutions | Search started | "..." |
| Procurement | 采购阶段 | Purchasing selected solution | Solution chosen | "..." |
| Implementation | 实施阶段 | Deploying and configuring solution | Contract signed | "..." |
| Validation | 验证阶段 | Testing and validating | Deployment complete | "..." |
| Normal Operation | 正常运营 | Routine operation | Validation passed | "..." |

#### 4.4 状态转换路径图

```
利益相关者状态路径:
初始状态 → 需求已识别 → 评估中 → 决策就绪 → 已决策 → 期待部署 → 验收中 → 满意/不满意

系统状态路径:
未部署 → 部署中 → 已部署 → 运行中 → (升级中 → 运行中) / (降级/故障 → 恢复中 → 运行中)

组织状态路径:
问题已识别 → 方案寻址 → 采购阶段 → 实施阶段 → 验证阶段 → 正常运营
```

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

- 本分析基于 `scenario_engine/SKILL.md` 的结构要求
- 所有分析项均包含原文引用或来源标记
- 对于推断结论，注明推断来源和原文依据
- 关键指标汇总和战略重点说明

---

## Processing Approach

1. If input is PDF, first convert key paragraphs to readable text with page references
2. Extract initial state from "problems before solution" descriptions
3. Extract final state from "benefits/outcomes" descriptions
4. Identify stakeholder states based on problem → solution → satisfaction flow
5. Identify system states based on deployment → operation flow
6. Map environment constraints from industry, region, and organization context
7. Build entity hierarchy from stakeholder roles and organization descriptions
8. Build system composition from products/solutions list
9. Extract lifecycle phases from scenario timeline
10. Parameterize all quantified metrics with structured format

## Further Notes

Output reports should use the local language. If local language cannot be determined, default to Chinese.

Every analysis item must include:
- Original text reference (page/section/quote)
- State transition mapping where applicable
- Parameterized format for quantified values