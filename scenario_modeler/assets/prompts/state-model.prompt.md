# State Model Synthesis Prompt

## Purpose

Synthesize state patterns from multiple scenario_engine analysis outputs. Build state model with state definitions, state types, and transition conditions for stakeholders, systems, and organizations.

---

## Input Requirements

Provide multiple `-analysis.md` documents with:
- Stakeholder expectations and influence levels
- Pre-deployment problems (initial states)
- Overall benefits/reviews (final states)
- Operational scenarios (state transitions)

---

## State Type Definitions

### Stakeholder States

| State | Definition | Typical Transitions |
|-------|------------|--------------------|
| Need Unidentified | Problem not yet recognized | → Need Identified (problem discovery) |
| Need Identified | Problem recognized, requirements emerging | → Evaluating (solution research) |
| Evaluating | Researching solutions and vendors | → Decision Ready (evaluation complete) |
| Decision Ready | Ready to make purchase decision | → Decided (decision made) |
| Decided | Purchase decision made | → Expecting (awaiting deployment) |
| Expecting | Awaiting deployment completion | → Accepting (deployment complete) |
| Accepting | Testing and validating solution | → Satisfied/Dissatisfied (acceptance complete) |
| Satisfied | Solution meets expectations | → Stable Operation (continued satisfaction) |
| Dissatisfied | Solution fails expectations | → Escalating (issue resolution) |
| Stable Operation | Routine operation with satisfaction | → Upgrading (new requirements) |
| Upgrading | Addressing new needs | → Stable Operation (upgrade complete) |

### System States

| State | Definition | Typical Transitions |
|-------|------------|--------------------|
| Not Deployed | Solution not yet installed | → Deploying (deployment start) |
| Deploying | Installation and configuration ongoing | → Deployed (deployment complete) |
| Deployed | Installation complete, awaiting acceptance | → Running (acceptance passed) |
| Running | Normal operation | → Upgrading (upgrade request) |
| Upgrading | Version update or enhancement | → Running (upgrade complete) |
| Degraded | Partial functionality available | → Running (issue resolved) |
| Fault | System failure or error | → Recovering (fault detected) |
| Recovering | Recovery actions ongoing | → Running (recovery complete) |
| Retired | System decommissioned | → (end state) |

### Organization States

| State | Definition | Typical Transitions |
|-------|------------|--------------------|
| Problem Unrecognized | Organization unaware of issue | → Problem Identified (issue discovery) |
| Problem Identified | Issue recognized, seeking solution | → Solution Seeking (search started) |
| Solution Seeking | Researching potential solutions | → Procurement (solution chosen) |
| Procurement | Purchasing selected solution | → Implementation (contract signed) |
| Implementation | Deploying and configuring solution | → Validation (deployment complete) |
| Validation | Testing and validating | → Normal Operation (validation passed) |
| Normal Operation | Routine operation | → Issue Detected (new problem) |
| Issue Detected | New issue recognized | → Resolution (response started) |
| Resolution | Addressing new issue | → Normal Operation (issue resolved) |

---

## Analysis Instructions

### Step 1: Initial State Extraction

1. Extract pre-deployment problems from each document
2. Identify stakeholder states implied by problems:
   - Network failure → Stakeholder: Need Identified
   - Capacity gap → Stakeholder: Need Identified
   - Compliance issue → Stakeholder: Need Identified
3. Identify system states implied by problems:
   - Legacy network → System: Degraded
   - Capacity lacking → System: Degraded
4. Identify organization states implied by problems:
   - Business impact → Organization: Problem Identified

### Step 2: Final State Extraction

1. Extract overall benefits/reviews from each document
2. Identify stakeholder states implied by results:
   - "100% reduction in tickets" → Stakeholder: Satisfied
   - "all learners connected" → Stakeholder: Satisfied
   - "issues resolved" → Stakeholder: Satisfied
3. Identify system states implied by results:
   - "stable operation" → System: Running
   - "coverage increased" → System: Running
4. Identify organization states implied by results:
   - "digital transformation achieved" → Organization: Normal Operation

### Step 3: Transition Identification

1. From operational scenarios, identify state transitions:
   - "deploy new network" → System: Deploying → Deployed
   - "acceptance testing" → Stakeholder: Accepting → Satisfied
   - "operations maintenance" → System: Running (maintained)
2. Extract transition triggers from scenario descriptions
3. Extract transition conditions from success criteria

### Step 4: State Frequency Analysis

1. Count frequency of each state appearing in documents
2. Build State × Industry matrix
3. Identify typical initial states per industry
4. Identify typical final states per industry

### Step 5: Transition Pattern Analysis

1. Identify common transition sequences:
   - Need Identified → Evaluating → Decided → Satisfied
   - Degraded → Deploying → Running
2. Calculate transition frequency
3. Identify industry-specific transition patterns
4. Identify rare transitions (edge cases)

---

## Output Format

Follow the template: `state-model-template.md`

**Required Sections**:

### 1. Stakeholder State Definition Table

| State | Definition | Typical Transitions | Frequency | Source Cases |

### 2. System State Definition Table

| State | Definition | Typical Transitions | Frequency | Source Cases |

### 3. Organization State Definition Table

| State | Definition | Typical Transitions | Frequency | Source Cases |

### 4. State Transition Diagram

```
Stakeholder States:
Need Unidentified → Need Identified → Evaluating → Decision Ready → Decided → Expecting → Accepting → Satisfied
                                                                      ↓
                                                                  Dissatisfied → Escalating → Satisfied

System States:
Not Deployed → Deploying → Deployed → Running → Upgrading → Running
                                    ↓
                              Degraded/Fault → Recovering → Running
```

### 5. Initial → Final State Mapping

| Initial State | Final State | Transition Path | Trigger | Source Cases |

### 6. Industry × State Matrix

| Industry | Typical Initial (Stakeholder) | Typical Initial (System) | Typical Final (Stakeholder) | Typical Final (System) |

### 7. Transition Condition Table

| From State | To State | Condition | Typical Trigger | Source Cases |

---

## Traceability Requirements

For each state and transition, include:
- Source Cases: Case IDs where this state/transition appears
- Original Quote: Original problem description or benefit description

---

## Quality Checklist

- [ ] All three state types are defined (Stakeholder, System, Organization)
- [ ] Initial states extracted from pre-deployment problems
- [ ] Final states extracted from benefits/reviews
- [ ] Transitions identified from operational scenarios
- [ ] State frequencies are calculated
- [ ] Transition conditions are documented

---

## Example Usage

```
State extraction example:
Original (initial): "Legacy network lacked capacity and coverage, unable to support high-density device connection"
→ Stakeholder State: Need Identified (IT team discovered capacity gap)
→ System State: Degraded (network capacity insufficient)
→ Organization State: Problem Identified (digital transformation blocked)

Original (final): "100% reduction in fault tickets, 2x coverage capacity, all learners first-connect success"
→ Stakeholder State: Satisfied (IT team, teachers, students satisfied)
→ System State: Running (network stable operation)
→ Organization State: Normal Operation (digital transformation goals achieved)

Transition path:
Degraded → Deploying → Running
Trigger: Purchase decision complete, 30 minutes deployment complete
```