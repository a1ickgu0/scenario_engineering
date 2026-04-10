# 贡献指南

感谢你对 SKILL 工程的兴趣！

## 工作流程

1. Fork 本仓库
2. 从 `dev` 分支创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的改动 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request 到 `dev` 分支

## 代码规范

- 使用 Black 进行代码格式化
- 使用 isort 管理导入
- 遵循 PEP 8 规范
- 添加适当的注释和文档

## 提交信息规范

使用以下格式提交信息：

```
feat: 添加新功能描述
fix: 修复 bug 描述
docs: 文档更新
style: 代码格式调整
refactor: 代码重构
test: 添加/修改测试
chore: 构建、依赖等非代码改动
```

## 测试

在提交 PR 之前，请确保所有测试通过：

```bash
pytest
```
