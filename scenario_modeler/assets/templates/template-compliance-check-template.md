# Template Compliance Check Report

## Document Information

| Field | Value |
|-------|-------|
| Project | [PROJECT_NAME] |
| Input Case Count | [N] |
| Output Directory | [OUTPUT_DIR] |
| Validation Time | [DATE_TIME] |
| Validator | scenario_modeler |

---

## 1. Overall Result

| Status | Output Count | Passed | Warning | Failed | Blocking Defects |
|--------|--------------|--------|---------|--------|------------------|
| [PASS/WARN/FAIL] | [COUNT] | [COUNT] | [COUNT] | [COUNT] | [COUNT] |

**Delivery Gate**: [PASS/BLOCKED]

---

## 2. Template Binding Matrix

| Output File | Bound Template | Template Found | Output Found | Status |
|-------------|----------------|----------------|--------------|--------|
| industry_model.md | industry-model-template.md | [YES/NO] | [YES/NO] | [PASS/FAIL] |
| stakeholder_model.md | stakeholder-model-template.md | [YES/NO] | [YES/NO] | [PASS/FAIL] |
| purchase_factor_model.md | purchase-factor-template.md | [YES/NO] | [YES/NO] | [PASS/FAIL] |
| use_case_fit_model.md | use-case-fit-model-template.md | [YES/NO] | [YES/NO] | [PASS/FAIL] |
| critical_capability_model.md | critical-capability-model-template.md | [YES/NO] | [YES/NO] | [PASS/FAIL] |
| buying_committee_model.md | buying-committee-model-template.md | [YES/NO] | [YES/NO] | [PASS/FAIL] |
| competitive_positioning_model.md | competitive-positioning-model-template.md | [YES/NO] | [YES/NO] | [PASS/FAIL] |
| cross_analysis_matrix.md | cross-analysis-template.md | [YES/NO] | [YES/NO] | [PASS/FAIL] |

---

## 3. Heading Compliance

| Output File | Required Headings | Found Headings | Missing Headings | Order Preserved | Status |
|-------------|-------------------|----------------|------------------|-----------------|--------|
| [FILE] | [COUNT] | [COUNT] | [LIST/NONE] | [YES/NO] | [PASS/FAIL] |

---

## 4. Table Schema Compliance

| Output File | Section | Required Columns | Missing / Renamed Columns | Status |
|-------------|---------|------------------|---------------------------|--------|
| [FILE] | [SECTION] | [COLUMNS] | [NONE/LIST] | [PASS/FAIL] |

---

## 5. Placeholder and Evidence-Gap Check

| Output File | Unresolved Placeholder | Location | Evidence-Gap Note Present | Status |
|-------------|------------------------|----------|---------------------------|--------|
| [FILE] | [PLACEHOLDER/TBD/TODO/N/A] | [SECTION] | [YES/NO] | [PASS/FAIL] |

---

## 6. Section Compression Check

| Output File | Template Section | Expected Detail | Observed Output | Status |
|-------------|------------------|-----------------|-----------------|--------|
| [FILE] | [SECTION] | [TABLE / SUBSECTIONS / TRACEABILITY] | [OBSERVATION] | [PASS/FAIL] |

---

## 7. Deviation Log

| ID | Output File | Section / Table | Deviation | Reason | Downstream Risk | Corrective Action | Approval Required |
|----|-------------|-----------------|-----------|--------|-----------------|-------------------|-------------------|
| [ID] | [FILE] | [SECTION] | [DEVIATION] | [REASON] | [RISK] | [ACTION] | [YES/NO] |

If there is no deviation, write: `No template deviations found.`

---

## 8. Blocking Defect List

| ID | Defect Type | Output File | Location | Required Fix |
|----|-------------|-------------|----------|--------------|
| [ID] | [MISSING_HEADING / ORDER_CHANGE / COLUMN_REMOVED / PLACEHOLDER / SECTION_COMPRESSED / UNLOGGED_DEVIATION] | [FILE] | [SECTION] | [FIX] |

If there is no blocking defect, write: `No blocking defects found.`

---

## 9. Final Validation Decision

| Gate | Result | Notes |
|------|--------|-------|
| Template Binding | [PASS/FAIL] | [NOTES] |
| Heading Presence and Order | [PASS/FAIL] | [NOTES] |
| Table Schema Preservation | [PASS/FAIL] | [NOTES] |
| Placeholder Resolution | [PASS/FAIL] | [NOTES] |
| Section Detail Preservation | [PASS/FAIL] | [NOTES] |
| Deviation Logging | [PASS/FAIL] | [NOTES] |

**Final Decision**: [APPROVED / BLOCKED]

**Required Follow-up**:
- [ACTION]
