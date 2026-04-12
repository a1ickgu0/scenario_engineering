# Category-Role Mapping Reference

## Purpose

This document provides standard mapping rules for classifying concrete stakeholder roles into abstract categories. It serves as a reference for stakeholder model synthesis.

---

## Standard Categories

| Category | Definition | Typical Traits |
|----------|------------|----------------|
| Decision Maker | Final decision authority or budget approval | High influence, strategic view, ROI focus |
| IT Lead | Technical architecture and operations lead | High influence, technical view, feasibility focus |
| Operator | Daily operations and execution | Medium-high influence, execution view, efficiency focus |
| User | Direct system users | Medium influence, experience view, usability focus |
| Regulator | Policy, compliance, industry oversight | High constraint, compliance view, risk focus |
| Partner | External support and service providers | Medium influence, service view, collaboration focus |

---

## Role-to-Category Mapping Rules

### Decision Maker Roles

| Concrete Role | Context Indicators | Mapping Reasoning |
|---------------|--------------------|--------------------|
| CEO | Executive title, final authority | Highest-level decision authority |
| CIO | Executive IT title | IT strategy + budget authority |
| CFO | Executive finance title | Budget approval authority |
| Board Member | Governance role | Strategic oversight + approval |
| Municipal Decision Layer | Government context | Public sector decision authority |
| NHS Management | Healthcare context | Healthcare governance authority |
| School Management | Education context | School-level decision authority |
| Director (non-IT) | Department leadership | Department-level authority |

### IT Lead Roles

| Concrete Role | Context Indicators | Mapping Reasoning |
|---------------|--------------------|--------------------|
| Digital Infrastructure Manager | Infrastructure focus | Technical architecture lead |
| IT Director | IT leadership title | IT operations authority |
| IS Director | IS leadership title | Information systems authority |
| Healthcare IT Lead | Healthcare context | Healthcare-specific IT lead |
| IT Operations Team Lead | Operations leadership | Operations management |
| Network Manager | Network focus | Network infrastructure lead |
| Security Lead | Security focus | Security architecture lead |

### Operator Roles

| Concrete Role | Context Indicators | Mapping Reasoning |
|---------------|--------------------|--------------------|
| IT Operations Team | Operations execution | Daily IT operations |
| IT Service Desk | Support function | Incident handling |
| Network Admin | Network execution | Network configuration |
| Security Operations | Security execution | Security monitoring |
| System Admin | System execution | System maintenance |
| IT Team (general) | General IT execution | General IT operations |

### User Roles

| Concrete Role | Context Indicators | Mapping Reasoning |
|---------------|--------------------|--------------------|
| Teacher | Education context | Direct system usage (teaching) |
| Educator | Education context | Direct system usage |
| Student (group) | Education context, scale noted | Primary user group |
| Doctor | Healthcare context | Clinical system usage |
| Nurse | Healthcare context | Clinical system usage |
| Patient | Healthcare context | Healthcare service user |
| Employee (general) | Workplace context | Workplace system user |
| Office Staff | Office context | Office system user |
| Retail Customer | Retail context | Retail service user |
| Hotel Guest | Hospitality context | Hospitality service user |
| Learner | Education/training context | Learning platform user |
| Researcher | Research context | Research system user |
| Fan/Attendee | Sports/Entertainment context | Event service user |

### Regulator Roles

| Concrete Role | Context Indicators | Mapping Reasoning |
|---------------|--------------------|--------------------|
| Government Agency | Policy context | Regulatory authority |
| Municipal Government | Local policy | Local regulatory authority |
| NHS Foundation Trust | Healthcare governance | Healthcare regulatory body |
| Ministry of Education | Education policy | Education regulatory authority |
| Compliance Officer | Compliance focus | Compliance oversight |
| Environmental Agency | Sustainability context | Environmental regulatory |
| Data Protection Authority | Privacy context | Data regulatory authority |

### Partner Roles

| Concrete Role | Context Indicators | Mapping Reasoning |
|---------------|--------------------|--------------------|
| Customer Success Manager | Vendor-provided | Lifecycle support provider |
| ASM Support Team | Vendor-provided | Managed service provider |
| System Integrator | Integration role | Integration partner |
| Vendor Technical Support | Vendor-provided | Technical support provider |
| Managed Service Provider | External operations | Operations outsourcing |
| Consultant | Advisory role | Advisory partner |
| Channel Partner | Sales role | Sales/distribution partner |

---

## Ambiguous Cases and Resolution Rules

### Case 1: IT Director with Budget Authority

**Ambiguity**: Could be Decision Maker (budget) or IT Lead (technical).

**Resolution Rule**: 
- If role emphasizes budget approval → Decision Maker
- If role emphasizes technical architecture → IT Lead
- If both equally emphasized → Decision Maker (higher authority)
- Document ambiguity in output

### Case 2: Teacher with Technical Role

**Ambiguity**: Teacher could be User (teaching) or Operator (if managing systems).

**Resolution Rule**:
- Primary teaching role → User
- Additional system management → note as dual role
- System management as primary → Operator
- Document dual role cases

### Case 3: CSM with Decision Influence

**Ambiguity**: External role but may influence decisions.

**Resolution Rule**:
- Always Partner (external)
- Note influence level separately
- Document decision influence in relationship model
- Do not reclassify as Decision Maker

### Case 4: Internal Consultant

**Ambiguity**: Could be Operator (if IT team) or Partner (if external).

**Resolution Rule**:
- If employed by organization → Operator (or IT Lead if senior)
- If employed by external firm → Partner
- Document employment context

---

## Mapping Validation Checklist

- [ ] All roles from source documents are mapped
- [ ] Each role maps to exactly one category
- [ ] Ambiguous cases are documented with reasoning
- [ ] Category definitions are applied consistently
- [ ] Industry-specific role variations are noted

---

## Category → Role Hierarchy Template

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
├── Teacher/Educator
├── Student (scale noted)
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