# Industry Taxonomy Reference

## Purpose

This document provides standard industry classification taxonomy for organizing and analyzing scenario_engine outputs. It defines primary and secondary industry categories.

---

## Primary Industry Categories

| Category | Definition | Typical Characteristics |
|----------|------------|------------------------|
| Education | Educational institutions and services | Policy mandates, student/teacher users, digital transformation goals |
| Healthcare | Medical and healthcare services | Compliance requirements (HIPAA), patient care focus, data security |
| Hospitality | Hotels, travel, hospitality services | Guest experience focus, distributed locations, subscription models |
| Manufacturing | Manufacturing and production | Efficiency focus, operational continuity, predictive maintenance |
| IT Services | IT services and solutions providers | Technology adoption, managed services, cloud transition |
| Logistics | Logistics and transportation | Network connectivity, supply chain integration, efficiency |
| Retail | Retail and consumer services | Customer experience, omnichannel, data analytics |
| Services & Utilities | Professional services, utilities | Service delivery, regulatory compliance, operational efficiency |
| Sports & Entertainment | Sports, entertainment, events | Fan engagement, high-density connectivity, real-time applications |
| Legal Services | Legal and professional services | Data security, compliance, client service |
| Research & Higher Education | Research institutions, universities | Research focus, innovation, collaboration platforms |

---

## Secondary Industry Classification

### Education Sub-Categories

| Sub-Category | Definition | Example Cases |
|--------------|------------|---------------|
| K-12 Education | Primary and secondary schools | Aberdeen City Council, Alleyn's School, Annie Wright Schools |
| Higher Education | Universities and colleges | Keele University, Canterbury Christ Church, London Metropolitan, Thomas More |
| School District | Multi-school district administration | Moreno Valley USD |

### Healthcare Sub-Categories

| Sub-Category | Definition | Example Cases |
|--------------|------------|---------------|
| Hospital | Hospital and medical center | Royal Devon Healthcare |
| NHS Trust | UK NHS Foundation Trust | Royal Devon Healthcare |
| Veterinary | Animal healthcare | West Park Animal Hospital |

### Hospitality Sub-Categories

| Sub-Category | Definition | Example Cases |
|--------------|------------|---------------|
| Hotel | Hotel and accommodation | Southern Sun, Aethos London, Ikyu Corporation |
| Resort | Resort and tourism | Pueblo Bonito, Red Sea Global |
| Travel Service | Online travel and booking | Ikyu Corporation, The Social Hub |

### Manufacturing Sub-Categories

| Sub-Category | Definition | Example Cases |
|--------------|------------|---------------|
| General Manufacturing | Manufacturing operations | Colep Packaging |
| Defense Manufacturing | Defense and military manufacturing | Australian Defence Apparel |
| Digital Twin / Smart Manufacturing | Advanced manufacturing with digital twin | Bosch Digital Twin |

### IT Services Sub-Categories

| Sub-Category | Definition | Example Cases |
|--------------|------------|---------------|
| IT Service Provider | IT services company | Intdev |
| Datacenter Services | Datacenter operations | Kyndryl Datacenter |

---

## Industry × Region Matrix (from source cases)

| Industry | UK | US | Japan | Belgium | India | SaudiArabia | SouthAfrica | Australia | Portugal | Germany | Mexico | Netherlands | Israel | Austria |
|----------|----|----|-------|---------|-------|-------------|-------------|-----------|----------|---------|--------|-------------|--------|---------|
| Education | 2 | 2 | - | - | - | - | - | - | - | - | - | - | - | - |
| Higher Education | 3 | - | - | 2 | 1 | - | - | - | - | - | - | - | - | - |
| Healthcare | 1 | 1 | - | - | - | - | - | - | - | - | - | - | - | - |
| Hospitality | 1 | - | 1 | - | - | 1 | 1 | - | - | - | 1 | 1 | - | - |
| Manufacturing | - | - | - | - | - | - | - | 1 | 1 | 2 | - | - | - | - |
| IT Services | - | 1 | - | - | - | - | 1 | - | - | - | - | - | - | - |
| Logistics | - | - | - | - | - | - | - | - | - | 1 | - | - | - | - |
| Retail | - | - | - | - | - | - | - | - | - | - | - | - | 1 | 1 |
| Services & Utilities | 1 | - | - | - | - | - | - | - | - | 1 | - | - | - | - |
| Sports & Entertainment | 1 | - | - | - | - | 1 | - | - | - | - | - | - | - | - |
| Legal Services | 1 | - | - | - | - | - | - | - | - | - | - | - | - | - |

---

## Industry Characteristics Summary

| Industry | Primary Purchase Driver | Typical Stakeholders | Typical Solutions | Key Metrics |
|----------|------------------------|---------------------|-------------------|-------------|
| Education | User Experience (student connectivity) | IT Lead, Teachers, Students | Wi-Fi APs, Mist Cloud, Marvis AI | Coverage rate, First-connect success |
| Healthcare | Security/Compliance | IT Lead, Doctors, Regulators | Zero-trust, Secure network | Compliance rate, Data security |
| Hospitality | Cost + Efficiency | IT Lead, Guests, CSM | NaaS, SD-WAN, Cloud management | Subscription cost, Response time |
| Manufacturing | Efficiency + Cost | IT Lead, Operators, Management | AI-native ops, Predictive maintenance | Ticket reduction, Efficiency gain |
| IT Services | Innovation + Efficiency | IT Lead, Clients, Partners | Cloud services, Managed services | Revenue growth, Service quality |
| Logistics | Security + Efficiency | IT Lead, Operators, Suppliers | Zero-trust, SD-WAN | Network security, Integration speed |
| Retail | User Experience + Data | IT Lead, Customers, Staff | Analytics platform, Omnichannel | Customer satisfaction, Data insights |
| Services & Utilities | Efficiency + Compliance | IT Lead, Operators, Regulators | Cloud mgmt, Compliance tools | Service efficiency, Compliance rate |
| Sports & Entertainment | User Experience | IT Lead, Fans, Event staff | High-density Wi-Fi, Real-time apps | Fan engagement, Connectivity rate |
| Legal Services | Security + Compliance | IT Lead, Lawyers, Clients | Data protection, Secure access | Data security, Client service |
| Research & Higher Education | Innovation + Collaboration | Researchers, IT Lead, Students | AI platform, Collaboration tools | Research output, Innovation index |

---

## Industry Identification Rules

### From Document Metadata

1. Extract industry from customer basic information table
2. Use standardized category names
3. Map to primary category first
4. Identify sub-category from company description

### From Company Description

1. Company type keywords:
   - "School", "University", "College", "USD" → Education
   - "Hospital", "NHS", "Healthcare", "Clinic" → Healthcare
   - "Hotel", "Resort", "Travel", "Tourism" → Hospitality
   - "Manufacturing", "Production", "Factory" → Manufacturing
   - "IT Services", "Datacenter", "Technology" → IT Services
   - "Logistics", "Transportation", "Supply Chain" → Logistics
   - "Retail", "Store", "Pharmacy", "Supermarket" → Retail

### From Purchase Factors

1. Factor patterns per industry:
   - "student connectivity", "1:1 device" → Education
   - "HIPAA", "patient data", "healthcare" → Healthcare
   - "guest experience", "hotel operations" → Hospitality
   - "production efficiency", "predictive maintenance" → Manufacturing

---

## Industry-Specific Notes

### Education Notes

- Policy mandates common (1:1 device, national goals)
- High user density (students, teachers)
- Distributed sites (multiple schools)
- Budget approval complexity (public sector)

### Healthcare Notes

- Compliance requirements mandatory (HIPAA, GDPR)
- Patient data security critical
- Regional health outcomes focus
- NHS specific governance (UK)

### Hospitality Notes

- Guest experience primary driver
- Distributed locations (national/global)
- Subscription models preferred (NaaS)
- External service providers common

### Manufacturing Notes

- Operational continuity critical
- Efficiency improvement focus
- Predictive maintenance adoption
- Supply chain integration needs