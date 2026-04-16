# Relationship Model Synthesis Prompt

## Purpose

Synthesize relationship patterns from multiple scenario_analyzer analysis outputs. Build relationship model with hierarchical, collaborative, conflicting, and dependency relations for OpenSCENARIO DSL preparation.

---

## Input Requirements

Provide multiple `-analysis.md` documents with:
- Stakeholder listings (hierarchical and collaborative relations)
- Conflicts and priorities (conflicting relations)
- Operational scenarios (dependency relations)
- Products and solutions (system-entity relations)

---

## Relationship Type Definitions

### Hierarchical Relations

| Relation Type | Definition | Examples |
|---------------|------------|----------|
| Supervision | Superior manages subordinate | CEO → CIO, School Management → IT Team |
| Reporting | Subordinate reports to superior | IT Director → CFO, IT Team → IT Director |
| Authorization | Authority delegation | Board → CEO, CFO → Budget Approval |
| Composition | Entity composed of sub-entities | Organization → Departments → Teams |

### Collaborative Relations

| Relation Type | Definition | Examples |
|---------------|------------|----------|
| Cooperation | Joint work toward common goal | IT Team ↔ Teachers (deployment) |
| Communication | Information exchange | IT Director ↔ Vendor CSM |
| Support | One provides support to another | CSM → IT Team (lifecycle support) |
| Service Delivery | Service provision | Vendor → Organization (product delivery) |

### Conflicting Relations

| Relation Type | Definition | Examples |
|---------------|------------|----------|
| Goal Conflict | Competing objectives | Cost Optimization ↔ Quality Improvement |
| Resource Conflict | Resource allocation disagreement | IT Team ↔ Finance (budget) |
| Priority Conflict | Priority disagreement | Security ↔ Convenience (access policy) |
| Interest Conflict | Stakeholder interest differences | IT Team ↔ Users (change resistance) |

### Dependency Relations

| Relation Type | Definition | Examples |
|---------------|------------|----------|
| Sequential Dependency | B depends on A completion | Deployment → Acceptance |
| Resource Dependency | B requires A's resources | IT Team depends on Budget |
| Information Dependency | B requires A's information | Decision depends on Evaluation results |
| Technical Dependency | B requires A's technical capability | Cloud service depends on Network |
| Integration Dependency | B requires integration with A | New system depends on existing infrastructure |

---

## Analysis Instructions

### Step 1: Hierarchical Relation Extraction

1. Infer supervision relations from stakeholder roles:
   - CEO + CIO appearing together → CEO → CIO (supervision)
   - School Management + IT Team → School Management → IT Team
2. Infer reporting relations from influence levels:
   - High influence roles likely receive reports from lower influence
3. Infer composition relations from organizational descriptions:
   - "67 schools" → Organization composed of 67 School sites
4. Build hierarchical tree per case

### Step 2: Collaborative Relation Extraction

1. Identify stakeholder pairs appearing in same scenario:
   - IT Team + Teachers in "classroom full-class connection" → Cooperation
2. Infer communication relations from scenario descriptions:
   - "Monthly executive management report" → CSM → Management (Communication)
3. Identify support relations from external stakeholder roles:
   - "Customer Success Manager" → Support to IT Team
4. Identify service delivery from product/solution:
   - Vendor provides product → Service Delivery

### Step 3: Conflicting Relation Extraction

1. Extract conflicts from conflict table
2. Identify stakeholder pairs involved in each conflict:
   - "Operations cost vs Innovation needs | IT team, Management" → IT Lead ↔ Decision Maker (Goal Conflict)
3. Classify by conflict type using taxonomy
4. Document resolution pattern per conflict

### Step 4: Dependency Relation Extraction

1. Infer sequential dependencies from lifecycle phases:
   - Evaluation phase → Decision phase → Deployment phase
2. Infer resource dependencies from purchase factors:
   - IT operations depend on Budget approval
3. Infer information dependencies from stakeholder expectations:
   - Decision Maker depends on IT Lead's technical assessment
4. Infer technical dependencies from products/solutions:
   - Wi-Fi APs depend on Network infrastructure
5. Infer integration dependencies from scenario descriptions:
   - New network depends on existing systems (migration)

### Step 5: Relation Frequency Analysis

1. Count frequency of each relation type across documents
2. Build Relation Type × Industry matrix
3. Identify common relations (appearing across industries)
4. Identify industry-specific relations

### Step 6: Relation Pattern Library

1. Identify relation combination patterns:
   - CEO → CIO → IT Director → IT Team (typical IT hierarchy)
   - Decision Maker ↔ IT Lead ↔ Vendor (typical purchase collaboration)
2. Build pattern templates
3. Document pattern frequency and industry context

---

## Output Format

Follow the template: `relationship-model-template.md`

**Required Sections**:

### 1. Hierarchical Relation Table

| From Entity | To Entity | Relation Type | Frequency | Industries | Source Cases |

### 2. Collaborative Relation Table

| Entity Pair | Relation Type | Context | Frequency | Industries | Source Cases |

### 3. Conflicting Relation Table

| Entity Pair | Conflict Type | Resolution | Frequency | Industries | Source Cases |

### 4. Dependency Relation Table

| From Entity | To Entity | Dependency Type | Condition | Source Cases |

### 5. Hierarchical Tree Template

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

### 6. Collaboration Network Template

```
Purchase Decision Network:
├── Decision Maker ↔ IT Lead (Communication: technical assessment)
├── IT Lead ↔ Vendor CSM (Communication: solution proposal)
├── Decision Maker ↔ CFO (Communication: budget approval)
├── IT Lead ↔ IT Team (Cooperation: evaluation support)
└── Vendor ↔ Organization (Service Delivery)
```

### 7. Dependency Chain Template

```
Lifecycle Dependency Chain:
Need Identification
  ↓ [Sequential]
Evaluation
  ↓ [Information: technical assessment]
Decision
  ↓ [Resource: budget]
Deployment
  ↓ [Technical: infrastructure]
Acceptance
  ↓ [Sequential]
Operations
```

### 8. Relation × Industry Matrix

| Relation Type | Education | Healthcare | Hospitality | Manufacturing |

---

## Traceability Requirements

For each relation entry, include:
- Source Cases: Case IDs where this relation appears
- Original Context: Original stakeholder or scenario description
- Inference Method: Direct extraction vs inferred from context

---

## Quality Checklist

- [ ] All four relation types are extracted
- [ ] Hierarchical trees are built per case
- [ ] Collaboration networks are identified
- [ ] Conflicts are classified by type
- [ ] Dependency chains are documented
- [ ] Relation patterns are identified

---

## Example Usage

```
Relation extraction example:
Original: "Digital Infrastructure Manager + IT Service Desk + 100% reduction in fault tickets"
→ Hierarchical: Digital Infrastructure Manager → IT Service Desk (Supervision)
→ Collaborative: IT Service Desk ↔ Students (Support: network troubleshooting)
→ Dependency: IT Service Desk depends on Network stability

Original: "Operations cost vs Innovation needs | IT team, Management"
→ Conflicting: IT Lead ↔ Decision Maker (Goal Conflict: Cost vs Innovation)
→ Resolution: Prioritize AIOps (automated operations)

Original: "Deployment → Acceptance → Operations"
→ Sequential Dependency: Deployment → Acceptance → Operations
→ Technical Dependency: Acceptance depends on Deployment completion
```