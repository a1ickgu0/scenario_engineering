# Confidence Level Framework for Inferred Information

## Purpose

This framework establishes confidence level standards and requirements for all inferred information in scenario_modeler analysis. It ensures transparency, traceability, and credibility of all conclusions and deductions.

---

## Confidence Level Definition

### Level 1: High Confidence (高置信度)

**Definition**: Information directly stated in source documents or strongly supported by multiple independent sources.

**Criteria**:
- **Direct Evidence**: Explicit statement in source document
- **Multiple Citations**: Mentioned in multiple source cases
- **Quantified Support**: Supported by specific numbers/metrics
- **Cross-Validation**: Consistent across multiple independent sources
- **Explicit Attribution**: Source clearly identifies responsible stakeholder

**Example**:
```
Original: "CIO has budget approval authority up to $5M" (Page 5, Line 23)
Confidence: HIGH
Basis: Explicit statement with specific quantitative authority amount
```

**Confidence Symbol**: ★★★★★

---

### Level 2: Medium Confidence (中置信度)

**Definition**: Information inferred from context, industry knowledge, or partial evidence.

**Criteria**:
- **Contextual Inference**: Reasonably deduced from surrounding context
- **Industry Standard**: Typical for industry based on common practices
- **Partial Evidence**: Some evidence but not conclusive
- **Single Citation**: Only mentioned in one source or one case
- **Expert Judgment**: Requires domain knowledge or interpretation

**Example**:
```
Original: "IT team manages network infrastructure" (Page 3, Line 15)
Inference: Network Administrator role exists
Confidence: MEDIUM
Basis: Infrastructure management implies network admin role, but role title not explicitly mentioned
```

**Confidence Symbol**: ★★★☆☆

---

### Level 3: Low Confidence (低置信度)

**Definition**: Information based on speculation, weak evidence, or significant assumptions.

**Criteria**:
- **Speculative**: Requires significant assumptions
- **Weak Evidence**: Limited or contradictory evidence
- **Ambiguous**: Source information is unclear or conflicting
- **Extrapolation**: Extended far beyond available evidence
- **Lack of Context**: Insufficient context to make reliable inference

**Example**:
```
Original: "IT department structured with multiple teams" (Page 7, Line 45)
Inference: Specific team composition (network, security, support)
Confidence: LOW
Basis: Team structure mentioned but no details on specific teams
```

**Confidence Symbol**: ★★☆☆☆

---

## Confidence Basis Categories

### Basis 1: Explicit Statement (原文明确陈述)

**Definition**: Information directly stated in source document.

**Confidence**: HIGH

**Requirements**:
- Direct quote or paraphrase from source
- No interpretation required
- Clear attribution of source
- Page/line reference provided

**Example**:
```
Information: CIO has budget approval authority
Basis: Explicit Statement
Source: Page 5, Line 23: "CIO has budget approval authority up to $5M"
Confidence: HIGH ★★★★★
```

---

### Basis 2: Direct Citation (直接引用)

**Definition**: Information quoted directly from stakeholder interview or case document.

**Confidence**: HIGH

**Requirements**:
- Verbatim or near-verbatim quote
- Attributed to specific stakeholder
- Context preserved
- Bilingual translation if non-Chinese

**Example**:
```
Information: Operations efficiency is primary driver
Basis: Direct Citation
Source: Page 3, Line 12: "Operations efficiency is our primary driver" (CIO interview)
Chinese: "运营效率是我们的主要驱动力" (CIO访谈)
Confidence: HIGH ★★★★★
```

---

### Basis 3: Multiple Source Agreement (多源一致)

**Definition**: Information consistent across multiple independent source cases.

**Confidence**: HIGH to MEDIUM

**Requirements**:
- Mentioned in ≥3 independent cases
- Consistent across cases
- No significant contradictions
- Cross-industry validation preferred

**Example**:
```
Information: IT Lead typically has high influence
Basis: Multiple Source Agreement
Sources: 45 cases mention IT Lead influence, 3 contradict
Confidence: HIGH ★★★★★
Note: High agreement ratio (45/48)
```

---

### Basis 4: Industry Standard (行业标准)

**Definition**: Information based on established industry practices or standards.

**Confidence**: MEDIUM

**Requirements**:
- Documented industry practice
- Reasoned from industry characteristics
- Supported by external reference
- Applied with caution (may vary by organization)

**Example**:
```
Information: Hospitals typically have CISO role for cybersecurity
Basis: Industry Standard
Source: Healthcare industry best practices (external reference)
Context: Generalization from multiple healthcare cases
Confidence: MEDIUM ★★★☆☆
Note: Industry standard, but individual hospitals may vary
```

---

### Basis 5: Contextual Inference (情境推理)

**Definition**: Information reasonably inferred from surrounding context.

**Confidence**: MEDIUM

**Requirements**:
- Logical inference from available context
- Minimal assumptions
- Alternative explanations considered
- Documented reasoning

**Example**:
```
Information: Network operations team exists
Basis: Contextual Inference
Source: Page 6, Line 30: "Managed by 15-person network operations team"
Reasoning: Team existence explicitly stated, role structure inferred
Confidence: MEDIUM ★★★☆☆
```

---

### Basis 6: Quantitative Support (量化支持)

**Definition**: Information supported by quantitative data or metrics.

**Confidence**: MEDIUM to HIGH

**Requirements**:
- Specific numbers or metrics provided
- Calculations or derivations clearly explained
- Data sources traceable
- Statistical significance considered

**Example**:
```
Information: Average stakeholder count is 6.4 per case
Basis: Quantitative Support
Calculation: 1069 total stakeholders / 167 cases = 6.4
Data: Extracted from all 167 analysis documents
Confidence: HIGH ★★★★★
Note: Exact count with clear derivation
```

---

### Basis 7: Expert Judgment (专家判断)

**Definition**: Information based on domain expertise or professional judgment.

**Confidence**: LOW to MEDIUM

**Requirements**:
- Requires specialized domain knowledge
- Not directly stated in sources
- Professional reasoning provided
- Flagged for verification

**Example**:
```
Information: IT Lead influence typically decreases in large organizations
Basis: Expert Judgment
Reasoning: Based on organizational theory and case observation
Evidence: 67% of large org cases show lower IT Lead influence
Confidence: MEDIUM ★★★☆☆
Note: Generalization from observed pattern
```

---

### Basis 8: Speculative Inference (推测推断)

**Definition**: Information based on significant assumptions or limited evidence.

**Confidence**: LOW

**Requirements**:
- Requires multiple assumptions
- Limited or weak evidence
- Alternative explanations possible
- Clearly labeled as speculative

**Example**:
```
Information: CIO likely reports to CEO in this organization
Basis: Speculative Inference
Reasoning: Typical org structure, CEO mentioned but reporting lines not stated
Confidence: LOW ★★☆☆☆
Note: Reporting structure not explicitly stated
```

---

## Confidence Assessment by Information Type

### Type 1: Stakeholder Role Classification

| Evidence | Confidence | Basis Category |
|----------|------------|----------------|
| Explicit title in source | HIGH | Explicit Statement |
| Role title mentioned but scope unclear | MEDIUM | Contextual Inference |
| Role implied by responsibilities | MEDIUM | Contextual Inference |
| Role inferred from organizational structure | LOW | Speculative Inference |

### Type 2: Business Driver Identification

| Evidence | Confidence | Basis Category |
|----------|------------|----------------|
| Explicit driver statement | HIGH | Direct Citation |
| Driver inferred from problem description | MEDIUM | Contextual Inference |
| Driver inferred from solution benefits | MEDIUM | Contextual Inference |
| Driver inferred from industry trends | LOW | Industry Standard |

### Type 3: Influence Level Assessment

| Evidence | Confidence | Basis Category |
|----------|------------|----------------|
| Explicit influence statement | HIGH | Explicit Statement |
| Influence inferred from decision authority | MEDIUM | Contextual Inference |
| Influence inferred from participation in key meetings | MEDIUM | Contextual Inference |
| Influence inferred from role hierarchy | LOW | Expert Judgment |

### Type 4: Quantified Metrics

| Evidence | Confidence | Basis Category |
|----------|------------|----------------|
| Explicit metric in source | HIGH | Direct Citation |
| Metric calculated from source data | HIGH | Quantitative Support |
| Metric estimated from similar cases | MEDIUM | Multiple Source Agreement |
| Metric inferred from industry benchmarks | LOW | Industry Standard |

### Type 5: Industry Characteristics

| Evidence | Confidence | Basis Category |
|----------|------------|----------------|
| Explicit industry statement | HIGH | Explicit Statement |
| Industry inferred from organizational type | MEDIUM | Contextual Inference |
| Industry inferred from challenges/solutions | MEDIUM | Contextual Inference |
| Industry inferred from regulatory environment | LOW | Industry Standard |

---

## Confidence Expression Format

### Standard Format

```
[Information Statement]

**Confidence Level**: [HIGH/MEDIUM/LOW]
**Confidence Symbol**: [★★★★★ / ★★★☆☆ / ★★☆☆☆]
**Basis**: [Basis Category]
**Evidence**: [Specific evidence with source references]
**Reasoning**: [Inference reasoning if applicable]
**Original Quote**: [Source quote with bilingual translation if non-Chinese]
```

### Examples

#### Example 1: High Confidence
```
**Primary Business Driver**: Operations Efficiency Optimization

**Confidence Level**: HIGH
**Confidence Symbol**: ★★★★★
**Basis**: Explicit Statement
**Evidence**: 
- Direct quote: "Operations efficiency is our primary driver" (Page 3, Line 12)
- Stated by CIO: Attribution clear
- Quantified: "30% efficiency improvement target"
**Reasoning**: Direct statement with quantitative target, no interpretation required
**Original Quote**: 
- English: "Operations efficiency is our primary driver, we're targeting 30% improvement"
- Chinese: "运营效率是我们的主要驱动力，我们的目标是提升30%"
```

#### Example 2: Medium Confidence
```
**Stakeholder Role**: Network Administrator

**Confidence Level**: MEDIUM
**Confidence Symbol**: ★★★☆☆
**Basis**: Contextual Inference
**Evidence**: 
- Source: "15-person network operations team" (Page 6, Line 30)
- Context: Infrastructure management responsibilities
- Pattern: Similar cases show network admin role
**Reasoning**: Team managing network infrastructure implies network administrator roles, but specific titles not mentioned
**Original Quote**: 
- English: "Our 15-person network operations team manages all infrastructure"
- Chinese: "我们的15人网络运营团队管理所有基础设施"
```

#### Example 3: Low Confidence
```
**Stakeholder Influence**: CIO reports to CEO

**Confidence Level**: LOW
**Confidence Symbol**: ★★☆☆☆
**Basis**: Speculative Inference
**Evidence**: 
- CEO mentioned as senior executive (Page 2, Line 8)
- CIO mentioned with decision authority (Page 5, Line 23)
- Reporting structure not explicitly stated
**Reasoning**: Typical org structure suggests CIO reports to CEO, but not explicitly stated in this case
**Original Quote**: 
- English: "CEO provides overall strategic direction" (Page 2, Line 8)
- Chinese: "CEO提供总体战略方向"
```

---

## Confidence Validation Rules

### Rule 1: Confidence Justification

**Rule**: Every confidence level must include explicit justification.

**Required Elements**:
- Confidence level (HIGH/MEDIUM/LOW)
- Basis category
- Specific evidence
- Reasoning (if inferred)
- Source references

### Rule 2: Confidence Calibration

**Rule**: Confidence levels should be calibrated across all cases.

**Calibration Principles**:
- Similar evidence → similar confidence levels
- Consistent application of basis categories
- Regular review of confidence assignments
- Adjustment based on validation feedback

### Rule 3: Confidence Escalation

**Rule**: Confidence can be upgraded with additional evidence.

**Escalation Criteria**:
- LOW → MEDIUM: Additional contextual evidence found
- MEDIUM → HIGH: Direct statement or multiple source agreement found
- Document escalation in analysis notes

### Rule 4: Confidence Downgrade

**Rule**: Confidence should be downgraded with contrary evidence.

**Downgrade Criteria**:
- Conflicting sources identified
- Evidence weaker than initially assessed
- Better alternatives available
- Document downgrade in analysis notes

---

## Integration with Output Templates

### Industry Model Integration

All industry conclusions must include:
- Confidence level and symbol
- Basis category
- Source references with bilingual quotes
- Evidence summary

**Example Table Format**:
```
| Industry Pattern | Confidence | Basis | Key Sources | Bilingual Quotes |
|-----------------|------------|--------|--------------|-----------------|
| Primary driver: Operations efficiency | ★★★★★ | Explicit Statement | 65 cases | "Operations efficiency is primary driver" / "运营效率是主要驱动力" |
| Secondary driver: Security compliance | ★★★☆☆ | Multiple Source | 48 cases | "Security critical for regulatory compliance" / "安全对监管合规至关重要" |
```

### Stakeholder Model Integration

All stakeholder classifications must include:
- Confidence level and symbol
- Basis category
- Source references with bilingual quotes
- Inference reasoning (if applicable)

**Example Table Format**:
```
| Category | Role | Confidence | Basis | Source | Bilingual Quote |
|----------|------|------------|--------|---------|----------------|
| Decision Maker | CIO | ★★★★★ | Explicit | Page 5, L23 | "CIO has budget authority" / "CIO拥有预算权" |
| IT Lead | Network Director | ★★★☆☆ | Contextual | Page 3, L12 | "Network operations overseen by" / "网络运营由...监督" |
```

### Purchase Factor Model Integration

All purchase factor conclusions must include:
- Confidence level and symbol
- Basis category (especially for quantified metrics)
- Source references with bilingual quotes
- MoE indicator traceability

**Example Table Format**:
```
| Purchase Factor | Quantified Metric | Confidence | Basis | Source | Bilingual Quote |
|----------------|------------------|------------|--------|---------|----------------|
| Operations efficiency | 30% improvement | ★★★★★ | Direct Citation | Page 3, L15 | "30% efficiency improvement" / "30%效率提升" |
| Cost savings | 40% reduction | ★★★☆☆ | Quantitative Support | Calculated | Derived from MPLS→SD-WAN transition / 从MPLS→SD-WAN转换得出 |
```

---

## Quality Assurance

### Confidence Assignment Checklist

- [ ] Every inference has confidence level assigned
- [ ] Confidence level justified with basis category
- [ ] Specific evidence provided with source references
- [ ] Bilingual quotes provided for non-Chinese sources
- [ ] Reasoning documented for inferred information
- [ ] Confidence levels calibrated across similar cases
- [ ] Low confidence items flagged for verification

### Confidence Documentation Requirements

- [ ] Confidence level expressed using standard format
- [ ] Confidence symbol included (star rating)
- [ ] Basis category clearly identified
- [ ] Source references complete (page/line)
- [ ] Bilingual translations provided
- [ ] Inference reasoning explained (if applicable)
- [ ] Escalation/downgrade documented (if applicable)

---

## Best Practices

1. **Be Explicit About Confidence**: Never hide uncertainty
2. **Use Basis Categories**: Apply standard basis categories consistently
3. **Provide Evidence**: Always include specific source references
4. **Use Bilingual Quotes**: Translate non-Chinese sources
5. **Document Reasoning**: Explain how inferences were made
6. **Calibrate Regularly**: Review and adjust confidence assignments
7. **Flag Uncertainty**: Clearly identify low-confidence conclusions
8. **Be Conservative**: When uncertain, choose lower confidence
9. **Provide Rationale**: Explain why confidence level was chosen
10. **Enable Verification**: Make it easy to verify confidence assessments

---

## Integration with Other Frameworks

This framework integrates with:

1. **Business Background Driver Priority**: Apply confidence to all business analysis
2. **MoE Indicators Framework**: Apply confidence to all quantified metrics
3. **Bilingual Quote Requirement**: Ensure all sources have bilingual translations
4. **Stakeholder Role Hierarchy**: Apply confidence to all role classifications
5. **Cross-Model Consistency**: Ensure consistent confidence application across models
6. **Input Validation Framework**: Flag low-confidence items for manual review