# Entity Model Output Template

## Document Information

| Field | Value |
|-------|-------|
| Model Type | Entity Model |
| Generation Date | [DATE] |
| Source Document Count | [COUNT] |
| Source Document Range | [CASE_IDS] |

---

## 1. Organization Entity Catalog

| Entity | Type | Parent | Scale | Industry | Source Cases |
|--------|------|--------|-------|----------|--------------|
| Aberdeen City Council | Company | - | Large (67 schools) | Education | [CASE_IDS] |
| Digital Infrastructure | Department | Aberdeen CC | - | Education | [CASE_IDS] |
| IT Operations Team | Team | Digital Infrastructure | - | Education | [CASE_IDS] |
| Digital Infrastructure Manager | Role | IT Ops Team | - | Education | [CASE_IDS] |
| School Site (67) | Site | Aberdeen CC | 67 locations | Education | [CASE_IDS] |
| Students (26,500) | User Group | School Sites | 26,500 users | Education | [CASE_IDS] |
| Teachers | Role | School Sites | - | Education | [CASE_IDS] |
| Ikyu Corporation | Company | - | Medium | Hospitality | [CASE_IDS] |
| ... | ... | ... | ... | ... | ... |

---

## 2. System Entity Catalog

| Entity | Type | Vendor | Category | Solutions Using | Source Cases |
|--------|------|--------|----------|-----------------|--------------|
| Mist Cloud | Platform | Juniper | Software | AI-native network | [CASE_IDS] |
| Marvis AI | Service | Juniper | AI Service | Proactive ops | [CASE_IDS] |
| Juniper AP34/AP45 | Product | Juniper | Hardware | Wi-Fi coverage | [CASE_IDS] |
| Juniper EX4650 | Product | Juniper | Hardware | Network infrastructure | [CASE_IDS] |
| Mist Access Assurance | Service | Juniper | Security | Zero-trust | [CASE_IDS] |
| HPE GreenLake NaaS | Solution | HPE | NaaS | Subscription network | [CASE_IDS] |
| Aruba Central | Platform | HPE Aruba | Software | Cloud management | [CASE_IDS] |
| EdgeConnect SD-WAN | Software | HPE Aruba | Network | WAN connectivity | [CASE_IDS] |
| ASM Portal | Platform | HPE Aruba | Service Portal | Managed services | [CASE_IDS] |
| ... | ... | ... | ... | ... | ... |

---

## 3. External Entity Catalog

| Entity | Type | Role | Requirements | Source Cases |
|--------|------|------|--------------|--------------|
| HPE Aruba Networking | Supplier | Vendor | Product delivery, Support | [CASE_IDS] |
| Customer Success Manager | Partner | Lifecycle support | Service delivery, Reporting | [CASE_IDS] |
| ASM Support Team | Partner | Managed service | 24x7x365 monitoring | [CASE_IDS] |
| UK Government | Regulator | Policy source | 1:1 device mandate | [CASE_IDS] |
| NHS Foundation Trust | Regulator | Healthcare governance | NHS digital strategy | [CASE_IDS] |
| Municipal Government | Regulator | Policy oversight | Public budget approval | [CASE_IDS] |
| ... | ... | ... | ... | ... |

---

## 4. Organization Entity Hierarchy Templates

### Template: Education Municipal Organization

```
Organization: [Municipal Authority Name]
├── Department: Digital Infrastructure
│   ├── Role: Digital Infrastructure Manager
│   └── Team: IT Operations Team
│       ├── Role: IT Service Desk
│       └── Role: Network Admin
├── Department: School Administration
│   ├── Role: School Management
│   └── Department: Education
│       ├── Role: Teachers
│       └── User Group: Students (26,500)
└── Sites: [N] School Locations, [M] Enterprise Sites
    ├── Site: School 1
    │   └── User Group: Students
    └── Site: Enterprise 1
        └── User Group: Staff
```

### Template: Hospitality Corporation

```
Organization: [Corporation Name]
├── Department: Information Systems
│   ├── Role: Director IS
│   └── Team: IT Operations
├── Department: Finance
│   └── Role: Finance Team
├── Sites: National Office Locations
    ├── Site: HQ Office
    │   └── User Group: Employees
    └── Site: Regional Office
        └── User Group: Regional Staff
```

---

## 5. System Entity Composition Templates

### Template: AI-Native Network Solution

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

### Template: NaaS Solution

```
Solution: HPE GreenLake for Networking
├── Platform: Aruba Central
├── Platform: ASM Portal
├── Product: HPE Aruba Wireless APs
├── Product: HPE Aruba Wired Switches
├── Software: EdgeConnect SD-WAN
└── Service: Customer Success Manager
```

---

## 6. External Entity Connection Templates

### Template: Education Municipal External Connections

```
Organization: Aberdeen City Council
├── ↔ Supplier: HPE Aruba Networking
│   ├── Service: Customer Success Manager
│   └── Platform: ASM Portal
├── ↔ Regulator: UK Government
│   ├── Policy: 1:1 Device Mandate
│   └── Compliance: UK Data Protection
```

### Template: Hospitality External Connections

```
Organization: Ikyu Corporation
├── ↔ Supplier: HPE Aruba Networking
│   ├── Service: Customer Success Manager
│   ├── Platform: ASM Portal
│   └── Service: 24x7x365 monitoring
├── ↔ Regulator: Japan Government
│   ├── Compliance: APPI
│   └── Standards: Industry standards
```

---

## 7. Entity × Industry Matrix

| Entity Type | Education | Healthcare | Hospitality | Manufacturing | IT Services | Logistics | Retail |
|-------------|-----------|------------|-------------|---------------|-------------|-----------|--------|
| Company | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Department | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Team | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Role | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Site | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| User Group | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Product | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Platform | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Service | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Supplier | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Partner | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Regulator | [N] | [N] | [N] | [N] | [N] | [N] | [N] |

---

## 8. Key Insights

### Pattern 1: Universal Supplier Entity

| Aspect | Finding | Interpretation | Business Implication | Source Cases |
|--------|---------|----------------|--------------------|--------------|
| HPE/Juniper Supplier | Appears in all industries | Vendor ecosystem universal | Vendor partnership positioning | [CASE_IDS] |

### Pattern 2: Industry-Specific User Groups

| Aspect | Finding | Interpretation | Business Implication | Source Cases |
|--------|---------|----------------|--------------------|--------------|
| Students (Education only) | Education-specific user group | Industry-specific primary users | Education user-centric positioning | [CASE_IDS] |

---

## 9. Traceability Summary

| Entity | Source Cases | Original Name | Inference Method |
|--------|--------------|----------------|------------------|
| [ENTITY_1] | [CASE_IDS] | [NAME] | [METHOD] |

---

## Notes

- [ENTITY CLASSIFICATION NOTES]
- [HIERARCHY INFERENCE NOTES]