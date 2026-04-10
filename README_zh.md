# SKILLs 仓库

Claude Code SKILLs 集合仓库，包含多个专业化的 SKILL 定义，用于增强代码分析、生成和工程实践功能。

## 📚 SKILL 列表

### scenario_engine
INCOSE 场景工程 SKILL，提供系统工程场景分析和建模能力。

- **位置**: [`scenario_engine/`](./scenario_engine/)
- **用途**: 系统工程场景分析、建模、需求分解
- **关键词**: 场景，系统工程，INCOSE，需求，用例

## 🏗️ 项目结构

```
SKILLs/
├── README.md                    # 主仓库说明（此文件）
├── README_zh.md                 # 中文说明
├── .gitignore                   # Git 忽略配置
├── CONTRIBUTING.md              # 贡献指南
│
├── scenario_engine/             # 场景工程 SKILL
│   ├── SKILL.md                # SKILL 定义文件
│   ├── README.md               # SKILL 说明文档
│   ├── README_zh.md            # SKILL 中文说明
│   └── assets/
│       ├── templates/          # 场景模板文件
│       ├── prompts/            # 提示词文件
│       ├── scripts/            # 辅助脚本
│       └── examples/           # 使用示例
│
└── [other-skill]/              # 其他 SKILL（遵循相同结构）
    └── ...
```

## 🚀 SKILL 使用

每个 SKILL 可以通过以下方式使用：

1. **在 Copilot 中**: 输入 `/` 后查找 SKILL 名称
2. **通过提示词**: 提及 SKILL 相关的关键词，Agent 会自动加载

## 📝 创建新 SKILL

参考 [CONTRIBUTING.md](./CONTRIBUTING.md) 了解如何创建新的 SKILL。

基本步骤：
1. 创建 `<skill-name>/` 目录
2. 添加 `SKILL.md` 文件（SKILL 定义）
3. 创建 `assets/` 目录组织资源
4. 编写 `README.md` 文档

## 🔄 分支管理

- `master` - 生产稳定版本
- `dev` - 开发分支，新特性和改进

## 📄 许可证

MIT