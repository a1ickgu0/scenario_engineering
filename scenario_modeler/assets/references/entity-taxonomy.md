# Entity Taxonomy Reference

## Purpose

This document provides standardized entity classification for modeling organizations, systems, and external entities in scenario analysis.

---

## Organization Entity Taxonomy

### Entity Type Definitions

| Entity Type | Definition | Attributes | Examples |
|-------------|------------|------------|----------|
| Company | Main organization entity | Name, Industry, Region, Scale | Aberdeen City Council, Ikyu Corporation |
| Department | Organizational unit | Name, Function, Parent Company | Digital Infrastructure, School Administration |
| Team | Working group | Name, Role, Parent Department | IT Operations Team, Security Team |
| Role | Individual position | Name, Title, Parent Team/Department | Digital Infrastructure Manager, IT Director |
| Site | Physical location | Name, Type, Address, Parent Company | School Site, Office Location, Hospital |
| User Group | Grouped users | Name, Scale, Type, Parent Site | Students (26,500), Teachers, Employees |

### Organization Entity Attributes

| Attribute | Definition | Values |
|-----------|------------|--------|
| org_name | Organization name | String (from document) |
| org_type | Organization type | municipal, private, public, ngo |
| org_industry | Industry classification | Education, Healthcare, etc. |
| org_region | Geographic location | UK, US, Japan, etc. |
| org_scale | Size category | small, medium, large, very_large |
| org_architecture | Structure type | centralized, distributed, federated, hybrid |
| org_budget_type | Budget classification | public, private, mixed |

### Organization Hierarchy Template

```
Company: [Organization Name]
├── Department: [Function-based department]
│   ├── Team: [Working group]
│   │   ├── Role: [Position]
│   │   └── Role: [Position]
│   └── Team: [Working group]
├── Department: [Another department]
│   └── Team: [Working group]
├── Site: [Physical location 1]
│   ├── User Group: [Users at site]
│   └── Department: [Site-level department]
├── Site: [Physical location 2]
│   └── User Group: [Users at site]
```

### Organization Type Mapping

| Organization Context | org_type | org_budget_type | Examples |
|---------------------|----------|-----------------|----------|
| City Council, Municipal | municipal | public | Aberdeen City Council |
| NHS Foundation Trust | public | public | Royal Devon Healthcare |
| School, University | public/private | varies | Alleyn's School (private), Keele University (public) |
| Corporation, Company | private | private | Ikyu Corporation, Colep Packaging |
| School District | public | public | Moreno Valley USD |
| Hospital (private) | private | private | West Park Animal Hospital |

---

## System Entity Taxonomy

### Entity Type Definitions

| Entity Type | Definition | Attributes | Examples |
|-------------|------------|------------|----------|
| Product | Commercial product | Name, Vendor, Version, Category | Juniper AP34, EX4650 Switch |
| Platform | Management platform | Name, Vendor, Features | Mist Cloud, Aruba Central |
| Service | Delivered service | Name, Provider, Type | Marvis AI, Access Assurance |
| Solution | Integrated solution | Name, Components, Purpose | HPE Juniper Networking |
| Component | Technical component | Name, Type, Parent Solution | Wi-Fi AP, Switch, Security module |

### System Entity Attributes

| Attribute | Definition | Values |
|-----------|------------|--------|
| sys_name | Product/service name | String (from document) |
| sys_vendor | Vendor/provider | HPE, Juniper, Aruba, etc. |
| sys_category | Product category | hardware, software, platform, service |
| sys_version | Version information | String (if available) |
| sys_function | Primary function | network, security, management, analytics |
| sys_state | Current state | not_deployed, deploying, running, etc. |

### System Composition Template

```
Solution: [Solution Name]
├── Platform: [Management platform]
│   ├── Service: [AI service]
│   ├── Service: [Assurance service]
│   └── Feature: [Platform feature]
├── Product: [Hardware product]
│   └── Component: [Product component]
├── Product: [Another hardware]
├── Service: [Support service]
└── Service: [Security service]
```

### Product Category Mapping

| Product/Service | sys_category | sys_function | sys_vendor |
|-----------------|--------------|--------------|------------|
| Juniper AP34/AP45 | hardware | network | Juniper |
| Juniper EX4650 Switch | hardware | network | Juniper |
| Mist Cloud | platform | management | Juniper |
| Marvis AI | service | analytics | Juniper |
| Access Assurance | service | security | Juniper |
| HPE GreenLake NaaS | solution | network | HPE |
| Aruba Central | platform | management | HPE Aruba |
| SD-WAN EdgeConnect | software | network | HPE Aruba |

---

## External Entity Taxonomy

### Entity Type Definitions

| Entity Type | Definition | Attributes | Examples |
|-------------|------------|------------|----------|
| Supplier | Product/service provider | Name, Type, Products | HPE Aruba Networking, Juniper |
| Partner | Collaborative partner | Name, Role, Services | System integrator, Consultant |
| Regulator | Regulatory body | Name, Type, Requirements | Government agency, NHS Trust |
| Service Provider | External service provider | Name, Type, Services | Managed service provider, CSM |

### External Entity Attributes

| Attribute | Definition | Values |
|-----------|------------|--------|
| ext_name | Entity name | String |
| ext_type | Entity type | supplier, partner, regulator, service_provider |
| ext_relationship | Relationship to org | vendor, consultant, oversight, support |
| ext_services | Services provided | List of services |
| ext_requirements | Requirements imposed | List of requirements |

### External Entity Connection Template

```
Organization: [Organization Name]
├── ↔ Supplier: [Vendor name]
│   ├── Products: [Product list]
│   ├── Services: [Service list]
│   └── Support: [Support type]
├── ↔ Partner: [Partner name]
│   ├── Role: [Partner role]
│   └── Services: [Service list]
├── ↔ Regulator: [Regulatory body]
│   ├── Requirements: [Requirement list]
│   └── Compliance: [Compliance standards]
└── ↔ Service Provider: [Provider name]
    ├── Services: [Managed services]
    └── Level: [Service level]
```

### External Entity Mapping

| External Role from Document | ext_type | ext_relationship | Examples |
|-----------------------------|----------|------------------|----------|
| Customer Success Manager (HPE) | supplier | support | Lifecycle management support |
| ASM Support Team | supplier | support | Managed service support |
| HPE Aruba Networking | supplier | vendor | Product provider |
| Municipal Government | regulator | oversight | Policy mandate source |
| NHS Foundation Trust | regulator | oversight | Healthcare governance |
| System Integrator | partner | consultant | Integration services |

---

## Entity Inference Rules

### From Customer Basic Information

1. Company name → Company entity
2. Industry → org_industry attribute
3. Country → org_region attribute
4. Company scale → org_scale attribute (inferred)

### From Stakeholder Listings

1. Role names → Role entities
2. Role hierarchy → Department/Team entities (inferred)
3. User groups → User Group entities
4. External stakeholders → External entities

### From Products/Solutions

1. Product names → Product entities
2. Platform names → Platform entities
3. Service names → Service entities
4. Solution names → Solution entities (composition inferred)

### From Pre-deployment Problems

1. Site mentions → Site entities
2. Scale mentions → User Group entities
3. Legacy system → System entity (state: degraded)

---

## Entity Frequency Analysis Template

| Entity Type | Entity Name | Frequency | Industries | Source Cases |
|-------------|-------------|-----------|------------|--------------|

**Example**:
| Role | Digital Infrastructure Manager | 5 | Education, Healthcare | Aberdeen, Keele, Royal Devon |