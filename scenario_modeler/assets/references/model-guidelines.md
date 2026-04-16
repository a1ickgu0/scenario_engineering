# Model Building Guidelines

## Purpose

This document provides methodological guidance for building synthesis models from multiple scenario_analyzer analysis outputs. It defines principles, processes, and quality criteria for model construction.

---

## Core Principles

### 1. Traceability Principle

**Definition**: Every model conclusion must be traceable to original source documents.

**Requirements**:
- Include source case IDs for every conclusion
- Preserve original wording for key findings
- Document inference method (direct extraction vs inference)
- Note variations and exceptions

### 2. Frequency-Weighted Principle

**Definition**: Model conclusions should reflect frequency-weighted patterns, not isolated cases.

**Requirements**:
- Report frequency counts for each pattern
- Calculate percentages where applicable
- Identify high-frequency patterns (>50% occurrence)
- Identify variant patterns (<20% occurrence)
- Avoid over-generalizing from rare cases

### 3. Semantic Grouping Principle

**Definition**: Group similar elements by semantic meaning, not just literal match.

**Requirements**:
- Use semantic similarity for grouping challenges, conflicts, expectations
- Define grouping criteria explicitly
- Document borderline cases with reasoning
- Preserve original expressions within groups

### 4. Two-Layer Abstraction Principle

**Definition**: Stakeholder model uses two-layer structure: Category Layer (abstract) + Role Layer (concrete).

**Requirements**:
- Map all concrete roles to standard categories
- Maintain category → role hierarchy
- Document boundary cases with reasoning
- Enable cross-industry comparison via categories
- Enable specific instantiation via roles

### 5. Hierarchical Structuring Principle

**Definition**: Purchase factor model uses hierarchical structure: Business Driver → Technical Implementation → Quantified Metrics.

**Requirements**:
- Map each factor to all three levels
- Maintain clear level boundaries
- Enable top-down analysis (driver → implementation)
- Enable bottom-up validation (metrics → implementation → driver)

---

## Model Building Process

### Phase 1: Data Collection

1. Gather all `-analysis.md` documents
2. Validate document completeness (required fields present)
3. Extract metadata (industry, country, company, year)
4. Create document inventory table

### Phase 2: Dimension Extraction

1. Extract industry dimension from metadata
2. Extract stakeholder dimension from listings
3. Extract purchase factor dimension from elements
4. Extract operational dimension from scenarios
5. Build dimension value lists

### Phase 3: Cross-Case Aggregation

1. Group cases by dimension values
2. Count frequency per value
3. Calculate cross-dimension frequencies
4. Identify patterns (high-frequency, cross-cutting)
5. Identify variations (low-frequency, isolated)

### Phase 4: Model Synthesis

1. Build model structure (tables, trees, matrices)
2. Populate with aggregated data
3. Add traceability references
4. Document patterns and variations
5. Generate key insights

### Phase 5: Quality Validation

1. Check traceability completeness
2. Validate frequency calculations
3. Review grouping criteria
4. Verify abstraction mappings
5. Check output format compliance

---

## Quality Criteria

### Criterion 1: Completeness

| Check | Requirement |
|-------|-------------|
| Document Coverage | All input documents are processed |
| Field Coverage | All required fields are extracted |
| Dimension Coverage | All dimensions are analyzed |
| Matrix Coverage | All required matrixes are built |

### Criterion 2: Accuracy

| Check | Requirement |
|-------|-------------|
| Frequency Counts | Accurate counts from source |
| Percentage Calculations | Correct percentage calculations |
| Mapping Accuracy | Correct category/level mappings |
| Traceability Links | Correct source case references |

### Criterion 3: Consistency

| Check | Requirement |
|-------|-------------|
| Classification Consistency | Same classification criteria across documents |
| Naming Consistency | Consistent entity/role naming |
| Format Consistency | Consistent output format |
| Language Consistency | Consistent output language |

### Criterion 4: Validity

| Check | Requirement |
|-------|-------------|
| Pattern Validity | Patterns reflect actual data distribution |
| Inference Validity | Inferences are logically sound |
| Grouping Validity | Semantic groups are meaningful |
| Abstraction Validity | Abstractions capture essential patterns |

---

## Model Types and Required Outputs

| Model Type | Primary Output | Secondary Output | Traceability |
|------------|----------------|------------------|--------------|
| Industry Model | Classification table, Challenge patterns | Regional matrix, Solution preferences | Source cases per conclusion |
| Stakeholder Model | Category definitions, Role catalog | Category-role hierarchy, Co-occurrence | Source cases per role |
| Purchase Factor Model | Driver/Implementation tables | Metric patterns, Industry-priority matrix | Source cases per factor |
| Lifecycle Model | Phase definitions, Transition graph | Action sequences, Trigger patterns | Source cases per phase |
| State Model | State definitions, Transition table | Initial/final mapping | Source cases per state |
| Environment Model | Environment element tables | Constraint patterns | Source cases per element |
| Entity Model | Entity catalogs, Hierarchy trees | Composition trees | Source cases per entity |
| Relationship Model | Relation type tables, Networks | Dependency chains | Source cases per relation |
| Interaction Sequence Model | Sequence catalog, Action patterns | Trigger/condition patterns | Source cases per sequence |
| Parameterization Model | Parameter catalogs, Value distributions | DSL-ready templates | Source cases per value |

---

## Handling Edge Cases

### Case 1: Ambiguous Classification

**Problem**: Element could belong to multiple categories.

**Solution**:
- Document both possible classifications
- Apply primary classification based on context
- Note ambiguity in output
- Preserve reasoning

### Case 2: Missing Required Fields

**Problem**: Source document missing required information.

**Solution**:
- Mark as incomplete in inventory
- Use inference from context where possible
- Note inference vs direct extraction
- Skip in frequency counts for missing fields

### Case 3: Low Sample Count

**Problem**: Insufficient cases for pattern identification (<3 cases).

**Solution**:
- Report as "insufficient data"
- Avoid pattern generalization
- Report individual cases separately
- Note need for more data

### Case 4: Cross-Dimension Anomalies

**Problem**: Pattern contradicts typical cross-dimension expectation.

**Solution**:
- Highlight as anomaly
- Investigate potential causes
- Document case-specific factors
- Note for further investigation

---

## Output Language Guidelines

### Default Language

- Use English for all model outputs, classifications, and technical terms
- Preserve original entity names from source documents (product names, company names)
- Use original wording for traceability references

### Special Cases

- Original product/solution names: Keep as-is from source documents
- Original stakeholder role names: Keep as-is from source documents
- Quantified metrics: Preserve original expressions with normalized format

---

## Version Control

- Update model version when adding new source cases
- Re-validate all patterns when source count changes significantly
- Document version changes in model output
- Archive previous versions for comparison