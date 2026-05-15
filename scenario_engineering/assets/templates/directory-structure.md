# Scenario Engineering Directory Structure

## Standard Directory Layout

```
project-{name}-{timestamp}/
│
├── state.json                     # Progress state (JSON, machine readable)
│   ├── meta                        # Project metadata
│   ├── config                      # Execution configuration
│   ├── progress                    # Current phase and details
│   ├── checkpoints                 # Execution history
│   ├── errors                      # Error log
│   └ resume_info                   # Recovery instructions
│
├── config.json                    # User configuration
│   ├── project                     # Project info
│   ├── execution                   # Mode settings
│   ├── input                       # Source files
│   ├── output                      # Output directories
│   ├── processing                  # Processing parameters
│   └── skill_references            # SKILL paths
│
├── inputs/
│   ├── raw/                        # Original input documents
│   │   ├── *.pdf                   # Customer story PDFs
│   │   ├── *.txt                   # Text narratives
│   │   └── *.md                    # Narrative documents
│   │
│   └── extracted/                  # PDF extracted text
│       └── *.txt                   # pdftotext output
│
├── outputs/
│   │
│   ├── progress/                   # MD progress reports (human readable)
│   │   ├── phase0-init-report.md   # Initialization summary
│   │   ├── phase1-survey-progress.md
│   │   ├── phase2-parser-progress.md
│   │   ├── phase3-analyzer-progress.md
│   │   ├── phase4-model-progress.md
│   │   └── final-summary.md        # Final execution summary
│   │
│   ├── phase1-survey/              # scenario_survey outputs
│   │   ├── questionnaires/         # Generated questionnaires
│   │   │   ├── {industry}-{country}-questionnaire-{lang}.md
│   │   │   └── ...
│   │   │
│   │   └── narratives/             # Synthesized narratives
│   │       ├── {customer}-narrative.md
│   │       └── ...
│   │
│   ├── phase2-parser/              # scenario_parser outputs
│   │   ├── extracted/              # Structured extraction checkpoint files
│   │   │   ├── {customer}-extracted.md
│   │   │   ├── {customer}-extracted.json
│   │   │   └── ...
│   │   └── problems/               # Parser problem tracking
│   │       └── problem-documents-list.md
│   │
│   ├── phase3-analyzer/           # scenario_analyzer outputs
│   │   ├── reports/                # Structured analysis reports
│   │   │   ├── {customer}-analysis.md (12 sections: 0-12)
│   │   │   └── ...
│   │   │
│   │   └── problems/               # Problem document tracking
│   │       ├── problem-documents-list.md
│   │       └── incomplete-reports-list.md
│   │
│   ├── phase4-model/               # scenario_modeler outputs
│   │   ├── industry-model.md       # Industry patterns
│   │   ├── stakeholder-model.md    # Category + Role hierarchy
│   │   ├── purchase-factor-model.md # Driver → Implementation → Metrics
│   │   ├── cross-analysis.md       # Cross-case matrices
│   │   └── critical-analysis.md    # Credibility ratings
│   │
│   └── phase5-final-report/        # Final validation
│       ├── execution-summary.md    # Complete execution log
│       ├── completeness-check.md   # Missing items report
│       └── recommendations.md      # Next steps suggestions
│
└── archive/                        # Completed state archives
    ├── state-final.json            # Final state snapshot
    └── state-backup-{timestamp}.json
```

## File Naming Conventions

### Input Files

| Type | Pattern | Example |
|------|---------|---------|
| PDF | `{customer-name}-{year}.pdf` | `southern-sun-2026.pdf` |
| Text | `{customer-name}-story.txt` | `hotel-chain-story.txt` |
| Narrative | `{customer-name}-narrative.md` | `hotel-chain-narrative.md` |

### Output Files

| Phase | Pattern | Example |
|-------|---------|---------|
| Questionnaire | `{industry}-{country}-questionnaire-{lang}.md` | `hospitality-malaysia-questionnaire-en.md` |
| Narrative | `{customer}-narrative.md` | `southern-sun-narrative.md` |
| Analysis | `{customer}-analysis.md` | `southern-sun-analysis.md` |
| Model | `{model-type}-model.md` | `industry-model.md` |

## Directory Creation Order

Phase 0 creates directories in this order:

1. `project-{name}-{timestamp}/` (root)
2. `inputs/raw/`
3. `inputs/extracted/`
4. `outputs/progress/`
5. `outputs/phase1-survey/questionnaires/`
6. `outputs/phase1-survey/narratives/`
7. `outputs/phase2-parser/extracted/`
8. `outputs/phase2-parser/problems/`
9. `outputs/phase3-analyzer/reports/`
10. `outputs/phase3-analyzer/problems/`
11. `outputs/phase4-model/`
12. `outputs/phase5-final-report/`
13. `archive/`

## State File Location

- **Active State**: `project-root/state.json`
- **Archived State**: `archive/state-final.json`
- **Backup States**: `archive/state-backup-{timestamp}.json`

## Recovery Discovery

When resuming, search for `state.json` in:
1. Current working directory
2. Most recent `project-*` directory
3. User-specified project directory

---

*Reference: Directory Structure Template v1.0*
