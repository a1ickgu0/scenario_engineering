# Relationship Model Output Template

## Document Information

| Field | Value |
|-------|-------|
| Model Type | Relationship Model |
| Generation Date | [DATE] |
| Source Document Count | [COUNT] |
| Source Document Range | [CASE_IDS] |

---

## 1. Hierarchical Relation Table

| From Entity | To Entity | Relation Type | Frequency | Industries | Source Cases |
|-------------|-----------|---------------|-----------|------------|--------------|
| CEO | CIO | Supervision | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| CIO | IT Director | Supervision | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| IT Director | IT Ops Team | Supervision | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| IT Ops Team | IT Service Desk | Supervision | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| IT Director | CFO | Reporting | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| Board | CEO | Authorization | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| Organization | Departments | Composition | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| Department | Teams | Composition | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| ... | ... | ... | ... | ... | ... |

---

## 2. Collaborative Relation Table

| Entity Pair | Relation Type | Context | Frequency | Industries | Source Cases |
|-------------|---------------|---------|-----------|------------|--------------|
| IT Lead ↔ Teachers | Cooperation | Deployment coordination | [COUNT] | Education | [CASE_IDS] |
| IT Lead ↔ Vendor CSM | Communication | Solution proposal | [COUNT] | All | [CASE_IDS] |
| Decision Maker ↔ CFO | Communication | Budget approval | [COUNT] | All | [CASE_IDS] |
| CSM → IT Team | Support | Lifecycle support | [COUNT] | Hospitality | [CASE_IDS] |
| Vendor → Organization | Service Delivery | Product delivery | [COUNT] | All | [CASE_IDS] |
| IT Lead ↔ IT Team | Cooperation | Evaluation support | [COUNT] | All | [CASE_IDS] |
| ... | ... | ... | ... | ... | ... |

---

## 3. Conflicting Relation Table

| Entity Pair | Conflict Type | Resolution | Frequency | Industries | Source Cases |
|-------------|---------------|------------|-----------|------------|--------------|
| IT Lead ↔ Decision Maker | Goal Conflict | ROI justification | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| IT Lead ↔ Finance | Resource Conflict | Subscription model | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| IT Lead ↔ User | Priority Conflict | Balance policy | [COUNT] | Education, Healthcare | [CASE_IDS] |
| Decision Maker ↔ Regulator | Interest Conflict | Compliance priority | [COUNT] | Healthcare | [CASE_IDS] |
| IT Team ↔ Management | Approach Conflict | AI-assisted, human oversight | [COUNT] | Manufacturing | [CASE_IDS] |
| ... | ... | ... | ... | ... | ... |

---

## 4. Dependency Relation Table

| From Entity | To Entity | Dependency Type | Condition | Source Cases |
|-------------|-----------|-----------------|-----------|--------------|
| Acceptance Phase | Deployment Phase | Sequential | Deployment complete | [CASE_IDS] |
| Deployment Phase | Decision Phase | Sequential | Decision made, contract signed | [CASE_IDS] |
| IT Operations | Budget | Resource | Budget approval | [CASE_IDS] |
| Decision Maker | IT Lead | Information | Technical assessment | [CASE_IDS] |
| Cloud Service | Network Infrastructure | Technical | Network connectivity | [CASE_IDS] |
| New System | Existing Systems | Integration | Legacy integration | [CASE_IDS] |
| Education Org | 1:1 Mandate | Policy | Policy compliance | [CASE_IDS] |
| ... | ... | ... | ... | ... |

---

## 5. Hierarchical Tree Template

```
Decision Maker
├── CIO / IT Director (Supervision)
│   ├── IT Operations Team (Supervision)
│   │   ├── IT Service Desk (Supervision)
│   │   └── Network Admin (Supervision)
│   └── Security Team (Supervision)
├── CFO (Supervision)
│   └── Finance Team (Supervision)
└── School Management (Supervision)
    ├── Teachers (Supervision)
    └── Students (Composition)
```

---

## 6. Collaboration Network Template

```
Purchase Decision Network:
├── Decision Maker ↔ IT Lead (Communication: technical assessment)
├── IT Lead ↔ Vendor CSM (Communication: solution proposal)
├── Decision Maker ↔ CFO (Communication: budget approval)
├── IT Lead ↔ IT Team (Cooperation: evaluation support)
└── Vendor ↔ Organization (Service Delivery)

Deployment Network:
├── IT Lead ↔ IT Team (Cooperation: deployment execution)
├── IT Team ↔ Vendor Support (Support: deployment guidance)
├── IT Team ↔ Site Staff (Cooperation: local coordination)
└── IT Lead ↔ Users (Communication: change notification)

Operations Network:
├── Users ↔ System (Use: daily operation)
├── Operator ↔ System (Monitor: performance monitoring)
├── AI ↔ Operator (Support: proactive identification)
├── CSM ↔ Organization (Support: lifecycle management)
```

---

## 7. Dependency Chain Template

```
Lifecycle Dependency Chain:
Need Identification
  ↓ [Sequential]
Evaluation & Selection
  ↓ [Information: technical assessment]
Purchase Decision
  ↓ [Resource: budget allocation]
Deployment
  ↓ [Technical: infrastructure ready]
Acceptance
  ↓ [Sequential]
Operations

System Dependency Chain:
Cloud Platform
  ↓ [Technical]
Network Infrastructure
  ↓ [Integration]
Existing Systems
  ↓ [Technical]
Security Module
```

---

## 8. Relation × Industry Matrix

| Relation Type | Education | Healthcare | Hospitality | Manufacturing | IT Services | Logistics | Retail |
|---------------|-----------|------------|-------------|---------------|-------------|-----------|--------|
| Supervision | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Cooperation | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Communication | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Support | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Goal Conflict | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Resource Conflict | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Sequential Dependency | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| ... | ... | ... | ... | ... | ... | ... | ... |

---

## 9. Key Insights

### Pattern 1: Universal IT Lead Decision Support

| Aspect | Finding | Interpretation | Business Implication | Source Cases |
|--------|---------|----------------|--------------------|--------------|
| IT Lead ↔ Decision Maker | Communication in all industries | Technical assessment universal | IT-focused engagement | [CASE_IDS] |

### Pattern 2: Industry-Specific Conflicts

| Aspect | Finding | Interpretation | Business Implication | Source Cases |
|--------|---------|----------------|--------------------|--------------|
| Healthcare Compliance Conflict | High in Healthcare | Compliance drives conflicts | Compliance positioning | [CASE_IDS] |

---

## 10. Traceability Summary

| Relation | Source Cases | Original Context | Inference Method |
|----------|--------------|------------------|------------------|
| [RELATION_1] | [CASE_IDS] | [CONTEXT] | [METHOD] |

---

## Notes

- [RELATION CLASSIFICATION NOTES]
- [NETWORK INFERENCE NOTES]