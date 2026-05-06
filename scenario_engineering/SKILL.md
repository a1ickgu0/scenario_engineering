---
name: scenario_engineering
description: "Top-level orchestration SKILL for the complete customer requirements engineering workflow. Coordinates scenario_survey, scenario_analyzer, and scenario_modeler with structured output management, progress tracking, and task recovery support. Manages directory structure, intermediate documents, and execution state persistence."
tags:
  - orchestration
  - workflow-coordination
  - pipeline-management
  - task-recovery
  - progress-tracking
  - directory-management
  - end-to-end-analysis
  - state-persistence
version: "0.2.0"
---

# Scenario Engineering SKILL

## Overview

This SKILL is the **top-level orchestrator** for the complete customer requirements engineering workflow. It coordinates three downstream SKILLs in a structured pipeline:

```
scenario_survey → scenario_analyzer → scenario_modeler
```

**Core Capabilities**:
1. **Pipeline Orchestration**: Unified entry point for end-to-end workflow
2. **Directory Management**: Structured output organization with intermediate documents
3. **Progress Tracking**: Dual-format tracking (JSON state + MD progress reports)
4. **Task Recovery**: Checkpoint-based resume from interruption
5. **SKILL Coordination**: Sequential invocation with state preservation

**Key Positioning**:
- **Role**: Workflow orchestrator, not content generator
- **Scope**: Manages execution flow, delegates analysis to specialized SKILLs
- **Output**: Directory structure, state files, progress reports, final summary

## When to Use

- **End-to-end analysis**: Need complete workflow from survey to modeling
- **Multi-document processing**: Have multiple customer stories to analyze
- **Batch operations**: Want systematic processing with progress tracking
- **Recovery scenarios**: Previous execution interrupted, need to continue
- **Structured outputs**: Require organized directory with intermediate files
- **Quality validation**: Need comprehensive completeness check

## Entry Point Selection

Select the appropriate SKILL entry point based on available input materials:

| Entry Point | Starting SKILL | Input Required | Use Case |
|-------------|----------------|----------------|----------|
| **Full Pipeline** | scenario_engineering | None (start fresh) | Complete end-to-end workflow |
| **Survey Only** | scenario_survey | Industry + Country | Generate questionnaires only |
| **Parser Only** | scenario_parser | PDF/Text files | Extract structured data from documents |
| **Analyzer Only** | scenario_analyzer | extracted.md + extracted.json | Generate analysis reports from parsed data |
| **Modeler Only** | scenario_modeler | Multiple *-analysis.md files | Synthesize cross-case models |

### Decision Tree

```
What do you want to do?
    ↓
├── Complete new project → scenario_engineering --new
│
├── Continue existing work → scenario_engineering --resume
│
├── Generate questionnaire only → /scenario_survey
│   (Have: Industry, Country, Language)
│
├── Extract from existing PDFs → /scenario_parser
│   (Have: PDF/Text documents)
│
├── Analyze extracted data → /scenario_analyzer
│   (Have: *-extracted.md + *-extracted.json)
│
└── Model from analyses → /scenario_modeler
    (Have: Multiple *-analysis.md files)
```

### Direct SKILL Invocation Examples

**Example 1: Generate Questionnaire Only**
```
/scenario_survey
→ Industry: Hospitality
→ Country: Malaysia
→ Language: English
→ Output: questionnaire.md
```

**Example 2: Extract from Existing PDFs**
```
/scenario_parser
→ Input: /path/to/customer-stories/*.pdf
→ Output: *-extracted.md + *-extracted.json
→ Feed to: scenario_analyzer
```

**Example 3: Analyze Already Extracted Data**
```
/scenario_analyzer
→ Input: outputs/phase2-parser/extracted/*-extracted.*
→ Output: *-analysis.md
→ Feed to: scenario_modeler
```

**Example 4: Model from Existing Analyses**
```
/scenario_modeler
→ Input: outputs/phase2b-analyzer/reports/*-analysis.md
→ Output: industry-model.md, stakeholder-model.md, purchase-factor-model.md
```

### Entry Point vs. Phase Selection

| Concept | Scope | Usage |
|---------|-------|-------|
| **Entry Point** | SKILL-level | Choose which SKILL to invoke directly |
| **Phase Selection** | Pipeline-level | Choose which phase to resume within full pipeline |

**Example**:
- `--from-skill parser` → Start directly with parser (Entry Point)
- `--from-phase 2` → Resume pipeline at Phase 2 (Phase Selection)

Both are supported in scenario_engineering with different default behaviors.

## Execution Modes

| Mode | Description | Usage |
|------|-------------|-------|
| `--new` | Start fresh project | New analysis pipeline |
| `--resume` | Resume interrupted task | Recovery from crash/interrupt |
| `--from-phase N` | Start from specific phase | Skip completed earlier phases |
| `--from-skill SKILL` | Start from specific SKILL | Direct SKILL entry point |
| `--validate` | Validate existing outputs | Quality check, report missing items |
| `--dry-run` | Plan without execution | Preview directory structure |

**Mode Selection Logic**:
```
If state.json exists:
  → Default to --resume (continue from last checkpoint)
Else:
  → Default to --new (create fresh project)

User can override with:
  --from-phase 2  → Skip phase 0-1, start analysis
  --from-skill parser  → Start directly from scenario_parser
  --from-skill analyzer → Start directly from scenario_analyzer
  --from-skill modeler → Start directly from scenario_modeler
  --validate      → Check outputs, no new generation
  --dry-run       → Show plan, no execution
```

### --from-skill Option Details

**Supported Values**:
- `--from-skill survey` → Start with scenario_survey only
- `--from-skill parser` → Start with scenario_parser (requires PDFs)
- `--from-skill analyzer` → Start with scenario_analyzer (requires extracted files)
- `--from-skill modeler` → Start with scenario_modeler (requires analysis files)

**Behavior**:
```
When --from-skill is specified:
  1. Skip all phases before the specified SKILL
  2. Initialize project directory structure
  3. Validate input requirements for target SKILL
  4. Invoke the specified SKILL directly
  5. Update state.json with appropriate phase markers
```

**Example: Starting from Parser**
```
/scenario_engineering --from-skill parser
→ Input: /path/to/documents/*.pdf
→ Skips: Phase 0 (init), Phase 1 (survey)
→ Starts: Phase 2a (parser)
→ Requires: Valid PDF/Text input directory
```

## Phase Definitions

### Phase 0: Initialization

**Purpose**: Setup project structure, determine input sources, validate inputs

**Input Source Determination**:

Phase 2 (Analysis) has two possible input sources:
1. **Survey Output**: Narratives from Phase 1 (`outputs/phase1-survey/narratives/`)
2. **Independent Files**: User-provided documents directory (PDFs, texts)

**Input Source Discovery**:
```
If user provides independent document directory:
  → Set input_mode = "independent"
  → Copy files to inputs/raw/
  → Skip Phase 1 (survey)

If no independent directory provided:
  → Set input_mode = "survey"
  → Require Phase 1 execution
  → Phase 2 uses survey outputs
```

**User Prompt for Input Directory**:
When starting a new project or `--from-phase 2`:
```
"请提供独立文档目录路径（如果跳过survey阶段直接进入analysis）：
→ 目录路径: /path/to/documents/
→ 包含文件: PDF文件为主，支持.txt和.md
→ 如不提供，将使用survey阶段的输出作为输入"
```

**Actions**:
1. Prompt user for input source (survey vs independent files)
2. If independent: Prompt for document directory path
3. Validate input sources (PDFs, texts, narratives)
4. Create output directory structure
5. Initialize state.json with input_mode
6. Create config.json from user parameters
7. Copy independent files to inputs/raw/ (if applicable)
8. Generate phase0-init-report.md

**Output**:
- `state.json` (initialized with input_mode)
- `config.json` (includes independent_directory if provided)
- `inputs/raw/*.pdf` (copied from independent source)
- `outputs/progress/phase0-init-report.md`

**Completion Criteria**: All directories created, input_mode determined, inputs validated

---

### Phase 1: Pre-Sales Survey (scenario_survey)

**Purpose**: Generate questionnaires and collect narratives

**SKILL Invocation**: `/scenario_survey`

**Skip Conditions**:
- User provided independent document directory (input_mode = "independent")
- User specifies `--skip-phase1` or `--from-phase 2`
- Narratives already exist in `outputs/phase1-survey/narratives/`

**When Skipped**: Proceed directly to Phase 2, use independent files as input

**Actions (when not skipped)**:
1. Read industry template from `scenario_survey/assets/templates/`
2. Generate industry-specific questionnaire
3. (Optional) Synthesize narrative from interview notes
4. Update state.json after each task
5. Generate phase1-survey-progress.md

**Output**:
- `outputs/phase1-survey/questionnaires/*.md`
- `outputs/phase1-survey/narratives/*.md`
- `outputs/progress/phase1-survey-progress.md`

**Completion Criteria**: All questionnaires/narratives generated

---

### Phase 2: Document Extraction & Analysis (Parser + Analyzer)

Phase 2 is now split into two sub-phases for better separation of concerns:

---

### Phase 2a: Document Extraction (scenario_parser)

**Purpose**: Extract structured data from documents into intermediate format

**SKILL Invocation**: `/scenario_parser`

**Input Sources (Two Modes)**:

| Mode | Input Location | Trigger Condition |
|------|----------------|-------------------|
| Survey Output | `outputs/phase1-survey/narratives/*.md` | input_mode = "survey", Phase 1 executed |
| Independent Files | `inputs/raw/*.pdf`, `inputs/raw/*.txt` | input_mode = "independent" |

**Actions**:
1. Determine input source mode from state.json
2. Build document list from appropriate source
3. Invoke scenario_parser for each document
4. Generate dual-format outputs (MD + JSON)
5. Track processed/pending/failed documents
6. Update state.json after each batch
7. Generate phase2a-parser-progress.md
8. Generate problem documents list

**Output**:
- `outputs/phase2-parser/extracted/*-extracted.md`
- `outputs/phase2-parser/extracted/*-extracted.json`
- `outputs/phase2-parser/problems/problem-documents-list.md`
- `outputs/progress/phase2a-parser-progress.md`

**Completion Criteria**: All valid documents extracted to MD + JSON

**Parallel Strategy**:

| Document Count | Recommended Agents |
|----------------|-------------------|
| 1-10 | 1 (serial) |
| 11-30 | 2-3 |
| 31-50 | 4-5 |
| 50+ | 6-8 |

**Recovery Support**: Parser outputs are checkpoint files - if Parser completes but Analyzer fails, skip Parser on resume

---

### Phase 2b: Structured Analysis (scenario_analyzer)

**Purpose**: Generate 12-section analysis reports from Parser outputs

**SKILL Invocation**: `/scenario_analyzer`

**Input Sources**:

| Input | Location | Purpose |
|-------|----------|---------|
| Parser MD | `outputs/phase2-parser/extracted/*-extracted.md` | Context verification |
| Parser JSON | `outputs/phase2-parser/extracted/*-extracted.json` | Structured data |

**Pre-Conditions**:
- Phase 2a completed
- Parser extracted files available

**Actions**:
1. Load Parser extracted.md + extracted.json
2. Validate input completeness
3. Invoke scenario_analyzer for each document
4. Generate 12-section analysis reports
5. Track processed/pending/failed documents
6. Update state.json after each batch
7. Generate phase2b-analyzer-progress.md

**Output**:
- `outputs/phase2b-analyzer/reports/*-analysis.md`
- `outputs/progress/phase2b-analyzer-progress.md`

**Completion Criteria**: All Parser outputs analyzed

**Parallel Strategy**:

| Document Count | Recommended Agents |
|----------------|-------------------|
| 1-5 | 1 (serial) |
| 6-15 | 2-3 |
| 16-30 | 4-5 |
| 31-50 | 6-8 |
| 50+ | 8-10 |

**Recovery Support**: If Analyzer fails, can resume from Parser checkpoint without re-extracting

---

### Phase 3: Cross-Case Modeling (scenario_modeler)

**Purpose**: Synthesize multiple analyses into models

**SKILL Invocation**: `/scenario_modeler`

**Actions**:
1. Collect all phase2b-analyzer reports
2. Invoke scenario_modeler for synthesis
3. Generate Industry/Stakeholder/Purchase models
4. Generate cross-analysis matrices
5. Update state.json
6. Generate phase3-model-progress.md

**Output**:
- `outputs/phase3-model/industry-model.md`
- `outputs/phase3-model/stakeholder-model.md`
- `outputs/phase3-model/purchase-factor-model.md`
- `outputs/phase3-model/cross-analysis.md`
- `outputs/progress/phase3-model-progress.md`

**Completion Criteria**: All model files generated

---

### Phase 4: Finalization

**Purpose**: Validate and summarize execution

**Actions**:
1. Generate execution-summary.md
2. Run completeness check on all outputs
3. Generate completeness-check.md (report missing items)
4. Archive state.json → archive/state-final.json
5. Update state.json phase_status to all completed

**Output**:
- `outputs/final-report/execution-summary.md`
- `outputs/final-report/completeness-check.md`
- `archive/state-final.json`

**Completion Criteria**: All phases verified complete

## Directory Structure

```
project-{name}-{timestamp}/
├── state.json                     # JSON state (machine readable)
├── config.json                    # Execution configuration
├── inputs/
│   ├── raw/                       # Original PDFs/texts
│   └── extracted/                 # PDF-to-text conversions
│
├── outputs/
│   ├── progress/                  # MD progress reports (human readable)
│   │   ├── phase0-init-report.md
│   │   ├── phase1-survey-progress.md
│   │   ├── phase2a-parser-progress.md    # NEW
│   │   ├── phase2b-analyzer-progress.md  # NEW
│   │   ├── phase3-model-progress.md
│   │   └── final-summary.md
│   │
│   ├── phase1-survey/
│   │   ├── questionnaires/
│   │   └── narratives/
│   │
│   ├── phase2-parser/             # NEW: Parser outputs
│   │   ├── extracted/             # Dual-format (MD + JSON)
│   │   │   ├── customer1-extracted.md
│   │   │   ├── customer1-extracted.json
│   │   │   └── ...
│   │   └── problems/
│   │
│   ├── phase2b-analyzer/          # NEW: Analyzer outputs
│   │   ├── reports/               # *-analysis.md files
│   │   └── problems/
│   │
│   ├── phase3-model/
│   │   ├── industry-model.md
│   │   ├── stakeholder-model.md
│   │   ├── purchase-factor-model.md
│   │   └ cross-analysis.md
│   │
│   └── final-report/
│       ├── execution-summary.md
│       └── completeness-check.md
│
└── archive/
    └── state-final.json
```

## Progress Tracking

### Dual-Format Approach

**JSON State File** (`state.json`):
- Machine-readable, for recovery logic
- Single source of truth
- Updated after each batch

**MD Progress Reports** (`outputs/progress/*.md`):
- Human-readable, for monitoring
- Updated in real-time during execution
- Contains detailed task lists

### State File Structure (Updated for Phase 2a/2b)

```json
{
  "meta": {
    "project_name": "hotel-chain-analysis",
    "created_at": "2026-04-21T10:00:00Z",
    "updated_at": "2026-04-21T14:30:00Z",
    "version": "1.0.0"
  },
  "config": {
    "industry": "Hospitality",
    "country": "Malaysia",
    "language": "English",
    "input_sources": ["inputs/raw/*.pdf"],
    "skip_phase1": false,
    "parallel_agents": 4
  },
  "progress": {
    "current_phase": "2b",
    "phase_status": {
      "phase0_init": "completed",
      "phase1_survey": "completed",
      "phase2a_parser": "completed",
      "phase2b_analyzer": "in_progress",
      "phase3_model": "pending",
      "phase4_final": "pending"
    },
    "phase_details": {
      "phase2a_parser": {
        "total_documents": 15,
        "processed": 15,
        "pending": 0,
        "failed": 0,
        "processed_files": ["doc-001-extracted.md", "doc-001-extracted.json", ...],
        "pending_files": [],
        "failed_files": []
      },
      "phase2b_analyzer": {
        "total_documents": 15,
        "processed": 8,
        "pending": 5,
        "failed": 2,
        "processed_files": ["doc-001-analysis.md", "doc-002-analysis.md"],
        "pending_files": ["doc-009-extracted.json", "doc-010-extracted.json"],
        "failed_files": [{"file": "doc-003-extracted.json", "reason": "JSON parse error"}]
      }
    }
  },
  "checkpoints": [
    {"timestamp": "...", "phase": "2a", "action": "parser_complete"}
  ],
  "errors": [],
  "resume_info": {
    "resume_from_phase": "2b",
    "resume_action": "continue_analyzer",
    "resume_files": ["doc-009-extracted.json", ...]
  }
}
```

### Progress Report Template

Each phase generates an MD report with:
- Execution status (phase, status, timestamps)
- Progress summary (total/completed/pending/failed counts)
- Completed tasks table
- Pending tasks table
- Failed tasks table
- Next actions checklist

## Recovery Mechanism

### Resume Workflow

```
1. Read state.json from project directory
2. Parse current_phase and phase_status
3. Identify resume_info.resume_action
4. Build task list from pending_files
5. Skip completed phases/documents
6. Execute from resume point
7. Update state.json after each batch
8. Update MD progress reports
```

### Resume Scenarios

| Scenario | Resume Action |
|----------|---------------|
| Phase 1 incomplete | Continue questionnaire/narrative generation |
| Phase 2 partial | Skip processed files, continue pending list |
| Phase 2 failed docs | Retry failed docs or skip with warning |
| Phase 3 not started | Collect phase2 reports, start synthesis |
| Crash mid-batch | Load checkpoint, continue from last document |

### Recovery Rules

**RR-01: Skip Completed Work**
- Check `processed_files` list before each task
- Do not re-process files already in completed list

**RR-02: Handle Failed Documents**
- Failed docs listed in `failed_files` with reason
- User can choose to retry or skip

**RR-03: Checkpoint Frequency**
- Update state.json after each batch (configurable)
- Default: every 5 documents in phase2

**RR-04: No Rollback**
- Forward recovery only, no reverting to previous phase
- If earlier phase output is invalid, user must start new project

## SKILL Invocation Mapping

### Phase 1 → scenario_survey

**Pre-conditions**:
- Industry specified
- Country specified (for language)
- Read industry template from `scenario_survey/assets/templates/`

**Invocation Context**:
```
/scenario_survey
→ Provide: industry, country, language
→ Output to: outputs/phase1-survey/
→ Read template: scenario_survey/assets/templates/{industry}-template.md
```

### Phase 2 → scenario_analyzer

**Pre-conditions**:
- Narratives or PDFs available in inputs/ or outputs/phase1-survey/narratives/
- Extract PDF text if needed

**Invocation Context**:
```
/scenario_analyzer
→ Provide: document path, output directory
→ Output to: outputs/phase2-analysis/reports/
→ Follow: 12-section structure, traceability requirements
→ Use parallel agents based on document count
```

### Phase 3 → scenario_modeler

**Pre-conditions**:
- Multiple analysis reports available in outputs/phase2-analysis/reports/
- At least 3 analyses for meaningful synthesis

**Invocation Context**:
```
/scenario_modeler
→ Provide: list of analysis files
→ Output to: outputs/phase3-model/
→ Generate: Industry, Stakeholder, Purchase Factor models
```

## Output Requirements

### Completeness Check (--validate mode)

Validates all phases:
```
Phase 0:
- [ ] state.json exists
- [ ] config.json valid
- [ ] inputs validated

Phase 1:
- [ ] Questionnaires generated (count matches expected)
- [ ] Narratives generated (if applicable)

Phase 2:
- [ ] Analysis reports generated (all valid documents)
- [ ] Each report has 12 sections (0-12)
- [ ] Traceability present in each report

Phase 3:
- [ ] Industry model generated
- [ ] Stakeholder model generated
- [ ] Purchase factor model generated
- [ ] Cross analysis generated

Phase 4:
- [ ] Execution summary generated
- [ ] Completeness check generated
```

**Output**: `outputs/final-report/completeness-check.md` listing all missing items

### Final Summary Content

`outputs/final-report/execution-summary.md` includes:
- Project metadata (name, industry, country)
- Execution timeline (start, end, duration)
- Phase completion status
- Document processing statistics
- Error summary
- Output file inventory

## Workflow Example

### New Project Execution

```
# Initialize new project
/scenario_engineering --new
→ Project: hotel-chain-analysis
→ Industry: Hospitality
→ Country: Malaysia
→ Input: 15 customer story PDFs

# Phase 0: Setup
→ Created: project-hotel-chain-analysis-20260421/
→ Created: state.json, config.json
→ Validated: 15 input PDFs

# Phase 1: Survey (optional, skip if narratives exist)
/scenario_survey
→ Generated: questionnaires, narratives
→ Updated: state.json

# Phase 2: Analysis
/scenario_analyzer (parallel, 4 agents)
→ Processed: 15 documents
→ Generated: 15 analysis reports
→ Updated: state.json after each batch

# Phase 3: Modeling
/scenario_modeler
→ Input: 15 analysis files
→ Generated: Industry, Stakeholder, Purchase models

# Phase 4: Finalization
→ Generated: execution-summary.md
→ Generated: completeness-check.md
→ Archived: state-final.json
```

### Resume from Interruption

```
# Previous run stopped at phase 2 (8/15 docs processed)
/scenario_engineering --resume

# Recovery logic:
→ Read state.json
→ Phase status: phase2_analysis in_progress
→ Pending: 7 documents (doc-009 to doc-015)
→ Resume: continue_analysis

# Continue execution:
/scenario_analyzer (remaining 7 docs)
→ Processed: doc-009 to doc-015
→ Generated: 7 analysis reports
→ Updated: state.json

# Proceed to phase 3:
/scenario_modeler
→ Generated: models

# Phase 4: Finalization
→ Completed
```

### Validation Mode

```
/scenario_engineering --validate
→ Read: state.json
→ Check: all output files
→ Report: outputs/final-report/completeness-check.md

Missing items reported:
- [ ] doc-003-analysis.md (failed: PDF corrupted)
- [ ] Section 7 in doc-005-analysis.md (missing lifecycle)
- [ ] industry-model.md (phase 3 not executed)
```

## Assets Structure

```
scenario_engineering/
├── SKILL.md                       # This file
├── README.md                      # English documentation
├── README_zh.md                   # Chinese documentation
└── assets/
    ├── templates/
    │   ├── state-template.json    # JSON state template
    │   ├── config-template.json   # Configuration template
    │   ├── progress-report-template.md  # MD progress template
    │   ├── directory-structure.md # Directory reference
    │   └── final-report-template.md # Final report template
    └ references/
    │   ├── recovery-guidelines.md # Recovery handling logic
    │   ├── phase-definitions.md   # Phase transition rules
    │   └── skill-invocation-mapping.md # How to invoke each SKILL
```

## Version History

- **0.2.0** (2026-05-06): Add entry point selection
  - Added Entry Point Selection section with decision tree
  - Added --from-skill option for direct SKILL invocation
  - Added Direct SKILL Invocation Examples
  - Distinguished entry point vs. phase selection
  - Updated execution modes table

- **0.1.0** (2026-04-21): Initial scenario_engineering SKILL design
  - Top-level orchestration for scenario_survey → scenario_analyzer → scenario_modeler
  - 5-phase execution model (0-4)
  - Dual-format progress tracking (JSON + MD)
  - Recovery mechanism with checkpoint-based resume
  - Directory structure management
  - Validation mode for completeness check