# Scenario Parser SKILL

Document extraction SKILL for parsing customer story documents into structured intermediate data.

## Overview

Extracts data from PDFs, texts, and narratives **without analysis**. Produces dual-format outputs (MD + JSON) that feed `scenario_analyzer`.

**Key Features**:
- PDF text extraction with reference markers
- Structured data extraction (stakeholders, products, metrics)
- Dual-format output for human and machine use
- Full traceability to source locations

## Input Sources

| Type | Format | Processing |
|------|--------|------------|
| PDF | `.pdf` | pdftotext extraction |
| Narrative | `.md` | Direct parsing |
| Text | `.txt` | Structure parsing |

## Output Files

For each document:
- `{customer}-extracted.md` - Human-readable with references
- `{customer}-extracted.json` - Structured data for Analyzer

## JSON Structure Highlights

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

## Extraction Guards

- Filename is helper context only and cannot be the sole evidence for company/customer identity.
- Stakeholders are split into organizational layer and concrete role title.
- Metrics preserve before/after comparisons and MoE candidates when source evidence exists.
- Non-Chinese quotes keep original wording, and language is preserved for downstream bilingual analysis.

## Quick Start

```bash
# Single document
/scenario_parser
→ Input: ./customer-story.pdf
→ Output: outputs/extracted/customer-extracted.md + .json

# Batch processing
/scenario_parser --batch
→ Input: ./documents/*.pdf
→ Output: outputs/extracted/*.md + *.json
```

## Integration

```
scenario_parser → scenario_analyzer

Parser outputs feed Analyzer:
- extracted.json → Structured data input
- extracted.md → Context verification
```

## Parallel Processing

| Documents | Agents |
|-----------|--------|
| 1-10 | 1 |
| 11-30 | 2-3 |
| 31-50 | 4-5 |
| 50+ | 6-8 |

## Documentation

- [README_zh.md](README_zh.md) - Chinese documentation
- [SKILL.md](SKILL.md) - Full SKILL definition
