# Input Validation Framework

## Purpose

This framework defines pre-processing and validation rules for scenario_analyzer outputs before model synthesis. It ensures data quality, completeness, and consistency to prevent downstream processing issues.

---

## Validation Phases

### Phase 1: File-Level Validation

**Check**: File existence and format

| Check | Requirement | Status |
|-------|-------------|--------|
| File Format | Must be Markdown (.md) | Required |
| File Name | Must follow `{customer}-analysis.md` pattern | Required |
| Encoding | UTF-8 | Required |
| Readability | File must be readable and parseable | Required |

### Phase 2: Structural Validation

**Check**: Document structure completeness

| Section | Required Fields | Validation Rule |
|---------|----------------|-----------------|
| 0. Customer Basic Information | Company name, Industry, Country, Year | All required |
| 1. Purchase Elements | Ranked list with business value and metrics | At least 1 element |
| 2. Stakeholder List | Roles, expectations, influence, value/risk | At least 1 stakeholder |
| 3. Conflicts and Priority | Conflict types and priorities | Optional |
| 4. State Model | Stakeholder/system states | Optional |
| 5. Environment Model | Industry/regional/organizational context | Optional |
| 6. Entity Model | Organizations, systems, external entities | Optional |
| 7. Lifecycle Phases | Scenario phases | Optional |
| 8. Operational Scenarios | Scenario descriptions | At least 1 scenario |
| 9. Engagement and Commitment | Stakeholder engagement levels | Optional |
| 10. Products and Solutions | Product/solution lists | At least 1 product |
| 11. Parameterization Model | Configurable parameters | Optional |
| 12. Traceability and Notes | Source references | Required |

### Phase 3: Data Quality Validation

**Check**: Data quality and consistency

| Data Type | Quality Check | Threshold | Action |
|-----------|----------------|-----------|--------|
| Company Name | Non-empty string | N/A | Reject if empty |
| Industry | Valid industry value | Must match taxonomy | Reject if invalid |
| Country | Valid country name | ISO code or full name | Reject if invalid |
| Year | Valid year | 2018-2026 | Warn if out of range |
| Purchase Elements | Count | ≥ 1 | Warn if 0 |
| Stakeholders | Count | ≥ 1 | Reject if 0 |
| Scenarios | Count | ≥ 1 | Reject if 0 |
| Products | Count | ≥ 1 | Reject if 0 |

### Phase 4: Cross-Field Validation

**Check**: Logical consistency between fields

| Cross-Field Check | Validation Rule | Action |
|-------------------|-----------------|--------|
| Industry × Country | Valid industry-country pair | Warn if unusual |
| Purchase Elements × Stakeholders | Stakeholders align with elements | Check consistency |
| Products × Industry | Valid product-industry alignment | Warn if mismatch |
| Year × Country | Valid year-country combination | Check plausibility |
| Metrics × Purchase Elements | Metrics support elements | Validate linkage |

### Phase 5: Traceability Validation

**Check**: Reference completeness

| Traceability Element | Requirement | Action |
|---------------------|-------------|--------|
| Customer Name | Present in each section | Warn if missing |
| Original Quotes | Present for key findings | Warn if missing |
| Reference Locations | Page/line annotations | Optional |
| Source Case ID | Consistent across document | Required |

---

## Validation Results

### Pass Criteria

Document passes validation if:
- All **Required** checks pass
- No **Reject** level failures
- At most 3 **Warn** level issues

### Validation Report Structure

```
# Input Validation Report

## Document: {customer}-analysis.md
**Validation Time**: YYYY-MM-DD HH:MM:SS

## Phase 1: File-Level Validation
| Check | Status | Notes |
|-------|--------|-------|
| File Format | ✓ Pass | Markdown format confirmed |
| File Name | ✓ Pass | Follows naming pattern |
| Encoding | ✓ Pass | UTF-8 encoding |
| Readability | ✓ Pass | File readable |

## Phase 2: Structural Validation
| Section | Required Fields | Status | Missing |
|---------|----------------|--------|---------|
| 0. Customer Basic Information | 4/4 | ✓ Pass | - |
| 1. Purchase Elements | - | ✓ Pass | - |
| 2. Stakeholder List | - | ✓ Pass | - |
| ... | ... | ... | ... |

## Phase 3: Data Quality Validation
| Data Type | Value | Status | Notes |
|-----------|-------|--------|-------|
| Company Name | "Aberdeen City Council" | ✓ Pass | - |
| Industry | "Government" | ✓ Pass | Valid taxonomy |
| Country | "UK" | ✓ Pass | Valid country |
| Year | "2026" | ✓ Pass | In range |
| Purchase Elements | 5 | ✓ Pass | Meets threshold |
| Stakeholders | 6 | ✓ Pass | Meets threshold |
| Scenarios | 3 | ✓ Pass | Meets threshold |
| Products | 4 | ✓ Pass | Meets threshold |

## Phase 4: Cross-Field Validation
| Check | Status | Details |
|-------|--------|---------|
| Industry × Country | ✓ Pass | Valid pair |
| Purchase Elements × Stakeholders | ✓ Pass | Consistent |
| Products × Industry | ○ Warn | Unusual product for government |
| Year × Country | ✓ Pass | Plausible |
| Metrics × Purchase Elements | ✓ Pass | Linked |

## Phase 5: Traceability Validation
| Element | Status | Notes |
|---------|--------|-------|
| Customer Name | ✓ Pass | Present in sections |
| Original Quotes | ○ Warn | Missing in section 5 |
| Reference Locations | ✓ Pass | Present where needed |
| Source Case ID | ✓ Pass | Consistent |

## Validation Summary
| Metric | Value |
|--------|-------|
| Required Checks | 20/20 Pass |
| Warn Issues | 2 |
| Overall Status | ✓ Pass |
| Action | Proceed to model synthesis |

## Issues Requiring Attention
1. [Traceability] Original quotes missing in section 5 (Environment Model)
2. [Cross-Field] Unusual product for government industry - verify alignment

## Recommendations
- Add traceability quotes to Environment Model section
- Verify product-industry alignment or document rationale
```

---

## Error Handling

### Error Types and Resolutions

| Error Type | Description | Resolution |
|-----------|-------------|------------|
| **Missing Required Field** | Required field is empty or missing | Reject document, request correction |
| **Invalid Industry** | Industry not in taxonomy | Reject, map to correct category |
| **Invalid Country** | Country not recognized | Reject, use ISO format |
| **Year Out of Range** | Year outside 2018-2026 | Warn, still accept |
| **Zero Count** | Critical section has zero items | Reject if required, warn if optional |
| **Inconsistent Cross-Field** | Logical inconsistency detected | Warn, flag for review |
| **Missing Traceability** | Key traceability elements missing | Warn, still accept |

### Recovery Actions

1. **Auto-Recover**: Minor warnings that can be accepted
2. **Flag for Review**: Issues requiring human judgment
3. **Reject**: Critical issues preventing processing

---

## Batch Processing

For multiple input documents:

### Validation Order

1. Collect all input files
2. Parallel validation (up to 10 files at once)
3. Aggregate results
4. Generate batch validation report

### Batch Report Structure

```
# Batch Input Validation Report

## Validation Summary
| Metric | Value |
|--------|-------|
| Total Documents | 122 |
| Passed | 115 |
| Passed with Warnings | 5 |
| Rejected | 2 |
| Pass Rate | 94.3% |

## Documents by Status
| Status | Count | Documents |
|--------|-------|-----------|
| ✓ Pass | 115 | [list] |
| ○ Warning | 5 | [list] |
| ✗ Reject | 2 | [list] |

## Rejected Documents
| Document | Reason | Action |
|----------|--------|--------|
| {customer}-analysis.md | Missing required fields | Reject, request correction |
| {customer}-analysis.md | Invalid industry | Reject, remap category |

## Documents with Warnings
| Document | Warning Count | Top Issues |
|----------|---------------|------------|
| {customer}-analysis.md | 2 | Missing traceability, cross-field inconsistency |
| ... | ... | ... |

## Overall Assessment
- **Pass Threshold Met**: Yes (>90% pass rate)
- **Action**: Proceed with passed documents, flag warnings for review
```

---

## Industry Taxonomy Reference

Valid industry values:

| Category | Industries |
|----------|------------|
| Hospitality | Hotels, Restaurants, Tourism |
| Healthcare | Hospitals, Clinics, Laboratories |
| Education | Schools, Universities, Training |
| Logistics | Transportation, Supply Chain, Distribution |
| Manufacturing | Industrial, Production, Assembly |
| Retail | E-commerce, Stores, Shopping Centers |
| Services | Professional, Financial, Consulting |
| Sports/Entertainment | Sports Venues, Entertainment, Media |
| Government | Public Sector, Government Agencies |
| Other | Industries not in above categories |

---

## Implementation Notes

### Validation Workflow

1. Load document using markdown parser
2. Check file-level requirements
3. Extract sections using heading patterns
4. Validate required fields in each section
5. Check data quality thresholds
6. Perform cross-field consistency checks
7. Validate traceability elements
8. Generate validation report
9. Determine pass/fail/warn status
10. Return report with recommendations

### Performance Considerations

- Single document validation: < 100ms
- Batch validation (100 docs): < 5 seconds
- Parallel processing recommended for > 10 documents

### Extensibility

- Add new validation rules to appropriate phase
- Update thresholds as needed
- Extend industry taxonomy as required
- Add cross-field rules for new relationships