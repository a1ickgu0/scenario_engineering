# Scenario Modeler SKILL

## Overview

The `scenario_modeler` SKILL synthesizes and abstracts structured models from multiple `scenario_engine` analysis outputs. It transforms individual case-level analyses into cross-case归纳 models that reveal patterns across industries, stakeholders, and purchase decisions.

This SKILL prepares structured inputs for OpenSCENARIO DSL modeling by providing lifecycle, state, environment, entity, relationship, and parameterization models.

## Key Capabilities

### 1. Industry Model Synthesis
- Industry classification and taxonomy
- Regional distribution patterns
- Typical challenges and pain points per industry
- Stakeholder role distributions
- Solution preference patterns

### 2. Stakeholder Model (Two-Layer Structure)

| Layer | Description |
|-------|-------------|
| Category Layer | Abstract classifications: Decision Maker, IT Lead, Operator, User, Regulator, Partner |
| Role Layer | Concrete roles extracted from cases: CEO, CIO, IT Director, Teacher, Student, etc. |
| Mapping | Category → Role relationships with frequency and industry context |

### 3. Purchase Factor Model (Hierarchical)

| Level | Content |
|-------|---------|
| Business Driver Layer | Why buy: Cost optimization, efficiency, security, experience, innovation, sustainability |
| Technical Implementation Layer | What to buy: AI-native ops, zero-trust, Wi-Fi, cloud mgmt, SD-WAN, NaaS |
| Quantified Metrics Layer | How to measure: Reduction rate, increase rate, time savings, coverage scale |

### 4. Supporting Models for OpenSCENARIO

| Model | Purpose |
|-------|---------|
| Lifecycle Model | Scenario phases with triggers, actions, completion criteria |
| State Model | Stakeholder/system/organization states and transitions |
| Environment Model | Industry constraints, regional characteristics, organizational context |
| Entity Model | Organizations, systems, external entities with attributes |
| Relationship Model | Hierarchical, collaborative, conflicting, dependency relations |
| Interaction Sequence Model | Actor-to-actor action flows |
| Parameterization Model | Configurable parameters for metrics, roles, scenarios |

## Input Requirements

**Source**: Multiple `-analysis.md` files from `scenario_engine` SKILL

**Required Fields**:
- Customer basic information (industry, country, company, year)
- Purchase elements (ranked with business value and metrics)
- Stakeholder listing (roles, expectations, influence, value/risk)
- Conflicts and priorities
- Operational scenarios
- Products and solutions

## Output Products

### Primary Outputs
1. **Industry Model**: Industry patterns, challenges, stakeholder distributions
2. **Stakeholder Model**: Category layer + Role layer with mappings
3. **Purchase Factor Model**: Hierarchical structure with quantification

### Supporting Outputs
4. **Lifecycle Model**: Phase sequence with triggers and actions
5. **State Model**: State definitions and transition conditions
6. **Environment Model**: Contextual constraints per dimension
7. **Entity Model**: Organization, system, external entity definitions
8. **Relationship Model**: Relation types and patterns
9. **Interaction Sequence Model**: Actor action flows
10. **Parameterization Model**: Configurable parameter definitions

### Cross-Analysis Matrixes
- Industry × Role matrix
- Industry × Purchase Factor matrix
- Role × Purchase Factor matrix
- Role × Conflict matrix

## Usage

### Invocation
Reference keywords like:
- "synthesize models from multiple analyses"
- "industry pattern extraction"
- "stakeholder model abstraction"
- "purchase factor synthesis"
- "prepare for OpenSCENARIO modeling"

### Example Workflow

1. Gather multiple `-analysis.md` documents (e.g., 30+ cases)
2. Parse structured fields from each document
3. Extract dimensions: industry, stakeholders, purchase factors
4. Aggregate patterns across documents with frequency counting
5. Generate synthesis models with traceability references
6. Build cross-dimension analysis matrixes
7. Format outputs using defined templates

## Directory Structure

```
scenario_modeler/
├── SKILL.md                          # Core definition
├── README.md                         # English documentation (this file)
├── README_zh.md                      # Chinese documentation
└── assets/
    ├── prompts/                      # Analysis prompts (17 files)
    │   ├── industry-synthesis.prompt.md
    │   ├── stakeholder-category.prompt.md
    │   ├── stakeholder-role.prompt.md
    │   ├── purchase-factor.prompt.md
    │   ├── cross-analysis.prompt.md
    │   ├── conflict-pattern.prompt.md
    │   ├── solution-preference.prompt.md
    │   ├── lifecycle-model.prompt.md
    │   ├── state-model.prompt.md
    │   ├── environment-model.prompt.md
    │   ├── entity-model.prompt.md
    │   ├── relationship-model.prompt.md
    │   ├── interaction-sequence.prompt.md
    │   └── parameterization.prompt.md
    ├── references/                   # Reference guides (10 files)
    │   ├── model-guidelines.md
    │   ├── category-role-mapping.md
    │   ├── industry-taxonomy.md
    │   ├── metric-taxonomy.md
    │   ├── state-definition.md
    │   ├── environment-taxonomy.md
    │   ├── entity-taxonomy.md
    │   ├── relationship-types.md
    │   └── openscenario-mapping.md
    └── templates/                    # Output templates (14 files)
        ├── industry-model-template.md
        ├── stakeholder-category-template.md
        ├── stakeholder-role-template.md
        ├── purchase-factor-template.md
        ├── cross-analysis-template.md
        ├── conflict-pattern-template.md
        ├── solution-preference-template.md
        ├── lifecycle-model-template.md
        ├── state-model-template.md
        ├── environment-model-template.md
        ├── entity-model-template.md
        ├── relationship-model-template.md
        ├── interaction-sequence-template.md
        └── parameterization-template.md
```

## Traceability

Each model conclusion includes:
- **Source Cases**: List of contributing case IDs
- **Frequency/Weight**: Pattern occurrence rate (e.g., "80% of Education cases")
- **Typical Quotes**: Key original wording preserved
- **Variations**: Exceptions across cases

## Output Language

- **Chinese (Default)**: For Chinese documentation and users
- **English**: For international documentation
- **Bilingual Tables**: Key tables include both languages

## Related SKILLs

- **scenario_engine**: Source SKILL that generates individual case analyses
- **pattern_modeler**: (deprecated) Original name, renamed to scenario_modeler

## Version History

- **0.1.0** (2026-04-11): Initial draft with OpenSCENARIO preparation support