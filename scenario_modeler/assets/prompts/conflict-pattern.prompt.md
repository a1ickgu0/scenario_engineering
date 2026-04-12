# Conflict Pattern Synthesis Prompt

## Purpose

Synthesize conflict patterns from the conflict sections of multiple scenario_engine analysis outputs. Build a conflict pattern library with types, stakeholder involvement, industry distribution, and resolution strategies.

---

## Input Requirements

Provide multiple `-analysis.md` documents with conflict sections containing:
- Conflict point
- Related stakeholders
- Root cause
- Priority recommendation
- Traceability reference

---

## Conflict Type Taxonomy

| Conflict Type | Definition | Typical Resolution |
|---------------|------------|--------------------|
| Cost vs Quality | Budget constraints limiting quality improvements | Prioritize ROI justification, phased investment |
| Cost vs Security | Security investment vs budget constraints | Prioritize compliance requirements, risk assessment |
| Security vs Convenience | Security measures reducing user convenience | Prioritize user experience, balance policy |
| Innovation vs Stability | New capabilities vs system reliability | Prioritize phased rollout, parallel operation |
| Capacity vs Cost | Scaling requirements vs budget | Prioritize NaaS/subscription model, elasticity |
| Short-term vs Long-term | Immediate needs vs strategic goals | Prioritize strategic alignment, roadmap planning |
| Customization vs Standardization | Specific needs vs standard solutions | Prioritize core customization, standard peripheral |
| Internal vs External | In-house vs outsourced operations | Prioritize hybrid approach, maintain core capability |
| Automation vs Control | Automated operations vs manual oversight | Prioritize AI-assisted, human oversight |

---

## Analysis Instructions

### Step 1: Conflict Extraction

1. Extract all conflicts from conflict table
2. Preserve original conflict descriptions
3. Extract related stakeholders
4. Extract root causes
5. Extract priority recommendations

### Step 2: Conflict Type Classification

1. Map each extracted conflict to one of the 9 Conflict Types
2. Use semantic similarity and stakeholder involvement patterns
3. Document reasoning for ambiguous classifications
4. Count frequency per Conflict Type

### Step 3: Stakeholder Involvement Analysis

1. Identify stakeholder pairs/groups involved in each conflict
2. Map stakeholders to their categories
3. Identify typical category pairs in conflict (e.g., Decision Maker vs IT Lead)
4. Count frequency per stakeholder pair

### Step 4: Root Cause Pattern Analysis

1. Group similar root causes by semantic similarity
2. Identify common root cause patterns:
   - Resource constraints (budget, time, capacity)
   - Process issues (approval, integration, knowledge)
   - Policy requirements (compliance, security)
   - Technology limitations (legacy, compatibility)
3. Count frequency per root cause pattern

### Step 5: Resolution Strategy Extraction

1. Extract all priority recommendations
2. Group similar recommendations by strategy type:
   - Prioritize X over Y (explicit priority)
   - Balance X and Y (compromise approach)
   - Phased approach (sequential resolution)
   - Hybrid solution (combined approach)
3. Identify typical resolution per Conflict Type

### Step 6: Industry Distribution Analysis

1. Build Industry × Conflict Type matrix
2. Calculate conflict frequency per industry
3. Identify industry-specific conflicts
4. Identify cross-industry common conflicts

---

## Output Format

Follow the template: `conflict-pattern-template.md`

**Required Sections**:

### 1. Conflict Type Frequency Table

| Conflict Type | Frequency | Typical Stakeholders | Typical Resolution | Source Cases |

### 2. Stakeholder Pair Conflict Matrix

| Stakeholder Pair | Conflict Types | Frequency | Resolution Pattern | Source Cases |

### 3. Root Cause Pattern Table

| Root Cause Pattern | Frequency | Associated Conflicts | Industries | Source Cases |

### 4. Resolution Strategy Catalog

| Strategy Type | Definition | Applicable Conflicts | Example Resolution |

### 5. Industry × Conflict Type Matrix

| Industry | Cost vs Quality | Cost vs Security | Security vs Convenience | Innovation vs Stability |

### 6. Conflict Detailed Analysis

For each unique conflict:

| Original Conflict | Conflict Type | Stakeholders | Root Cause | Resolution | Industry | Source |

---

## Traceability Requirements

For each conflict entry, include:
- Original Description: Exact wording from source
- Source Cases: Case IDs where this conflict appears
- Resolution Quote: Original priority recommendation wording

---

## Quality Checklist

- [ ] All conflicts from source documents are extracted
- [ ] Each conflict is classified to a Conflict Type
- [ ] Stakeholder involvement is mapped to categories
- [ ] Root causes are grouped by pattern
- [ ] Resolution strategies are categorized
- [ ] Industry distribution is calculated

---

## Example Usage

```
Conflict extraction example:
Original: "Operations cost vs Innovation needs | IT team, Management | Traditional operations consume significant time"
→ Conflict Type: Innovation vs Stability
→ Stakeholders: IT Lead (IT team), Decision Maker (Management)
→ Root Cause: Process issue (traditional operations model limitation)
→ Resolution: Prioritize AIOps automation
→ Source: Education-UK-06-Aberdeen

Common conflict patterns:
- Security vs Convenience: Most common in Healthcare industry (balance of compliance and convenience)
- Cost vs Quality: More common in Manufacturing industry (investment decision trade-off)
- Capacity vs Cost: Common in Education industry (high-density device connection needs)
```