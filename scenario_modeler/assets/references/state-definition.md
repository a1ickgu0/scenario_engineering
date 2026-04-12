# State Definition Reference

## Purpose

This document provides standard state definitions for Stakeholder, System, and Organization dimensions, enabling consistent state modeling across scenario analyses.

---

## Stakeholder States

### State Definition Table

| State ID | State | Definition | Entry Condition | Exit Condition |
|----------|-------|------------|-----------------|----------------|
| S01 | Need Unidentified | Problem not yet recognized | Initial state (default) | Problem discovery event |
| S02 | Need Identified | Problem recognized, requirements emerging | Problem confirmed | Solution research initiated |
| S03 | Evaluating | Researching solutions and vendors | Requirements documented | Vendor selection ready |
| S04 | Decision Ready | Ready to make purchase decision | Evaluation complete | Decision process initiated |
| S05 | Decided | Purchase decision made | Decision finalized | Deployment planning |
| S06 | Expecting | Awaiting deployment completion | Decision made, contract signed | Deployment started |
| S07 | Accepting | Testing and validating solution | Deployment complete | Acceptance complete |
| S08 | Satisfied | Solution meets expectations | Acceptance passed | Stable operation |
| S09 | Dissatisfied | Solution fails expectations | Acceptance failed | Issue resolution initiated |
| S10 | Stable Operation | Routine operation with satisfaction | Sustained satisfaction | New requirement or issue |
| S11 | Upgrading | Addressing new needs | New requirement identified | Upgrade complete |
| S12 | Escalating | Seeking issue resolution | Issue unresolved | Resolution found |

### State Transition Rules

```
S01 (Need Unidentified)
  ↓ [Problem discovery] 
S02 (Need Identified)
  ↓ [Requirements documented]
S03 (Evaluating)
  ↓ [Evaluation complete]
S04 (Decision Ready)
  ↓ [Decision made]
S05 (Decided)
  ↓ [Contract signed]
S06 (Expecting)
  ↓ [Deployment started]
S07 (Accepting)
  ↓ [Acceptance passed] → S08 (Satisfied)
  ↓ [Acceptance failed] → S09 (Dissatisfied)
  
S08 (Satisfied)
  ↓ [Sustained operation] → S10 (Stable Operation)
  ↓ [New requirement] → S11 (Upgrading)

S09 (Dissatisfied)
  ↓ [Issue resolution] → S12 (Escalating)
  ↓ [Resolution found] → S08 (Satisfied)

S10 (Stable Operation)
  ↓ [New requirement] → S11 (Upgrading)
  ↓ [Issue detected] → S12 (Escalating)

S11 (Upgrading)
  ↓ [Upgrade complete] → S10 (Stable Operation)

S12 (Escalating)
  ↓ [Resolution found] → S08 (Satisfied) or S10 (Stable Operation)
```

---

## System States

### State Definition Table

| State ID | State | Definition | Entry Condition | Exit Condition |
|----------|-------|------------|-----------------|----------------|
| T01 | Not Deployed | Solution not yet installed | Initial state (pre-purchase) | Deployment initiated |
| T02 | Deploying | Installation and configuration ongoing | Deployment initiated | Installation complete |
| T03 | Deployed | Installation complete, awaiting acceptance | Installation complete | Acceptance testing |
| T04 | Running | Normal operation | Acceptance passed | Issue detected or upgrade requested |
| T05 | Upgrading | Version update or enhancement | Upgrade requested | Upgrade complete |
| T06 | Degraded | Partial functionality available | Partial failure | Issue resolved or escalated |
| T07 | Fault | System failure or error | Critical failure | Recovery initiated |
| T08 | Recovering | Recovery actions ongoing | Fault detected | Recovery complete |
| T09 | Retired | System decommissioned | Retirement decision | End state |

### State Transition Rules

```
T01 (Not Deployed)
  ↓ [Deployment initiated]
T02 (Deploying)
  ↓ [Installation complete] → T03 (Deployed)
  
T03 (Deployed)
  ↓ [Acceptance passed] → T04 (Running)

T04 (Running)
  ↓ [Upgrade requested] → T05 (Upgrading)
  ↓ [Partial failure] → T06 (Degraded)
  ↓ [Critical failure] → T07 (Fault)

T05 (Upgrading)
  ↓ [Upgrade complete] → T04 (Running)

T06 (Degraded)
  ↓ [Issue resolved] → T04 (Running)
  ↓ [Critical failure] → T07 (Fault)

T07 (Fault)
  ↓ [Recovery initiated] → T08 (Recovering)

T08 (Recovering)
  ↓ [Recovery complete] → T04 (Running)
  ↓ [Recovery failed] → T07 (Fault) (re-enter)
```

---

## Organization States

### State Definition Table

| State ID | State | Definition | Entry Condition | Exit Condition |
|----------|-------|------------|-----------------|----------------|
| O01 | Problem Unrecognized | Organization unaware of issue | Initial state (default) | Issue discovery |
| O02 | Problem Identified | Issue recognized, seeking solution | Issue confirmed | Solution search initiated |
| O03 | Solution Seeking | Researching potential solutions | Problem priority set | Solution chosen |
| O04 | Procurement | Purchasing selected solution | Solution approved | Contract signed |
| O05 | Implementation | Deploying and configuring solution | Contract signed | Deployment complete |
| O06 | Validation | Testing and validating | Deployment complete | Validation complete |
| O07 | Normal Operation | Routine operation | Validation passed | Issue detected |
| O08 | Issue Detected | New issue recognized | Issue discovered | Resolution initiated |
| O09 | Resolution | Addressing new issue | Resolution process started | Issue resolved |

### State Transition Rules

```
O01 (Problem Unrecognized)
  ↓ [Issue discovery]
O02 (Problem Identified)
  ↓ [Priority set]
O03 (Solution Seeking)
  ↓ [Solution chosen]
O04 (Procurement)
  ↓ [Contract signed]
O05 (Implementation)
  ↓ [Deployment complete]
O06 (Validation)
  ↓ [Validation passed] → O07 (Normal Operation)
  ↓ [Validation failed] → O08 (Issue Detected)

O07 (Normal Operation)
  ↓ [Issue detected] → O08 (Issue Detected)

O08 (Issue Detected)
  ↓ [Resolution initiated] → O09 (Resolution)

O09 (Resolution)
  ↓ [Issue resolved] → O07 (Normal Operation)
```

---

## State Correlation Matrix

| Organization State | Typical Stakeholder State | Typical System State |
|--------------------|--------------------------|---------------------|
| O01 Problem Unrecognized | S01 Need Unidentified | T01 Not Deployed |
| O02 Problem Identified | S02 Need Identified | T01 Not Deployed |
| O03 Solution Seeking | S03 Evaluating | T01 Not Deployed |
| O04 Procurement | S04-S05 Decision Ready/Decided | T01 Not Deployed |
| O05 Implementation | S06 Expecting | T02 Deploying |
| O06 Validation | S07 Accepting | T03 Deployed |
| O07 Normal Operation | S08/S10 Satisfied/Stable | T04 Running |
| O08 Issue Detected | S09/S12 Dissatisfied/Escalating | T06/T07 Degraded/Fault |
| O09 Resolution | S12 Escalating | T08 Recovering |

---

## State Attribute Definitions

### Influence Level Changes by State

| Stakeholder State | Influence Level Change | Notes |
|-------------------|------------------------|-------|
| Need Unidentified → Identified | Influence awareness increases | Problem recognition |
| Evaluating → Decision Ready | Influence peaks for decision | Decision phase |
| Accepting → Satisfied | Influence validates success | Acceptance phase |
| Dissatisfied → Escalating | Influence applies pressure | Issue escalation |

### Priority Level Changes by State

| Stakeholder State | Priority Level | Notes |
|-------------------|----------------|-------|
| Need Identified | High (problem urgent) | Problem recognition |
| Evaluating | High (decision pending) | Evaluation phase |
| Expecting | Medium-High (awaiting) | Deployment anticipation |
| Accepting | High (validation critical) | Acceptance phase |
| Satisfied | Medium (stable) | Post-acceptance |
| Dissatisfied | High (issue urgent) | Problem state |

---

## State Inference Rules from Source

### From Pre-deployment Problems

| Problem Type | Initial Stakeholder State | Initial System State | Initial Organization State |
|--------------|--------------------------|---------------------|---------------------------|
| Network failure/capacity gap | S02 Need Identified | T01 Not Deployed (or T06 Degraded legacy) | O02 Problem Identified |
| Compliance issue | S02 Need Identified | T01 Not Deployed | O02 Problem Identified |
| Legacy system limitation | S02 Need Identified | T06 Degraded | O02 Problem Identified |
| Business transformation need | S02 Need Identified | T01 Not Deployed | O02 Problem Identified |

### From Overall Benefits

| Benefit Type | Final Stakeholder State | Final System State | Final Organization State |
|--------------|------------------------|--------------------|-------------------------|
| "100% reduction in tickets" | S08 Satisfied | T04 Running | O07 Normal Operation |
| "all learners connected" | S08/S10 Satisfied/Stable | T04 Running | O07 Normal Operation |
| "stable operation achieved" | S10 Stable Operation | T04 Running | O07 Normal Operation |
| "digital transformation achieved" | S10 Stable Operation | T04 Running | O07 Normal Operation |

---

## State Duration Reference

| State | Typical Duration | Notes |
|-------|------------------|-------|
| Deploying (T02) | 30min - 2hr | Network deployment typical |
| Accepting (S07) | 1hr - 1day | Testing and validation |
| Recovering (T08) | minutes - hours | Depends on fault severity |
| Evaluation (S03) | weeks - months | Vendor evaluation period |
| Stable Operation (S10/T04) | ongoing | Normal operating state |