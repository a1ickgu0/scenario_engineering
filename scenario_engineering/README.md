# Scenario Engineering SKILL

Top-level orchestration SKILL for the complete customer requirements engineering workflow.

## Overview

This SKILL coordinates three downstream SKILLs in a structured pipeline:

```
scenario_survey → scenario_analyzer → scenario_modeler
```

**Key Features**:
- **Pipeline Orchestration**: Unified entry point for end-to-end workflow
- **Directory Management**: Structured output organization
- **Progress Tracking**: JSON state + MD progress reports
- **Task Recovery**: Resume from interruption
- **SKILL Coordination**: Sequential invocation with state preservation

## Execution Modes

| Mode | Description | Usage |
|------|-------------|-------|
| `--new` | Start fresh project | New analysis pipeline |
| `--resume` | Resume interrupted task | Recovery from crash |
| `--from-phase N` | Start from specific phase | Skip earlier phases |
| `--validate` | Validate existing outputs | Quality check only |
| `--dry-run` | Plan without execution | Structure preview |

## Phase Definitions

| Phase | Name | SKILL | Output |
|-------|------|-------|--------|
| 0 | Initialization | - | Directory structure, state.json |
| 1 | Pre-Sales Survey | scenario_survey | Questionnaires, narratives |
| 2 | Structured Analysis | scenario_analyzer | Analysis reports (12 sections) |
| 3 | Cross-Case Modeling | scenario_modeler | Industry/Stakeholder/Purchase models |
| 4 | Finalization | - | Execution summary, completeness check |

## Directory Structure

```
project-{name}-{timestamp}/
├── state.json                     # Progress state (JSON)
├── config.json                    # Configuration
├── inputs/
│   ├── raw/                       # Original PDFs/texts
│   └── extracted/                 # PDF-to-text
├── outputs/
│   ├── progress/                  # MD progress reports
│   ├── phase1-survey/
│   ├── phase2-analysis/
│   ├── phase3-model/
│   └── final-report/
└── archive/
    └── state-final.json
```

## Quick Start

```bash
# New project
/scenario_engineering --new
→ Industry: Hospitality
→ Country: Malaysia
→ Input: ./customer-stories/*.pdf

# Resume interrupted task
/scenario_engineering --resume

# Validate outputs
/scenario_engineering --validate

# Start from specific phase
/scenario_engineering --from-phase 2
```

## Recovery Mechanism

- **State File**: `state.json` tracks progress
- **Checkpoints**: Updated after each batch
- **Resume**: Skip completed work, continue pending
- **No Rollback**: Forward recovery only

## Assets

| Type | Files |
|------|-------|
| Templates | state-template.json, config-template.json, progress-report-template.md |
| References | recovery-guidelines.md, phase-definitions.md, skill-invocation-mapping.md |

## Documentation

- [README_zh.md](README_zh.md) - Chinese documentation
- [SKILL.md](SKILL.md) - Full SKILL definition