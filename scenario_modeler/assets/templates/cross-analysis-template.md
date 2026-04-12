# Cross-Analysis Matrix Output Template

## Document Information

| Field | Value |
|-------|-------|
| Model Type | Cross-Analysis Matrix |
| Generation Date | [DATE] |
| Source Document Count | [COUNT] |
| Source Document Range | [CASE_IDS] |

---

## 1. Industry × Stakeholder Category Matrix

| Industry | Decision Maker | IT Lead | Operator | User | Regulator | Partner | Dominant Category |
|----------|----------------|---------|----------|------|-----------|---------|-------------------|
| Education | [%] | [%] | [%] | [%] | [%] | [%] | User |
| Higher Education | [%] | [%] | [%] | [%] | [%] | [%] | User + IT Lead |
| Healthcare | [%] | [%] | [%] | [%] | [%] | [%] | User + Regulator |
| Hospitality | [%] | [%] | [%] | [%] | [%] | [%] | User + Partner |
| Manufacturing | [%] | [%] | [%] | [%] | [%] | [%] | IT Lead + Operator |
| IT Services | [%] | [%] | [%] | [%] | [%] | [%] | IT Lead + Partner |
| Logistics | [%] | [%] | [%] | [%] | [%] | [%] | IT Lead + User |
| Retail | [%] | [%] | [%] | [%] | [%] | [%] | User |
| Services & Utilities | [%] | [%] | [%] | [%] | [%] | [%] | IT Lead + Operator |
| Sports & Entertainment | [%] | [%] | [%] | [%] | [%] | [%] | User (high density) |
| Legal Services | [%] | [%] | [%] | [%] | [%] | [%] | User + Security focus |

### Matrix Insights

| Pattern | Observation | Interpretation | Source Cases |
|---------|-------------|----------------|--------------|
| User universality | User appears in all industries (>90%) | Direct usage universal requirement | [CASE_IDS] |
| IT Lead high frequency | IT Lead appears >70% in all industries | Technical expertise always needed | [CASE_IDS] |
| Regulator high in Healthcare | Regulator 80% in Healthcare | Compliance critical for healthcare | [CASE_IDS] |
| Partner high in Hospitality | Partner 40% in Hospitality | External services common | [CASE_IDS] |

---

## 2. Industry × Stakeholder Role Matrix (Top Roles)

| Role | Education | Higher Ed | Healthcare | Hospitality | Manufacturing | IT Services | Logistics | Retail |
|------|-----------|-----------|------------|-------------|---------------|-------------|-----------|--------|
| Digital Infrastructure Manager | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| IT Director | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Teacher | [N] | [N] | - | - | - | - | - | - |
| Student | [N] | [N] | - | - | - | - | - | - |
| Doctor | - | - | [N] | - | - | - | - | - |
| Patient | - | - | [N] | - | - | - | - | - |
| Hotel Guest | - | - | - | [N] | - | - | - | - |
| Employee | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| CSM | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |

### Industry-Specific Role Patterns

| Industry | Industry-Specific Roles | Cross-Industry Roles |
|----------|------------------------|---------------------|
| Education | Teacher, Student | IT Director, CSM |
| Healthcare | Doctor, Nurse, Patient | IT Director, Regulator |
| Hospitality | Hotel Guest | IT Team, CSM |
| ... | ... | ... |

---

## 3. Industry × Business Driver Matrix

| Industry | Cost | Efficiency | Security | Experience | Innovation | Sustainability | Primary Driver |
|----------|------|------------|----------|------------|------------|----------------|----------------|
| Education | [RANK] | [RANK] | [RANK] | [RANK] | [RANK] | [RANK] | Experience |
| Higher Education | [RANK] | [RANK] | [RANK] | [RANK] | [RANK] | [RANK] | Efficiency + Innovation |
| Healthcare | [RANK] | [RANK] | [RANK] | [RANK] | [RANK] | [RANK] | Security |
| Hospitality | [RANK] | [RANK] | [RANK] | [RANK] | [RANK] | [RANK] | Cost |
| Manufacturing | [RANK] | [RANK] | [RANK] | [RANK] | [RANK] | [RANK] | Efficiency |
| IT Services | [RANK] | [RANK] | [RANK] | [RANK] | [RANK] | [RANK] | Innovation + Efficiency |
| Logistics | [RANK] | [RANK] | [RANK] | [RANK] | [RANK] | [RANK] | Security + Efficiency |
| Retail | [RANK] | [RANK] | [RANK] | [RANK] | [RANK] | [RANK] | Experience |
| ... | ... | ... | ... | ... | ... | ... | ... |

### Driver Priority Patterns

| Industry | Primary Driver | Reasoning | Source Cases |
|----------|----------------|-----------|--------------|
| Education | User Experience | 1:1 device mandate, student connectivity | [CASE_IDS] |
| Healthcare | Security/Compliance | HIPAA, patient data protection | [CASE_IDS] |
| Hospitality | Cost Optimization | NaaS preference, subscription model | [CASE_IDS] |
| Manufacturing | Efficiency | Operational efficiency, predictive maintenance | [CASE_IDS] |

---

## 4. Stakeholder Category × Business Driver Matrix

| Category | Cost | Efficiency | Security | Experience | Innovation | Sustainability |
|----------|------|------------|----------|------------|------------|----------------|
| Decision Maker | [%] | [%] | [%] | [%] | [%] | [%] |
| IT Lead | [%] | [%] | [%] | [%] | [%] | [%] |
| Operator | [%] | [%] | [%] | [%] | [%] | [%] |
| User | [%] | [%] | [%] | [%] | [%] | [%] |
| Regulator | [%] | [%] | [%] | [%] | [%] | [%] |
| Partner | [%] | [%] | [%] | [%] | [%] | [%] |

### Category-Driver Alignment

| Category | Primary Drivers | Secondary Drivers | Typical Expectation |
|----------|-----------------|-------------------|--------------------|
| Decision Maker | Cost, Innovation | Efficiency, Security | ROI, Strategic value |
| IT Lead | Efficiency, Security | Cost, Innovation | Technical feasibility |
| Operator | Efficiency | Cost, Security | Simplified operations |
| User | Experience, Efficiency | Security | Usability, Reliability |
| Regulator | Security, Compliance | Cost | Compliance requirements |
| Partner | Efficiency, Collaboration | Cost | Service delivery success |

---

## 5. Stakeholder Role × Business Driver Matrix (Top Roles)

| Role | Primary Drivers | Secondary Drivers | Typical Expectation | Source Cases |
|------|-----------------|-------------------|--------------------|--------------|
| Digital Infrastructure Manager | Efficiency, Innovation | Cost, Security | Simplified operations, AIOps support | [CASE_IDS] |
| IT Director | Efficiency, Security | Cost, Innovation | Feasibility, Operations efficiency | [CASE_IDS] |
| CFO | Cost | Efficiency | Cost optimization, Budget control | [CASE_IDS] |
| Teacher | Experience | Efficiency | All students connected simultaneously | [CASE_IDS] |
| Student | Experience | - | Stable Wi-Fi connection | [CASE_IDS] |
| Doctor | Security, Experience | Efficiency | Quick access to patient information | [CASE_IDS] |
| Patient | Experience, Security | - | Better care and accessibility | [CASE_IDS] |
| Hotel Guest | Experience | - | Reduced network latency | [CASE_IDS] |
| CSM | Collaboration, Efficiency | Cost | Service delivery, Lifecycle management | [CASE_IDS] |

---

## 6. Stakeholder Category × Conflict Matrix

| Category | Cost vs Quality | Cost vs Security | Security vs Convenience | Innovation vs Stability | Capacity vs Cost | Short vs Long-term |
|----------|-----------------|------------------|-------------------------|------------------------|------------------|--------------------|
| Decision Maker | [%] | [%] | [%] | [%] | [%] | [%] |
| IT Lead | [%] | [%] | [%] | [%] | [%] | [%] |
| Operator | [%] | [%] | [%] | [%] | [%] | [%] |
| User | [%] | [%] | [%] | [%] | [%] | [%] |
| Regulator | [%] | [%] | [%] | [%] | [%] | [%] |
| Partner | [%] | [%] | [%] | [%] | [%] | [%] |

### Conflict Involvement Patterns

| Conflict Type | Most Involved Categories | Resolution Pattern | Source Cases |
|---------------|-------------------------|--------------------|--------------|
| Cost vs Quality | Decision Maker, IT Lead | ROI justification | [CASE_IDS] |
| Security vs Convenience | IT Lead, User | Balance policy | [CASE_IDS] |
| Innovation vs Stability | Decision Maker, IT Lead | Phased rollout | [CASE_IDS] |

---

## 7. Key Cross-Dimension Insights

### Insight 1: Universal Patterns

| Pattern | Matrix | Observation | Interpretation | Source Cases |
|---------|--------|-------------|----------------|--------------|
| User universality | Industry × Category | User in all industries | Direct usage fundamental | [CASE_IDS] |
| Efficiency universal | Industry × Driver | Efficiency in all industries | Operational improvement universal | [CASE_IDS] |

### Insight 2: Industry Differentiation

| Pattern | Matrix | Observation | Interpretation | Source Cases |
|---------|--------|-------------|----------------|--------------|
| Healthcare Security | Industry × Driver | Security primary in Healthcare | Compliance-driven industry | [CASE_IDS] |
| Hospitality Cost | Industry × Driver | Cost primary in Hospitality | Subscription model preference | [CASE_IDS] |

### Insight 3: Stakeholder-Driver Alignment

| Pattern | Matrix | Observation | Interpretation | Source Cases |
|---------|--------|-------------|----------------|--------------|
| IT Lead-Efficiency | Category × Driver | IT Lead prioritizes Efficiency | Technical operations focus | [CASE_IDS] |
| User-Experience | Role × Driver | User prioritizes Experience | Direct usage impact | [CASE_IDS] |

---

## 8. Traceability Summary

| Matrix Cell | Value | Source Cases | Frequency | Example Quote |
|-------------|-------|--------------|-----------|---------------|
| [CELL_REF] | [VALUE] | [CASE_IDS] | [%] | [QUOTE] |

---

## Notes

- [MATRIX CALCULATION NOTES]
- [PATTERN SIGNIFICANCE THRESHOLDS]