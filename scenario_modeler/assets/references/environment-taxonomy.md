# Environment Taxonomy Reference

## Purpose

This document provides standardized environment/context classification for modeling scenario environments across industry, regional, organizational, and technical dimensions.

---

## Industry Environment Taxonomy

### Regulations

| Regulation | Industry | Region | Requirements |
|------------|----------|--------|--------------|
| HIPAA | Healthcare | US | Patient data protection |
| FERPA | Education | US | Student data protection |
| GDPR | All | EU/UK | Personal data protection |
| UK Data Protection Act | All | UK | Data privacy compliance |
| PCI-DSS | Retail | Global | Payment data security |
| NHS Digital Strategy | Healthcare | UK | Healthcare digital transformation |
| APPI | All | Japan | Personal information protection |

### Industry Standards

| Standard | Application | Requirements |
|----------|-------------|--------------|
| IEEE 802.11ax (Wi-Fi 6/6E) | Network | High-density wireless |
| ISO 27001 | Security | Information security management |
| Zero-trust Architecture | Security | Fine-grained access control |
| IEEE 802.1X | Network | Port-based network access control |

### Industry Policies

| Policy | Industry | Region | Requirements |
|--------|----------|--------|--------------|
| 1:1 Device Mandate | Education | Various | Device provision per student |
| NHS Digital Transformation | Healthcare | UK | Healthcare digitization |
| Digital Education Strategy | Education | Various | Education technology adoption |
| Sustainability Mandate | All | Various | Environmental compliance |

---

## Regional Environment Taxonomy

### National Regulations

| Region | Key Regulations | Cultural Traits | Market Maturity | Economic Context |
|--------|-----------------|-----------------|-----------------|------------------|
| UK | GDPR, UK DPA, NHS Strategy | Digital adoption culture | Mature | Public/private mixed |
| US | HIPAA, FERPA, State laws | Innovation-driven | Mature | Private-dominant |
| Japan | APPI, Industry standards | Technology adoption | Mature | Private-dominant |
| EU (Belgium) | GDPR, EU standards | Compliance-focused | Mature | Mixed |
| India | Data Protection Bill, Industry rules | Emerging digital | Growing | Private-dominant |
| Saudi Arabia | Local data laws, Vision 2030 | Transformation-focused | Emerging | Public investment |
| South Africa | POPIA, Industry regulations | Developing digital | Developing | Mixed |
| Australia | Privacy Act, Industry standards | Innovation culture | Mature | Mixed |
| Germany | GDPR, Industry standards | Engineering focus | Mature | Private-dominant |
| Portugal | GDPR, EU standards | EU-aligned | Mature | Mixed |
| Netherlands | GDPR, EU standards | Innovation culture | Mature | Mixed |
| Israel | Privacy Protection Law | Tech innovation | Mature | Private-dominant |
| Austria | GDPR, EU standards | EU-aligned | Mature | Mixed |

### Regional Characteristics

| Region | Budget Type Typical | Procurement Process | Tech Adoption Speed |
|--------|---------------------|--------------------|--------------------|
| UK | Public (municipal), Private (enterprise) | Formal process (public), Faster (private) | High |
| US | Private-dominant | Fast decision cycles | Very High |
| Japan | Private-dominant | Formal approval process | High |
| Saudi Arabia | Public investment | Government-led | Medium-High |
| India | Mixed | Corporate process | Medium-High |

---

## Organizational Environment Taxonomy

### Scale Categories

| Scale Category | Characteristics | Typical Industries |
|----------------|-----------------|--------------------|
| Small (<1000 users) | Single site, limited IT | Small business, clinics |
| Medium (1000-10000) | Multiple sites, dedicated IT | Schools, regional facilities |
| Large (10000-50000) | Many sites, IT department | School districts, universities |
| Very Large (>50000) | Distributed enterprise | Multi-national, government |

### Architecture Types

| Architecture | Characteristics | Typical Contexts |
|--------------|-----------------|-----------------|
| Centralized | Single management point | Single-site organizations |
| Distributed | Multiple sites, local management | Multi-site, regional |
| Federated | Independent sites, shared standards | School districts, university systems |
| Hybrid | Mix of centralized and distributed | Complex organizations |

### Budget Constraints

| Constraint Type | Characteristics | Typical Contexts |
|------------------|-----------------|-----------------|
| CapEx Approval Difficulty | Long approval cycles, budget limits | Public sector, municipal |
| OpEx Preference | Subscription models preferred | Private sector, cost-conscious |
| Budget Limited | Strict budget limits | Small organizations, public |
| Budget Flexible | Faster approval, investment focus | Large private, growth-focused |

### Strategic Directions

| Direction | Characteristics | Typical Industries |
|-----------|-----------------|--------------------|
| Digital Transformation | Technology adoption, process digitization | All industries |
| Sustainability | Environmental focus, efficiency | Manufacturing, hospitality |
| Innovation Leadership | Technology leadership, competitive advantage | IT services, tech-focused |
| Cost Optimization | Efficiency focus, cost reduction | All industries |
| Compliance Focus | Regulatory compliance priority | Healthcare, legal, finance |
| User Experience | Customer/user satisfaction focus | Hospitality, retail, education |

---

## Technical Environment Taxonomy

### Existing Tech Stack

| Stack Type | Characteristics | Typical Contexts |
|------------|-----------------|-----------------|
| Legacy Network | Aging infrastructure, limited capacity | Pre-upgrade state |
| Cloud Services | Cloud-based systems, flexibility | Modern organizations |
| Hybrid Infrastructure | On-premises + cloud | Transitioning organizations |
| Modern Stack | Current technology, capable | Tech-forward organizations |

### Integration Constraints

| Integration | Requirements | Typical Contexts |
|-------------|--------------|-----------------|
| ServiceNow | ITSM integration | IT operations |
| ASM Portal | NaaS management portal | NaaS subscribers |
| Existing Identity Systems | Directory integration | Organizations with IAM |
| Legacy System Integration | Compatibility requirements | Migration contexts |

### Technical Standards Requirements

| Standard | Requirement Type | Typical Industries |
|----------|------------------|--------------------|
| Wi-Fi 6/6E | High-density wireless | Education, hospitality, events |
| Zero-trust | Fine-grained access control | Healthcare, finance, all |
| SD-WAN | Software-defined WAN | Distributed organizations |
| AI-native Operations | AI-driven management | Tech-forward organizations |

---

## Environment Constraint Pattern Library

### Pattern 1: Education + UK + Municipal

| Dimension | Elements |
|-----------|----------|
| Industry | Education (K-12), 1:1 device mandate |
| Regional | UK, GDPR, UK DPA, public budget |
| Organizational | Distributed (67 schools), CapEx approval difficulty |
| Technical | Legacy network, Wi-Fi 6/6E requirement |

### Pattern 2: Healthcare + US + Private

| Dimension | Elements |
|-----------|----------|
| Industry | Healthcare, HIPAA compliance |
| Regional | US, innovation culture, private budget |
| Organizational | Centralized or distributed, budget flexible |
| Technical | Zero-trust requirement, cloud transition |

### Pattern 3: Hospitality + Japan + Private

| Dimension | Elements |
|-----------|----------|
| Industry | Hospitality, guest experience focus |
| Regional | Japan, APPI, formal process, mature market |
| Organizational | Distributed (national offices), OpEx preference |
| Technical | NaaS subscription, cloud management |

### Pattern 4: Manufacturing + Germany + Private

| Dimension | Elements |
|-----------|----------|
| Industry | Manufacturing, efficiency focus |
| Regional | Germany, GDPR, engineering culture |
| Organizational | Centralized, budget for efficiency |
| Technical | AI-native ops, predictive maintenance |

---

## Environment Element Extraction Rules

### From Customer Basic Information

1. Industry → Industry Environment (regulations, standards)
2. Country → Regional Environment (regulations, culture)
3. Company scale description → Organizational Environment (scale, architecture)

### From Pre-deployment Problems

1. Compliance mentions → Industry Environment (regulations)
2. Policy mentions → Industry Environment (policies)
3. Budget mentions → Organizational Environment (constraints)
4. Legacy system mentions → Technical Environment (existing stack)

### From Purchase Factors

1. Security/compliance factors → Industry Environment (compliance)
2. Innovation factors → Strategic Direction
3. Cost factors → Budget Constraints
4. Technical factors → Technical Standards

### From Products/Solutions

1. Integration mentions → Integration Constraints
2. Standard mentions → Technical Standards
3. Vendor ecosystem → Vendor Relationships