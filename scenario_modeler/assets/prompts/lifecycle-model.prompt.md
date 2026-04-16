# Lifecycle Model Synthesis Prompt

## Purpose

Synthesize scenario lifecycle patterns from operational scenario sections of multiple scenario_analyzer analysis outputs. Build lifecycle model with phases, triggers, actions, and completion criteria, structured for OpenSCENARIO DSL preparation.

---

## Input Requirements

Provide multiple `-analysis.md` documents with operational scenario sections containing:
- Scenario name
- Description
- Users/participants
- Success criteria
- Traceability reference

---

## Lifecycle Phase Definitions

| Phase | Definition | Typical Trigger | Typical Actions | Typical Completion |
|-------|------------|-----------------|-----------------|--------------------|
| Need Identification | Problem discovery and requirement definition | Performance issue, policy mandate, business change | Assess current state, document requirements, identify stakeholders | Requirements documented, stakeholders identified |
| Evaluation & Selection | Solution research and vendor evaluation | Requirements ready, budget approved | Research solutions, evaluate vendors, compare options | Vendor selected, solution chosen |
| Purchase Decision | Final decision and contract signing | Evaluation complete, proposal ready | Review proposals, negotiate terms, approve budget | Contract signed, budget allocated |
| Deployment | Solution installation and configuration | Contract signed, schedule confirmed | Install hardware, configure software, integrate systems | System installed, configuration complete |
| Acceptance | Testing and validation | Deployment complete, system ready | Run tests, validate requirements, document results | Tests passed, acceptance signed |
| Operations | Daily operation and maintenance | Acceptance complete, system live | Monitor performance, resolve issues, optimize operations | Stable operation, issues resolved |

---

## Analysis Instructions

### Step 1: Scenario Extraction

1. Extract all operational scenarios from operational scenario table
2. Preserve scenario names and descriptions
3. Extract participants/actors
4. Extract success criteria
5. Note industry context for each scenario

### Step 2: Phase Mapping

1. Map each extracted scenario to a Lifecycle Phase
2. Use scenario description and participant actions:
   - "Classroom full-class connection" → Operations (daily use)
   - "School network migration" → Deployment (implementation)
   - "AIOps fault resolution" → Operations (maintenance)
   - "Zero-trust access control" → Operations (security operation)
3. Document reasoning for ambiguous mappings

### Step 3: Trigger Extraction

1. Infer start triggers from scenario context:
   - Previous phase completion
   - External event (policy change, performance issue)
   - Internal event (decision made, contract signed)
2. Normalize trigger expressions
3. Identify common trigger patterns per phase

### Step 4: Action Sequence Analysis

1. Extract actions from scenario descriptions
2. Identify actor for each action
3. Build action sequences with order:
   - Actor1 → Action1 → Actor2 → Action2 → ...
4. Identify parallel vs sequential actions
5. Identify decision points in sequences

### Step 5: Completion Criteria Extraction

1. Extract success criteria from success criteria field
2. Normalize completion expressions:
   - "All students first-connect success" → First-connect success rate: 100%
   - "Minimal downtime, zero-touch configuration" → Downtime: minimal, Configuration: zero-touch
3. Identify quantitative vs qualitative criteria
4. Identify industry-specific criteria patterns

### Step 6: Phase Transition Conditions

1. Identify conditions for phase-to-phase transition
2. Build phase transition graph:
   - Need Identification → Evaluation: "Requirements documented"
   - Evaluation → Decision: "Vendor selected"
   - Decision → Deployment: "Contract signed"
   - Deployment → Acceptance: "Configuration complete"
   - Acceptance → Operations: "Tests passed"
3. Identify rollback conditions (phase regression)

---

## Output Format

Follow the template: `lifecycle-model-template.md`

**Required Sections**:

### 1. Lifecycle Phase Overview

| Phase | Definition | Frequency | Industries | Source Cases |

### 2. Phase Trigger Patterns

| Phase | Typical Triggers | Trigger Types | Source Cases |

### 3. Phase Action Sequences

For each phase, provide action sequence:

```
Phase: Need Identification
├── Trigger: Performance issue detected
├── Actions:
│   ├── IT Lead → Assess current state
│   ├── IT Lead → Document requirements
│   ├── Decision Maker → Confirm budget possibility
├── Completion: Requirements documented
└── Next Phase: Evaluation & Selection
```

### 4. Phase Completion Criteria

| Phase | Quantitative Criteria | Qualitative Criteria | Source Cases |

### 5. Phase Transition Graph

```
Need Identification
  ↓ [Requirements documented]
Evaluation & Selection
  ↓ [Vendor selected]
Purchase Decision
  ↓ [Contract signed]
Deployment
  ↓ [Configuration complete]
Acceptance
  ↓ [Tests passed]
Operations
  ↓ [Stable operation]
```

### 6. Industry × Phase Scenario Matrix

| Industry | Need Identification | Evaluation | Decision | Deployment | Acceptance | Operations |

### 7. Rollback Conditions

| From Phase | To Phase | Condition | Source Cases |

---

## Traceability Requirements

For each phase and action, include:
- Source Cases: Case IDs where this pattern appears
- Original Scenario: Original scenario name from source
- Original Description: Original action description

---

## Quality Checklist

- [ ] All scenarios are mapped to lifecycle phases
- [ ] Triggers are extracted and normalized
- [ ] Action sequences have identified actors
- [ ] Completion criteria are classified by type
- [ ] Phase transitions are documented
- [ ] Rollback conditions are identified

---

## Example Usage

```
Scenario mapping example:
Original: "School network migration | 30 minutes to complete new network deployment | IT team | Minimal downtime, zero-touch configuration"
→ Phase: Deployment
→ Trigger: Purchase decision complete, contract signed
→ Actions:
  ├── IT Lead → Plan migration
  ├── Operator → Execute migration (30 minutes)
  ├── Operator → Validate configuration
→ Completion: Minimal downtime, zero-touch configuration complete
→ Source: Education-UK-06-Aberdeen

Phase transition:
Deployment → Acceptance: Configuration complete, system ready
Acceptance → Operations: Tests passed, acceptance signed
```