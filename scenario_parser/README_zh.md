# Scenario Parser SKILL

文档提取 SKILL，用于从客户故事文档中解析结构化中间数据。

## 概述

从 PDF、文本和叙事文档中提取数据**不进行分析**。生成双格式输出（MD + JSON），供 `scenario_analyzer` 使用。

**核心特性**：
- PDF 文本提取，带引用标记
- 结构化数据提取（利益相关者、产品、指标）
- 双格式输出，人类和机器均可使用
- 完整追溯性到源位置

## 输入来源

| 类型 | 格式 | 处理方式 |
|------|------|----------|
| PDF | `.pdf` | pdftotext 提取 |
| 叙事文档 | `.md` | 直接解析 |
| 文本 | `.txt` | 结构解析 |

## 输出文件

每个文档生成：
- `{customer}-extracted.md` - 人类可读，带引用
- `{customer}-extracted.json` - 结构化数据，供 Analyzer 使用

## JSON 结构概要

```json
{
  "content_extract": { "company", "industry", "country", "year", "company_identification_basis" },
  "stakeholder_mentions": [{ "name", "role_type", "role_title_raw", "stakeholder_layer_hint", "expectations_raw", "reference" }],
  "pain_points_mentions": [{ "stakeholder", "pain_point", "reference" }],
  "product_mentions": [{ "name", "type", "reference" }],
  "metrics_mentions": [{ "value", "unit", "before_value", "after_value", "moe_candidate", "reference" }],
  "raw_quotes": [{ "quote", "language", "speaker", "reference" }]
}
```

## 提取防错规则

- 文件名只可作为辅助线索，不能单独作为公司/客户识别依据。
- 利益相关者必须拆分为组织层级与具体角色名。
- 指标在原文有证据时，要保留部署前/后对比与 MoE 候选标记。
- 非中文引用保留原文，并保留语言字段供下游双语分析使用。

## 快速开始

```bash
# 单文档处理
/scenario_parser
→ 输入：./customer-story.pdf
→ 输出：outputs/extracted/customer-extracted.md + .json

# 批量处理
/scenario_parser --batch
→ 输入：./documents/*.pdf
→ 输出：outputs/extracted/*.md + *.json
```

## 集成流程

```
scenario_parser → scenario_analyzer

Parser 输出供给 Analyzer：
- extracted.json → 结构化数据输入
- extracted.md → 上下文验证
```

## 并行处理策略

| 文档数量 | Agent 数量 |
|----------|------------|
| 1-10 | 1 |
| 11-30 | 2-3 |
| 31-50 | 4-5 |
| 50+ | 6-8 |

## 文档

- [README.md](README.md) - 英文文档
- [SKILL.md](SKILL.md) - 完整 SKILL 定义
