# Stakeholder Role Model Output Template

## Document Information

| Field | Value |
|-------|-------|
| Model Type | Stakeholder Role Model |
| Generation Date | [DATE] |
| Source Document Count | [COUNT] |
| Source Document Range | [CASE_IDS] |

---

## 1. Master Role Catalog

| Role Name | Category | Type | Frequency | Industries | Source Cases |
|-----------|----------|------|-----------|------------|--------------|
| Digital Infrastructure Manager | IT Lead | Operator | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| IT Director | IT Lead | Operator | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| CEO | Decision Maker | Decision | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| CIO | Decision Maker | Decision | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| CFO | Decision Maker | Decision | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| Municipal Decision Layer | Regulator | Oversight | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| NHS Management | Regulator | Oversight | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| School Management | Decision Maker | Decision | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| IT Operations Team | Operator | Operator | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| IT Service Desk | Operator | Operator | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| Teacher | User | User | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| Student (scale noted) | User | User | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| Doctor | User | User | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| Nurse | User | User | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| Patient | User | User | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| Employee | User | User | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| Retail Customer | User | User | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| Hotel Guest | User | User | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| Customer Success Manager | Partner | Partner | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| ASM Support Team | Partner | Partner | [COUNT] | [INDUSTRIES] | [CASE_IDS] |
| ... | ... | ... | ... | ... | ... |

---

## 2. Role Detailed Attributes

### Role: Digital Infrastructure Manager

| Attribute | Typical Values | Variant Values | Source Cases |
|-----------|----------------|----------------|--------------|
| Role Name | Digital Infrastructure Manager | IS Director, Network Manager | [CASE_IDS] |
| Category | IT Lead | - | - |
| Type | Operator | - | - |
| Influence | High | Medium-High | [CASE_IDS] |
| Priority | High | Medium-High | [CASE_IDS] |
| Expectations (Typical) | Simplified operations, AIOps support, Innovation focus | [VARIANT_EXPECTATIONS] | [CASE_IDS] |
| Value Focus | Efficiency, Innovation | Cost, Security | [CASE_IDS] |
| Participation Phases | Need Id, Evaluation, Decision, Deployment, Acceptance | Operations | [CASE_IDS] |

### Role: Teacher

| Attribute | Typical Values | Variant Values | Source Cases |
|-----------|----------------|----------------|--------------|
| Role Name | Teacher, Educator | - | [CASE_IDS] |
| Category | User | - | - |
| Type | User | - | - |
| Influence | Medium-High | Medium | [CASE_IDS] |
| Priority | High | Medium | [CASE_IDS] |
| Expectations (Typical) | All students connected simultaneously, Fast reliable Wi-Fi | [VARIANT_EXPECTATIONS] | [CASE_IDS] |
| Value Focus | User Experience, Usability | Reliability | [CASE_IDS] |
| Participation Phases | Acceptance, Operations | Need Id (feedback) | [CASE_IDS] |

[Continue for other roles...]

---

## 3. Category → Role Hierarchy

```
Decision Maker
├── CEO
├── CIO
├── CFO
├── Board Member
├── Municipal Decision Layer
├── NHS Management
├── School Management
└── Director (non-IT)

IT Lead
├── Digital Infrastructure Manager
├── IT Director / IS Director
├── Healthcare IT Lead
├── IT Operations Team Lead
├── Network Manager
└── Security Lead

Operator
├── IT Operations Team
├── IT Service Desk
├── Network Admin
├── Security Operations
├── System Admin
└── IT Team (general)

User
├── Student (scale noted)
├── Teacher/Educator
├── Doctor
├── Nurse
├── Patient
├── Employee
├── Retail Customer
├── Hotel Guest
├── Learner
├── Researcher
└── Fan/Attendee

Regulator
├── Government Agency
├── Municipal Government
├── NHS Foundation Trust
├── Ministry of Education
├── Compliance Officer
├── Environmental Agency
└── Data Protection Authority

Partner
├── Customer Success Manager
├── ASM Support Team
├── System Integrator
├── Vendor Technical Support
├── Managed Service Provider
├── Consultant
└── Channel Partner
```

---

## 4. Role × Industry Matrix

| Role | Education | Higher Ed | Healthcare | Hospitality | Manufacturing | IT Services | Logistics | Retail | Services | Sports | Legal |
|------|-----------|-----------|------------|-------------|---------------|-------------|-----------|--------|----------|--------|-------|
| Digital Infrastructure Manager | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| IT Director | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Teacher | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Student | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Doctor | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Employee | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Hotel Guest | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| CSM | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

### Industry-Specific Roles

| Industry | Industry-Specific Roles | Cross-Industry Roles | Notes |
|----------|------------------------|---------------------|-------|
| Education | Teacher, Student, School Management | IT Director, IT Team | Education-specific user roles |
| Healthcare | Doctor, Nurse, Patient, NHS Management | IT Director, Regulator | Healthcare-specific users |
| Hospitality | Hotel Guest, Travel Customer | IT Team, CSM | Guest-centric |
| Manufacturing | Production Operator, Plant Manager | IT Team, Security | Manufacturing-specific |
| ... | ... | ... | ... |

---

## 5. Role Co-occurrence Patterns

| Role Pair | Frequency | Industries | Relationship Type | Typical Conflict/Collaboration | Source Cases |
|-----------|-----------|------------|-------------------|------------------------------|--------------|
| IT Lead + User | [%] | [INDUSTRIES] | Support | Collaboration (service delivery) | [CASE_IDS] |
| Decision Maker + IT Lead | [%] | [INDUSTRIES] | Collaborative | Decision support | [CASE_IDS] |
| IT Lead + Partner | [%] | [INDUSTRIES] | Collaborative | External support | [CASE_IDS] |
| Decision Maker + Regulator | [%] | [INDUSTRIES] | Compliance | Policy constraint | [CASE_IDS] |
| IT Lead + Finance | [%] | [INDUSTRIES] | Conflict | Budget negotiation | [CASE_IDS] |
| ... | ... | ... | ... | ... | ... |

---

## 6. Key Insights

### Pattern 1: Cross-Industry IT Lead

| Aspect | Finding | Interpretation | Business Implication | Source Cases |
|--------|---------|----------------|--------------------|--------------|
| Role prevalence | IT Lead appears in all industries | IT expertise universal need | IT-focused engagement strategy | [CASE_IDS] |

### Pattern 2: Industry-Specific Users

| Aspect | Finding | Interpretation | Business Implication | Source Cases |
|--------|---------|----------------|--------------------|--------------|

---

## 7. Traceability Summary

| Role | Source Cases | Frequency | Original Expectation Quote |
|------|--------------|-----------|---------------------------|
| [ROLE_1] | [CASE_IDS] | [COUNT] | [QUOTE] |
| [ROLE_2] | [CASE_IDS] | [COUNT] | [QUOTE] |

---

## Notes

- [ROLE NORMALIZATION NOTES]
- [BOUNDARY CASE NOTES]