# Customer Story Analysis Guidelines

This file guides how to perform INCOSE requirements engineering analysis on vendor customer stories, with output structured for OpenSCENARIO DSL preparation.

## Core Analysis Dimensions

### 1. Stakeholder Identification

Identify the following types of stakeholders:
- Users
- Customers
- Operators
- Maintainers
- Supporters
- Regulators
- Community/Public
- Suppliers

During analysis, focus on:
- Roles and responsibilities
- **Pain points and challenges** (see Section 1.1 below)
- Expectations and needs
- Values and risks
- Influence and decision-making power
- Relationship with the system
- **Relationship types**: Hierarchical, Collaborative, Conflicting, Dependency

#### 1.1 Pain Points and Challenges

For each stakeholder, extract specific difficulties faced in current state:

| Pain Point Type | Definition | Examples |
|-----------------|------------|----------|
| **Workflow bottlenecks** | Process obstacles affecting efficiency | Time-consuming troubleshooting, manual configuration, fragmented tools |
| **Efficiency obstacles** | Factors causing resource waste | Repetitive tasks, slow response times, lack of automation |
| **Experience barriers** | Issues affecting satisfaction | Unstable connectivity, complex authentication, poor user experience |
| **Decision constraints** | Factors hindering effective decisions | Lack of real-time data, limited visibility, information gaps |

**Pain Point Extraction Requirements**:
- Pain points must come from original text with citations
- Distinguish from expectations: Pain points are current state problems, expectations are desired state solutions
- Each stakeholder must have at least one identified pain point
- Pain points establish the causal chain to expectations (why the stakeholder needs what they need)

**Example Pain Point Extraction**:
```
原文： "IT team spent days troubleshooting network issues, responding reactively to problems"
→ Stakeholder: IT Operations Team
→ Pain Points: 
  - Workflow bottleneck: Time-consuming troubleshooting (days)
  - Efficiency obstacle: Reactive response mode (no proactive capability)
  - Experience barrier: Lack of unified tools for diagnosis
→ Expectation: Automation, unified management platform, proactive monitoring
→ Original Quote: "troubleshooting days→hours" (line X)
```

### 2. Purchase Elements

Extract purchase elements from a business value perspective, typically including:
- Cost savings
- Efficiency improvement
- Risk reduction
- Compliance
- User experience

Require at least 3-5 items, consistent with descriptions in the story.

**Parameterization format**: Each metric should have name, type, value, unit structure.

### 3. Expectations and Needs

For each stakeholder, clarify:
- What do they want to "get"?
- What should the system "satisfy"?
- Which are core needs vs. desired needs?

### 4. Influence and Benefits

Analyze each stakeholder's:
- Degree of influence on system decisions
- Value gained from the system
- Potential risks or costs incurred

### 5. Priority and Conflicts

Identify:
- Conflict points between different stakeholders
- Possible priority ranking
- Whether these conflicts lead to project risks or design trade-offs

### 6. Commitment and Engagement

Provide stakeholder participation recommendations at different lifecycle stages:
- Requirements definition
- Design review
- Testing and acceptance
- Operations validation
- Continuous improvement

### 7. Operational Concept

Extract "operational concept" or "usage concept" from the customer story:
- Who uses the system, when, where, and how?
- How does the system support core business processes?
- What are inputs, outputs, and success conditions?
- Are there environmental, timing, or process prerequisites?

**Enhanced structure**: Trigger → Actions → Conditions → Result (State Transition)

### 8. Product and Solution Identification

Clarify what is mentioned in the story:
- Specific products or product lines
- Services or solution patterns
- Technical components or platforms
- Delivery and implementation methods

**Entity mapping**: Map products/solutions to entity hierarchy tree.

---

## OpenSCENARIO Preparation Models

### 9. State Model

#### Stakeholder States

| State | Chinese | Definition | Typical Transitions |
|-------|---------|------------|--------------------|
| Need Unidentified | 需求未识别 | Problem not yet recognized | → Need Identified (problem discovery) |
| Need Identified | 需求已识别 | Problem recognized, requirements emerging | → Evaluating (solution research) |
| Evaluating | 评估中 | Researching solutions and vendors | → Decision Ready (evaluation complete) |
| Decision Ready | 决策就绪 | Ready to make purchase decision | → Decided (decision made) |
| Decided | 已决策 | Purchase decision made | → Expecting (awaiting deployment) |
| Expecting | 期待部署 | Awaiting deployment completion | → Accepting (deployment complete) |
| Accepting | 验收中 | Testing and validating solution | → Satisfied/Dissatisfied (acceptance complete) |
| Satisfied | 满意 | Solution meets expectations | → Stable Operation (continued satisfaction) |
| Dissatisfied | 不满意 | Solution fails expectations | → Escalating (issue resolution) |

#### System States

| State | Chinese | Definition | Typical Transitions |
|-------|---------|------------|--------------------|
| Not Deployed | 未部署 | Solution not yet installed | → Deploying (deployment start) |
| Deploying | 部署中 | Installation and configuration ongoing | → Deployed (deployment complete) |
| Deployed | 已部署 | Installation complete, awaiting acceptance | → Running (acceptance passed) |
| Running | 运行中 | Normal operation | → Upgrading (upgrade request) |
| Upgrading | 升级中 | Version update or enhancement | → Running (upgrade complete) |
| Degraded | 降级运行 | Partial functionality available | → Running (issue resolved) |
| Fault | 故障 | System failure or error | → Recovering (fault detected) |
| Recovering | 恢复中 | Recovery actions ongoing | → Running (recovery complete) |

#### Organization States

| State | Chinese | Definition | Typical Transitions |
|-------|---------|------------|--------------------|
| Problem Unrecognized | 问题未识别 | Organization unaware of issue | → Problem Identified (issue discovery) |
| Problem Identified | 问题已识别 | Issue recognized, seeking solution | → Solution Seeking (search started) |
| Solution Seeking | 方案寻址 | Researching potential solutions | → Procurement (solution chosen) |
| Procurement | 采购阶段 | Purchasing selected solution | → Implementation (contract signed) |
| Implementation | 实施阶段 | Deploying and configuring solution | → Validation (deployment complete) |
| Validation | 验证阶段 | Testing and validating | → Normal Operation (validation passed) |
| Normal Operation | 正常运营 | Routine operation | → Issue Detected (new problem) |

### 10. Environment Model

#### Industry Environment

| Dimension | Chinese | Definition | Examples |
|-----------|---------|------------|----------|
| Industry Regulations | 行业法规 | Industry-specific legal requirements | HIPAA (Healthcare), FERPA (Education), PCI-DSS (Retail) |
| Industry Standards | 行业标准 | Industry-specific technical/operational standards | ISO 27001 (Security), IEEE 802.11 (Wi-Fi) |
| Compliance Requirements | 合规要求 | Mandatory compliance obligations | GDPR (EU data), UK Data Protection Act |
| Industry Policies | 行业政策 | Government or industry body policies | 1:1 device mandate (Education), NHS digital strategy |
| Industry Practices | 行业惯例 | Common industry operational practices | Cloud adoption, remote work support |

#### Regional Environment

| Dimension | Chinese | Definition | Examples |
|-----------|---------|------------|----------|
| National Regulations | 国家法规 | Country-specific legal requirements | UK GDPR, US HIPAA, Japan APPI |
| Cultural Characteristics | 文化特性 | Cultural factors affecting adoption | Remote work culture, digital readiness |
| Market Maturity | 市场成熟度 | Technology adoption stage | Early adopter vs mainstream |
| Economic Context | 经济环境 | Economic factors affecting investment | Public vs private budget, growth rate |

#### Organizational Environment

| Dimension | Chinese | Definition | Examples |
|-----------|---------|------------|----------|
| Organizational Scale | 组织规模 | Size of organization | 67 schools, 26,500 students, 31,000 users |
| Architecture Type | 架构类型 | Organization structure | Centralized, distributed, federated |
| Budget Constraints | 预算约束 | Financial limitations | CapEx approval difficulty, OpEx preference |
| Strategic Direction | 战略方向 | Organizational strategic goals | Digital transformation, sustainability |

#### Technical Environment

| Dimension | Chinese | Definition | Examples |
|-----------|---------|------------|----------|
| Existing Tech Stack | 现有技术栈 | Current technology infrastructure | Legacy network, cloud services |
| Integration Constraints | 集成约束 | Integration requirements/limitations | ServiceNow integration, existing systems |
| Technical Standards | 技术标准 | Required technical specifications | Wi-Fi 6/6E, zero-trust architecture |
| Vendor Relationships | 供应商关系 | Existing vendor partnerships | HPE Aruba, Juniper ecosystem |

### 11. Entity Model

#### Organization Entity Types

| Entity Type | Chinese | Definition | Attributes |
|-------------|---------|------------|------------|
| Company | 公司 | Main organization | Name, Industry, Region, Scale |
| Department | 部门 | Organizational unit | Name, Function, Parent |
| Team | 团队 | Working group | Name, Role, Members, Parent |
| Role | 角色 | Individual position | Name, Responsibility, Parent |
| Site/Location | 站点/位置 | Physical location | Name, Type, Address, Scale |
| User Group | 用户群体 | User classification | Name, Scale, Characteristics |

#### System Entity Types

| Entity Type | Chinese | Definition | Attributes |
|-------------|---------|------------|------------|
| Solution | 方案 | Integrated solution | Name, Components, Purpose |
| Product | 产品 | Commercial product | Name, Vendor, Version, Category |
| Platform | 平台 | Management platform | Name, Type, Features |
| Service | 服务 | Delivered service | Name, Type, Provider |
| Component | 组件 | Technical component | Name, Type, Function |

#### External Entity Types

| Entity Type | Chinese | Definition | Attributes |
|-------------|---------|------------|------------|
| Supplier | 供应商 | Product/service provider | Name, Type, Relationship |
| Regulator | 监管机构 | Regulatory body | Name, Type, Requirements |
| Partner | 合作伙伴 | Collaborative partner | Name, Role, Services |

### 12. Lifecycle Model

| Phase | Chinese | Start Trigger | Key Actions | Completion Criteria |
|-------|---------|---------------|-------------|---------------------|
| Need Identification | 需求识别 | Problem discovery event | Problem definition, requirement gathering | Requirements documented |
| Evaluation | 评估选型 | Requirements documented | Solution research, vendor evaluation | Evaluation report complete |
| Decision | 购买决策 | Evaluation complete | Business negotiation, contract signing | Contract signed |
| Deployment | 部署实施 | Contract signed | Installation, configuration, integration | System available |
| Acceptance | 验收测试 | System available | Function validation, performance testing | Acceptance report passed |
| Operations | 运维运营 | Acceptance passed | Daily operations, issue handling | Continuous stable operation |

### 13. Relationship Types

| Relation Type | Chinese | Definition | Examples |
|---------------|---------|------------|----------|
| Hierarchical | 层级关系 | Superior-subordinate, management | CEO → CIO → IT Director |
| Collaborative | 协作关系 | Joint participation, cooperation | IT Team ↔ Supplier |
| Conflicting | 对立关系 | Conflict, competition | Cost Optimization ↔ Quality Improvement |
| Dependency | 依赖关系 | Pre/post dependency | Deployment Phase → Acceptance Phase |

### 14. Parameterization Model

| Parameter Type | Chinese | Definition | Format Example |
|----------------|---------|------------|----------------|
| Metric Parameters | 量化指标参数 | Performance, efficiency indicators | `fault_ticket_reduction: {type: metric, value: 100, unit: %}` |
| Role Attribute Parameters | 角色属性参数 | Influence, priority, participation phase | `influence_level: {type: role_attribute, value: high}` |
| Scenario Parameters | 场景参数 | Deployment time, coverage scale, user count | `user_count: {type: scenario, value: 26500, unit: users}` |
| Constraint Parameters | 约束参数 | Budget limit, time constraints, compliance | `compliance: {type: constraint, value: [HIPAA, GDPR]}` |

---

## Traceability and Evidence

Every point must preserve original text basis. Common forms:

- Direct quote sentences
- Page/paragraph markers
- Reference section titles
- Keywords from original text

If using inferred conclusions, must note:

- Inference source
- Original text basis
- Information points recommended for further verification

---

## Output Format Recommendations

Recommend using structured tables and itemized lists to make analysis easy to read and review.

### Example: State Extraction

```
状态提取示例：
原文（初始）："原有网络缺乏容量和覆盖，无法支持高密度设备连接"
→ Stakeholder State: Need Identified (IT团队发现容量缺口)
→ System State: Degraded (网络容量不足)
→ Organization State: Problem Identified (教育数字化转型受阻)

原文（最终）："100%减少故障工单，2倍覆盖容量，所有学习者首次连接成功"
→ Stakeholder State: Satisfied (IT团队、教师、学生满意)
→ System State: Running (网络稳定运行)
→ Organization State: Normal Operation (教育数字化目标达成)

转换路径：
Degraded → Deploying → Running
触发：购买决策完成，30分钟部署完成
```

### Example: Entity Hierarchy

```
实体层级提取示例：
原文："Aberdeen City Council | Digital Infrastructure Manager | 67学校、26,500学生"
→ Organization Entities:
  - Company: Aberdeen City Council (Type: Municipal)
  - Department: Digital Infrastructure (Parent: Aberdeen CC)
  - Role: Digital Infrastructure Manager (Parent: Digital Infrastructure)
  - Sites: 67 Schools (Parent: Aberdeen CC)
  - User Group: Students (Scale: 26,500)
```

### Example: Parameterization

```
参数化提取示例：
原文："100% Reduction in network-related trouble tickets"
→ Parameter:
  - param_name: fault_ticket_reduction
  - param_type: metric
  - param_value: 100
  - param_unit: %
  - original_quote: "100% Reduction in network-related trouble tickets"
```

---

## Further Work

This SKILL is designed for OpenSCENARIO DSL preparation. Future expansions can include:
- Automatic state transition identification
- Entity relationship inference
- Constraint pattern recognition
- Parameter type classification
- Cross-case model synthesis (via scenario_modeler SKILL)