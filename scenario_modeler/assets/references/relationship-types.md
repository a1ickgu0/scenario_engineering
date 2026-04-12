# Relationship Types Reference

## Purpose

This document provides standardized relationship type definitions for modeling entity and stakeholder relations in scenario analysis.

---

## Hierarchical Relations

### Relation Type Definitions

| Relation Type | Definition | From Entity | To Entity | Example |
|---------------|------------|-------------|-----------|---------|
| Supervision | Superior manages subordinate | Higher role | Lower role | CEO → CIO |
| Reporting | Subordinate reports to superior | Lower role | Higher role | IT Director → CFO |
| Authorization | Authority delegation | Authority holder | Delegate | Board → CEO |
| Composition | Entity composed of sub-entities | Parent entity | Child entity | Organization → Departments |
| Membership | Member belongs to group | Individual | Group | Employee → Department |

### Hierarchical Relation Patterns

```
Supervision Chain:
CEO → CIO → IT Director → IT Operations Team → IT Service Desk

Composition Tree:
Organization
├── Department: Digital Infrastructure
│   ├── Team: IT Operations
│   └── Team: Network Admin
├── Department: Finance
│   └── Role: CFO
└── Site: School Locations
    ├── User Group: Teachers
    └── User Group: Students
```

### Hierarchical Relation Attributes

| Attribute | Definition | Values |
|-----------|------------|--------|
| relation_type | Relation classification | supervision, reporting, authorization, composition, membership |
| direction | Relation direction | top-down, bottom-up, bidirectional |
| strength | Relation strength | strong, medium, weak |
| formal | Formal/informal | formal, informal |

---

## Collaborative Relations

### Relation Type Definitions

| Relation Type | Definition | Entity Pair | Example |
|---------------|------------|-------------|---------|
| Cooperation | Joint work toward common goal | Peer entities | IT Team ↔ Teachers (deployment) |
| Communication | Information exchange | Any entity pair | IT Director ↔ Vendor CSM |
| Support | One provides support to another | Provider → Receiver | CSM → IT Team |
| Service Delivery | Service provision | Provider → Receiver | Vendor → Organization |
| Consultation | Advisory interaction | Consultant → Client | Consultant → Management |

### Collaborative Relation Patterns

```
Purchase Collaboration Network:
├── Decision Maker ↔ IT Lead (Communication: technical assessment)
├── IT Lead ↔ Vendor CSM (Communication: solution proposal)
├── Decision Maker ↔ CFO (Communication: budget approval)
├── IT Lead ↔ IT Team (Cooperation: evaluation support)
└── Vendor ↔ Organization (Service Delivery)

Deployment Collaboration:
├── IT Team ↔ Vendor Support (Support: deployment guidance)
├── IT Team ↔ Site Staff (Cooperation: local coordination)
└── IT Lead ↔ Users (Communication: change notification)
```

### Collaborative Relation Attributes

| Attribute | Definition | Values |
|-----------|------------|--------|
| relation_type | Relation classification | cooperation, communication, support, service_delivery, consultation |
| context | Relation context | purchase, deployment, operations, evaluation |
| frequency | Interaction frequency | high, medium, low, periodic |
| channel | Communication channel | meeting, report, portal, direct |

---

## Conflicting Relations

### Relation Type Definitions

| Relation Type | Definition | Entity Pair | Example |
|---------------|------------|-------------|---------|
| Goal Conflict | Competing objectives | Role pair | Cost Optimization ↔ Quality Improvement |
| Resource Conflict | Resource allocation disagreement | Role pair | IT Team ↔ Finance (budget) |
| Priority Conflict | Priority disagreement | Role pair | Security ↔ Convenience (access policy) |
| Interest Conflict | Stakeholder interest differences | Role pair | IT Team ↔ Users (change resistance) |
| Approach Conflict | Different solution preferences | Role pair | In-house ↔ Outsourced (operations) |

### Conflict Pattern Library

| Conflict Pattern | Entity Pair | Root Cause | Resolution Pattern | Frequency |
|------------------|-------------|------------|--------------------|-----------|
| Cost vs Quality | Decision Maker ↔ IT Lead | Budget constraints vs capability needs | Prioritize ROI justification | High |
| Cost vs Security | Finance ↔ IT Lead | Budget vs compliance | Prioritize compliance requirements | Medium-High |
| Security vs Convenience | IT Lead ↔ Users | Security measures vs usability | Balance policy, user experience | Medium |
| Innovation vs Stability | Management ↔ IT Team | New vs reliable | Phased rollout | Medium |
| Capacity vs Cost | IT Lead ↔ Finance | Scaling needs vs budget | Subscription model | Medium |
| Automation vs Control | IT Team ↔ Management | Automated vs manual | AI-assisted, human oversight | Low |

### Conflict Resolution Strategies

| Strategy | Application | Example |
|----------|-------------|---------|
| Prioritize X over Y | Clear priority case | Security > Convenience |
| Balance X and Y | Compromise needed | Cost and Quality balanced |
| Phased Approach | Sequential resolution | Innovation → Stability (phased) |
| Hybrid Solution | Combined approach | In-house core + Outsourced peripheral |

---

## Dependency Relations

### Relation Type Definitions

| Relation Type | Definition | From Entity | To Entity | Example |
|---------------|------------|-------------|-----------|---------|
| Sequential Dependency | B depends on A completion | Later phase | Earlier phase | Acceptance → Deployment |
| Resource Dependency | B requires A's resources | Resource user | Resource owner | IT Team → Budget |
| Information Dependency | B requires A's information | Information user | Information provider | Decision → Evaluation results |
| Technical Dependency | B requires A's technical capability | System B | System A | Cloud service → Network |
| Integration Dependency | B requires integration with A | New system | Existing system | New network → Legacy integration |
| Policy Dependency | B depends on policy mandate | Organization | Policy source | Education → 1:1 mandate |

### Dependency Chain Patterns

```
Lifecycle Dependency Chain:
Need Identification
  ↓ [Sequential]
Evaluation
  ↓ [Information: technical assessment]
Decision
  ↓ [Resource: budget]
Deployment
  ↓ [Technical: infrastructure]
Acceptance
  ↓ [Sequential]
Operations

System Dependency Chain:
Cloud Platform
  ↓ [Technical]
Network Infrastructure
  ↓ [Integration]
Existing Systems
  ↓ [Technical]
Security Module
```

### Dependency Relation Attributes

| Attribute | Definition | Values |
|-----------|------------|--------|
| relation_type | Relation classification | sequential, resource, information, technical, integration, policy |
| criticality | Dependency criticality | critical, important, moderate |
| condition | Dependency condition | Condition expression |
| failure_impact | Impact if dependency fails | blocking, degraded, workaround |

---

## Relation Frequency by Industry

| Relation Category | Education | Healthcare | Hospitality | Manufacturing | IT Services |
|-------------------|-----------|------------|-------------|---------------|-------------|
| Supervision (high) | High | High | Medium | High | Medium |
| Cooperation (high) | High | Medium | High | Medium | High |
| Goal Conflict | Medium | High | Medium | High | Medium |
| Resource Conflict | High (public budget) | Medium | Low (OpEx) | Medium | Low |
| Sequential Dependency | High | High | High | High | High |
| Policy Dependency | High (mandates) | High (compliance) | Low | Medium | Low |

---

## Relation Inference Rules

### From Stakeholder Listings

1. Hierarchical role pairs (e.g., CEO + CIO) → Supervision relation
2. Same-scenario role pairs → Cooperation relation
3. Conflict-related role pairs → Conflicting relation
4. Influence level differences → Hierarchical relation strength

### From Conflicts Table

1. Stakeholder pairs in conflict → Conflicting relation
2. Priority recommendation → Resolution strategy
3. Root cause → Conflict type classification

### From Operational Scenarios

1. Actor sequence → Sequential Dependency
2. Actor interactions → Cooperation/Communication
3. Actor resource mentions → Resource Dependency

### From Products/Solutions

1. System composition → Composition relation
2. Integration mentions → Integration Dependency
3. Vendor mentions → Service Delivery relation