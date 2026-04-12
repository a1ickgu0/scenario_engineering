# Interaction Sequence Model Output Template

## Document Information

| Field | Value |
|-------|-------|
| Model Type | Interaction Sequence Model |
| Generation Date | [DATE] |
| Source Document Count | [COUNT] |
| Source Document Range | [CASE_IDS] |

---

## 1. Interaction Sequence Catalog

| Sequence ID | Sequence Name | Phase | Trigger | Actors | Source Cases |
|--------------|---------------|-------|---------|--------|--------------|
| SEQ001 | Classroom Full-Class Connection | Operations | Class session starts | Teacher, Students, Wi-Fi Network | [CASE_IDS] |
| SEQ002 | School Network Migration | Deployment | Purchase decision complete | IT Team, Mist Cloud | [CASE_IDS] |
| SEQ003 | AIOps Fault Resolution | Operations | Fault detected | Marvis AI, IT Ops Team | [CASE_IDS] |
| SEQ004 | Zero-trust Access Control | Operations | Device authentication request | User, Access Assurance, Network | [CASE_IDS] |
| SEQ005 | NaaS Monthly Billing | Operations | Monthly cycle | Organization, HPE GreenLake | [CASE_IDS] |
| SEQ006 | Customer Success Monthly Report | Operations | Monthly schedule | CSM, Management | [CASE_IDS] |
| ... | ... | ... | ... | ... | ... |

---

## 2. Detailed Sequence Definitions

### Sequence SEQ001: Classroom Full-Class Connection

```
Sequence: Classroom Full-Class Connection
├── Phase: Operations
├── Trigger: Class session starts, students attempt connection
├── Actors:
│   ├── Teacher (User)
│   ├── Students (User Group)
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

### Sequence SEQ002: School Network Migration

```
Sequence: School Network Migration
├── Phase: Deployment
├── Trigger: Purchase decision complete, schedule confirmed
├── Actors:
│   ├── IT Team (Operator)
│   ├── Mist Cloud (System)
├── Actions:
│   ├── 1. IT Team → Plan migration (Document)
│   ├── 2. Mist Cloud → Generate configuration (Configure)
│   ├── 3. IT Team → Execute migration (Deploy) [30 min]
│   ├── 4. IT Team → Validate settings (Test)
├── Conditions:
│   ├── Pre: New equipment ready, configuration generated
│   ├── Execution: Minimal downtime target (30 min)
│   └ and Post: Configuration complete, network operational
├── Result: Network migrated successfully
├── State Transition: Deploying → Running (System)
└── Source: Education-UK-06-Aberdeen
```

[Continue for other sequences...]

---

## 3. Action Type Frequency

| Action Type | Frequency | Typical Actors | Typical Phase | Source Cases |
|-------------|-----------|----------------|---------------|--------------|
| Assess | [COUNT] | IT Lead, IT Team | Need Identification | [CASE_IDS] |
| Document | [COUNT] | IT Lead, Management | Need Identification, Evaluation | [CASE_IDS] |
| Communicate | [COUNT] | All actors | All phases | [CASE_IDS] |
| Configure | [COUNT] | IT Team, System | Deployment, Operations | [CASE_IDS] |
| Deploy | [COUNT] | IT Team, Vendor | Deployment | [CASE_IDS] |
| Test | [COUNT] | IT Team, Users | Acceptance | [CASE_IDS] |
| Approve | [COUNT] | Decision Maker, CFO | Decision | [CASE_IDS] |
| Monitor | [COUNT] | IT Team, System, AI | Operations | [CASE_IDS] |
| Resolve | [COUNT] | IT Team, AI, Vendor | Operations | [CASE_IDS] |
| Use | [COUNT] | Users | Operations | [CASE_IDS] |
| Report | [COUNT] | All actors | All phases | [CASE_IDS] |

---

## 4. Trigger Type Frequency

| Trigger Type | Frequency | Typical Sequences | Source Cases |
|--------------|-----------|-------------------|--------------|
| Event Trigger | [COUNT] | Problem discovery, Decision made | [CASE_IDS] |
| Time Trigger | [COUNT] | Monthly report, Scheduled maintenance | [CASE_IDS] |
| State Trigger | [COUNT] | Deployment complete, Acceptance passed | [CASE_IDS] |
| Policy Trigger | [COUNT] | 1:1 mandate compliance | [CASE_IDS] |
| User Trigger | [COUNT] | Connection attempt, Usage request | [CASE_IDS] |
| System Trigger | [COUNT] | Fault detected, Performance threshold | [CASE_IDS] |

---

## 5. Condition Type Frequency

| Condition Type | Frequency | Typical Expressions | Source Cases |
|----------------|-----------|--------------------|--------------|
| Pre-condition | [COUNT] | Network deployed, Configuration ready | [CASE_IDS] |
| Execution condition | [COUNT] | Coverage available, Time target | [CASE_IDS] |
| Post-condition | [COUNT] | Success rate: 100%, Tests passed | [CASE_IDS] |
| Quantitative | [COUNT] | 30min, 100%, 2x | [CASE_IDS] |
| Qualitative | [COUNT] | Configuration complete, Stable operation | [CASE_IDS] |

---

## 6. Industry × Sequence Pattern Matrix

| Industry | Typical Deployment Sequences | Typical Operations Sequences | Typical Resolution Sequences |
|----------|------------------------------|------------------------------|------------------------------|
| Education | Network migration (30min) | Classroom connection, Student use | AIOps fault resolution |
| Healthcare | Compliance deployment | Patient data access, Clinical use | Security incident response |
| Hospitality | NaaS subscription setup | Guest Wi-Fi, Monthly billing | Network quality issue |
| Manufacturing | Predictive maintenance setup | Production monitoring, Maintenance | Equipment fault resolution |
| IT Services | Client service deployment | Service delivery, Client support | Service issue resolution |
| ... | ... | ... | ... |

---

## 7. Sequence Template Library

| Template Name | Phases | Actors | Action Pattern | Conditions | Frequency |
|----------------|--------|--------|----------------|------------|-----------|
| Deployment Template | Deployment | IT Team, System | Plan → Configure → Deploy → Validate | Pre: ready; Post: complete | High |
| Acceptance Template | Acceptance | IT Team, Users | Test → Validate → Report | Pre: deployed; Post: passed | High |
| Fault Resolution Template | Operations | AI, IT Team, Vendor | Detect → Diagnose → Resolve → Verify | Pre: fault; Post: resolved | Medium |
| User Connection Template | Operations | Users, System | Request → Authenticate → Connect → Use | Pre: deployed; Post: connected | High |
| Monthly Reporting Template | Operations | CSM, Management | Collect → Analyze → Report → Review | Pre: data; Post: delivered | Medium |

---

## 8. Key Insights

### Pattern 1: Fast Deployment Sequence

| Aspect | Finding | Interpretation | Business Implication | Source Cases |
|--------|---------|----------------|--------------------|--------------|
| Deployment time | Education: 30min typical | Zero-touch effective | Fast deployment positioning | [CASE_IDS] |

### Pattern 2: AI-Proactive Resolution

| Aspect | Finding | Interpretation | Business Implication | Source Cases |
|--------|---------|----------------|--------------------|--------------|
| AIOps sequences | Marvis AI proactively identifies | AI reduces manual intervention | AI-native positioning | [CASE_IDS] |

---

## 9. Traceability Summary

| Sequence | Source Cases | Original Scenario Name | Original Description |
|----------|--------------|------------------------|---------------------|
| [SEQUENCE_1] | [CASE_IDS] | [SCENARIO_NAME] | [DESCRIPTION] |

---

## Notes

- [SEQUENCE PARSING NOTES]
- [ACTION CLASSIFICATION NOTES]