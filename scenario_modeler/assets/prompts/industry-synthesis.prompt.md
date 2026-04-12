# Industry Synthesis Prompt

## Purpose

Synthesize industry-level patterns from multiple scenario_engine analysis outputs, including industry classification, regional distribution, typical challenges, stakeholder distributions, solution preferences, **purchase factors per industry**, and **critical analysis**.

---

## Input Requirements

Provide multiple `-analysis.md` documents with the following fields:
- Customer basic information (industry, country, company, year)
- Purchase elements (ranked list with business value and metrics)
- Stakeholder listing
- Conflicts and priorities
- Products and solutions
- Traceability references (page numbers, original quotes)

---

## Analysis Instructions

### Step 1: Industry Classification Extraction

1. Extract all unique industry values from input documents
2. Identify primary industry categories (Education, Healthcare, Hospitality, Manufacturing, ITServices, Logistics, Retail, etc.)
3. Identify secondary industry sub-categories where available:
   - Education → K-12, Higher Education
   - Healthcare → Hospital, Clinic, NHS Trust
   - Hospitality → Hotel, Resort, Travel Service
4. Count frequency per category/sub-category
5. List all case IDs belonging to each category

### Step 2: Regional Distribution Analysis

1. Extract all unique country/region values
2. Map regions to industries
3. Build Region × Industry distribution matrix
4. Identify regional concentration patterns
5. Note regional variations in purchase preferences

### Step 3: Typical Challenges Extraction

1. Extract "pre-deployment problems" from each document
2. Group similar challenges by semantic similarity
3. Count frequency per challenge type
4. Identify industry-specific challenges vs cross-industry challenges
5. Preserve original wording for typical challenges
6. **MANDATORY**: Include customer name attribution for each challenge

### Step 4: Stakeholder Distribution Analysis

1. Extract all stakeholder roles from each document
2. Count occurrence frequency per role within each industry
3. Identify roles appearing in >50% of cases per industry (typical roles)
4. Identify roles appearing in <20% of cases per industry (variant roles)
5. Build Industry × Role matrix with frequency counts

### Step 5: Solution Preference Extraction

1. Extract all products/solutions from each document
2. Identify common products appearing across multiple industries
3. Identify industry-specific products/solutions
4. Count frequency per product/solution
5. Map products to purchase factors they satisfy
6. **MANDATORY**: Include customer name and original quote for key solutions

### Step 6: Purchase Factor Synthesis per Industry (MANDATORY)

**For each industry, extract at least 3-5 purchase factors with full traceability:**

1. Extract ranked purchase factors from each document's "Purchase Elements" section
2. Group factors by industry category
3. For each industry, synthesize the top 3-5 factors with:
   - Ranking (1st, 2nd, 3rd, etc.)
   - Business importance level (Highest, High, Medium)
   - Typical expression/quote from source
   - **Customer name attribution** (e.g., "Aberdeen City Council", "Southern Sun", "Colep Packaging")
   - **Original quote reference** (Page number or line number)
4. Format as detailed tables per industry

**Example format:**

```
#### Education (K-12) 行业购买要素 (5项)

| 排名 | 购买要素 | 业务重要性 | 典型表述 | 来源客户 |
|------|----------|------------|----------|----------|
| 1 | 设备密度与连接可靠性 | Highest | "lacked capacity for 1:1 learning for 26,500 learners" (Page 1) | Aberdeen City Council |
| 2 | AIOps运维简化 | Highest | "take a cloud-first and AIOps approach" (Page 1) | Aberdeen City Council (Iain Pilbeam-Cornfield) |
```

### Step 7: Critical Analysis (MANDATORY)

**Apply objective correction to all major conclusions:**

1. **Data Source Limitations Assessment**:
   - Identify supplier perspective bias (all documents from same vendor)
   - Identify survivorship bias (no failure cases)
   - Identify quantified data source concerns (all metrics from customer/vendor reports)
   - Identify non-random distribution (reflects vendor market coverage, not real demand)

2. **Objective Industry Correction**:
   - For each major industry, provide:
     - Original conclusion from synthesis
     - Objective correction perspective
     - Industry domain knowledge补充

3. **Technical Solution Objective Assessment**:
   - For each major solution, provide:
     - Supplier claimed effects
     - Customer verification status
     - Objective evaluation with caveats

4. **Market Distribution Objective Interpretation**:
   - Supplier perspective interpretation vs objective interpretation

5. **Data Usage Recommendations**:
   - Market analysis: supplement with third-party data
   - ROI calculation: independently verify hidden costs
   - Risk assessment: need failure case analysis

6. **Conclusion Credibility Rating**:
   - Use star rating (★☆☆☆☆ to ★★★★☆)
   - Rate: Industry challenges, Technical effects, Quantified metrics, Regional insights, Solution preferences

---

## Output Format

Follow the template: `industry-model-template.md`

**Required Sections**:

### 1. Industry Classification Table
| Industry (Primary) | Sub-Category | Case Count | Case IDs |

### 2. Regional Distribution Matrix
| Industry | UK | US | Japan | Belgium | India | SaudiArabia | Other |

### 3. Typical Challenges by Industry
| Industry | Challenge Type | Frequency | Customer Name | Typical Quote | Source Cases |

### 4. Stakeholder Distribution Matrix
| Industry | Decision Maker | IT Lead | Operator | User | Regulator | Partner |

### 5. Solution Preference Table
| Product/Solution | Frequency | Customer Name | Industries | Original Quote |

### 6. Purchase Factor Synthesis per Industry (MANDATORY)
**For each industry, provide 3-5 factors:**
| Industry | 排名 | 购买要素 | 业务重要性 | 典型表述 | 来源客户 |

### 7. Key Insights
| Pattern | Finding | Customer Name | Original Quote | Source Cases |

### 8. Traceability Summary (Enhanced)
**Four sub-tables:**
- Industry Challenge Traceability
- Solution Preference Traceability
- Key Insight Traceability
- Regional Distribution Traceability

Each table must include: Source Cases, Frequency, **Customer Name**, **Original Quote**

### 9. Critical Analysis (MANDATORY)
**Required sub-sections:**
- Data Source Limitations Assessment
- Objective Industry Correction (for major industries)
- Technical Solution Objective Assessment
- Market Distribution Objective Interpretation
- Data Usage Recommendations
- Conclusion Credibility Rating

---

## Traceability Requirements (Enhanced)

For each conclusion, include:
- **Source Cases**: List case IDs (e.g., "Education-UK-Aberdeen-City-Council")
- **Frequency**: Percentage or count (e.g., "80% of Education cases")
- **Customer Name**: Specific customer attribution (e.g., "Aberdeen City Council", "Southern Sun")
- **Original Quote**: Key original wording with reference (Page number, line number, or paragraph)
- **Variations**: Note exceptions or variations

---

## Quality Checklist

- [ ] All industries from input documents are classified
- [ ] Regional distribution covers all countries mentioned
- [ ] Challenges are grouped by semantic similarity, with customer name attribution
- [ ] Stakeholder roles are mapped to categories
- [ ] Products/solutions are identified with customer name and original quote
- [ ] **Purchase factors per industry: at least 3-5 items with customer name and quote**
- [ ] Each conclusion has enhanced traceability (customer name + original quote)
- [ ] **Critical analysis chapter included with all 6 sub-sections**
- [ ] Conclusion credibility ratings assigned

---

## Example Usage

```
Input: 28 analysis documents from scenario_engine/tests/result_v2/analysis/
Output:
- Education industry: 5 cases (Aberdeen City Council, Alleyn's School, Annie Wright Schools, Moreno Valley USD)
- Purchase factors (Education): 
  1. 设备密度与连接可靠性 - Aberdeen City Council: "lacked capacity for 1:1 learning for 26,500 learners" (Page 1)
  2. AIOps运维简化 - Aberdeen City Council: "100% ticket reduction" (Page 1)
- Critical Analysis: Supplier bias identified, objective correction applied, credibility rating ★★★☆☆ for challenges
```