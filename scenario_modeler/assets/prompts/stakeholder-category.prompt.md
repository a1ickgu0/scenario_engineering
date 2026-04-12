# Stakeholder Category Synthesis Prompt

## Purpose

Abstract stakeholder category classifications from multiple scenario_engine analysis outputs. Define standard category types with clear boundaries and traits for cross-industry comparison.

---

## Input Requirements

Provide multiple `-analysis.md` documents with stakeholder listing sections.

---

## Category Definitions

Use the following standard categories:

| Category | Definition | Typical Traits |
|----------|------------|----------------|
| Decision Maker | Final decision authority or budget approval | High influence, strategic view, ROI focus |
| IT Lead | Technical architecture and operations lead | High influence, technical view, feasibility focus |
| Operator | Daily operations and execution | Medium-high influence, execution view, efficiency focus |
| User | Direct system users | Medium influence, experience view, usability focus |
| Regulator | Policy, compliance, industry oversight | High constraint, compliance view, risk focus |
| Partner | External support and service providers | Medium influence, service view, collaboration focus |

---

## Analysis Instructions

### Step 1: Role Extraction

1. Extract all unique stakeholder roles from the stakeholder listing table
2. Preserve original role names (e.g., "Digital Infrastructure Manager", "CEO", "26,500 students")
3. Note influence level and priority from each document

### Step 2: Role-to-Category Mapping

1. Map each extracted role to one of the 6 standard categories
2. Use the following mapping rules:
   - **Decision Maker**: Roles with budget/decision authority (CEO, CIO, CFO, Board, Municipal leadership, NHS management, School management)
   - **IT Lead**: Technical architecture roles (IT Director, Digital Infrastructure Manager, IT Operations Team Lead, Healthcare IT Lead)
   - **Operator**: Daily execution roles (IT Operations Team, Network Operations Management, IT Service Desk)
   - **User**: Direct usage roles (Teacher, Student, Doctor, Nurse, Patient, Employee, Customer, Guest)
   - **Regulator**: External constraint roles (Municipal decision layer, National policy, HIPAA compliance, Environmental requirements)
   - **Partner**: External support roles (Customer Success Manager, ASM support team, System integrator, Supplier)

### Step 3: Category Frequency Analysis

1. Count occurrence frequency per category across all documents
2. Calculate category distribution per industry
3. Identify dominant categories per industry
4. Identify category combinations commonly appearing together

### Step 4: Category Traits Extraction

1. Extract typical expectations per category from source documents
2. Identify typical influence levels per category
3. Identify typical value/risk patterns per category
4. Identify typical participation phases per category

### Step 5: Boundary Clarification

1. Identify roles that could belong to multiple categories
2. Define clear boundary rules for ambiguous cases:
   - IT Director with budget authority → Decision Maker (if budget decision) or IT Lead (if technical focus)
   - Teacher with technical responsibility → User (if teaching focus) or Operator (if system operation)
3. Document reasoning for boundary decisions

---

## Output Format

Follow the template: `stakeholder-category-template.md`

**Required Sections**:

### 1. Category Definition Table

| Category | Definition | Traits | Frequency |

### 2. Category × Industry Distribution

| Industry | Decision Maker | IT Lead | Operator | User | Regulator | Partner |

### 3. Category Typical Expectations

| Category | Typical Expectations | Typical Quote | Source Cases |

### 4. Category Typical Participation Phases

| Category | Typical Phases | Typical Actions | Source Cases |

### 5. Boundary Clarification Cases

| Ambiguous Role | Possible Categories | Assigned Category | Reasoning | Source Cases |

---

## Traceability Requirements

For each category conclusion, include:
- Source Cases: List case IDs where this pattern appears
- Frequency: Occurrence count across documents
- Typical Quote: Original expectation wording

---

## Quality Checklist

- [ ] All extracted roles are mapped to a category
- [ ] Category definitions are consistent across all analyses
- [ ] Boundary cases are documented with reasoning
- [ ] Frequency counts are accurate
- [ ] Typical expectations are preserved from original wording

---

## Example Usage

```
Role list extracted:
- Digital Infrastructure Manager → IT Lead
- 26,500 students → User
- Municipal decision layer → Regulator
- Customer Success Manager (HPE) → Partner

Output:
- IT Lead appears in Education industry at 70% frequency
- User appears in all industries with highest frequency
- Decision Maker and IT Lead frequently co-appear (collaborative decision)
```