# SKILL Invocation Mapping

## Overview

This document defines how scenario_engineering invokes each downstream SKILL, including context passing, output handling, and state synchronization.

---

## SKILL Dependency Graph

```
scenario_engineering (orchestrator)
│
├── Phase 0: Input Source Determination
│   ├── User Prompt: Independent directory path?
│   ├── input_mode: "survey" OR "independent"
│   └── If independent: Copy files to inputs/raw/
│
├── Phase 1 ──► scenario_survey (optional)
│   ├── Triggered when: input_mode = "survey"
│   ├── Reads: assets/templates/{industry}-template.md
│   ├── Invokes: /scenario_survey
│   └── Outputs: questionnaires, narratives
│   │
│   └── Skip when: input_mode = "independent"
│
├── Phase 2 ──► scenario_parser (NEW)
│   ├── Input Sources:
│   │   ├── Survey output: outputs/phase1-survey/narratives/*.md
│   │   ├── Independent files: inputs/raw/*.pdf, *.txt
│   ├── Invokes: /scenario_parser
│   └── Outputs: *-extracted.md + *-extracted.json
│   │
│   └── Recovery: Parser outputs are checkpoint files
│
├── Phase 3 ──► scenario_analyzer (MODIFIED)
│   ├── Input: outputs/phase2-parser/extracted/*-extracted.md + *.json
│   ├── Invokes: /scenario_analyzer
│   └── Outputs: *-analysis.md (12 sections)
│   │
│   └── Recovery: Can resume from Parser checkpoint
│
└── Phase 4 ──► scenario_modeler
│   ├── Input: outputs/phase3-analyzer/reports/*-analysis.md
│   ├── Invokes: /scenario_modeler
│   └── Outputs: Industry/Stakeholder/Purchase models
```

---

## Input Source Determination

### User Prompt Sequence

When starting a new project or `--from-phase 2`:

```
Step 1: Determine input source type
"请选择输入来源类型："
→ 1. 使用 survey 输出 (完整流程)
→ 2. 使用独立文档目录 (跳过 survey)

Step 2 (if independent):
"请提供独立文档目录路径："
→ 目录路径: /path/to/documents/
→ 包含文件: PDF文件为主，支持 .txt 和 .md
→ 文件将被复制到 inputs/raw/

Step 3: Confirm
"确认输入配置："
→ 输入模式: {{INPUT_MODE}}
→ 文件数量: {{FILE_COUNT}}
→ 行业: {{INDUSTRY}}
```

### Input Mode Configuration

| Mode | Phase 1 | Phase 2 Input | Phase 3 Input | Use Case |
|------|---------|-----------------|----------------|----------|
| survey | Execute | outputs/phase1-survey/narratives/*.md | outputs/phase2-parser/extracted/* | Complete workflow |
| independent | Skip | inputs/raw/*.pdf, *.txt | outputs/phase2-parser/extracted/* | Direct processing |

---

## Phase 1: scenario_survey Invocation

### Skip Conditions

Phase 1 is skipped when:
- `input_mode = "independent"`
- User specifies `--skip-phase1`
- User specifies `--from-phase 2`

### Invocation Context

```markdown
/scenario_survey

Context provided:
- Industry: {{INDUSTRY}}
- Country: {{COUNTRY}}
- Language: {{LANGUAGE}}
- Template reference: scenario_survey/assets/templates/{{INDUSTRY}}-template.md
- Output directory: outputs/phase1-survey/
```

---

## Phase 2: scenario_parser Invocation

### Pre-Invocation Setup

| Step | Action | Data Source |
|------|--------|-------------|
| 1 | Determine input source mode | state.json config.input_mode |
| 2 | Build document list | Based on input_mode |
| 3 | Determine parallel strategy | Based on document count |

### Invocation Context (Per Document)

```markdown
/scenario_parser

Context provided:
- Document path: {{DOCUMENT_PATH}}
- Output directory: outputs/phase2-parser/extracted/
- Expected output: {{CUSTOMER}}-extracted.md + {{CUSTOMER}}-extracted.json

Instructions:
1. Extract text from PDF if needed
2. Add reference markers (Page X, Line Y)
3. Extract customer info, stakeholders, products, metrics
4. Generate dual-format outputs
5. Preserve full traceability
```

### Output Handling

| Output Type | Location | State Update |
|-------------|----------|--------------|
| Extracted MD | `outputs/phase2-parser/extracted/*-extracted.md` | Add to processed_files |
| Extracted JSON | `outputs/phase2-parser/extracted/*-extracted.json` | Add to processed_files |
| Progress Report | `outputs/progress/phase2-parser-progress.md` | Update after each batch |

---

## Phase 3: scenario_analyzer Invocation

### Pre-Invocation Setup

| Step | Action | Data Source |
|------|--------|-------------|
| 1 | Load Parser outputs | outputs/phase2-parser/extracted/*.md + *.json |
| 2 | Validate input completeness | Check required JSON fields |
| 3 | Determine parallel strategy | Based on document count |

### Invocation Context (Per Document)

```markdown
/scenario_analyzer

Context provided:
- Parser MD: outputs/phase2-parser/extracted/{{CUSTOMER}}-extracted.md
- Parser JSON: outputs/phase2-parser/extracted/{{CUSTOMER}}-extracted.json
- Output directory: outputs/phase3-analyzer/reports/

Instructions:
1. Load extracted.md for context verification
2. Load extracted.json for structured data
3. Generate 12-section analysis report
4. Follow quality requirements:
   - Traceability: Use references from extracted files
   - Completeness: All 12 sections required
   - Synthesis: Each table needs explanation
```

### Output Handling

| Output Type | Location | State Update |
|-------------|----------|--------------|
| Analysis Report | `outputs/phase3-analyzer/reports/*-analysis.md` | Add to processed_files |
| Progress Report | `outputs/progress/phase3-analyzer-progress.md` | Update after each batch |

---

## Phase 4: scenario_modeler Invocation

### Pre-Invocation Setup

| Step | Action | Data Source |
|------|--------|-------------|
| 1 | Collect analysis file paths | outputs/phase3-analyzer/reports/*.md |
| 2 | Validate minimum count | ≥ 3 files for synthesis |

### Invocation Context

```markdown
/scenario_modeler

Context provided:
- Analysis files: [
    outputs/phase3-analyzer/reports/customer1-analysis.md,
    outputs/phase3-analyzer/reports/customer2-analysis.md,
    ...
  ]
- Output directory: outputs/phase4-model/
```

---

## State Synchronization

### After Phase 2 (Parser)

```json
{
  "progress": {
    "current_phase": 2,
    "phase_status": {
      "phase2_parser": "completed",
      "phase3_analyzer": "pending"
    }
  },
  "checkpoints": [
    {"timestamp": "...", "phase": 2, "action": "parser_complete"}
  ]
}
```

### After Phase 3 (Analyzer)

```json
{
  "progress": {
    "current_phase": 3,
    "phase_status": {
      "phase2_parser": "completed",
      "phase3_analyzer": "completed"
    }
  },
  "checkpoints": [
    {"timestamp": "...", "phase": 2, "action": "parser_complete"},
    {"timestamp": "...", "phase": 3, "action": "analyzer_complete"}
  ]
}
```

---

## Recovery Support

### Independent Recovery for Parser and Analyzer

| Scenario | Resume Action |
|----------|---------------|
| Parser fails, Analyzer not started | Retry Parser only |
| Parser completes, Analyzer fails | Skip Parser, retry Analyzer |
| Both partially complete | Resume from last failed phase |
| Crash mid-Parser batch | Continue Parser from pending list |
| Crash mid-Analyzer batch | Continue Analyzer from pending list |

---

## Error Handling Per SKILL

### scenario_parser Errors

| Error | Handling |
|-------|----------|
| PDF corrupted | Add to failed_files, skip |
| Content missing | Mark as insufficient, skip |
| Extraction incomplete | Log warning, proceed with partial data |

### scenario_analyzer Errors

| Error | Handling |
|-------|----------|
| JSON parse error | Add to failed_files, skip |
| Missing required fields | Mark as insufficient, log warning |
| Section incomplete | Log warning, include partial analysis |

---

## Invocation Sequence

```
Phase 0: Input source determination
│
Phase 1 (optional): scenario_survey
│   └── for each questionnaire/narrative needed
│       ├── Invoke /scenario_survey
│       └── Update state
│
Phase 2: scenario_parser
│   ├── Build document list
│   ├── for each batch:
│   │   ├── Invoke /scenario_parser
│   │   ├── Generate extracted.md + extracted.json
│   │   └── Update state
│   └── Set phase2 completed
│
Phase 3: scenario_analyzer
│   ├── Load Parser outputs
│   ├── for each batch:
│   │   ├── Invoke /scenario_analyzer
│   │   ├── Generate analysis.md
│   │   └── Update state
│   └── Set phase3 completed
│
Phase 4: scenario_modeler
│   ├── Collect analysis files
│   ├── Invoke /scenario_modeler
│   └── Update state
│
Phase 5: Finalization
```

---

*Reference: SKILL Invocation Mapping v1.1*
