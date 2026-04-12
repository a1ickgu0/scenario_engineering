# Environment Model Synthesis Prompt

## Purpose

Synthesize environment/contextual patterns from multiple scenario_engine analysis outputs. Build environment model with industry constraints, regional characteristics, and organizational context for OpenSCENARIO DSL preparation.

---

## Input Requirements

Provide multiple `-analysis.md` documents with:
- Customer basic information (industry, country, company)
- Pre-deployment problems (environmental constraints)
- Stakeholder listings (regulatory/external stakeholders)
- Purchase elements (compliance/security factors)

---

## Environment Dimension Definitions

### Industry Environment

| Dimension | Definition | Examples |
|-----------|------------|----------|
| Industry Regulations | Industry-specific legal requirements | HIPAA (Healthcare), FERPA (Education), PCI-DSS (Retail) |
| Industry Standards | Industry-specific technical/operational standards | ISO 27001 (Security), IEEE 802.11 (Wi-Fi) |
| Compliance Requirements | Mandatory compliance obligations | GDPR (EU data), UK Data Protection Act |
| Industry Policies | Government or industry body policies | 1:1 device mandate (Education), NHS digital strategy |
| Industry Practices | Common industry operational practices | Cloud adoption, remote work support |

### Regional Environment

| Dimension | Definition | Examples |
|-----------|------------|----------|
| National Regulations | Country-specific legal requirements | UK GDPR, US HIPAA, Japan APPI |
| Cultural Characteristics | Cultural factors affecting adoption | Remote work culture, digital readiness |
| Market Maturity | Technology adoption stage | Early adopter vs mainstream |
| Economic Context | Economic factors affecting investment | Public vs private budget, growth rate |
| Infrastructure Availability | Available supporting infrastructure | Cloud services, network coverage |

### Organizational Environment

| Dimension | Definition | Examples |
|-----------|------------|----------|
| Organizational Scale | Size of organization | 67 schools, 26,500 students, 31,000 users |
| Architecture Type | Organization structure | Centralized, distributed, federated |
| Budget Constraints | Financial limitations | CapEx approval difficulty, OpEx preference |
| Technical Capabilities | Existing technical expertise | IT team size, internal knowledge |
| Strategic Direction | Organizational strategic goals | Digital transformation, sustainability |

### Technical Environment

| Dimension | Definition | Examples |
|-----------|------------|----------|
| Existing Tech Stack | Current technology infrastructure | Legacy network, cloud services |
| Integration Constraints | Integration requirements/limitations | ServiceNow integration, existing systems |
| Technical Standards | Required technical specifications | Wi-Fi 6/6E, zero-trust architecture |
| Vendor Relationships | Existing vendor partnerships | HPE Aruba, Juniper ecosystem |
| Migration Requirements | Migration from existing systems | 30-minute migration, zero-touch config |

---

## Analysis Instructions

### Step 1: Industry Environment Extraction

1. Extract industry from customer basic information
2. Infer industry regulations from purchase factors (security/compliance)
3. Infer industry policies from pre-deployment problems (mandates, goals)
4. Document typical industry environment per industry category
5. Count frequency per environment element

### Step 2: Regional Environment Extraction

1. Extract country/region from customer basic information
2. Infer national regulations from stakeholder listings (regulator roles)
3. Infer cultural characteristics from operational scenarios (work patterns)
4. Document typical regional environment per country/region
5. Identify cross-region common elements and regional-specific elements

### Step 3: Organizational Environment Extraction

1. Extract organizational scale from company descriptions:
   - "67 schools, 26,500 students" → Scale: Multi-site, Large user base
   - "National offices wireless LAN" → Scale: Distributed, National
2. Infer architecture type from scenario descriptions:
   - "67 schools, 100 enterprise sites" → Architecture: Distributed/Federated
   - "Centralized management monitoring" → Architecture: Centralized management
3. Extract budget constraints from purchase factors (NaaS, CapEx difficulty)
4. Extract strategic direction from overall benefits (digital transformation)

### Step 4: Technical Environment Extraction

1. Extract existing tech stack from pre-deployment problems:
   - "Legacy network aging" → Existing: Legacy network
   - "Business infrastructure transitioning to cloud" → Existing: Cloud transition
2. Extract integration constraints from products/solutions:
   - "ServiceNow integration" → Integration: ServiceNow
   - "ASM portal" → Integration: ASM platform
3. Extract technical standards from purchase factors:
   - "Wi-Fi 6/6E" → Standard: IEEE 802.11ax
   - "Zero-trust" → Standard: Zero-trust architecture
4. Extract vendor relationships from products/solutions:
   - "HPE Juniper Networking" → Vendor: HPE/Juniper ecosystem

### Step 5: Environment Element Frequency

1. Count frequency of each environment element across documents
2. Build Environment Element × Industry matrix
3. Build Environment Element × Region matrix
4. Identify common elements (appearing across industries/regions)
5. Identify specific elements (appearing in limited contexts)

### Step 6: Environment Constraint Patterns

1. Identify constraint combinations appearing together:
   - Education + UK + Public budget → 1:1 mandate + GDPR + CapEx difficulty
   - Healthcare + US + Private → HIPAA + High security + Cloud transition
2. Build constraint pattern library
3. Identify pattern frequency

---

## Output Format

Follow the template: `environment-model-template.md`

**Required Sections**:

### 1. Industry Environment Table

| Industry | Regulations | Standards | Compliance | Policies | Practices | Source Cases |

### 2. Regional Environment Table

| Region/Country | National Regulations | Cultural Traits | Market Maturity | Economic Context | Source Cases |

### 3. Organizational Environment Table

| Scale Category | Architecture Types | Budget Constraints | Technical Capabilities | Strategic Directions | Source Cases |

### 4. Technical Environment Table

| Existing Stack | Integration Constraints | Technical Standards | Vendor Relationships | Migration Requirements | Source Cases |

### 5. Environment Element Frequency

| Environment Element | Type | Frequency | Industries | Regions | Source Cases |

### 6. Constraint Pattern Library

| Pattern Name | Industries | Regions | Elements | Frequency | Source Cases |

### 7. Industry × Region Environment Matrix

| Industry × Region | Regulations | Policies | Budget | Tech Stack | Source Cases |

---

## Traceability Requirements

For each environment element, include:
- Source Cases: Case IDs where this element appears
- Original Quote: Original problem or stakeholder description
- Inference Method: How this element was inferred (direct/inferred)

---

## Quality Checklist

- [ ] All four environment dimensions are analyzed
- [ ] Industry environment elements are extracted
- [ ] Regional environment elements are extracted
- [ ] Organizational environment elements are extracted
- [ ] Technical environment elements are extracted
- [ ] Constraint patterns are identified
- [ ] Traceability references are complete

---

## Example Usage

```
Environment extraction example:
Original: "Aberdeen City Council | UK | Education | 67 schools, 26,500 students"
→ Industry Environment:
  - Policy: 1:1 device mandate (national education digital goal)
  - Compliance: UK Data Protection
→ Regional Environment:
  - National Regulations: UK GDPR
  - Economic Context: Public budget (municipal budget)
→ Organizational Environment:
  - Scale: 67 schools, 26,500 students (Multi-site, Large)
  - Architecture: Distributed (67 schools, 100 sites)
  - Budget: CapEx approval process (municipal approval)
→ Technical Environment:
  - Existing: Legacy network (aging network)
  - Standard: Wi-Fi 6/6E, zero-trust (purchase factors)
  - Vendor: HPE Juniper (solutions)
→ Source: Education-UK-06-Aberdeen

Constraint pattern:
Education + UK + Municipal → [1:1 mandate, GDPR, Public budget, Distributed architecture]
```