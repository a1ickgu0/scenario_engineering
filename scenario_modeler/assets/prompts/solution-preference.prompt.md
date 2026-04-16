# Solution Preference Synthesis Prompt

## Purpose

Synthesize product/solution preferences from multiple scenario_analyzer analysis outputs. Build solution preference patterns by industry, purchase factor, and stakeholder expectations.

---

## Input Requirements

Provide multiple `-analysis.md` documents with product/solution sections containing:
- Product/solution name
- Description
- Quantified benefits
- Needs satisfied
- Traceability reference

---

## Analysis Instructions

### Step 1: Solution Extraction

1. Extract all products/solutions from product/solution table
2. Preserve original product names
3. Extract descriptions and quantified benefits
4. Extract needs satisfied mapping
5. Normalize product names:
   - "Juniper AP34/AP45 Wireless Access Points" → "Juniper Wi-Fi AP (AP34/AP45)"
   - "HPE Aruba Networking EdgeConnect SD-WAN" → "HPE Aruba SD-WAN (EdgeConnect)"

### Step 2: Solution Classification

1. Classify solutions by type:
   - **Hardware**: APs, Switches, Controllers
   - **Software/Platform**: Cloud management, AI platforms, NaaS
   - **Services**: Support, Customer Success, Managed services
   - **Security**: Access control, Zero-trust, NAC
2. Count frequency per solution type

### Step 3: Industry × Solution Analysis

1. Build Industry × Solution matrix
2. Count appearance frequency per industry
3. Identify industry-specific solutions (appearing in only one industry)
4. Identify cross-industry solutions (appearing in multiple industries)
5. Calculate solution preference ranking per industry

### Step 4: Solution × Purchase Factor Mapping

1. Map each solution to Purchase Factors it satisfies
2. Use the "needs satisfied" field and semantic analysis
3. Build Solution → Business Driver → Technical Implementation chain
4. Identify solutions satisfying multiple factors (versatile solutions)
5. Identify solutions satisfying single factor (specialized solutions)

### Step 5: Solution × Stakeholder Mapping

1. Identify stakeholders benefiting from each solution
2. Map to stakeholder categories
3. Build Solution × Stakeholder Category matrix
4. Identify primary beneficiaries per solution

### Step 6: Solution Combination Patterns

1. Identify solutions appearing together in same case
2. Build solution combination frequency table
3. Identify typical solution bundles (common combinations)
4. Analyze bundle characteristics by industry

---

## Output Format

Follow the template: `solution-preference-template.md`

**Required Sections**:

### 1. Solution Frequency Table

| Solution | Type | Frequency | Industries | Source Cases |

### 2. Solution × Industry Matrix

| Solution | Education | Healthcare | Hospitality | Manufacturing | ITServices |

### 3. Solution × Purchase Factor Mapping

| Solution | Business Drivers | Technical Implementations | Quantified Benefits | Source Cases |

### 4. Solution × Stakeholder Category Matrix

| Solution | Decision Maker | IT Lead | Operator | User | Regulator | Partner | Primary Beneficiary |

### 5. Solution Combination Patterns

| Combination | Frequency | Industries | Combined Benefits | Source Cases |

### 6. Industry Solution Preference Ranking

| Industry | Top Solution 1 | Top Solution 2 | Top Solution 3 | Preference Pattern |

### 7. Versatile vs Specialized Solutions

| Versatile Solutions | Factors Satisfied | Industries | Frequency |
| Specialized Solutions | Single Factor | Industries | Frequency |

---

## Traceability Requirements

For each solution entry, include:
- Original Name: Exact product name from source
- Source Cases: Case IDs where this solution appears
- Benefits Quote: Original quantified benefits wording
- Needs Quote: Original needs satisfied wording

---

## Quality Checklist

- [ ] All solutions from source documents are extracted
- [ ] Solution names are normalized but traceable
- [ ] Each solution is classified by type
- [ ] Solution × Industry matrix is complete
- [ ] Solution × Purchase Factor mapping is accurate
- [ ] Solution combinations are identified

---

## Example Usage

```
Solution extraction example:
Original: "Juniper Mist Access Assurance"
→ Type: Security
→ Industries: Education, Healthcare
→ Purchase Factors: Security/Compliance (Zero-trust)
→ Stakeholders: IT Lead, User (secure access control)
→ Quantified Benefits: "Fine-grained security policy"
→ Source: Education-UK-06-Aberdeen, Healthcare-UK-03-Royal-Devon

Cross-industry solutions:
- Marvis AI: appears in Education(3), Manufacturing(2), Healthcare(1) → cross-industry universal
- HPE GreenLake NaaS: appears in Hospitality(2), ITServices(1) → service industry oriented

Solution combinations:
- Juniper Wi-Fi AP + Mist Cloud + Marvis AI: high-frequency combination, typical for Education industry
- SD-WAN + NaaS + Cloud Management: typical combination for Hospitality industry
```