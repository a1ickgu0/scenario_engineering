# 场景工程 SKILL

这是一个通用的 INCOSE 需求工程 SKILL，专注于从厂商 customer story PDF 或文本中提取需求和利益相关者信息。它可以在 Claude 中使用，也可以应用于其他 LLM 或手工分析流程。 **输出结构化用于 OpenSCENARIO DSL 准备**。

## 📋 目的

本 SKILL 的目标是引导分析人员从 customer story 文本中提取：

1. 文章名、国家、行业、公司名、文档年份
2. 关键利益相关者及其角色
3. 购买要素和业务价值，并基于业务重要性进行评估与排序
4. 各方期望/需求、影响与利益、优先级/冲突、承诺与参与
5. 运行使用构想（operational concept / usage concept）
6. 引用的产品、服务与解决方案
7. **ConOps 状态模型**: 基于真实业务/任务线程的参与者状态、系统状态与状态转换
8. **环境模型**: 行业、地域、组织和技术约束
9. **实体模型**: 组织层级、系统组成、外部链接
10. **生命周期阶段**: 阶段序列、触发条件和完成标准
11. **参数化模型**: OpenSCENARIO DSL 的结构化指标与 MoE 分析

## 🔍 核心能力

### 1. 利益相关者提取
- 识别用户、客户、运营方、维护方、支持方、监管机构、社群／公众、供应商等
- 区分组织层级、角色名、期望、价值、风险、优先级和冲突
- 关联生命周期中的参与与验收
- **关系类型**: 层级关系、协作关系、对立关系、依赖关系

### 2. 购买要素分析
- 提取 customer story 中的 3-5 个业务购买要素
- 基于客户业务的重要性对这些购买要素进行评估与排序
- 从客户视角描述"为什么要买""需要解决什么问题"
- 补充战略意图、业务意图，以及部署前/后量化证据
- **MoE 分析**: 识别效果性指标，并说明来源、论据、依据

### 3. 运行构想
- 描述系统运行/使用构想
- 提取关键使用场景、环境、交互和成功标准
- **增强结构**: 触发器 → 动作 → 条件 → 结果（状态转换）

### 4. 产品与解决方案识别
- 抽取 story 中的产品、服务、解决方案、技术或交付形式
- 映射到利益相关者需求
- **实体映射**: 产品/解决方案映射到实体层级树

### 5. 可追溯性
- 所有分析要点须基于原文内容
- 提供原文引用、段落或关键句回溯信息

### 6. PDF 处理支持
- 支持PDF文档的文本提取和分析
- 提供工具集成指南和命令示例
- 保持页面和段落引用以支持追溯

### 7. ConOps 状态模型（OpenSCENARIO 准备）
- 基于真实业务/任务线程构建状态模型，而不是套用泛化采购占位状态
- 区分参与者状态、系统状态和结果状态
- 将状态转换与部署前后收益、MoE 建立关联

### 8. 环境模型（OpenSCENARIO 准备）
- 行业环境: 法规、标准、合规要求、行业政策
- 地域环境: 国家法规、文化特性、市场成熟度
- 组织环境: 规模、架构类型、预算约束
- 技术环境: 现有技术栈、集成约束

### 9. 实体模型（OpenSCENARIO 准备）
- 组织实体层级: 公司 → 部门 → 团队 → 角色
- 系统实体组成: 解决方案 → 产品 → 服务
- 外部实体链接: 供应商、监管机构、合作伙伴

### 10. 生命周期模型（OpenSCENARIO 准备）
- 阶段序列: 需求识别 → 评估 → 决策 → 部署 → 验收 → 运营
- 阶段触发条件、动作和完成标准

### 11. 参数化模型（OpenSCENARIO 准备）
- 量化指标参数: 名称、类型、值、单位
- 角色属性参数: 影响力、优先级、参与阶段
- 场景参数: 部署时间、覆盖范围、用户数量
- 约束参数: 预算、合规要求

## 🛠️ PDF 处理工具集成

### 推荐工具
- **pdftotext**: Linux/Mac 原生工具，保持布局
- **pdf2txt.py**: Python PDFMiner 工具
- **在线转换器**: 浏览器-based PDF转文本工具
- **OCR工具**: tesseract 用于扫描PDF

### 使用示例
```bash
# 基本文本提取
pdftotext input.pdf output.txt

# 保持布局结构
pdftotext -layout input.pdf output.txt

# 指定页面范围
pdftotext -f 1 -l 5 input.pdf output.txt

# Python 方式
python -c "import pdfminer; pdfminer.high_level.extract_text('input.pdf')"
```

### 处理步骤
1. **提取文本**: 将PDF转换为纯文本格式
2. **添加引用**: 标记页码、章节位置
3. **清理内容**: 移除页眉页脚和格式噪音
4. **验证完整性**: 确保文本可读且内容完整

### 追溯标记
- 页面引用: "Page 3, paragraph 2"
- 章节标记: "Section 2.1: Customer Challenges"
- 直接引用原文内容

```
scenario_analyzer/
├── SKILL.md                # SKILL 元数据定义
├── README.md               # 当前说明文档
├── README_zh.md            # 中文说明文档
├── tests/                  # 文档验证和测试样例存放目录
└── assets/
    ├── prompts/            # 核心提示词
    │   └── customer-story-analysis.prompt.md
    └── references/         # 分析指南
        └── analysis-guidelines.md
```

## 🚀 开始使用

1. 将厂商 customer story 的 PDF 文本内容复制或转换为可供分析的可读文本
2. 启动本 SKILL，说明你需要提取下面这些维度：
   - 购买要素、战略意图、业务意图与 MoE
   - 利益相关者、组织层级与角色名
   - 影响力与利益
   - 优先级与冲突
   - 承诺与参与
   - 运行使用构想
   - 产品与解决方案
   - **ConOps 状态模型**（OpenSCENARIO）
   - **环境模型**（OpenSCENARIO）
   - **实体模型**（OpenSCENARIO）
   - **生命周期阶段**（OpenSCENARIO）
   - **参数化模型**（OpenSCENARIO）
3. 输出应以结构化表格为主，并附上补充说明和原文回溯标记

本 SKILL 适用于 Claude、其他 LLM 平台或手工分析流程。输出通过 `scenario_modeler` SKILL 进行下游处理，用于 OpenSCENARIO DSL 生成。

## 输出结构

```
## 0. 客户基本信息 (Customer Basic Information)
   - 基本信息表格
   - 公司识别依据与置信度
   - 应用产品与方案之前的问题 (初始状态)
   - 整体使用效果/收益综述 (最终状态)
   - 部署前后效果对比

## 1. 购买要素 (Purchase Elements with Parameterization)
   - 战略意图 / 业务意图 / 量化表达
   - 1.1 MoE 指标分析

## 2. 利益相关者清单 (Stakeholder List with Relationship Types)
   - 组织层级与角色名拆分

## 3. 冲突与优先级 (Conflicts and Priority)

## 4. 基于 ConOps 的状态模型 (ConOps-Grounded State Model)
   - 运行线程状态表
   - 参与者/系统状态表
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
```

## 🧭 你现在的第一步

请把第一份厂商 customer story 的文本内容贴给我，或至少给出第一段关键句。我们从这份真实内容开始进行 stakeholder extraction 和需求分析。

---

## 版本历史

- **0.2.0** (2026-04-12): 增加 OpenSCENARIO DSL 准备支持 - 状态模型、环境模型、实体模型、生命周期阶段、参数化模型、关系类型、增强的运行场景和触发/转换
- **0.1.0** (2026-04-10): 初始版本，用于客户故事的 INCOSE 需求工程 SKILL

---

**[English Version](README.md)**
