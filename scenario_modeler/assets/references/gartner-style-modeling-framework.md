# Gartner-Style Strategic Modeling Framework

## Purpose

This framework upgrades `scenario_modeler` from cross-case synthesis to strategic market modeling for data communication, networking, and cybersecurity scenarios. It translates customer case evidence into Gartner-style advisory outputs: use-case fit, critical capability assessment, buying committee logic, and competitive positioning.

---

## Core Principle

**Use case before vendor, capability before product, decision before feature.**

Strategic model outputs must not start from product inventory. They must start from:
- Market definition and boundary
- Customer operating model
- Adoption trigger
- Business risk or opportunity
- Buying committee
- Critical capability required
- Evidence strength and measurement gap
- Competitive or substitution context

---

## Required Strategic Models

| Model | Primary Question | Required Output |
|-------|------------------|-----------------|
| Use Case Fit Model | Which customer use cases fit which solution patterns? | Use-case taxonomy, fit scores, adoption triggers, barriers, metrics, scenario implications |
| Critical Capability Model | Which capabilities matter most by use case and industry? | Capability taxonomy, weighting, table-stakes vs differentiators, evidence strength |
| Buying Committee Model | Who actually shapes the purchase and what proof do they need? | Role influence, proof burden, objections, engagement sequence |
| Competitive Positioning Model | What market position, substitution pattern, and vendor narrative does the evidence imply? | Market definition, competitor alternatives, differentiation, risk, proof burden |

---

## Data Communication Domain Taxonomy

| Domain | Scope | Typical Buying Trigger |
|--------|-------|------------------------|
| Campus LAN/WLAN | Campus, school, hospital, hospitality, venue access networks | Coverage, density, user experience, operational simplicity |
| Branch WAN / SD-WAN | Distributed branches, stores, clinics, logistics sites | MPLS replacement, cloud access, resilience, cost optimization |
| SASE / SSE / ZTNA | Remote users, cloud apps, secure access | Hybrid work, VPN replacement, unified policy, user friction reduction |
| NGFW / Firewall Platform | Perimeter, branch, data center, segmentation | Threat exposure, compliance, lifecycle refresh, policy consistency |
| NAC / Identity-Based Access | Device onboarding, segmentation, IoT/OT control | Unauthorized device risk, audit, IoT/IoMT growth |
| AIOps / Observability | Network monitoring, troubleshooting, automation | Staff shortage, ticket volume, MTTR reduction |
| NaaS / Managed Networking | Subscription networking, MSP delivery | Budget smoothing, lifecycle management, skills gap |
| Cloud Networking | Multi-cloud connectivity and cloud security | Cloud migration, app modernization, distributed users |
| Industrial / OT Networking | Manufacturing, utilities, logistics, field operations | Downtime risk, OT segmentation, edge operations |

---

## Gartner-Style Evaluation Rules

### 1. Use-Case-Based Evaluation

Do not score a capability globally. Score it against a specific use case.

Example:
- `Centralized policy management` is differentiating for distributed branch security.
- The same capability may be table stakes for a mature NGFW replacement.

### 2. Table Stakes vs Differentiator

Every capability must be classified:

| Class | Meaning |
|-------|---------|
| Table Stakes | Required to be considered, but not enough to win |
| Differentiator | Changes shortlisting, proof burden, or willingness to pay |
| Emerging Differentiator | Not yet universal, but strategically important |
| Optional Enhancer | Useful but not decision-critical |

### 3. Buying Trigger and Barrier

Every use case and capability must identify:
- Why now?
- What makes adoption hard?
- Which stakeholder can block the project?
- What proof resolves the objection?

### 4. Evidence Strength

Use the same HIGH/MEDIUM/LOW evidence convention as the Business Insight Quality Framework.

Strategic conclusions must explicitly separate:
- Direct customer quote
- Vendor case narrative
- Cross-case frequency
- Analyst inference
- Unsupported measurement gap

### 5. Competitive Context

Strategic outputs must identify the displaced or compared alternative:
- Legacy firewall
- VPN-only architecture
- MPLS WAN
- Manual NAC or static VLAN segmentation
- Multi-console operations
- Best-of-breed security stack
- Integrated platform
- Managed service / NaaS provider

---

## Required Advisory Questions

Each strategic model should answer:

| Question | Why It Matters |
|----------|----------------|
| What market or use case is this evidence really about? | Prevents broad, generic conclusions |
| Which customer segments fit best? | Supports prioritization |
| What is table stakes vs differentiating? | Supports positioning |
| Who needs what proof? | Supports sales execution |
| What metric proves the value? | Supports MoE and ROI |
| What could make this conclusion wrong? | Controls vendor-case bias |
| What scenario should be modeled next? | Connects advisory insight to DSL preparation |

---

## Anti-Patterns

| Anti-Pattern | Required Correction |
|--------------|---------------------|
| "NGFW is important for security" | Name the use case: distributed policy control, audit readiness, segmentation, remote access, or lifecycle refresh |
| "SASE improves experience" | Explain the trade-off: security inspection depth vs user friction for remote/cloud access |
| "AIOps reduces operations burden" | Specify ticket volume, MTTR, operator-to-device ratio, or policy-change workload |
| "CIO is key stakeholder" | Identify funding authority, risk acceptance role, required proof, and likely objection |
| "Vendor X has strong solution breadth" | State whether breadth is a differentiator or merely table stakes for the use case |

---

## Delivery Gate

Strategic model delivery is incomplete unless all four outputs exist:
- `use_case_fit_model.md`
- `critical_capability_model.md`
- `buying_committee_model.md`
- `competitive_positioning_model.md`

Each must include:
- Market/use-case definition
- Segment or industry applicability
- Capability or stakeholder implication
- Evidence strength
- Counter-evidence or limitation
- Recommended action
- Scenario modeling implication
