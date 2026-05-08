# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## Repository Overview

This is a SKILLs repository containing specialized SKILL definitions for Codex. SKILLs form a complete workflow chain from pre-sales survey to cross-case modeling for customer requirements engineering.

## Repository Distribution

When this repository is provided by GitHub URL and the goal is to discover or install skills automatically:

1. If only the repository root is inspected, read root `SKILL.md` first.
2. Read `skills-index.json` as the repository manifest.
3. Treat each listed `path` as a child skill root and `SKILL.md` as the canonical entry file.
4. Read `agents/openai.yaml` under the repository root or child skill when UI-facing metadata is needed.
5. Use `scripts/install-skills.py` to install one skill or all skills into the target skill directory.

Default Codex destination is `~/.codex/skills`. For Claude Code, pass an explicit `--dest` that matches the user's configured skill directory.

## SKILL Chain Architecture

```
scenario_engineering (顶层编排)
    ↓
scenario_survey (售前收集期望) → scenario_parser (文档提取) → scenario_analyzer (结构化分析) → scenario_modeler (跨案例建模)
```

| Stage | Phase | SKILL | Input | Output |
|-------|-------|-------|-------|--------|
| Orchestration | 0 | scenario_engineering | Project config | Directory structure, state.json |
| Pre-Sales | 1 | scenario_survey | Industry + Country | Questionnaire + Narrative |
| Extraction | 2 | scenario_parser | PDF/Text/Narrative | extracted.md + extracted.json |
| Analysis | 3 | scenario_analyzer | Parser outputs | 12-section analysis |
| Modeling | 4 | scenario_modeler | Multiple analyses | Industry/Stakeholder/Purchase models |
| Finalization | 5 | scenario_engineering | All outputs | Summary + Archive |

## Current SKILLs

### scenario_engineering (v0.1.0) - NEW

**Top-level orchestration SKILL** for coordinating the complete workflow.

**Structure**: [scenario_engineering/](scenario_engineering/)
- [SKILL.md](scenario_engineering/SKILL.md) - Orchestration definition
- [assets/templates/](scenario_engineering/assets/templates/) - State/Config/Progress templates
- [assets/references/](scenario_engineering/assets/references/) - Phase definitions, Recovery guidelines

**Key Features**:
- Pipeline orchestration (6 phases: 0-5)
- Directory management with structured outputs
- Dual-format progress tracking (JSON state + MD reports)
- Task recovery with checkpoint-based resume
- SKILL coordination and invocation mapping

**Invocation**: Keywords like "orchestration", "pipeline", "workflow", "project setup"

### scenario_survey (v0.3.0)

**Pre-sales survey SKILL** for collecting customer expectations.

**Structure**: [scenario_survey/](scenario_survey/)
- [SKILL.md](scenario_survey/SKILL.md) - SKILL definition
- [assets/templates/](scenario_survey/assets/templates/) - 9 industry questionnaires

**Key Features**:
- Customer-friendly language (no INCOSE jargon)
- Multi-language support (default English)
- Industry-specific templates

**Invocation**: Keywords like "survey", "questionnaire", "interview guide", "pre-sales"

### scenario_parser (v0.1.0) - NEW

**Document extraction SKILL** for parsing into structured intermediate data.

**Structure**: [scenario_parser/](scenario_parser/)
- [SKILL.md](scenario_parser/SKILL.md) - Parser definition
- [assets/templates/](scenario_parser/assets/templates/) - extracted-json-template.json, extracted-md-template.md
- [assets/references/](scenario_parser/assets/references/) - extraction-patterns.md

**Output**: Dual-format files:
- `{customer}-extracted.md` - Human-readable with references
- `{customer}-extracted.json` - Structured data for Analyzer

**JSON Structure**:
```json
{
  "customer_info": { "title", "company", "industry", "country" },
  "stakeholder_mentions": [{ "name", "role_type", "expectations_raw", "reference" }],
  "pain_points_mentions": [{ "stakeholder", "pain_point", "reference" }],
  "product_mentions": [{ "name", "type", "reference" }],
  "metrics_mentions": [{ "value", "unit", "context", "reference" }],
  "raw_quotes": [{ "quote", "speaker", "reference" }]
}
```

**Invocation**: Keywords like "parser", "extract", "PDF parsing", "document extraction"

### scenario_analyzer (v0.7.0) - MODIFIED

**INCOSE requirements engineering SKILL** for structured analysis.

**Structure**: [scenario_analyzer/](scenario_analyzer/)
- [SKILL.md](scenario_analyzer/SKILL.md) - SKILL definition
- [assets/prompts/](scenario_analyzer/assets/prompts/) - Analysis prompt
- [assets/references/](scenario_analyzer/assets/references/) - Analysis guidelines

**Input Change**: Now requires Parser outputs (`*-extracted.md` + `*-extracted.json`)

**Output Structure** (12 sections, numbered 0-12):
- 0. Customer Basic Information
- 1. Purchase Elements (ranked, quantified)
- 2. Stakeholder List (roles, pain points, expectations)
- 3. Conflicts and Priority
- 4. State Model
- 5. Environment Model
- 6. Entity Model
- 7. Lifecycle Phases
- 8. Operational Scenarios
- 9. Engagement and Commitment
- 10. Products and Solutions
- 11. Parameterization Model
- 12. Traceability and Notes

**Invocation**: Keywords like "customer story", "stakeholder analysis", "INCOSE"

### scenario_modeler (v0.5.0)

**Cross-case modeling SKILL** for synthesizing patterns.

**Structure**: [scenario_modeler/](scenario_modeler/)
- [SKILL.md](scenario_modeler/SKILL.md) - SKILL definition
- [assets/prompts/](scenario_modeler/assets/prompts/) - 17 synthesis prompts
- [assets/templates/](scenario_modeler/assets/templates/) - 14 output templates

**Output Models**:
- Industry Model (patterns, challenges, solutions)
- Stakeholder Model (Category + Role layers)
- Purchase Factor Model (Driver → Implementation → Metrics)

**Invocation**: Keywords like "model synthesis", "cross-case", "pattern extraction"

## Workflow Example

```
# Option A: Orchestrated (Full Pipeline)
/scenario_engineering --new
→ Industry: Hospitality, Country: Malaysia
→ Input: ./customer-stories/*.pdf
→ Outputs complete project directory

# Option B: Manual Step-by-Step
/scenario_survey
→ Output: questionnaire + narrative

/scenario_parser
→ Input: narrative or PDF
→ Output: extracted.md + extracted.json

/scenario_analyzer
→ Input: extracted.md + extracted.json
→ Output: analysis.md (12 sections)

/scenario_modeler
→ Input: multiple analysis.md files
→ Output: Industry/Stakeholder/Purchase models
```

## Critical Operational Rules

### scenario_engineering: Recovery Rules

- **RR-01**: Forward recovery only (no rollback)
- **RR-02**: Skip completed work (check processed_files)
- **RR-03**: Parser outputs are checkpoints (Analyzer can resume separately)
- **RR-04**: state.json tracks phase2_parser and phase3_analyzer independently

### scenario_survey: Industry Template Reference (TR-01 to TR-04)

**MANDATORY**: Read corresponding template from `assets/templates/` first.

| Industry | Template File |
|----------|---------------|
| Hospitality | hospitality-template.md |
| Healthcare | healthcare-template.md |
| Education | education-template.md |
| Logistics | logistics-template.md |
| Manufacturing | manufacturing-template.md |
| Retail | retail-template.md |
| Services | services-template.md |
| Sports/Entertainment | sports-entertainment-template.md |
| Generic/Other | generic-template.md |

### scenario_parser: Extraction Rules

- **ER-01**: Every extracted item must include reference (`Page X, Line Y`)
- **ER-02**: Preserve original language (do not translate)
- **ER-03**: Multiple mentions recorded separately
- **ER-04**: JSON must be parseable, MD must be readable

### scenario_analyzer: Quality Requirements

**Input Validation**: Check Parser outputs before analysis:
- extracted.json parseable
- Required fields present (customer_info, stakeholder_mentions)
- At least 1 product_mention

**Output Completeness**: All 12 sections (0-12) must be generated.

**Traceability**: Use references from extracted files.

**Parallel Processing**:

| Document Count | Recommended Agents |
|----------------|-------------------|
| 1-5 | 1 (serial) |
| 6-15 | 2-3 |
| 16-30 | 4-5 |
| 31-50 | 6-8 |
| 50+ | 8-10 |

## Directory Structure (scenario_engineering)

```
project-{name}-{timestamp}/
├── state.json                     # Progress state
├── config.json                    # Configuration
├── inputs/
│   ├── raw/                       # Original PDFs/texts
│   └── extracted/                 # PDF-to-text
├── outputs/
│   ├── progress/                  # MD progress reports
│   ├── phase1-survey/
│   ├── phase2-parser/             # Parser outputs (NEW)
│   │   └── extracted/             # *.md + *.json
│   ├── phase3-analyzer/           # Analyzer outputs (NEW)
│   │   └── reports/               # *-analysis.md
│   ├── phase4-model/
│   └── phase5-final-report/
└── archive/
    └── state-final.json
```

## PDF Processing Workflow

When processing customer story PDFs:

1. **Extract text**: `pdftotext -layout input.pdf output.txt`
2. **Add references**: Mark page numbers, sections
3. **Clean content**: Remove headers, footers
4. **Validate**: Ensure text is complete

## Language Handling

Generate localized output for customers from major countries. English is fallback for minor countries.

| Region | Countries | Language |
|--------|-----------|----------|
| East Asia | China, Japan, Korea | Chinese/Japanese/Korean |
| Europe | Germany, France, Italy, Spain | German/French/Italian/Spanish |
| Southeast Asia | Malaysia, Thailand, Vietnam | Malay/Thai/Vietnamese |
| Middle East | Saudi Arabia, UAE, Egypt | Arabic |
| English-speaking | USA, UK, Australia | English |

## Creating New SKILLs

Follow the standard structure:
```
skill-name/
├── SKILL.md           # Required: YAML frontmatter + definition
├── README.md          # Required: English documentation
├── README_zh.md       # Optional: Chinese documentation
└── assets/
    ├── prompts/       # Prompt templates
    ├── references/    # Reference documents
    ├── templates/     # Output templates
    └── tests/         # Generated examples
```

## Branch Conventions

- `main` - Production stable version
- `dev` - Development branch for new features

## Commit Message Format

```
feat: Add feature description
fix: Fix bug description
docs: Documentation update
refactor: Code refactor description
test: Test-related description
chore: Misc changes description
```
