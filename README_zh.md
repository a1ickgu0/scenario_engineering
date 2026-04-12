# SKILLs 仓库

Claude Code SKILLs 集合仓库，包含多个专业化的 SKILL 定义，用于增强代码分析、生成和工程实践功能。

## 📚 SKILL 列表

### scenario_engine

INCOSE 需求工程 SKILL，用于从客户故事 PDF 或文本中提取利益相关者信息和运营概念。输出结构化准备用于 OpenSCENARIO DSL。

- **位置**: [`scenario_engine/`](./scenario_engine/)
- **用途**: 单案例客户故事分析、需求提取、OpenSCENARIO 准备
- **关键词**: 需求工程、INCOSE、利益相关者分析、客户故事、场景分析
- **版本**: 0.2.0
- **输出**: 生成 `-analysis.md` 文件（客户信息、购买要素、利益相关者、状态/环境/实体模型、生命周期、参数化）

### scenario_modeler

SKILL 用于综合多个 scenario_engine 分析结果生成归纳模型和跨案例模式。为 OpenSCENARIO DSL 生成准备行业、利益相关者和购买要素模型。

- **位置**: [`scenario_modeler/`](./scenario_modeler/)
- **用途**: 多案例综合、跨案例模式挖掘、行业/利益相关者/购买要素模型生成、OpenSCENARIO DSL 准备
- **关键词**: 场景建模、综合、跨案例分析、行业模型、利益相关者模型、DSL 准备
- **版本**: 0.1.0
- **输入**: 来自 scenario_engine 的多个 `-analysis.md` 文件
- **输出**: 行业模型、利益相关者模型、购买要素模型、状态/环境/实体/生命周期/参数化模型和交叉分析矩阵

## 🏗️ 项目结构

```
SKILLs/
├── README.md                    # 仓库说明（英文版本）
├── README_zh.md                 # 仓库说明（中文版本，本文件）
├── CHANGES_ANALYSIS.md          # 最近变更的详细分析
├── COMMIT_MESSAGE.md            # 提交消息总结
├── .gitignore                   # Git 忽略配置
├── CONTRIBUTING.md              # 贡献指南
│
├── scenario_engine/             # 场景工程 SKILL
│   ├── SKILL.md                # SKILL 定义及元数据
│   ├── README.md               # SKILL 说明（英文）
│   ├── README_zh.md            # SKILL 说明（中文）
│   ├── CLAUDE.md               # Claude Code 编码指南
│   └── assets/
│       ├── prompts/            # 提示词文件
│       ├── references/         # 参考文档
│       └── examples/           # 使用示例
│
├── scenario_modeler/           # 场景建模综合 SKILL
│   ├── SKILL.md                # SKILL 定义及元数据
│   ├── README.md               # SKILL 说明（英文）
│   ├── README_zh.md            # SKILL 说明（中文）
│   └── assets/
│       ├── prompts/            # 17 个分析和综合提示词文件
│       ├── references/         # 10 个参考指南和映射文档
│       └── templates/          # 14 个输出模板
│
└── [other-skill]/              # 其他 SKILL（遵循相同结构）
    └── ...
```

## 🚀 SKILL 使用

每个 SKILL 可以通过以下方式使用：

1. **在 Copilot 中**: 输入 `/` 后查找 SKILL 名称
2. **通过提示词**: 提及 SKILL 相关的关键词，Agent 会自动加载

### 工作流：客户故事 → OpenSCENARIO DSL

```
客户故事 PDF/文本
    ↓
[scenario_engine] - 单案例分析
    ↓
*-analysis.md 文件（每个故事一个）
    ↓
[scenario_modeler] - 多案例综合
    ↓
行业/利益相关者/购买要素模型
    ↓
OpenSCENARIO DSL（参数定义）
```

## 📊 最近变更

- **2026-04-12**: scenario_engine 升级至 v0.2.0，新增 OpenSCENARIO DSL 准备支持
  - 新增 5 个分析维度: 状态模型、环境模型、实体模型、生命周期阶段、参数化
  - 输出扩展从 9 项到 14 项，提供双语文档
  - 详见 [SCENARIO_ENGINE_CHANGES.md](./SCENARIO_ENGINE_CHANGES.md)（详细分析）
  - 详见 [SCENARIO_ENGINE_COMMIT.md](./SCENARIO_ENGINE_COMMIT.md)（升级总结）

- **2026-04-12**: 新增 `scenario_modeler` SKILL（v0.1.0），共 42 个新文件
  - 17 个用于模型综合和 OpenSCENARIO 准备的提示词模板
  - 10 个分类体系和映射关系参考指南
  - 14 个结构化输出模板
  - 详见 [CHANGES_ANALYSIS.md](./CHANGES_ANALYSIS.md)（详细分析）
  - 详见 [COMMIT_MESSAGE.md](./COMMIT_MESSAGE.md)（提交消息总结）

## 📝 创建新 SKILL

参考 [CONTRIBUTING.md](./CONTRIBUTING.md) 了解如何创建新的 SKILL。

基本步骤：

1. 创建 `<skill-name>/` 目录
2. 添加 `SKILL.md` 文件（SKILL 定义）
3. 创建 `assets/` 目录组织资源
4. 编写 `README.md` 文档（英文）
5. 可选：添加 `README_zh.md` 文档（中文版本）

## 🔄 分支管理

- `master` - 生产稳定版本
- `dev` - 开发分支，新特性和改进

## 📄 许可证

MIT