# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## SKILL Overview

This is the **scenario_engine** SKILL - an INCOSE requirements engineering workflow for extracting stakeholder information, operational concepts, and product/solution details from vendor customer story PDFs or text narratives. Outputs are structured for OpenSCENARIO DSL preparation via the downstream `scenario_modeler` SKILL.

## Directory Structure

```
scenario_engine/
├── SKILL.md                              # SKILL metadata (YAML frontmatter + definition)
├── README.md                             # English documentation
├── README_zh.md                          # Chinese documentation
├── assets/
│   ├── prompts/
│   │   └── customer-story-analysis.prompt.md   # Core analysis prompt template
│   └── references/
│       └── analysis-guidelines.md              # INCOSE analysis guidelines
└── tests/
    ├── docs/                             # Source PDF documents (customer stories)
    ├── tmp/                              # Extracted text files
    └── result/                           # Analysis output files (.md)
```

## PDF Processing Commands

When analyzing PDF customer stories, extract text first:

```bash
# Preserve layout (recommended)
pdftotext -layout input.pdf output.txt

# Specify page range
pdftotext -f 1 -l 10 input.pdf output.txt

# Python PDFMiner approach
pdf2txt.py -o output.txt input.pdf
```

After extraction, clean headers/footers and validate text completeness before analysis.

## Analysis Output Structure

All analyses must follow this structured table format (12 sections):

### Core Sections (0-3)
- **0. Customer Basic Information**: title, country, industry, company, year, initial/final states
- **1. Purchase Elements**: 3-5 business factors ranked by importance with parameterized metrics
- **2. Stakeholder List**: role, type, expectations, influence, benefits/risks, relationship types, priority
- **3. Conflicts and Priority**: conflict points, stakeholders, root cause, recommendations

### OpenSCENARIO Preparation Sections (4-7, 11)
- **4. State Model**: Stakeholder/System/Organization states with transition triggers and paths
- **5. Environment Model**: Industry/Regional/Organizational/Technical environment constraints
- **6. Entity Model**: Organization hierarchy tree, System composition tree, External connections
- **7. Lifecycle Phases**: Phase sequence with triggers, actions, completion criteria
- **11. Parameterization Model**: Metric, Role attribute, Scenario, Constraint parameters

### Supporting Sections (8-10, 12)
- **8. Operational Scenarios**: scenarios with trigger conditions, execution conditions, state transitions
- **9. Engagement and Commitment**: participation stages, evaluation focus
- **10. Products and Solutions**: entity hierarchy mapping
- **12. Traceability and Notes**: original references, inference notes

## Traceability Requirements

Every analysis point must include original text references:

- Page reference: `Page 3, paragraph 2: "..."`
- Section marker: `Section 2.1: Customer Challenges`
- Direct quote with context

Inferred conclusions must note the inference source and original text basis.

## Output Language

Use the local language of the source document. Default to Chinese if the language cannot be determined.

## State Model Definitions

### Stakeholder States
- Need Identified → Evaluating → Decision Ready → Decided → Expecting → Accepting → Satisfied/Dissatisfied

### System States
- Not Deployed → Deploying → Deployed → Running → Upgrading / Degraded → Fault → Recovering

### Organization States
- Problem Identified → Solution Seeking → Procurement → Implementation → Validation → Normal Operation

## Environment Dimensions

| Dimension | Examples |
|-----------|----------|
| Industry Environment | HIPAA, GDPR, FERPA, ISO 27001, 1:1 device mandate |
| Regional Environment | National regulations, cultural traits, market maturity |
| Organizational Environment | Scale, architecture type (Centralized/Distributed), budget constraints |
| Technical Environment | Existing tech stack, integration constraints, vendor relationships |

## Entity Types

- **Organization**: Company → Department → Team → Role → Site → User Group
- **System**: Solution → Product → Platform → Service → Component
- **External**: Supplier → Regulator → Partner

## Relationship Types

| Type | Definition |
|------|------------|
| Hierarchical | 上级-下级, 管理关系 |
| Collaborative | 联合参与, 合作关系 |
| Conflicting | 冲突, 竞争关系 |
| Dependency | 前后依赖, 支撑关系 |

## Lifecycle Phases

| Phase | Trigger | Completion Criteria |
|-------|---------|---------------------|
| Need Identification | Problem discovery | Requirements documented |
| Evaluation | Requirements documented | Evaluation report complete |
| Decision | Evaluation complete | Contract signed |
| Deployment | Contract signed | System available |
| Acceptance | System available | Acceptance report passed |
| Operations | Acceptance passed | Continuous stable operation |

## Parameterization Format

```
param_name: {type: metric/role_attribute/scenario/constraint, value: X, unit: Y}
```

Examples:
- `fault_ticket_reduction: {type: metric, value: 100, unit: %}`
- `influence_level: {type: role_attribute, value: high}`
- `user_count: {type: scenario, value: 26500, unit: users}`
- `compliance: {type: constraint, value: [HIPAA, GDPR]}`

## Branch Conventions

- `main` - Production stable version
- `dev` - Development branch

## Commit Message Format

```
feat: Add feature description
fix: Fix bug description
docs: Documentation update
refactor: Code refactor description
test: Test-related description
chore: Misc changes description
```