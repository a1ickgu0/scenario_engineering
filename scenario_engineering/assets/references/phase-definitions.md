# Phase Definitions

## Overview

This document defines the 6 execution phases (0-5) for scenario_engineering, including transitions, pre-conditions, and completion criteria.

---

## Phase 0: Initialization

### Purpose

Setup project structure, determine input sources, validate inputs.

### Input Source Determination

Phase 2 (Parser) has two possible input sources:
1. **Survey Output**: Narratives from Phase 1 (`outputs/phase1-survey/narratives/`)
2. **Independent Files**: User-provided documents (PDFs primarily)

### User Prompt for Input Directory

When starting with `--new` or `--from-phase 2`:
```
"请提供独立文档目录路径（如果跳过survey阶段直接进入文档提取流程）：
→ 目录路径: /path/to/documents/
→ 包含文件: PDF文件为主，支持 .txt 和 .md 格式
→ 如不提供，将使用survey阶段的输出作为输入"
```

### Input Mode Detection

```
If user provides independent_directory:
  → input_mode = "independent"
  → Copy files to inputs/raw/
  → Set skip_phase1 = true

If no independent_directory:
  → input_mode = "survey"
  → Phase 1 required
  → Phase 2 uses survey outputs
```

### Pre-Conditions

| Condition | Validation |
|-----------|------------|
| Input mode determined | Either "survey" or "independent" |
| If independent: directory provided | Directory exists and contains files |
| Industry specified | Valid industry from taxonomy |
| Country specified | Valid country for language handling |
| Output directory writable | Directory creation permission |

### Actions

| Step | Action | Output |
|------|--------|--------|
| 1 | Prompt user for input source type | Determine input_mode |
| 2 | If independent: prompt for directory path | Store independent_directory |
| 3 | Create project root directory | `project-{name}-{timestamp}/` |
| 4 | Create subdirectories | `inputs/`, `outputs/`, `archive/` |
| 5 | Copy independent files if applicable | `inputs/raw/*.pdf` |
| 6 | Initialize state.json | `state.json` with input_mode |
| 7 | Create config.json | `config.json` from user params |
| 8 | Validate input files | Check PDF readable, text complete |
| 9 | Extract PDF text if needed | `inputs/extracted/*.txt` |
| 10 | Generate init report | `outputs/progress/phase0-init-report.md` |
| 11 | Update state | Set phase0 completed |

### Completion Criteria

- Input mode determined (survey or independent)
- All directories created
- state.json initialized with correct input_mode
- If independent: files copied to inputs/raw/
- Input files validated
- Phase0 init report generated

### Transition

```
Phase 0 → Phase 1 OR Phase 2

If input_mode = "independent":
  → Skip Phase 1
  → Phase 0 → Phase 2 (with skip_phase1 = true)

If input_mode = "survey":
  → Phase 0 → Phase 1 (normal flow)
```

---

## Phase 1: Pre-Sales Survey (scenario_survey)

### Purpose

Generate industry-specific questionnaires, synthesize narratives from interviews.

### SKILL Invoked

`/scenario_survey`

### Skip Conditions

Phase 1 is skipped when:
- `input_mode = "independent"`
- User specifies `--skip-phase1`
- User specifies `--from-phase 2`

### Pre-Conditions (when not skipped)

| Condition | Source |
|-----------|--------|
| Phase 0 completed | state.json phase0 status |
| Industry template available | scenario_survey/assets/templates/{industry}-template.md |
| Country specified | config.json country |

### Actions (when not skipped)

| Step | Action | Output |
|------|--------|--------|
| 1 | Read industry template | Template content loaded |
| 2 | Generate questionnaire | `outputs/phase1-survey/questionnaires/{industry}-{country}-q-{lang}.md` |
| 3 | (Optional) Synthesize narrative | `outputs/phase1-survey/narratives/{customer}-narrative.md` |
| 4 | Update state after each file | Add to processed_files |
| 5 | Generate progress report | `outputs/progress/phase1-survey-progress.md` |
| 6 | Set phase completed | Update state.json |

### Completion Criteria

- Questionnaires generated (count matches expected)
- Narratives generated (if provided interview notes)
- Progress report updated
- state.json phase1 = completed

### Transition

```
Phase 1 → Phase 2
Conditions:
  - phase1 status = completed
  - phase2 status = pending
  - narratives available OR narratives skipped
```

---

## Phase 2: Document Extraction (scenario_parser)

### Purpose

Extract structured data from documents into intermediate format (MD + JSON).

### SKILL Invoked

`/scenario_parser`

### Pre-Conditions

| Condition | Source |
|-----------|--------|
| Phase 0 or 1 completed | state.json |
| Input documents available | inputs/raw/*.pdf OR outputs/phase1-survey/narratives/*.md |

### Input Sources

| Mode | Input Location |
|------|----------------|
| survey | outputs/phase1-survey/narratives/*.md |
| independent | inputs/raw/*.pdf, inputs/raw/*.txt |

### Actions

| Step | Action | Output |
|------|--------|--------|
| 1 | Build document list | From input source |
| 2 | Invoke scenario_parser per document | /scenario_parser |
| 3 | Generate extracted.md | `outputs/phase2-parser/extracted/*-extracted.md` |
| 4 | Generate extracted.json | `outputs/phase2-parser/extracted/*-extracted.json` |
| 5 | Track progress per batch | Update state.json |
| 6 | Generate progress report | `outputs/progress/phase2-parser-progress.md` |
| 7 | Set phase completed | Update state.json |

### Output

- `outputs/phase2-parser/extracted/*-extracted.md`
- `outputs/phase2-parser/extracted/*-extracted.json`
- `outputs/progress/phase2-parser-progress.md`

### Parallel Strategy

| Document Count | Agents | Strategy |
|----------------|--------|----------|
| 1-10 | 1 | Serial |
| 11-30 | 2-3 | Small batch parallel |
| 31-50 | 4-5 | Medium batch parallel |
| 50+ | 6-8 | Large batch parallel |

### Completion Criteria

- All documents extracted to dual format
- JSON files valid and complete
- MD files readable with references

### Transition

```
Phase 2 → Phase 3
Conditions:
  - phase2_parser status = completed
  - phase3_analyzer status = pending
  - Parser outputs available
```

---

## Phase 3: Structured Analysis (scenario_analyzer)

### Purpose

Generate 12-section analysis reports from Parser outputs.

### SKILL Invoked

`/scenario_analyzer`

### Pre-Conditions

| Condition | Source |
|-----------|--------|
| Phase 2 completed | state.json phase2_parser status |
| Parser outputs available | outputs/phase2-parser/extracted/*.md + *.json |

### Actions

| Step | Action | Output |
|------|--------|--------|
| 1 | Load Parser outputs | extracted.md + extracted.json |
| 2 | Validate input completeness | Check required fields |
| 3 | Invoke scenario_analyzer per document | /scenario_analyzer |
| 4 | Generate 12-section reports | `outputs/phase3-analyzer/reports/*-analysis.md` |
| 5 | Track progress per batch | Update state.json |
| 6 | Generate progress report | `outputs/progress/phase3-analyzer-progress.md` |
| 7 | Set phase completed | Update state.json |

### Output

- `outputs/phase3-analyzer/reports/*-analysis.md`
- `outputs/progress/phase3-analyzer-progress.md`

### Parallel Strategy

| Document Count | Agents | Strategy |
|----------------|--------|----------|
| 1-5 | 1 | Serial |
| 6-15 | 2-3 | Small parallel |
| 16-30 | 4-5 | Medium parallel |
| 31-50 | 6-8 | Large parallel |
| 50+ | 8-10 | Max throughput |

### Quality Requirements

Follow scenario_analyzer's quality requirements:
- Output completeness: All 12 sections (0-12)
- Traceability: Use references from extracted files
- Statistical rules: Customer uniqueness, multi-customer citations
- Summary sections: Each table needs synthesis

### Completion Criteria

- All Parser outputs analyzed
- Each report has 12 sections
- Traceability preserved

### Transition

```
Phase 3 → Phase 4
Conditions:
  - phase3_analyzer status = completed
  - phase4_model status = pending
  - At least 3 analysis reports generated
  (Minimum 3 for meaningful cross-case synthesis)
```

---

## Phase 4: Cross-Case Modeling (scenario_modeler)

### Purpose

Synthesize multiple analyses into Industry, Stakeholder, Purchase Factor models.

### SKILL Invoked

`/scenario_modeler`

### Pre-Conditions

| Condition | Source |
|-----------|--------|
| Phase 3 completed | state.json |
| Analysis reports available | outputs/phase3-analyzer/reports/*.md |
| Minimum 3 reports | For meaningful synthesis |

### Actions

| Step | Action | Output |
|------|--------|--------|
| 1 | Collect analysis file paths | From phase3 outputs |
| 2 | Invoke scenario_modeler | Provide file list |
| 3 | Generate Industry Model | `outputs/phase4-model/industry-model.md` |
| 4 | Generate Stakeholder Model | `outputs/phase4-model/stakeholder-model.md` |
| 5 | Generate Purchase Factor Model | `outputs/phase4-model/purchase-factor-model.md` |
| 6 | Generate Cross Analysis | `outputs/phase4-model/cross-analysis.md` |
| 7 | Update state.json | Set phase4 completed |

### Output

- `outputs/phase4-model/industry-model.md`
- `outputs/phase4-model/stakeholder-model.md`
- `outputs/phase4-model/purchase-factor-model.md`
- `outputs/phase4-model/cross-analysis.md`

### Completion Criteria

- All 4 model files generated
- state.json phase4 = completed

### Transition

```
Phase 4 → Phase 5
Conditions:
  - phase4_model status = completed
  - phase5_final status = pending
```

---

## Phase 5: Finalization

### Purpose

Validate outputs, generate execution summary, archive state.

### Pre-Conditions

| Condition | Source |
|-----------|--------|
| All previous phases completed | state.json phase_status |
| Output files generated | outputs/* directories |

### Actions

| Step | Action | Output |
|------|--------|--------|
| 1 | Run completeness check | Scan all output directories |
| 2 | Generate execution summary | `outputs/phase5-final-report/execution-summary.md` |
| 3 | Generate completeness check report | `outputs/phase5-final-report/completeness-check.md` |
| 4 | Archive state.json | `archive/state-final.json` |
| 5 | Update state final status | All phases completed |

### Validation Checklist

```
Phase 0: state.json, config.json valid
Phase 1: Questionnaires/narratives count matches
Phase 2: All extracted files present (MD + JSON)
Phase 3: All reports have 12 sections, traceability present
Phase 4: All 4 model files present
Phase 5: Reports generated, state archived
```

### Completion Criteria

- All phases validated complete
- Missing items reported (if any)
- State archived
- Final reports generated

---

## Phase Transition Summary

| From | To | Trigger | Skip Condition |
|------|-----|---------|----------------|
| 0 | 1 | Init complete | input_mode=independent → go to 2 |
| 1 | 2 | Survey complete | - |
| 2 | 3 | Parser complete | - |
| 3 | 4 | Analyzer complete | <3 reports → skip phase4 |
| 4 | 5 | Models complete | - |
| 5 | End | Validation complete | - |

---

## Exception Handling

### Phase Failure

If a phase fails:
1. Set phase status to "failed"
2. Record error in errors array
3. Generate progress report with failure details
4. Prompt user for action (retry / skip / abort)

### Phase Incomplete

If phase incomplete at crash:
1. Phase status remains "in_progress"
2. processed_files tracks completed items
3. pending_files tracks remaining items
4. Resume from pending list

### Independent Recovery (Phase 2/3)

| Scenario | Resume Action |
|----------|---------------|
| Parser fails, Analyzer not started | Retry Parser only |
| Parser completes, Analyzer fails | Skip Parser, retry Analyzer |
| Both partially complete | Resume from last failed phase |

---

*Reference: Phase Definitions v1.1*
