# Entity Model Synthesis Prompt

## Purpose

Synthesize entity patterns from multiple scenario_analyzer analysis outputs. Build entity model with organization entities, system entities, and external entities, including attributes and relationships for OpenSCENARIO DSL preparation.

---

## Input Requirements

Provide multiple `-analysis.md` documents with:
- Customer basic information (company, industry, country)
- Stakeholder listings (organizational roles)
- Products and solutions (system entities)
- External stakeholders (partner entities)

---

## Entity Type Definitions

### Organization Entities

| Entity Type | Definition | Attributes |
|-------------|------------|------------|
| Company | Main organization | Name, Industry, Region, Scale |
| Department | Organizational unit | Name, Function, Parent |
| Team | Working group | Name, Role, Members, Parent |
| Project Group | Project-specific group | Name, Purpose, Duration |
| Site/Location | Physical location | Name, Type, Address, Scale |

### System Entities

| Entity Type | Definition | Attributes |
|-------------|------------|------------|
| Product | Commercial product | Name, Vendor, Version, Category |
| Solution | Integrated solution | Name, Components, Purpose |
| Component | Technical component | Name, Type, Function |
| Service | Delivered service | Name, Type, Provider |
| Platform | Management platform | Name, Type, Features |

### External Entities

| Entity Type | Definition | Attributes |
|-------------|------------|------------|
| Supplier | Product/service provider | Name, Type, Relationship |
| Regulator | Regulatory body | Name, Type, Requirements |
| Partner | Collaborative partner | Name, Role, Services |
| Customer/Client | External customer | Name, Type, Requirements |

---

## Analysis Instructions

### Step 1: Organization Entity Extraction

1. Extract company name from customer basic information
2. Infer organizational structure from stakeholder listings:
   - "Digital Infrastructure Manager" → Department: IT/Infrastructure
   - "IT Operations Team" → Team: IT Operations
   - "School Management" → Department: School Administration
3. Extract site/location information from descriptions:
   - "67 schools" → Sites: 67 School locations
   - "National offices" → Sites: National office locations
4. Build organization entity hierarchy

### Step 2: System Entity Extraction

1. Extract products from product/solution table
2. Classify by entity type:
   - "Juniper AP34/AP45" → Product (Hardware)
   - "Mist Cloud" → Platform (Software)
   - "Marvis AI" → Service (AI service)
3. Identify solution compositions:
   - "HPE Juniper Networking" → Solution containing multiple products
4. Extract version/category from descriptions

### Step 3: External Entity Extraction

1. Extract external stakeholders from stakeholder listings:
   - "Customer Success Manager (HPE)" → Supplier/Partner
   - "Municipal decision layer" → Regulator (for municipal organizations)
   - "NHS Management" → Regulator (for healthcare)
2. Infer entity types from context:
   - Vendor mentions → Supplier
   - Policy mentions → Regulator
3. Extract relationship information

### Step 4: Entity Attribute Extraction

For each entity, extract:

| Attribute Category | Attributes | Source |
|--------------------|-----------|--------|
| Identity | Name, ID, Type | Direct extraction |
| Classification | Industry, Category, Role | Metadata, classification |
| Scale | Size, Count, Coverage | Descriptions, quantified metrics |
| State | Current status | Initial/final states |
| Relationships | Parent, Children, Associates | Hierarchy inference |

### Step 5: Entity Frequency Analysis

1. Count frequency of each entity type across documents
2. Build Entity Type × Industry matrix
3. Identify common entities (appearing across industries)
4. Identify industry-specific entities

### Step 6: Entity Relationship Mapping

1. Build organization hierarchy tree per case
2. Build system composition tree (solution → products)
3. Build external entity connection graph (organization ↔ external)
4. Identify common relationship patterns

---

## Output Format

Follow the template: `entity-model-template.md`

**Required Sections**:

### 1. Organization Entity Catalog

| Entity | Type | Parent | Scale | Industry | Source Cases |

### 2. System Entity Catalog

| Entity | Type | Vendor | Category | Solutions Using | Source Cases |

### 3. External Entity Catalog

| Entity | Type | Role | Requirements | Source Cases |

### 4. Organization Entity Hierarchy Template

```
Organization: Aberdeen City Council
├── Department: Digital Infrastructure
│   ├── Role: Digital Infrastructure Manager
│   └── Team: IT Operations Team
│       └── Role: IT Service Desk
├── Department: School Administration
│   ├── Role: School Management
│   └── Department: Education
│       ├── Role: Teachers
│       └── User Group: Students (26,500)
└── Sites: 67 Schools, 100 Enterprise Sites
```

### 5. System Entity Composition Template

```
Solution: HPE Juniper Networking AI-Native Network
├── Platform: Mist Cloud
│   ├── Service: Marvis AI
│   └── Service: Wi-Fi/Wired Assurance
├── Product: Juniper AP34/AP45 (Wi-Fi 6/6E APs)
├── Product: Juniper EX4650/EX4400/EX4100 (Switches)
├── Service: Juniper Mist Access Assurance
└── Service: Juniper AI Advanced Care
```

### 6. External Entity Connection Template

```
Organization: Aberdeen City Council
├── ↔ Supplier: HPE Aruba Networking
│   ├── Service: Customer Success Manager
│   └── Platform: ASM Portal
├── ↔ Regulator: UK Government
│   ├── Policy: 1:1 Device Mandate
│   └── Compliance: UK Data Protection
```

### 7. Entity × Industry Matrix

| Entity Type | Education | Healthcare | Hospitality | Manufacturing | ITServices |

---

## Traceability Requirements

For each entity entry, include:
- Source Cases: Case IDs where this entity appears
- Original Name: Original entity name from source
- Inference Method: Direct extraction vs inferred from context

---

## Quality Checklist

- [ ] All three entity types are extracted (Organization, System, External)
- [ ] Organization hierarchy is built per case
- [ ] System composition is identified per solution
- [ ] External entity connections are mapped
- [ ] Entity attributes are extracted
- [ ] Entity frequency analysis is complete

---

## Example Usage

```
Entity extraction example:
Original: "Aberdeen City Council | Digital Infrastructure Manager | 67 schools, 26,500 students"
→ Organization Entities:
  - Company: Aberdeen City Council (Type: Municipal)
  - Department: Digital Infrastructure (Parent: Aberdeen CC)
  - Role: Digital Infrastructure Manager (Parent: Digital Infrastructure)
  - Sites: 67 Schools (Parent: Aberdeen CC)
  - User Group: Students (Scale: 26,500)

Original: "Juniper AP34/AP45 | Mist Cloud | Marvis AI"
→ System Entities:
  - Product: Juniper AP34/AP45 (Type: Hardware, Vendor: Juniper)
  - Platform: Mist Cloud (Type: Software Platform)
  - Service: Marvis AI (Type: AI Service, Parent: Mist Cloud)

Original: "Customer Success Manager (HPE)"
→ External Entities:
  - Supplier: HPE Aruba Networking
  - Service: Customer Success Manager (Role: Lifecycle management)
```