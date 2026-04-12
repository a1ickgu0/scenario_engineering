# 场景建模器 SKILL

## 概述

`scenario_modeler` SKILL 从多个 `scenario_engine` 分析输出中综合抽象出结构化模型。将单个案例层面的分析转化为跨案例归纳模型，揭示行业、利益相关者和购买决策的模式、共性和差异。

本 SKILL 为 OpenSCENARIO DSL 建模准备结构化输入，提供生命周期、状态、环境、实体、关系和参数化模型。

## 核心能力

### 1. 行业模型综合
- 行业分类和层级体系
- 地域分布模式
- 各行业典型挑战和痛点
- 利益相关者角色分布
- 解决方案偏好模式

### 2. 利益相关者模型（双层结构）

| 层级 | 说明 |
|------|------|
| 分类层 | 抽象分类：决策者、IT负责人、运营方、用户、监管方、合作伙伴 |
| 角色层 | 具象角色提取：CEO、CIO、IT总监、教师、学生等 |
| 映射关系 | 分类→角色的映射关系，含频次和行业上下文 |

### 3. 购买要素模型（层级结构）

| 层级 | 内容 |
|------|------|
| 业务驱动层 | 为什么买：成本优化、效率提升、安全合规、用户体验、创新转型、可持续发展 |
| 技术实现层 | 买什么能力：AI原生运维、零信任安全、Wi-Fi覆盖、云端管理、SD-WAN、NaaS订阅 |
| 量化指标层 | 如何衡量：减少率、提升率、时间节省、覆盖规模 |

### 4. OpenSCENARIO 准备支撑模型

| 模型 | 用途 |
|------|------|
| 生命周期模型 | 场景阶段序列，含触发条件、动作序列、完成标准 |
| 状态模型 | 利益相关者/系统/组织状态定义及转换条件 |
| 环境模型 | 行业约束、地域特性、组织环境等上下文 |
| 实体模型 | 组织实体、系统实体、外部实体及其属性 |
| 关系模型 | 层级关系、协作关系、对立关系、依赖关系 |
| 交互序列模型 | 角色间动作流程 |
| 参数化模型 | 可配置参数定义：量化指标、角色属性、场景参数、约束参数 |

## 输入要求

**来源文档**：多个 `scenario_engine` SKILL 生成的 `-analysis.md` 文件

**必需字段**：
- 客户基本信息（行业、国家、公司、年份）
- 购买要素（排序列表，含业务价值和量化指标）
- 利益相关者清单（角色、期望、影响力、价值/风险）
- 冲突与优先级
- 运行场景
- 产品与解决方案

## 输出成果

### 主要输出
1. **行业模型**：行业模式、挑战共性、利益相关者分布
2. **利益相关者模型**：分类层 + 角色层及映射关系
3. **购买要素模型**：层级结构及量化方式

### 支撑输出
4. **生命周期模型**：阶段序列、触发条件、动作序列
5. **状态模型**：状态定义及转换条件
6. **环境模型**：各维度上下文约束
7. **实体模型**：组织、系统、外部实体定义
8. **关系模型**：关系类型及模式
9. **交互序列模型**：角色动作流程
10. **参数化模型**：可配置参数定义

### 交叉分析矩阵
- 行业 × 角色矩阵
- 行业 × 购买要素矩阵
- 角色 × 购买要素矩阵
- 角色 × 冲突矩阵

## 使用方式

### 触发关键词
- "从多个分析中综合模型"
- "行业模式提取"
- "利益相关者模型抽象"
- "购买要素综合"
- "准备 OpenSCENARIO 建模输入"

### 工作流程示例

1. 收集多个 `-analysis.md` 文档（如 30+ 案例）
2. 解析每个文档的结构化字段
3. 提取维度：行业、利益相关者、购买要素
4. 跨文档聚合模式并统计频次
5. 生成综合模型并标注追溯来源
6. 构建跨维度分析矩阵
7. 使用定义模板格式化输出

## 目录结构

```
scenario_modeler/
├── SKILL.md                          # 核心定义
├── README.md                         # 英文文档
├── README_zh.md                      # 中文文档（本文件）
└── assets/
    ├── prompts/                      # 分析提示词（17个文件）
    │   ├── industry-synthesis.prompt.md         # 行业模型综合
    │   ├── stakeholder-category.prompt.md       # 利益相关者分类层
    │   ├── stakeholder-role.prompt.md           # 利益相关者角色层
    │   ├── purchase-factor.prompt.md            # 购买要素层级
    │   ├── cross-analysis.prompt.md             # 交叉分析矩阵
    │   ├── conflict-pattern.prompt.md           # 冲突模式库
    │   ├── solution-preference.prompt.md        # 解决方案偏好
    │   ├── lifecycle-model.prompt.md            # 生命周期模型
    │   ├── state-model.prompt.md                # 状态模型
    │   ├── environment-model.prompt.md          # 环境模型
    │   ├── entity-model.prompt.md               # 实体模型
    │   ├── relationship-model.prompt.md         # 关系模型
    │   ├── interaction-sequence.prompt.md       # 交互序列模型
    │   └── parameterization.prompt.md           # 参数化模型
    ├── references/                   # 参考指南（10个文件）
    │   ├── model-guidelines.md                  # 模型构建方法论
    │   ├── category-role-mapping.md             # 分类-角色映射参考
    │   ├── industry-taxonomy.md                 # 行业分类体系
    │   ├── metric-taxonomy.md                   # 量化指标术语库
    │   ├── state-definition.md                  # 状态定义参考
    │   ├── environment-taxonomy.md              # 环境分类参考
    │   ├── entity-taxonomy.md                   # 实体分类参考
    │   ├── relationship-types.md                # 关系类型参考
    │   └── openscenario-mapping.md              # OpenSCENARIO 映射参考
    └── templates/                   # 输出模板（14个文件）
        ├── industry-model-template.md           # 行业模型输出模板
        ├── stakeholder-category-template.md     # 分类层输出模板
        ├── stakeholder-role-template.md         # 角色层输出模板
        ├── purchase-factor-template.md          # 购买要素输出模板
        ├── cross-analysis-template.md           # 交叉矩阵输出模板
        ├── conflict-pattern-template.md         # 冲突模式输出模板
        ├── solution-preference-template.md      # 解决方案偏好输出模板
        ├── lifecycle-model-template.md          # 生命周期输出模板
        ├── state-model-template.md              # 状态模型输出模板
        ├── environment-model-template.md        # 环境模型输出模板
        ├── entity-model-template.md             # 实体模型输出模板
        ├── relationship-model-template.md       # 关系模型输出模板
        ├── interaction-sequence-template.md     # 交互序列输出模板
        └── parameterization-template.md         # 参数化输出模板
```

## 追溯性要求

每个模型结论需包含：
- **来源案例**：贡献该结论的案例 ID 列表
- **频次/权重**：模式出现频率（如"在 80% 的教育行业案例中出现")
- **典型引用**：保留原文关键表述用于验证
- **变异说明**：案例间的例外或变异情况

## 输出语言

- **中文（默认）**：用于中文文档和用户
- **英文**：用于国际化文档
- **双语表格**：关键表格同时包含中英文术语

## 相关 SKILL

- **scenario_engine**：生成单个案例分析的源 SKILL
- **pattern_modeler**：（已废弃）原名，已更名为 scenario_modeler

## 版本历史

- **0.1.0** (2026-04-11)：初始版本，含 OpenSCENARIO 准备支撑