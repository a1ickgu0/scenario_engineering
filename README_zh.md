# SKILLs 仓库

Claude Code SKILL 集合仓库，包含从售前调研到跨案例建模的完整需求工程工作流。

## 📚 SKILL 列表

### scenario_engineering（新增）

**顶层编排 SKILL**，协调完整工作流管道。管理目录结构、进度跟踪和任务恢复。

- **位置**: [`scenario_engineering/`](./scenario_engineering/)
- **用途**: 管道编排、目录管理、进度跟踪、任务恢复
- **关键词**: 编排、工作流协调、管道管理、任务恢复
- **版本**: 0.1.0
- **输入**: 项目配置（行业、国家、输入来源）
- **输出**: 完整项目目录，包含所有中间和最终输出
- **阶段**: 0（初始化）→ 1（调研）→ 2a（解析）→ 2b（分析）→ 3（建模）→ 4（完成）

### scenario_survey

**售前调研 SKILL**，用于生成行业定制化问卷收集客户期望和需求。使用客户友好语言（无专业术语），支持多语言输出（默认英文）。

- **位置**: [`scenario_survey/`](./scenario_survey/)
- **用途**: 售前需求收集、客户期望采集、利益相关者识别
- **关键词**: 售前调研、访谈指南、问卷生成、利益相关者引导、期望收集
- **版本**: 0.3.0
- **输入**: 行业选择 + 客户国家（语言定制）
- **输出**: 行业定制问卷 + 客户需求叙事文档
- **语言**: 英文（默认）、中文、日语、德语、法语、西班牙语、阿拉伯语

### scenario_parser（新增）

**文档提取 SKILL**，用于解析客户故事 PDF 和叙事文档生成结构化中间数据。输出双格式文件（MD + JSON），保留完整追溯性。

- **位置**: [`scenario_parser/`](./scenario_parser/)
- **用途**: 数据提取、PDF解析、中间格式生成
- **关键词**: 文档提取、PDF解析、数据提取、中间输出
- **版本**: 0.1.0
- **输入**: PDF文件、文本文档、调研叙事
- **输出**: `*-extracted.md` + `*-extracted.json`（双格式中间文件）
- **输出结构**: customer_info、stakeholder_mentions、pain_points、products、metrics、quotes

### scenario_analyzer

**INCOSE 需求工程 SKILL**，基于 scenario_parser 输出生成结构化分析。创建 12 节分析报告，用于 OpenSCENARIO DSL 准备。

- **位置**: [`scenario_analyzer/`](./scenario_analyzer/)
- **用途**: 单案例结构化分析、需求工程、OpenSCENARIO 准备
- **关键词**: 需求工程、INCOSE、利益相关者分析、客户故事
- **版本**: 0.7.0
- **输入**: Parser 输出（`*-extracted.md` + `*-extracted.json`）
- **输出**: 12 节分析报告（`*-analysis.md`）
- **变更**: 现需 parser 输出作为输入（架构拆分，从 v0.6.0）

### scenario_modeler

**跨案例建模 SKILL**，用于综合多个 scenario_analyzer 分析结果生成归纳模型。为 OpenSCENARIO DSL 生成准备行业、利益相关者和购买要素模型。

- **位置**: [`scenario_modeler/`](./scenario_modeler/)
- **用途**: 多案例综合、跨案例模式挖掘、模型生成
- **关键词**: 场景建模、综合、跨案例分析、行业模型
- **版本**: 0.5.0
- **输入**: 来自 scenario_analyzer 的多个 `-analysis.md` 文件
- **输出**: 行业模型、利益相关者模型、购买要素模型，含批判性分析

---

## 🔗 SKILL 链路工作流

从售前调研到跨案例建模的完整工作流：

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    编排层（scenario_engineering）                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Phase 0: 初始化                                                          │
│  • 确定输入来源（调研或独立文件）                                           │
│  • 创建输出目录结构                                                        │
│  • 初始化 state.json 进度跟踪                                              │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                           售前阶段（Phase 1）                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  [scenario_survey]                                                       │
│  • 生成行业定制问卷                                                        │
│  • 多语言支持                                                              │
│  • 收集：利益相关者、使用场景、成功标准                                      │
│         ↓                                                                │
│  客户需求叙事文档                                                          │
│                                                                          │
│  （可选 - 若提供独立文件则跳过）                                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                          提取阶段（Phase 2a）                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  [scenario_parser]                                                       │
│  • PDF/文本/叙事 → 结构化数据                                              │
│  • 双格式输出（MD + JSON）                                                 │
│  • 保留完整追溯性                                                          │
│         ↓                                                                │
│  提取文件（*-extracted.md + *-extracted.json）                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                          分析阶段（Phase 2b）                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  [scenario_analyzer]                                                     │
│  • 输入：Parser 输出（MD + JSON）                                          │
│  • INCOSE 需求工程方法                                                     │
│  • 12章节结构化输出                                                         │
│  • 状态/环境/实体/生命周期模型                                              │
│         ↓                                                                │
│  单案例分析报告（*-analysis.md）                                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                          建模阶段（Phase 3）                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  [scenario_modeler]                                                      │
│  • 跨案例综合                                                              │
│  • 行业/利益相关者/购买要素模型                                             │
│  • 批判性分析含可信度评级                                                   │
│         ↓                                                                │
│  OpenSCENARIO DSL 准备                                                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                          完成阶段（Phase 4）                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  • 验证完整性                                                              │
│  • 生成执行摘要                                                            │
│  • 归档 state.json                                                        │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### 架构变更（2026-04-21）

| 原架构 | 新架构 |
|--------|--------|
| `scenario_analyzer`（PDF → 分析） | `scenario_parser` + `scenario_analyzer` |
| 直接 PDF 处理 | Parser 输出中间 MD + JSON |
| 单阶段分析 | Phase 2a（Parser）+ Phase 2b（Analyzer） |

**拆分优势**:
- 解耦：Parser 可独立运行，批量 PDF 处理
- 灵活：Analyzer 接受 Parser 输出或手动准备的数据
- 可恢复：Parser 输出是检查点，Analyzer 可单独重试
- 可验证：中间数据可在分析前检查质量

---

## 🏗️ 项目结构

```
SKILLs/
├── README.md                    # 仓库说明（英文版本）
├── README_zh.md                 # 仓库说明（中文版本，本文件）
├── CLAUDE.md                    # Claude Code 指南
├── CONTRIBUTING.md              # 贡献指南
│
├── scenario_engineering/        # 编排 SKILL（新增）
│   ├── SKILL.md                 # SKILL 定义
│   ├── README.md                # 说明文档（英文）
│   ├── README_zh.md             # 说明文档（中文）
│   └── assets/
│       ├── templates/           # 状态/配置/进度模板
│       └── references/          # 阶段定义、恢复指南
│
├── scenario_survey/             # 售前调研 SKILL
│   ├── SKILL.md                 # SKILL 定义
│   ├── README.md                # 说明文档（英文）
│   ├── README_zh.md             # 说明文档（中文）
│   └── assets/
│       ├── templates/           # 9个行业问卷模板
│       └── references/          # 行业模式库
│
├── scenario_parser/             # 文档提取 SKILL（新增）
│   ├── SKILL.md                 # SKILL 定义
│   ├── README.md                # 说明文档（英文）
│   ├── README_zh.md             # 说明文档（中文）
│   └── assets/
│       ├── templates/           # 提取 JSON/MD 模板
│       └── references/          # 提取规则参考
│
├── scenario_analyzer/           # 分析 SKILL
│   ├── SKILL.md                 # SKILL 定义（v0.7.0）
│   ├── README.md                # 说明文档（英文）
│   ├── README_zh.md             # 说明文档（中文）
│   ├── CLAUDE.md                # Claude Code 指南
│   └── assets/
│       ├── prompts/             # 分析提示
│       └── references/          # 分析指南
│
├── scenario_modeler/            # 跨案例建模 SKILL
│   ├── SKILL.md                 # SKILL 定义
│   ├── README.md                # 说明文档（英文）
│   ├── README_zh.md             # 说明文档（中文）
│   └── assets/
│       ├── prompts/             # 17个综合提示
│       ├── references/          # 10个参考指南
│       └── templates/           # 14个输出模板
│
└── [other-skill]/               # 其他 SKILL（遵循相同结构）
```

---

## 🚀 SKILL 使用

每个 SKILL 可以通过以下方式使用：

1. **在 Claude Code 中**: 输入 `/` 后查找 SKILL 名称
2. **通过提示词**: 提及 SKILL 相关关键词，Agent 会自动加载

### 快速开始示例

**完整管道（编排模式）**:
```
# 启动完整工作流
/scenario_engineering --new
→ 行业：酒店业
→ 国家：马来西亚
→ 输入：./customer-stories/*.pdf
→ 输出完整项目目录
```

**逐步执行（手动模式）**:
```
# 步骤1：售前调研
/scenario_survey
→ 生成马来西亚连锁酒店问卷

# 步骤2：访谈后合成叙事
/scenario_survey --synthesize
→ 客户需求叙事文档

# 步骤3：从文档提取数据
/scenario_parser
→ 输入：叙事或 PDF
→ 输出：extracted.md + extracted.json

# 步骤4：结构化分析
/scenario_analyzer
→ 输入：extracted.md + extracted.json
→ 输出：analysis.md（12章节）

# 步骤5：跨案例建模
/scenario_modeler
→ 输入：多个 analysis.md 文件
→ 输出：行业/利益相关者/购买要素模型
```

---

## 📊 最近变更

- **2026-04-21**: 架构重构
  - **新增 `scenario_engineering`** (v0.1.0) - 顶层编排 SKILL
  - **新增 `scenario_parser`** (v0.1.0) - 文档提取为 MD + JSON
  - **修改 `scenario_analyzer`** (v0.7.0) - 现接受 Parser 输出作为输入
  - Phase 2 拆分为 Phase 2a（Parser）+ Phase 2b（Analyzer）
  - Parser/Analyzer 独立恢复支持

- **2026-04-16**: 增强 `scenario_analyzer` (v0.6.0)
  - 新增利益相关者痛点提取
  - 新增表格综述说明

- **2026-04-12**: 新增 `scenario_survey` SKILL (v0.2.0)
  - 售前定位、多语言支持
  - 9个行业定制问卷模板

- **2026-04-12**: 新增 `scenario_modeler` SKILL (v0.1.0)
  - 42个文件用于跨案例综合

---

## 📝 创建新 SKILL

参考 [CONTRIBUTING.md](./CONTRIBUTING.md) 了解如何创建新 SKILL。

标准 SKILL 结构：
```
skill-name/
├── SKILL.md           # 必需：YAML frontmatter + 定义
├── README.md          # 必需：英文说明文档
├── README_zh.md       # 可选：中文说明文档
└── assets/
    ├── prompts/       # 提示模板
    ├── references/    # 参考文档
    ├── templates/     # 输出模板
    └── tests/         # 生成的示例
```

---

## 🔄 分支管理

- `main` - 生产稳定版本
- `dev` - 开发分支，新特性和改进

---

## 📄 许可证

MIT