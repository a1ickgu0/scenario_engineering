# Execution Summary Report

## Project Information

- **Project Name**: {{PROJECT_NAME}}
- **Industry**: {{INDUSTRY}}
- **Country**: {{COUNTRY}}
- **Language**: {{LANGUAGE}}
- **Timestamp**: {{PROJECT_TIMESTAMP}}

## Execution Timeline

| Event | Timestamp | Duration |
|-------|-----------|----------|
| Project Created | {{CREATED_AT}} | - |
| Phase 0 Completed | {{PHASE0_COMPLETED_AT}} | {{PHASE0_DURATION}} |
| Phase 1 Completed | {{PHASE1_COMPLETED_AT}} | {{PHASE1_DURATION}} |
| Phase 2 Completed | {{PHASE2_COMPLETED_AT}} | {{PHASE2_DURATION}} |
| Phase 3 Completed | {{PHASE3_COMPLETED_AT}} | {{PHASE3_DURATION}} |
| Phase 4 Completed | {{PHASE4_COMPLETED_AT}} | {{PHASE4_DURATION}} |
| Phase 5 Completed | {{PHASE5_COMPLETED_AT}} | {{PHASE5_DURATION}} |
| **Total Execution** | - | {{TOTAL_DURATION}} |

## Phase Completion Status

| Phase | Status | Tasks | Completed | Failed |
|-------|--------|-------|-----------|--------|
| Phase 0: Init | {{PHASE0_STATUS}} | - | {{PHASE0_COMPLETED}} | {{PHASE0_FAILED}} |
| Phase 1: Survey | {{PHASE1_STATUS}} | {{PHASE1_TOTAL}} | {{PHASE1_COMPLETED}} | {{PHASE1_FAILED}} |
| Phase 2: Parser | {{PHASE2_STATUS}} | {{PHASE2_TOTAL}} | {{PHASE2_COMPLETED}} | {{PHASE2_FAILED}} |
| Phase 3: Analyzer | {{PHASE3_STATUS}} | {{PHASE3_TOTAL}} | {{PHASE3_COMPLETED}} | {{PHASE3_FAILED}} |
| Phase 4: Model | {{PHASE4_STATUS}} | {{PHASE4_TOTAL}} | {{PHASE4_COMPLETED}} | {{PHASE4_FAILED}} |
| Phase 5: Final | {{PHASE5_STATUS}} | - | - | - |

## Document Processing Statistics

### Phase 1 (Survey)

- **Questionnaires Generated**: {{QUESTIONNAIRES_COUNT}}
- **Narratives Generated**: {{NARRATIVES_COUNT}}
- **Template Used**: {{TEMPLATE_USED}}

### Phase 2 (Parser)

- **Total Documents**: {{TOTAL_DOCUMENTS}}
- **Successfully Extracted**: {{SUCCESS_DOCUMENTS}}
- **Failed**: {{FAILED_DOCUMENTS}}
- **Skipped**: {{SKIPPED_DOCUMENTS}}
- **Success Rate**: {{SUCCESS_RATE}}%

### Phase 3 (Analyzer)

- **Total Analysis Inputs**: {{ANALYZER_TOTAL_DOCUMENTS}}
- **Successfully Analyzed**: {{ANALYZER_SUCCESS_DOCUMENTS}}
- **Failed**: {{ANALYZER_FAILED_DOCUMENTS}}
- **Skipped**: {{ANALYZER_SKIPPED_DOCUMENTS}}
- **Success Rate**: {{ANALYZER_SUCCESS_RATE}}%

### Phase 4 (Model)

- **Analysis Files Input**: {{ANALYSIS_FILES_COUNT}}
- **Models Generated**: {{MODELS_COUNT}}
  - Industry Model: {{INDUSTRY_MODEL_STATUS}}
  - Stakeholder Model: {{STAKEHOLDER_MODEL_STATUS}}
  - Purchase Factor Model: {{PURCHASE_MODEL_STATUS}}
  - Cross Analysis: {{CROSS_ANALYSIS_STATUS}}

## Error Summary

| Error Type | Count | Affected Files |
|------------|-------|----------------|
| PDF Corrupted | {{PDF_CORRUPTED_COUNT}} | {{PDF_CORRUPTED_FILES}} |
| Content Missing | {{CONTENT_MISSING_COUNT}} | {{CONTENT_MISSING_FILES}} |
| Parse Error | {{PARSE_ERROR_COUNT}} | {{PARSE_ERROR_FILES}} |
| Other | {{OTHER_ERROR_COUNT}} | {{OTHER_ERROR_FILES}} |

## Output File Inventory

### Phase 1 Outputs
```
outputs/phase1-survey/
├── questionnaires/
│   ├── {{QUESTIONNAIRE_FILES_LIST}}
└── narratives/
│   ├── {{NARRATIVE_FILES_LIST}}
```

### Phase 2 Outputs
```
outputs/phase2-parser/
├── extracted/
│   ├── {{EXTRACTED_FILES_LIST}}
└── problems/
│   ├── problem-documents-list.md
```

### Phase 3 Outputs
```
outputs/phase3-analyzer/
├── reports/
│   ├── {{ANALYSIS_FILES_LIST}}
└── problems/
│   ├── incomplete-reports-list.md
```

### Phase 4 Outputs
```
outputs/phase4-model/
├── {{MODEL_FILES_LIST}}
```

### Phase 5 Outputs
```
outputs/phase5-final-report/
├── execution-summary.md (this file)
├── completeness-check.md
└── recommendations.md
```

## Quality Metrics

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Document Coverage | {{DOCUMENT_COVERAGE}}% | 100% | {{COVERAGE_STATUS}} |
| Section Completeness | {{SECTION_COMPLETENESS}}% | 100% | {{COMPLETENESS_STATUS}} |
| Traceability Coverage | {{TRACEABILITY_COVERAGE}}% | 100% | {{TRACEABILITY_STATUS}} |
| Error Rate | {{ERROR_RATE}}% | <5% | {{ERROR_RATE_STATUS}} |

## Execution Configuration

- **Execution Mode**: {{EXECUTION_MODE}}
- **Parallel Agents**: {{PARALLEL_AGENTS}}
- **Checkpoint Frequency**: {{CHECKPOINT_FREQUENCY}}
- **Resume Count**: {{RESUME_COUNT}} (number of times resumed)

## Recommendations

{{RECOMMENDATIONS_SECTION}}

## Next Steps

- [ ] Review completeness-check.md for missing items
- [ ] Address failed documents ({{FAILED_DOCUMENTS}} items)
- [ ] Validate analysis report quality
- [ ] Proceed to downstream processing if applicable

---

*Report generated: {{REPORT_GENERATED_AT}}*
*State archived: archive/state-final.json*
