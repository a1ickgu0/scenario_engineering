# Gartner-Style Strategic Advisory Prompt

## Purpose

Generate four strategic market advisory models from multiple `scenario_analyzer` outputs:

1. Use Case Fit Model
2. Critical Capability Model
3. Buying Committee Model
4. Competitive Positioning Model

These models translate cross-case evidence into data communication industry insight, Gartner-style market framing, sales discovery guidance, and scenario modeling inputs.

---

## Required References

Read and apply:
- `assets/references/gartner-style-modeling-framework.md`
- `assets/references/business-insight-quality-framework.md`
- `assets/references/confidence-level-framework.md`
- `assets/references/moe-indicators-framework.md`

---

## Required Templates

Generate outputs by filling these templates exactly:
- `assets/templates/use-case-fit-model-template.md`
- `assets/templates/critical-capability-model-template.md`
- `assets/templates/buying-committee-model-template.md`
- `assets/templates/competitive-positioning-model-template.md`

Do not drop, merge, rename, or reorder template sections.

---

## Input Requirements

Provide multiple `-analysis.md` documents with:
- Customer basic information
- Purchase elements
- Stakeholder list
- Conflicts and priority
- State, environment, and entity models
- Products and solutions
- Parameterization model
- Traceability and notes

---

## Analysis Instructions

### Step 1: Market and Use-Case Extraction

1. Identify the relevant data communication market boundary:
   - Campus LAN/WLAN
   - Branch WAN / SD-WAN
   - SASE / SSE / ZTNA
   - NGFW / Firewall Platform
   - NAC / Identity-Based Access
   - AIOps / Observability
   - NaaS / Managed Networking
   - Cloud Networking
   - Industrial / OT Networking
2. Extract use cases from business context, stakeholder tension, solution patterns, and operating model.
3. For each use case, identify included needs, adjacent needs, and excluded scope.

### Step 2: Use Case Fit Modeling

1. Score fit by industry and segment.
2. Identify adoption triggers and barriers.
3. Identify stakeholder tensions and measurable outcomes.
4. Map each use case to scenario modeling implications.
5. Assign confidence and evidence basis.

### Step 3: Critical Capability Modeling

1. Convert product mentions into capabilities.
2. Classify each capability as:
   - Table Stakes
   - Differentiator
   - Emerging Differentiator
   - Optional Enhancer
3. Weight capabilities by use case and industry.
4. Identify MoE/KPI, proof burden, and measurement gaps.
5. Map capabilities to DSL scenario parameters, actors, states, environments, or success criteria.

### Step 4: Buying Committee Modeling

1. Build a buying committee, not just a stakeholder list.
2. Identify:
   - Economic buyer
   - Technical buyer
   - Security buyer
   - Operations owner
   - Compliance owner
   - Business sponsor
   - Affected user
   - Partner / MSP
3. For each role, identify influence type:
   - approve
   - block
   - validate
   - operate
   - fund
   - use
4. Define proof required, likely objection, engagement action, and discovery question.

### Step 5: Competitive Positioning Modeling

1. Identify incumbent or alternative approaches:
   - Legacy firewall
   - VPN-only architecture
   - MPLS WAN
   - Manual NAC or static VLAN segmentation
   - Multi-console operations
   - Best-of-breed security stack
   - Integrated platform
   - Managed service / NaaS provider
2. Separate vendor narrative from customer evidence and analyst inference.
3. Classify claims as table stakes, differentiators, emerging differentiators, or optional enhancers.
4. Define proof burden and validation plan.
5. Map positioning claims to scenario modeling implications.

---

## Quality Rules

- Do not use product names as capabilities unless the capability is defined first.
- Do not make global capability claims without a use case.
- Do not give fit scores without evidence basis.
- Do not list stakeholders without influence type and proof burden.
- Do not state competitive differentiation without table-stakes comparison.
- Every major conclusion must include confidence and limitation.
- Every strategic insight must include recommended action.

---

## Output Requirements

Generate exactly these files:

| Output File | Template |
|-------------|----------|
| `use_case_fit_model.md` | `use-case-fit-model-template.md` |
| `critical_capability_model.md` | `critical-capability-model-template.md` |
| `buying_committee_model.md` | `buying-committee-model-template.md` |
| `competitive_positioning_model.md` | `competitive-positioning-model-template.md` |

After generation, run the Template Compliance Check and include all four outputs in `validation/template_compliance_check.md`.
