# Business Insight Quality Framework

## Purpose

This framework defines the minimum quality bar for scenario_modeler outputs. It exists to prevent model synthesis from becoming a table-filling exercise. Every primary model must explain business meaning, decision impact, and evidence strength, not only count patterns.

---

## Core Principle

**Insight before inventory**: Start each primary model with the business interpretation of the evidence, then provide tables and matrices as support.

An output is not considered high quality when it only answers:
- What appeared?
- How often did it appear?
- Which customer said it?

An output is high quality only when it also answers:
- Why does this pattern matter to the customer business?
- What pressure or constraint creates the pattern?
- Which stakeholder decision does it affect?
- What solution capability resolves the pressure?
- What measurable outcome should prove success?
- What evidence weakens or qualifies the conclusion?

---

## Required Business Reasoning Chain

Each major conclusion must follow this chain:

```text
Business Context
  -> Trigger or Pressure
  -> Stakeholder Decision Tension
  -> Purchase Factor
  -> Technical Capability
  -> Measurable Outcome
  -> Risk or Counter-Evidence
  -> Recommended Action
```

### Required Fields

| Field | Question Answered | Quality Bar |
|-------|-------------------|-------------|
| Business Context | What business situation is the customer in? | Industry, operating model, scale, regulation, or strategic goal is named |
| Trigger or Pressure | Why now? | Event, risk, lifecycle change, budget pressure, compliance pressure, or growth pressure is explicit |
| Decision Tension | What trade-off must be resolved? | Names both sides of the tension, such as security depth vs user friction |
| Purchase Factor | What business value is being bought? | Expressed as customer value, not product name |
| Technical Capability | What capability enables the value? | Product may be named, but capability must be named first |
| Measurable Outcome | How should success be verified? | Metric, proxy metric, or measurement gap is stated |
| Risk or Counter-Evidence | What could make this conclusion wrong? | Includes data limitation, missing evidence, or alternative interpretation |
| Recommended Action | What should a seller, analyst, or modeler do next? | Action is specific and tied to the evidence |

---

## Insight Types

Every primary model should include at least three of the following insight types.

| Insight Type | Purpose | Example Prompt |
|--------------|---------|----------------|
| Causal Insight | Explain why a pattern appears | What business pressure causes this purchase factor to recur? |
| Segmentation Insight | Explain where a pattern differs | Which industries or organization types behave differently, and why? |
| Stakeholder Insight | Explain who changes the decision | Which role can accelerate, block, or reframe the purchase? |
| Capability Fit Insight | Explain why a capability matters | Which capability is necessary, differentiating, or merely table stakes? |
| Metric Insight | Explain how value should be proven | Which metrics prove value, and which are only vendor claims? |
| Evolution Insight | Explain change over time | What strengthened, weakened, or emerged across years? |
| Counter-Insight | Explain what the data does not prove | What alternative explanation or missing evidence should temper the conclusion? |
| Action Insight | Translate finding into next step | What should be asked, validated, positioned, or modeled next? |

---

## Anti-Generic Rules

Avoid generic conclusions unless they are immediately sharpened by evidence and implication.

| Generic Output to Avoid | Required Upgrade |
|-------------------------|------------------|
| Security is important | Security is a gating condition for regulated sectors; it becomes differentiating only when paired with low-friction operations or audit automation |
| IT Lead is important | IT Lead is the evidence owner for feasibility and operations risk; budget approval still depends on executive risk framing |
| User experience matters | User experience matters when service continuity or adoption is revenue-, care-, learning-, or citizen-service critical |
| Centralized management reduces complexity | Centralized management matters when site count, team size, policy drift, or audit burden creates operational leverage |
| SD-WAN improves connectivity | SD-WAN matters when application experience, branch resilience, cloud access, and circuit cost are all in tension |

---

## Evidence Strength Rules

Each insight must include an evidence strength label.

| Level | Criteria |
|-------|----------|
| HIGH | Direct quote or metric from multiple customers, consistent across at least two industries or a clearly bounded segment |
| MEDIUM | Direct evidence exists, but sample is narrow, metrics are sparse, or wording comes from vendor case narratives |
| LOW | Inferred from solution selection, weak quote, sparse sample, or taxonomy expectation |

When evidence is LOW or MEDIUM, the model must include a recommended validation question.

---

## Output Quality Rubric

| Dimension | Poor | Acceptable | Strong |
|-----------|------|------------|--------|
| Information Density | Repeats counts and product names | Adds representative quotes and summaries | Compresses evidence into ranked business conclusions with exceptions |
| Depth | Lists what appears | Explains some relationships | Explains causal mechanisms, trade-offs, and decision consequences |
| Business Relevance | Mentions business value generally | Connects factors to industry/stakeholder context | Produces actions for positioning, validation, or scenario design |
| Traceability | Has source IDs only | Has source IDs and quotes | Has source IDs, quotes, confidence, and counter-evidence |
| Specificity | Uses broad categories | Names industries and roles | Names segment, trigger, stakeholder tension, metric, and next step |

---

## Mandatory Primary Model Gate

Before finalizing Industry, Stakeholder, Purchase Factor, or Cross-Analysis outputs, check:

- [ ] The model starts with an executive business insight summary before detailed tables.
- [ ] At least five conclusions use the full business reasoning chain.
- [ ] Each major insight has confidence and evidence basis.
- [ ] Generic statements are sharpened with segment, trigger, stakeholder, or metric detail.
- [ ] Product names are not used as purchase factors.
- [ ] At least three counter-evidence or limitation notes are tied to specific conclusions.
- [ ] Recommended actions are specific enough to drive follow-up survey, sales discovery, or DSL modeling.

