# 贡献指南

感谢你对 SKILLs 仓库的兴趣和贡献！

## 📋 贡献类型

我们欢迎以下类型的贡献：

1. **新 SKILL 开发** - 创建新的 SKILL 定义
2. **SKILL 改进** - 增强现有 SKILL 功能
3. **模板和资源** - 添加有用的模板、提示词、示例
4. **文档** - 改进和完善文档
5. **Bug 修复** - 修复现有 SKILL 中的问题

## 🚀 工作流程

### 1. Fork 和分支

```bash
# Fork 仓库（通过 GitHub UI）
# Clone 你的 fork
git clone https://github.com/your-username/SKILLs.git

# 创建特性分支（从 dev 分支）
git checkout -b feature/your-feature-name
```

### 2. 创建新 SKILL

如果添加新的 SKILL，遵循标准目录结构：

```
your-skill-name/
├── SKILL.md                 # SKILL 定义文件（必须）
├── README.md               # SKILL 文档（必须）
└── assets/
    ├── templates/          # 模板文件
    ├── prompts/            # 提示词文件
    ├── examples/           # 使用示例
    └── references/         # 参考文档
```

### 3. SKILL.md 文件要求

新 SKILL 必须包含以下 YAML frontmatter：

```yaml
---
name: skill-name
description: "Clear description. Use when: specific use cases"
tags:
  - tag1
  - tag2
version: "0.1.0"
---
```

### 4. 提交改动

```bash
# 添加改动
git add .

# 提交（遵循提交信息规范）
git commit -m "feat: 添加新 SKILL"
git commit -m "docs: 改进 XXX SKILL 文档"
git commit -m "fix: 修复 XXX SKILL 中的问题"

# 推送到你的 fork
git push origin feature/your-feature-name
```

### 5. 提交 Pull Request

1. 在 GitHub 上创建 Pull Request
2. 目标分支：`dev`（开发新特性）或 `master`（bug 修复）
3. 描述你的改动
4. 等待审查和批准

## 📝 提交信息规范

使用以下格式提交信息：

```
feat: 添加新功能描述
fix: 修复 bug 描述
docs: 文档更新描述
refactor: 代码重构描述
test: 测试相关描述
chore: 杂项改动描述
```

**示例**：
```bash
git commit -m "feat: Add INCOSE scenario analysis SKILL"
git commit -m "docs: Update scenario-engine README with examples"
git commit -m "fix: Correct typo in use-case template"
```

## 🎨 代码规范

### 文档规范

- 使用 Markdown 格式
- 遵循 [文档标准](scenario_engine/assets/references/documentation-standards.md)
- 保持清晰和一致的风格
- 检查拼写和语法

### 命名规范

**文件名**：
- 使用小写字母
- 用连字符分隔单词：`scenario-template.md`
- 避免空格和特殊字符

**SKILL 名称**：
- 使用小写字母
- 用连字符分隔：`skill-name`
- 有意义且描述性

### 模板和示例

- 使用已有的模板确保一致性
- 提供现实的示例
- 包含清晰的说明和注释

## ✅ 检查清单

提交 PR 前，确保：

- [ ] 代码/文档清晰明了
- [ ] 拼写和语法正确
- [ ] 遵循命名规范
- [ ] 附加必要的 YAML frontmatter
- [ ] 包含相关的 README 或文档
- [ ] 如果是新 SKILL，更新主 README.md
- [ ] 提交信息清晰有意义
- [ ] 本地测试通过（如适用）

## 🐛 报告 Bug

如果发现 bug：

1. 检查是否已有相关 issue
2. 创建新 issue 并详细描述：
   - Bug 描述
   - 复现步骤
   - 预期行为
   - 实际行为
   - 相关 SKILL 名称

## 💡 建议和讨论

- 在 Discussions 中提出想法
- 标记相关的 issue
- 提供背景和用例

## 📚 资源

- [SKILL 定义文档](scenario_engine/SKILL.md)
- [场景工程最佳实践](scenario_engine/assets/references/best-practices.md)
- [文档标准](scenario_engine/assets/references/documentation-standards.md)
- [INCOSE 实践](scenario_engine/assets/references/incose-practices.md)

## 🤝 社区

- 尊重所有贡献者
- 建设性提供反馈
- 帮助他人改进

## 📄 许可证

通过提交贡献，你同意你的改动在 MIT 许可证下发布。

---

感谢你的贡献！我们期待与你合作！🎉
