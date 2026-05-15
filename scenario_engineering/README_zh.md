# Scenario Engineering SKILL

客户需求工程完整工作流的顶层编排 SKILL。

## 概述

本 SKILL 协调四个下游 SKILL 构成结构化流水线：

```
scenario_survey → scenario_parser → scenario_analyzer → scenario_modeler
```

**核心特性**：
- **流水线编排**：端到端工作流统一入口
- **目录管理**：结构化输出组织
- **进度跟踪**：JSON 状态文件 + MD 进度报告
- **任务恢复**：中断后支持继续执行
- **SKILL 协调**：顺序调用并保持状态

## 执行模式

| 模式 | 描述 | 用途 |
|------|------|------|
| `--new` | 启动新项目 | 新工作流流水线 |
| `--resume` | 恢复中断任务 | 从崩溃恢复 |
| `--from-phase N` | 从指定阶段开始 | 跳过已完成阶段 |
| `--validate` | 验证现有输出 | 仅质量检查 |
| `--dry-run` | 仅规划不执行 | 目录结构预览 |

## 阶段定义

| 阶段 | 名称 | SKILL | 输出 |
|------|------|-------|------|
| 0 | 初始化 | - | 目录结构、state.json |
| 1 | 售前调研 | scenario_survey | 问卷、叙事文档 |
| 2 | 文档提取 | scenario_parser | extracted.md + extracted.json |
| 3 | 结构化分析 | scenario_analyzer | 分析报告（12 章节） |
| 4 | 跨案例建模 | scenario_modeler | 行业/利益相关者/购买模型 |
| 5 | 最终化 | - | 执行摘要、完整性检查 |

## 目录结构

```
project-{name}-{timestamp}/
├── state.json                     # 进度状态（JSON）
├── config.json                    # 配置文件
├── inputs/
│   ├── raw/                       # 原始 PDF/文本
│   └── extracted/                 # PDF 转文本
├── outputs/
│   ├── progress/                  # MD 进度报告
│   ├── phase1-survey/
│   ├── phase2-parser/
│   │   ├── extracted/
│   │   └── problems/
│   ├── phase3-analyzer/
│   │   ├── reports/
│   │   └── problems/
│   ├── phase4-model/
│   └── phase5-final-report/
└── archive/
    └── state-final.json
```

## 快速开始

```bash
# 用模板初始化一个新项目工作区
python3 scenario_engineering/scripts/init_project.py --project-name hospitality-poc

# 新项目
/scenario_engineering --new
→ 行业：酒店业
→ 国家：马来西亚
→ 输入：./customer-stories/*.pdf

# 恢复中断任务
/scenario_engineering --resume

# 验证输出
/scenario_engineering --validate

# 从特定阶段开始
/scenario_engineering --from-phase 2
```

## 恢复机制

- **状态文件**：`state.json` 跟踪进度
- **检查点**：每批次后更新
- **恢复**：跳过已完成工作，继续待处理
- **无回滚**：仅向前恢复

## 资产文件

| 类型 | 文件 |
|------|------|
| 模板 | state-template.json, config-template.json, progress-report-template.md |
| 参考 | recovery-guidelines.md, phase-definitions.md, skill-invocation-mapping.md |

## 文档

- [README.md](README.md) - 英文文档
- [SKILL.md](SKILL.md) - 完整 SKILL 定义
