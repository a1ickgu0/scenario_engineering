# Stakeholder Category Model Output Template

## Document Information

| Field | Value |
|-------|-------|
| Model Type | Stakeholder Category Model |
| Generation Date | [DATE] |
| Source Document Count | [COUNT] |
| Source Document Range | [CASE_IDS] |

---

## 1. Category Definitions

| Category | Definition | Typical Traits | Frequency |
|----------|------------|----------------|-----------|
| Decision Maker | Final decision authority or budget approval | High influence, strategic view, ROI focus | [%] |
| IT Lead | Technical architecture and operations lead | High influence, technical view, feasibility focus | [%] |
| Operator | Daily operations and execution | Medium-high influence, execution view, efficiency focus | [%] |
| User | Direct system users | Medium influence, experience view, usability focus | [%] |
| Regulator | Policy, compliance, industry oversight | High constraint, compliance view, risk focus | [%] |
| Partner | External support and service providers | Medium influence, service view, collaboration focus | [%] |

---

## 2. Category × Industry Distribution

| Industry | Decision Maker | IT Lead | Operator | User | Regulator | Partner | Dominant Category |
|----------|----------------|---------|----------|------|-----------|---------|-------------------|
| Education | [%] | [%] | [%] | [%] | [%] | [%] | [CATEGORY] |
| Higher Education | [%] | [%] | [%] | [%] | [%] | [%] | [CATEGORY] |
| Healthcare | [%] | [%] | [%] | [%] | [%] | [%] | [CATEGORY] |
| Hospitality | [%] | [%] | [%] | [%] | [%] | [%] | [CATEGORY] |
| Manufacturing | [%] | [%] | [%] | [%] | [%] | [%] | [CATEGORY] |
| IT Services | [%] | [%] | [%] | [%] | [%] | [%] | [CATEGORY] |
| Logistics | [%] | [%] | [%] | [%] | [%] | [%] | [CATEGORY] |
| Retail | [%] | [%] | [%] | [%] | [%] | [%] | [CATEGORY] |
| ... | ... | ... | ... | ... | ... | ... | ... |

### Industry Category Patterns

| Industry | High-Frequency Categories (>50%) | Variant Categories (<20%) | Notes |
|----------|----------------------------------|--------------------------|-------|
| Education | [CATEGORY_LIST] | [CATEGORY_LIST] | User always present (students) |
| Healthcare | [CATEGORY_LIST] | [CATEGORY_LIST] | Regulator high (compliance) |
| Hospitality | [CATEGORY_LIST] | [CATEGORY_LIST] | Partner higher (external services) |
| ... | ... | ... | ... |

---

## 3. Category Typical Expectations

| Category | Typical Expectations | Typical Quote | Source Cases |
|----------|---------------------|---------------|--------------|
| Decision Maker | ROI justification, Strategic alignment | [QUOTE] | [CASE_IDS] |
| IT Lead | Feasibility, Efficiency, Innovation | [QUOTE] | [CASE_IDS] |
| Operator | Simplified operations, Automation | [QUOTE] | [CASE_IDS] |
| User | Usability, Reliability, Experience | [QUOTE] | [CASE_IDS] |
| Regulator | Compliance, Security, Risk mitigation | [QUOTE] | [CASE_IDS] |
| Partner | Collaboration, Service delivery | [QUOTE] | [CASE_IDS] |

---

## 4. Category Typical Participation Phases

| Category | Typical Phases | Typical Actions | Source Cases |
|----------|----------------|-----------------|--------------|
| Decision Maker | Need Identification, Decision, Acceptance | [ACTION_LIST] | [CASE_IDS] |
| IT Lead | All phases | [ACTION_LIST] | [CASE_IDS] |
| Operator | Deployment, Operations | [ACTION_LIST] | [CASE_IDS] |
| User | Acceptance, Operations | [ACTION_LIST] | [CASE_IDS] |
| Regulator | Need Identification, Acceptance | [ACTION_LIST] | [CASE_IDS] |
| Partner | Deployment, Operations | [ACTION_LIST] | [CASE_IDS] |

### Participation Phase Matrix

| Category | Need Id | Evaluation | Decision | Deployment | Acceptance | Operations |
|----------|---------|------------|----------|------------|------------|------------|
| Decision Maker | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| IT Lead | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| Operator | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| User | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| Regulator | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| Partner | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] |

---

## 5. Category Influence Distribution

| Category | High Influence | Medium-High Influence | Medium Influence | Low Influence | Typical Level |
|----------|----------------|-----------------------|------------------|---------------|---------------|
| Decision Maker | [%] | [%] | [%] | [%] | High |
| IT Lead | [%] | [%] | [%] | [%] | High |
| Operator | [%] | [%] | [%] | [%] | Medium-High |
| User | [%] | [%] | [%] | [%] | Medium |
| Regulator | [%] | [%] | [%] | [%] | High (constraint) |
| Partner | [%] | [%] | [%] | [%] | Medium |

---

## 6. Boundary Clarification Cases

| Ambiguous Role | Possible Categories | Assigned Category | Reasoning | Source Cases |
|----------------|---------------------|-------------------|-----------|--------------|
| [ROLE_1] | [CATEGORY_LIST] | [CATEGORY] | [REASONING] | [CASE_IDS] |
| [ROLE_2] | [CATEGORY_LIST] | [CATEGORY] | [REASONING] | [CASE_IDS] |
| ... | ... | ... | ... | ... |

---

## 7. Category Co-occurrence Patterns

| Category Pair | Frequency | Industries | Relationship Type | Typical Context |
|---------------|-----------|------------|-------------------|-----------------|
| Decision Maker + IT Lead | [%] | [INDUSTRIES] | Collaborative (decision support) | [CONTEXT] |
| IT Lead + User | [%] | [INDUSTRIES] | Support (service delivery) | [CONTEXT] |
| Decision Maker + Regulator | [%] | [INDUSTRIES] | Compliance (policy) | [CONTEXT] |
| IT Lead + Partner | [%] | [INDUSTRIES] | Collaborative (external support) | [CONTEXT] |
| ... | ... | ... | ... | ... |

---

## 8. Key Insights

### Pattern 1: [PATTERN_NAME]

| Aspect | Finding | Interpretation | Business Implication | Source Cases |
|--------|---------|----------------|--------------------|--------------|

### Pattern 2: [PATTERN_NAME]

| Aspect | Finding | Interpretation | Business Implication | Source Cases |
|--------|---------|----------------|--------------------|--------------|

---

## 9. Traceability Summary

| Category Conclusion | Source Cases | Frequency | Typical Quote |
|--------------------|--------------|-----------|---------------|
| [CONCLUSION_1] | [CASE_IDS] | [%] | [QUOTE] |
| [CONCLUSION_2] | [CASE_IDS] | [%] | [QUOTE] |

---

## Notes

- [ADDITIONAL NOTES]
- [CATEGORY DEFINITION CONSISTENCY NOTES]