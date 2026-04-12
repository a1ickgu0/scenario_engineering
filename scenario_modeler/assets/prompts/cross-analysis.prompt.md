# Cross-Analysis Matrix Prompt

## Purpose

Generate cross-dimension analysis matrixes to identify patterns and relationships between Industry, Stakeholder (Category/Role), and Purchase Factor dimensions.

---

## Input Requirements

Provide synthesized outputs from:
- Industry Model (industry-synthesis)
- Stakeholder Category Model (stakeholder-category)
- Stakeholder Role Model (stakeholder-role)
- Purchase Factor Model (purchase-factor)

---

## Matrix Types

### Matrix 1: Industry × Stakeholder Category

**Purpose**: Identify which stakeholder categories are more common in which industries.

| Dimension | Rows | Columns | Cell Value |
|-----------|------|---------|------------|
| Industry × Category | Industries | 6 Categories | Frequency count / Percentage |

**Analysis Focus**:
- Dominant categories per industry (highest frequency)
- Category absence patterns (categories not appearing in certain industries)
- Cross-industry common categories (appearing in all industries)

### Matrix 2: Industry × Stakeholder Role

**Purpose**: Identify which specific roles appear in which industries.

| Dimension | Rows | Columns | Cell Value |
|-----------|------|---------|------------|
| Industry × Role | Industries | Role List | Presence count / Frequency |

**Analysis Focus**:
- Industry-specific roles (appearing only in one industry)
- Cross-industry roles (appearing in multiple industries)
- Role concentration per industry

### Matrix 3: Industry × Business Driver

**Purpose**: Identify which purchase motivations have higher priority in which industries.

| Dimension | Rows | Columns | Cell Value |
|-----------|------|---------|------------|
| Industry × Driver | Industries | 6 Business Drivers | Priority ranking / Frequency |

**Analysis Focus**:
- Primary driver per industry (highest priority)
- Driver ranking variations across industries
- Industry-specific driver patterns

### Matrix 4: Stakeholder Category × Business Driver

**Purpose**: Identify which stakeholder categories care about which purchase motivations.

| Dimension | Rows | Columns | Cell Value |
|-----------|------|---------|------------|
| Category × Driver | 6 Categories | 6 Business Drivers | Association strength |

**Analysis Focus**:
- Category-driver alignment (which categories prioritize which drivers)
- Category expectation patterns
- Driver influence by stakeholder type

### Matrix 5: Stakeholder Role × Business Driver

**Purpose**: Identify which specific roles care about which purchase motivations.

| Dimension | Rows | Columns | Cell Value |
|-----------|------|---------|------------|
| Role × Driver | Role List | 6 Business Drivers | Expectation frequency |

**Analysis Focus**:
- Role-specific expectations (which drivers each role emphasizes)
- Role-driver patterns within same category
- Role expectation variations across industries

### Matrix 6: Stakeholder Category × Conflict

**Purpose**: Identify which stakeholder categories are involved in which conflict types.

| Dimension | Rows | Columns | Cell Value |
|-----------|------|---------|------------|
| Category × Conflict | 6 Categories | Conflict Types | Involvement frequency |

**Analysis Focus**:
- Categories frequently in conflict
- Conflict patterns between category pairs
- Resolution patterns per category

---

## Analysis Instructions

### Step 1: Data Preparation

1. Compile industry list from Industry Model
2. Compile stakeholder categories and roles from Stakeholder Model
3. Compile business drivers from Purchase Factor Model
4. Compile conflict patterns from source documents

### Step 2: Matrix Construction

For each matrix type:

1. **Initialize matrix structure**: Create empty matrix with row/column headers
2. **Populate cell values**: Count occurrences/frequency for each cell
3. **Calculate percentages**: Normalize counts to percentages where applicable
4. **Add traceability**: Note source cases for significant patterns

### Step 3: Pattern Identification

For each matrix:

1. **Identify high-frequency cells**: Values > threshold (e.g., >50%)
2. **Identify zero-value cells**: Patterns not appearing
3. **Identify correlation patterns**: Rows with similar column distributions
4. **Identify outlier patterns**: Cells significantly different from row/column averages

### Step 4: Insight Generation

For each significant pattern, generate:

1. **Pattern Description**: What the pattern shows
2. **Interpretation**: Why this pattern might exist
3. **Business Implication**: How this affects decision-making
4. **Traceability**: Source cases supporting the pattern

---

## Output Format

Follow the template: `cross-analysis-template.md`

**Required Sections**:

### 1. Industry × Stakeholder Category Matrix

| Industry | Decision Maker | IT Lead | Operator | User | Regulator | Partner | Dominant Category |

### 2. Industry × Stakeholder Role Matrix (Top 20 Roles)

| Role | Education | Healthcare | Hospitality | Manufacturing | ITServices | Logistics | Retail |

### 3. Industry × Business Driver Matrix

| Industry | Cost | Efficiency | Security | Experience | Innovation | Sustainability | Primary Driver |

### 4. Stakeholder Category × Business Driver Matrix

| Category | Cost | Efficiency | Security | Experience | Innovation | Sustainability |

### 5. Stakeholder Role × Business Driver Matrix (Top Roles)

| Role | Primary Drivers | Secondary Drivers | Source Cases |

### 6. Stakeholder Category × Conflict Matrix

| Category | Cost vs Quality | Security vs Convenience | Innovation vs Stability |

### 7. Key Insights

For each significant pattern:

| Pattern | Matrix | Description | Interpretation | Business Implication | Source Cases |

---

## Traceability Requirements

For each matrix cell with significant value, include:
- Source Cases: Case IDs contributing to this cell value
- Frequency: Count and percentage
- Example: Representative case example

---

## Quality Checklist

- [ ] All 6 matrix types are constructed
- [ ] Cell values are accurate and normalized
- [ ] Dominant patterns are identified per matrix
- [ ] Key insights have interpretations and implications
- [ ] Traceability references are complete

---

## Example Usage

```
Matrix example: Industry × Stakeholder Category

| Industry | Decision Maker | IT Lead | Operator | User | Regulator | Partner |
|----------|----------------|---------|----------|------|-----------|---------|
| Education | 70% | 80% | 40% | 100% | 30% | 20% |
| Healthcare | 60% | 70% | 50% | 90% | 80% | 30% |
| Hospitality | 50% | 60% | 60% | 100% | 20% | 40% |

Insight:
- User appears at 90%+ across all industries (universal role)
- Regulator highest in Healthcare (80%), related to medical compliance requirements
- Partner higher in Hospitality (40%), related to external managed services
```