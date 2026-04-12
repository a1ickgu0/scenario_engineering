# Stakeholder Model Output Template

## Document Information

| Field | Value |
|-------|-------|
| Model Type | Stakeholder Model |
| Layer Structure | Category Layer + Role Layer |
| Generation Date | [DATE] |
| Source Document Count | [COUNT] |
| Source Document Range | [CASE_IDS] |
| SKILL Version | scenario_modeler v0.2.0 |

---

## Part A: Category Layer (类别层)

### A1. Category Definitions

| Category | Definition | Typical Traits | Frequency | Source Cases |
|----------|------------|----------------|-----------|--------------|
| Decision Maker | Final decision authority or budget approval | High influence, strategic view, ROI focus | [%] | [CASE_IDS] |
| IT Lead | Technical architecture and operations lead | High influence, technical view, feasibility focus | [%] | [CASE_IDS] |
| Operator | Daily operations and execution | Medium-high influence, execution view, efficiency focus | [%] | [CASE_IDS] |
| User | Direct system users | Medium influence, experience view, usability focus | [%] | [CASE_IDS] |
| Regulator | Policy, compliance, industry oversight | High constraint, compliance view, risk focus | [%] | [CASE_IDS] |
| Partner | External support and service providers | Medium influence, service view, collaboration focus | [%] | [CASE_IDS] |

### A2. Category × Industry Distribution Matrix

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
| Sports & Entertainment | [%] | [%] | [%] | [%] | [%] | [%] | [CATEGORY] |

### A3. Industry Category Patterns

| Industry | High-Frequency Categories (>50%) | Low-Frequency Categories (<20%) | Pattern Notes |
|----------|----------------------------------|----------------------------------|---------------|
| Education | [CATEGORY_LIST] | [CATEGORY_LIST] | [NOTES] |
| Healthcare | [CATEGORY_LIST] | [CATEGORY_LIST] | [NOTES] |
| Hospitality | [CATEGORY_LIST] | [CATEGORY_LIST] | [NOTES] |
| Manufacturing | [CATEGORY_LIST] | [CATEGORY_LIST] | [NOTES] |
| [Continue for other industries...] | ... | ... | ... |

---

### A4. Category Typical Expectations (Enhanced Traceability)

| Category | Typical Expectations | Customer Name | Original Quote | Source Cases |
|----------|---------------------|---------------|----------------|--------------|
| Decision Maker | ROI justification, Strategic alignment | [CUSTOMER_NAME] | [QUOTE] (Page X) | [CASE_IDS] |
| IT Lead | Feasibility, Efficiency, Innovation | [CUSTOMER_NAME] | [QUOTE] (Page X) | [CASE_IDS] |
| Operator | Simplified operations, Automation | [CUSTOMER_NAME] | [QUOTE] (Page X) | [CASE_IDS] |
| User | Usability, Reliability, Experience | [CUSTOMER_NAME] | [QUOTE] (Page X) | [CASE_IDS] |
| Regulator | Compliance, Security, Risk mitigation | [CUSTOMER_NAME] | [QUOTE] (Page X) | [CASE_IDS] |
| Partner | Collaboration, Service delivery | [CUSTOMER_NAME] | [QUOTE] (Page X) | [CASE_IDS] |

---

### A5. Category Participation Phase Matrix

| Category | Need Id | Evaluation | Decision | Deployment | Acceptance | Operations | Source Cases |
|----------|---------|------------|----------|------------|------------|------------|--------------|
| Decision Maker | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [CASE_IDS] |
| IT Lead | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [CASE_IDS] |
| Operator | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [CASE_IDS] |
| User | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [CASE_IDS] |
| Regulator | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [CASE_IDS] |
| Partner | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [✓/○] | [CASE_IDS] |

**符号说明**: ✓ = 高频参与, ○ = 低频/不参与

---

### A6. Category Influence Distribution

| Category | High Influence | Medium-High Influence | Medium Influence | Low Influence | Typical Level | Source Cases |
|----------|----------------|-----------------------|------------------|---------------|---------------|--------------|
| Decision Maker | [%] | [%] | [%] | [%] | High | [CASE_IDS] |
| IT Lead | [%] | [%] | [%] | [%] | High | [CASE_IDS] |
| Operator | [%] | [%] | [%] | [%] | Medium-High | [CASE_IDS] |
| User | [%] | [%] | [%] | [%] | Medium | [CASE_IDS] |
| Regulator | [%] | [%] | [%] | [%] | High (constraint) | [CASE_IDS] |
| Partner | [%] | [%] | [%] | [%] | Medium | [CASE_IDS] |

---

## Part B: Role Layer (角色层)

### B1. Master Role Catalog

| Role Name | Category | Type | Frequency | Industries | Source Cases |
|-----------|----------|------|-----------|------------|--------------|
| Digital Infrastructure Manager | IT Lead | Operator | [%] | [INDUSTRIES] | [CASE_IDS] |
| IT Director / IS Director | IT Lead | Operator | [%] | [INDUSTRIES] | [CASE_IDS] |
| Network Manager | IT Lead | Operator | [%] | [INDUSTRIES] | [CASE_IDS] |
| CIO / COO | Decision Maker | Decision | [%] | [INDUSTRIES] | [CASE_IDS] |
| CEO / Board | Decision Maker | Decision | [%] | [INDUSTRIES] | [CASE_IDS] |
| School Management | Decision Maker | Decision | [%] | [INDUSTRIES] | [CASE_IDS] |
| IT Operations Team | Operator | Operator | [%] | [INDUSTRIES] | [CASE_IDS] |
| Network Admin | Operator | Operator | [%] | [INDUSTRIES] | [CASE_IDS] |
| Teacher / Educator | User | User | [%] | [INDUSTRIES] | [CASE_IDS] |
| Student / Learner | User | User | [%] | [INDUSTRIES] | [CASE_IDS] |
| Researcher | User | User | [%] | [INDUSTRIES] | [CASE_IDS] |
| Clinical Teams | User | User | [%] | [INDUSTRIES] | [CASE_IDS] |
| Patient | User | User | [%] | [INDUSTRIES] | [CASE_IDS] |
| Hotel Guest | User | User | [%] | [INDUSTRIES] | [CASE_IDS] |
| Employee / Staff | User | User | [%] | [INDUSTRIES] | [CASE_IDS] |
| Fan / Attendee | User | User | [%] | [INDUSTRIES] | [CASE_IDS] |
| Government Agency | Regulator | Oversight | [%] | [INDUSTRIES] | [CASE_IDS] |
| TISAX / Industry Standard | Regulator | Oversight | [%] | [INDUSTRIES] | [CASE_IDS] |
| Customer Success Manager | Partner | Partner | [%] | [INDUSTRIES] | [CASE_IDS] |
| MSP / Managed Service Provider | Partner | Partner | [%] | [INDUSTRIES] | [CASE_IDS] |
| HPE Aruba / Vendor | Partner | Partner | [%] | [INDUSTRIES] | [CASE_IDS] |
| [Continue for other roles...] | ... | ... | ... | ... | ... |

---

### B2. Category → Role Hierarchy

```
Decision Maker
├── CEO / Board Member
├── CIO / COO
├── CFO / Finance Director
├── School Management / District Admin
├── Municipal Decision Layer
├── NHS Management / Trust Board
└── Director (non-IT functions)

IT Lead
├── Digital Infrastructure Manager
├── IT Director / IS Director
├── Network Manager / Head of Network Services
├── Healthcare IT Lead
├── IT Operations Team Lead
├── Infrastructure Cloud Architect
├── VP IT & Digitization
└── Security Lead

Operator
├── IT Operations Team
├── IT Service Desk / Help Desk
├── Network Admin
├── Security Operations
├── System Admin
├── Facilities Team
├── Production Operator
└── Stadium Operations Team

User
├── Student / Learner (scale noted)
├── Teacher / Educator
├── Researcher / PhD Student
├── Clinical Teams / Doctor
├── Nurse / Community Nurse
├── Patient
├── Employee / Staff
├── Retail Customer / Shopper
├── Hotel Guest
├── Fan / Attendee
├── Media Team
├── Players (Sports)
└── External Consultant (user of system)

Regulator
├── Government Agency / Ministry
├── Municipal Government / City Council
├── NHS England / NHS Foundation Trust
├── Ministry of Education
├── TISAX / Industry Compliance Body
├── Environmental Agency
└── Data Protection Authority

Partner
├── Customer Success Manager (CSM)
├── ASM / Technical Support Team
├── System Integrator (SI)
├── Managed Service Provider (MSP)
├── Channel Partner / Reseller
├── Technology Vendor (HPE Aruba)
└── Consultant / Advisory
```

---

### B3. Role × Industry Matrix

| Role | Education | Higher Ed | Healthcare | Hospitality | Manufacturing | IT Services | Logistics | Retail | Sports |
|------|-----------|-----------|------------|-------------|---------------|-------------|-----------|--------|--------|
| Digital Infrastructure Manager | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| IT Director | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Network Manager | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| CIO/COO | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Teacher | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Student | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Researcher | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Clinical Teams | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Patient | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Hotel Guest | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Employee/Staff | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Fan/Attendee | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Regulator | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| CSM | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| MSP | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| [Continue...] | ... | ... | ... | ... | ... | ... | ... | ... | ... |

---

### B4. Industry-Specific Roles

| Industry | Industry-Specific Roles | Cross-Industry Roles | Notes |
|----------|------------------------|---------------------|-------|
| Education (K-12) | Teacher, Student, School Board | IT Director, IT Team, CSM | [NOTES] |
| Higher Education | Researcher, PhD Student, Faculty | IT Director, Network Manager | [NOTES] |
| Healthcare | Clinical Teams, Doctor, Nurse, Patient | IT Director, Regulator | [NOTES] |
| Hospitality | Hotel Guest, Wi-Fi Concierge | IT Director, Partner | [NOTES] |
| Manufacturing | Production Operator, Plant Manager | IT Director, MSP | [NOTES] |
| IT Services | Enterprise Customer, Infrastructure Architect | IT Team, Partner | [NOTES] |
| Logistics | Automotive Client, Supply Chain Operator | IT Director, Regulator (TISAX) | [NOTES] |
| Retail | Shopper, Store Staff, Loyalty Member | IT Director, IT Team | [NOTES] |
| Sports & Entertainment | Fan, Media Team, Players, Stadium Ops | IT Director, IT Team | [NOTES] |

---

### B5. Role Detailed Attributes (Enhanced Traceability)

#### Role: Digital Infrastructure Manager (IT Lead Category)

| Attribute | Typical Values | Customer Name | Original Quote | Source Cases |
|-----------|----------------|---------------|----------------|--------------|
| Role Name | Digital Infrastructure Manager | [CUSTOMER_NAME] | [QUOTE] (Page X) | [CASE_IDS] |
| Category | IT Lead | - | - | - |
| Influence | High | [CUSTOMER_NAME] | [QUOTE] | [CASE_IDS] |
| Priority | 1 (Highest) | [CUSTOMER_NAME] | [QUOTE] | [CASE_IDS] |
| Expectations | Simplified operations, AIOps support | [CUSTOMER_NAME] | [QUOTE] (Page X) | [CASE_IDS] |
| Value Focus | Efficiency, Innovation | [CUSTOMER_NAME] | [QUOTE] | [CASE_IDS] |
| Participation | All phases | [CUSTOMER_NAME] | [QUOTE] | [CASE_IDS] |

#### Role: Teacher / Educator (User Category)

| Attribute | Typical Values | Customer Name | Original Quote | Source Cases |
|-----------|----------------|---------------|----------------|--------------|
| Role Name | Teacher, Educator | [CUSTOMER_NAME] | [QUOTE] (Page X) | [CASE_IDS] |
| Category | User | - | - | - |
| Influence | Medium-High | [CUSTOMER_NAME] | [QUOTE] | [CASE_IDS] |
| Priority | 2 | [CUSTOMER_NAME] | [QUOTE] | [CASE_IDS] |
| Expectations | All students connected simultaneously | [CUSTOMER_NAME] | [QUOTE] (Page X) | [CASE_IDS] |
| Value Focus | User Experience, Reliability | [CUSTOMER_NAME] | [QUOTE] | [CASE_IDS] |
| Participation | Acceptance, Operations | [CUSTOMER_NAME] | [QUOTE] | [CASE_IDS] |

[Continue for other key roles...]

---

### B6. Role Co-occurrence Patterns

| Role Pair | Frequency | Industries | Relationship Type | Customer Name | Typical Quote | Source Cases |
|-----------|-----------|------------|-------------------|---------------|---------------|--------------|
| IT Lead + User | [%] | [INDUSTRIES] | Support (service delivery) | [CUSTOMER_NAME] | [QUOTE] | [CASE_IDS] |
| Decision Maker + IT Lead | [%] | [INDUSTRIES] | Collaborative (decision) | [CUSTOMER_NAME] | [QUOTE] | [CASE_IDS] |
| IT Lead + Partner | [%] | [INDUSTRIES] | Collaborative (external) | [CUSTOMER_NAME] | [QUOTE] | [CASE_IDS] |
| Decision Maker + Regulator | [%] | [INDUSTRIES] | Compliance (policy) | [CUSTOMER_NAME] | [QUOTE] | [CASE_IDS] |
| IT Lead + Operator | [%] | [INDUSTRIES] | Hierarchical (management) | [CUSTOMER_NAME] | [QUOTE] | [CASE_IDS] |
| User + Partner | [%] | [INDUSTRIES] | Service (delivery) | [CUSTOMER_NAME] | [QUOTE] | [CASE_IDS] |

---

## Part C: Key Insights (Enhanced Traceability)

### C1. Pattern: [PATTERN_NAME]

| Aspect | Finding | Customer Name | Original Quote | Business Implication | Source Cases |
|--------|---------|---------------|----------------|--------------------|--------------|
| [ASPECT] | [FINDING] | [CUSTOMER_NAME] | [QUOTE] (Page X) | [IMPLICATION] | [CASE_IDS] |

### C2. Pattern: [PATTERN_NAME]

| Aspect | Finding | Customer Name | Original Quote | Business Implication | Source Cases |
|--------|---------|---------------|----------------|--------------------|--------------|

[Continue for other patterns...]

---

## Part D: Traceability Summary (Enhanced - 4 Sub-tables)

### D1. Category Traceability

| Category Conclusion | Source Cases | Frequency | Customer Name | Original Quote |
|--------------------|--------------|-----------|---------------|----------------|
| [CONCLUSION_1] | [CASE_IDS] | [%] | [CUSTOMER_NAME] | [QUOTE] (Page X) |
| [CONCLUSION_2] | [CASE_IDS] | [%] | [CUSTOMER_NAME] | [QUOTE] (Page X) |

### D2. Role Traceability

| Role | Source Cases | Frequency | Customer Name | Original Quote |
|------|--------------|-----------|---------------|----------------|
| [ROLE_1] | [CASE_IDS] | [%] | [CUSTOMER_NAME] | [QUOTE] (Page X) |
| [ROLE_2] | [CASE_IDS] | [%] | [CUSTOMER_NAME] | [QUOTE] (Page X) |

### D3. Industry Role Pattern Traceability

| Industry | Role Pattern | Customer Name | Original Quote | Source Cases |
|----------|--------------|---------------|----------------|--------------|
| [INDUSTRY] | [PATTERN] | [CUSTOMER_NAME] | [QUOTE] (Page X) | [CASE_IDS] |

### D4. Co-occurrence Pattern Traceability

| Role Pair | Frequency | Customer Name | Original Quote | Source Cases |
|-----------|-----------|---------------|----------------|--------------|
| [PAIR_1] | [%] | [CUSTOMER_NAME] | [QUOTE] (Page X) | [CASE_IDS] |

---

## Part E: Critical Analysis (MANDATORY)

### E1. Data Source Limitations Assessment

| Limitation | Impact Level | Analysis | Effect on Conclusions |
|------------|--------------|----------|----------------------|
| Supplier Perspective Bias | High | All documents from same vendor (HPE), stakeholder roles may be vendor-centric | Role roles may emphasize vendor-facing roles (CSM, Partner) |
| No Negative Stakeholders | High | All cases are successful deployments, no dissatisfied stakeholders | Cannot assess stakeholder conflict patterns, resistance scenarios |
| IT Lead Overrepresentation | Medium | IT Lead appears in 100% cases, may reflect vendor contact point bias | IT Lead frequency may overestimate actual decision influence |
| User Scale Variations | Medium | User scales vary dramatically (2 to 62,000+), aggregation challenges | User influence patterns may not reflect scale-specific dynamics |
| Role Definition Variance | Low | Role names vary by industry/region, standardization introduces bias | Some role nuances may be lost in standardization |

### E2. Objective Stakeholder Correction

#### Industry: Education

| Original Conclusion | Objective Correction | Industry Domain Knowledge |
|---------------------|----------------------|---------------------------|
| [ORIGINAL] | [CORRECTION] | [KNOWLEDGE] |

#### Industry: Healthcare

| Original Conclusion | Objective Correction | Industry Domain Knowledge |
|---------------------|----------------------|---------------------------|
| [ORIGINAL] | [CORRECTION] | [KNOWLEDGE] |

[Continue for other industries...]

### E3. Role Influence Objective Assessment

| Role | Supplier Perspective Influence | Objective Assessment | Caveats |
|------|-------------------------------|----------------------|---------|
| [ROLE_1] | [SUPPLIER_VIEW] | [OBJECTIVE_VIEW] | [CAVEATS] |

### E4. Stakeholder Distribution Objective Interpretation

| Distribution Finding | Supplier Perspective | Objective Interpretation |
|---------------------|---------------------|-------------------------|
| [FINDING] | [SUPPLIER_VIEW] | [OBJECTIVE_VIEW] |

### E5. Data Usage Recommendations

| Usage Scenario | Recommended Approach |
|----------------|---------------------|
| Stakeholder Engagement | Supplement with organizational analysis, verify actual decision structure |
| Role Mapping | Validate with customer interviews, confirm role titles and responsibilities |
| Influence Assessment | Cross-reference with third-party research, verify budget authority |
| Conflict Analysis | Request failure case analysis, assess stakeholder resistance patterns |
| User Experience Design | Conduct direct user research, verify user needs beyond vendor claims |

### E6. Conclusion Credibility Rating

| Conclusion Type | Credibility Rating | Rating Basis |
|-----------------|--------------------|--------------|
| Category Definition | ★★★★☆ (High) | Standardized categories, clear definitions |
| IT Lead Universality | ★★★☆☆ (Medium-High) | 100% frequency, but reflects vendor contact bias |
| User Role Distribution | ★★★☆☆ (Medium-High) | User roles from customer quotes, but vendor-filtered |
| Role Influence Levels | ★★☆☆☆ (Medium-Low) | Influence from vendor case success stories, no negative cases |
| Industry Role Patterns | ★★★☆☆ (Medium-High) | Patterns observed, but reflects vendor market coverage |
| Co-occurrence Patterns | ★★☆☆☆ (Medium-Low) | Patterns may reflect vendor engagement process, not actual dynamics |

---

## Part F: Notes

### Role Standardization Notes
- "IT Director" and "IS Director" merged into same role
- "Digital Infrastructure Manager" is Education-specific IT Lead naming
- "Student" and "Learner" merged, scale parameter noted separately
- "Guest" covers Hotel Guest and Travel Customer

### Boundary Case Notes
- "Infrastructure Cloud Architect" (Kyndryl) mapped to IT Lead category
- "Wi-Fi Concierge" (Pueblo Bonito) mapped to Operator category
- "External Consultant" (Schnellecke) mapped to User category as system user

### Analysis Limitations
- Source documents are vendor customer success stories, supplier perspective bias present
- All cases are successful deployments, no failure case comparison
- Role distribution reflects vendor market penetration, not random sample

### Recommended Follow-up
- Generate Purchase Factor Model for stakeholder × factor mapping
- Generate Industry Model for industry-specific stakeholder patterns
- Generate OpenSCENARIO preparation models for DSL modeling support

---

*Report Generation Time: [DATE]*
*SKILL Version: scenario_modeler v0.2.0*
*Analysis Framework: Cross-case Inductive Analysis*