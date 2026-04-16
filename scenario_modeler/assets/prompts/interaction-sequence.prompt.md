# Interaction Sequence Model Synthesis Prompt

## Purpose

Synthesize interaction sequence patterns from operational scenarios of multiple scenario_analyzer analysis outputs. Build interaction sequence model with actors, actions, triggers, conditions, and state transitions for OpenSCENARIO DSL preparation.

---

## Input Requirements

Provide multiple `-analysis.md` documents with operational scenario sections containing:
- Scenario name
- Description with actions
- Actors
- Success criteria
- Traceability reference

---

## Interaction Sequence Structure

```
Interaction Sequence
├── Sequence ID: Unique identifier
├── Sequence Name: Descriptive name
├── Phase Context: Associated lifecycle phase
├── Trigger: Start condition/event
├── Actors: Participants in sequence
│   ├── Actor1: Role/Entity
│   ├── Actor2: Role/Entity
│   └── ...
├── Actions: Action sequence with order
│   ├── Action1: Actor → Action
│   ├── Action2: Actor → Action
│   └── ...
├── Conditions: Execution conditions
│   ├── Pre-condition: Before sequence starts
│   ├── Execution condition: During execution
│   └── Post-condition: After completion
├── Result: Outcome description
└── State Transition: State change resulting from sequence
```

---

## Action Type Definitions

| Action Type | Definition | Examples |
|-------------|------------|----------|
| Assess | Evaluate current state or capability | Assess network capacity, Evaluate vendor options |
| Document | Record information formally | Document requirements, Create deployment plan |
| Communicate | Exchange information | Report to management, Discuss with vendor |
| Configure | Set system parameters | Configure network, Set access policies |
| Deploy | Install or implement | Deploy new network, Install hardware |
| Test | Validate functionality | Run acceptance tests, Validate connectivity |
| Approve | Authorize decision | Approve budget, Sign contract |
| Monitor | Observe system status | Monitor performance, Check network status |
| Resolve | Fix issues | Resolve fault, Troubleshoot problem |
| Optimize | Improve performance | Optimize configuration, Tune parameters |
| Use | Operate system | Use Wi-Fi, Access network |
| Report | Provide information | Report issues, Submit status report |

---

## Analysis Instructions

### Step 1: Scenario Parsing

1. Extract each operational scenario from source documents
2. Parse scenario description to identify:
   - Actions mentioned (e.g., "deploy", "validate", "connect")
   - Actors involved (e.g., "IT team", "teachers", "students")
   - Sequence implied (order of actions)
3. Preserve original wording for actions

### Step 2: Actor Identification

1. Extract actors from users/participants field
2. Infer additional actors from action descriptions:
   - "IT team deploys" → Actor: IT Team
   - "Marvis AI identifies problem" → Actor: Marvis AI (System)
3. Map actors to stakeholder categories
4. Identify actor roles per action

### Step 3: Action Sequence Building

1. Identify action sequence order from description:
   - Temporal order: "First X, then Y, finally Z"
   - Logical order: X enables Y, Y requires X
2. Assign each action to its actor
3. Build ordered action list:
   ```
   1. IT Lead → Assess current network
   2. IT Lead → Document requirements
   3. IT Team → Deploy new network
   4. IT Team → Configure settings
   5. Teachers → Test connectivity
   6. Students → Use network
   ```
4. Handle parallel actions (multiple actors doing simultaneous actions)

### Step 4: Trigger Extraction

1. Infer triggers from scenario context:
   - Previous scenario completion
   - External event (policy change, performance issue)
   - Internal decision (purchase made, budget approved)
2. Normalize trigger expressions
3. Classify trigger types:
   - Event trigger: Specific event occurrence
   - Time trigger: Time-based condition
   - State triggers: State change condition

### Step 5: Condition Extraction

1. Extract success criteria from success criteria field
2. Classify by condition type:
   - Pre-condition: Must be true before sequence starts
   - Execution condition: Must be maintained during execution
   - Post-condition: Must be true after completion
3. Normalize condition expressions
4. Identify quantitative vs qualitative conditions

### Step 6: State Transition Mapping

1. Identify state before sequence (pre-state)
2. Identify state after sequence (post-state)
3. Build state transition pair
4. Link transition to conditions

### Step 7: Sequence Frequency Analysis

1. Count frequency of similar sequences across documents
2. Identify common sequence patterns per phase
3. Identify industry-specific sequences
4. Build sequence template library

---

## Output Format

Follow the template: `interaction-sequence-template.md`

**Required Sections**:

### 1. Interaction Sequence Catalog

| Sequence ID | Sequence Name | Phase | Trigger | Actors | Source Cases |

### 2. Detailed Sequence Definition

For each sequence:

```
Sequence: Classroom Full-Class Connection
├── Phase: Operations
├── Trigger: Class session starts, students attempt connection
├── Actors:
│   ├── Teacher (User)
│   └── Students (User Group)
│   └── Wi-Fi Network (System)
├── Actions:
│   ├── 1. Students → Attempt Wi-Fi connection (Use)
│   ├── 2. Wi-Fi Network → Authenticate devices (Configure)
│   ├── 3. Wi-Fi Network → Provide connectivity (Serve)
│   ├── 4. Teacher → Verify all connected (Monitor)
│   └── 5. Teacher → Report success (Report)
├── Conditions:
│   ├── Pre: Network deployed and configured
│   ├── Execution: Wi-Fi coverage available
│   └── Post: All students connected (100% success rate)
├── Result: First-connect success for all learners
├── State Transition: Expecting → Satisfied (Stakeholder)
└── Source: Education-UK-06-Aberdeen
```

### 3. Action Type Frequency Table

| Action Type | Frequency | Typical Actors | Typical Phase | Source Cases |

### 4. Trigger Type Frequency Table

| Trigger Type | Frequency | Typical Sequences | Source Cases |

### 5. Condition Type Frequency Table

| Condition Type | Frequency | Typical Expressions | Source Cases |

### 6. Industry × Sequence Pattern Matrix

| Industry | Typical Deployment Sequences | Typical Operations Sequences | Typical Resolution Sequences |

### 7. Sequence Template Library

| Template Name | Phases | Actors | Action Pattern | Conditions | Frequency |

---

## Traceability Requirements

For each sequence entry, include:
- Source Cases: Case IDs where this sequence appears
- Original Scenario Name: Original scenario name from source
- Original Description: Original action description wording

---

## Quality Checklist

- [ ] All operational scenarios are parsed
- [ ] Actors are identified for each action
- [ ] Action sequences are ordered correctly
- [ ] Triggers are extracted and classified
- [ ] Conditions are extracted and classified
- [ ] State transitions are mapped
- [ ] Sequence templates are identified

---

## Example Usage

```
Scenario parsing example:
Original: "School network migration | 30 minutes to complete new network deployment | IT team | Minimal downtime, zero-touch configuration"
→ Sequence: School Network Migration
→ Phase: Deployment
→ Trigger: Purchase decision complete, schedule confirmed
→ Actors: IT Team (Operator), Mist Cloud (System)
→ Actions:
  1. IT Team → Plan migration (Document)
  2. Mist Cloud → Generate configuration (Configure)
  3. IT Team → Execute migration (Deploy) [30 min]
  4. IT Team → Validate settings (Test)
→ Conditions:
  Pre: New equipment ready, configuration generated
  Execution: Minimal downtime target (30 min)
  Post: Configuration complete, network operational
→ State Transition: Deploying → Running (System)
→ Source: Education-UK-06-Aberdeen

Sequence template:
Deployment sequence template: Assess → Plan → Configure → Deploy → Validate
```