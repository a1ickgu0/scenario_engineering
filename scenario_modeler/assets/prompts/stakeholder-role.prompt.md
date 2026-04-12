# Stakeholder Role Synthesis Prompt

## Purpose

Extract and synthesize concrete stakeholder roles from multiple scenario_engine analysis outputs. Build a comprehensive role catalog with attributes, industry context, and category mappings.

---

## Input Requirements

Provide multiple `-analysis.md` documents with stakeholder listing sections containing:
- Stakeholder name/role
- Type
- Role description
- Expectations/needs
- Influence level
- Value/risk
- Priority
- Traceability reference

---

## Role Extraction Rules

### Role Naming Convention

1. **Preserve original names**: Use exact role names from source documents
   - Example: "Digital Infrastructure Manager (Pilbeam-Cornfield)" → Keep full name
2. **Standardize user groups**: Group similar user roles with scale notation
   - Example: "26,500 students", "31,000 learners", "students" → "Student (learner group, scale varies)"
3. **Normalize titles**: Standardize executive titles
   - Example: "Director Information Systems", "IS Director" → "IT Director / IS Director"
4. **Preserve external roles**: Keep external partner roles with company context
   - Example: "Customer Success Manager (HPE Aruba)"

### Role Attributes to Extract

| Attribute | Source Field | Extraction Method |
|-----------|--------------|-------------------|
| Role Name | Stakeholder field | Direct extraction |
| Type | Type field | Direct extraction |
| Role Description | Role field | Direct extraction |
| Category | - | Map to standard category |
| Expectations | Expectations/needs field | Direct extraction, preserve wording |
| Influence | Influence field | Normalize: high/medium-high/medium/low |
| Value/Risk | Value/risk field | Direct extraction |
| Priority | Priority field | Normalize: high/medium-high/medium/low |
| Industries | - | From document metadata |
| Source Cases | - | From document filename |

---

## Analysis Instructions

### Step 1: Role Catalog Building

1. Extract all unique role names from all documents
2. Apply naming normalization rules
3. Create master role list with all attributes
4. Count frequency per unique role

### Step 2: Role Attribute Synthesis

1. For each unique role, aggregate expectations across all appearances
2. Identify common expectations (appear in >50% of role appearances)
3. Identify variant expectations (appear in <50% of role appearances)
4. Synthesize typical influence level per role
5. Synthesize typical value/risk pattern per role

### Step 3: Role × Industry Matrix

1. List all unique roles
2. Map each role to industries where it appears
3. Count frequency per industry
4. Identify industry-specific roles (appear in only one industry)
5. Identify cross-industry roles (appear in multiple industries)

### Step 4: Role × Category Mapping

1. Map each role to its category (use stakeholder-category prompt)
2. Build Category → Role hierarchy tree
3. Identify typical roles per category
4. Identify variant roles per category

### Step 5: Role Relationship Patterns

1. Identify roles that frequently appear together in same document
2. Identify roles with conflicting expectations
3. Identify roles with collaborative relationships
4. Build co-occurrence matrix

---

## Output Format

Follow the template: `stakeholder-role-template.md`

**Required Sections**:

### 1. Master Role Catalog

| Role Name | Category | Type | Frequency | Industries |

### 2. Role Detailed Attributes

For each role, provide:

| Role | Expectations (Typical) | Expectations (Variant) | Influence | Value/Risk | Source Cases |

### 3. Category → Role Hierarchy

```
Decision Maker
├── CEO
├── CIO
├── CFO
├── Board Member
├── Municipal Decision Layer
├── NHS Management
└── School Management

IT Lead
├── Digital Infrastructure Manager
├── IT Director / IS Director
├── Healthcare IT Lead
└── IT Operations Team Lead

User
├── Student (scale noted)
├── Teacher/Educator
├── Doctor
├── Nurse
├── Patient
├── Employee
├── Retail Customer
└── Hotel Guest
```

### 4. Role × Industry Matrix

| Role | Education | Healthcare | Hospitality | Manufacturing | ITServices |

### 5. Role Co-occurrence Patterns

| Role Pair | Frequency | Industries | Relationship Type | Typical Conflict/Collaboration |

---

## Traceability Requirements

For each role entry, include:
- Source Cases: All case IDs where this role appears
- Frequency: Total appearance count
- Original Expectations: Preserve key wording from source

---

## Quality Checklist

- [ ] All roles from source documents are extracted
- [ ] Role names are normalized but traceable to original
- [ ] Each role is mapped to a category
- [ ] Influence levels are normalized
- [ ] Expectations preserve original wording
- [ ] Industry × Role matrix is complete
- [ ] Co-occurrence patterns are identified

---

## Example Usage

```
Role extraction example:
Original: "Digital Infrastructure Manager (Pilbeam-Cornfield)"
→ Role Name: Digital Infrastructure Manager
→ Category: IT Lead
→ Industry: Education
→ Influence: high
→ Expectation: "Simplified operations, AIOps support, innovation focus"
→ Source: Education-UK-06-Aberdeen

Role frequency:
- IT Director: appears 15 times, across Education/Healthcare/Manufacturing
- Teacher: appears 8 times, only Education industry
- CEO: appears 3 times, across Manufacturing/ITServices
```