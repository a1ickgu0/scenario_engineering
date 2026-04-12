# Parameterization Model Synthesis Prompt

## Purpose

Synthesize configurable parameters from multiple scenario_engine analysis outputs. Build parameterization model with metric parameters, role attribute parameters, scenario parameters, and constraint parameters for OpenSCENARIO DSL preparation.

---

## Input Requirements

Provide multiple `-analysis.md` documents with:
- Purchase elements (quantified metrics)
- Stakeholder listings (influence, priority attributes)
- Operational scenarios (scenario-specific parameters)
- Pre-deployment problems (constraint parameters)

---

## Parameter Type Definitions

### Metric Parameters

| Parameter Category | Definition | Data Type | Examples |
|--------------------|------------|-----------|----------|
| Reduction Rate | Percentage reduction in metric | Percentage | fault_ticket_reduction: 100%, downtime_reduction: 50% |
| Increase Rate | Factor or percentage increase | Factor/Percentage | coverage_increase: 2x, capacity_increase: 100% |
| Time Metric | Duration or time savings | Duration | deploy_time: 30min, resolution_time: hours_to_minutes |
| Coverage Scale | Number of users/devices/sites | Count | user_count: 26500, site_count: 67, device_count: 31000 |
| Availability | Uptime or success rate percentage | Percentage | uptime: 99.9%, first_connect_success: 100% |
| Cost Metric | Financial measurement | Currency/Ratio | opex_ratio: monthly, capex_eliminated: true |

### Role Attribute Parameters

| Parameter Category | Definition | Data Type | Examples |
|--------------------|------------|-----------|----------|
| Influence Level | Stakeholder influence strength | Enum | high, medium-high, medium, low |
| Priority | Stakeholder priority ranking | Enum/Number | high(1), medium-high(2), medium(3), low(4) |
| Participation Phase | Lifecycle phases involved | Enum Set | need_identification, evaluation, decision, deployment, acceptance, operations |
| Value Focus | Primary value expectation | Enum | efficiency, cost, security, experience, innovation |
| Risk Sensitivity | Risk concern level | Enum | high, medium, low |

### Scenario Parameters

| Parameter Category | Definition | Data Type | Examples |
|--------------------|------------|-----------|----------|
| Scenario Duration | Time to complete scenario | Duration | migration_duration: 30min, test_duration: 1hour |
| Actor Count | Number of actors involved | Count | teacher_count: 1, student_count: 26500 |
| Success Threshold | Success criteria threshold | Percentage/Count | success_rate: 100%, min_connected: 26500 |
| Action Sequence | Number and order of actions | Sequence | action_count: 5, sequence: assess→deploy→validate |

### Constraint Parameters

| Parameter Category | Definition | Data Type | Examples |
|--------------------|------------|-----------|----------|
| Budget Limit | Maximum budget available | Currency | budget_max: $500000 |
| Time Constraint | Deadline or time limitation | Duration | deployment_deadline: 30days |
| Compliance Requirement | Mandatory compliance standards | Enum Set | compliance: HIPAA, GDPR, FERPA |
| Policy Mandate | Required by policy | Enum | mandate: 1:1_device, nhs_digital |
| Integration Constraint | Required integrations | Enum Set | integration: ServiceNow, ASM_portal |
| Technical Standard | Required technical specifications | Enum Set | standard: WiFi6, zero_trust |

---

## Analysis Instructions

### Step 1: Metric Parameter Extraction

1. Extract quantified metrics from purchase elements:
   - "100% Reduction in network-related trouble tickets"
   - "2x Wi-Fi coverage and capacity"
   - "30 Minutes downtime"
2. Normalize to parameter format:
   - fault_ticket_reduction: 100% (Percentage)
   - coverage_increase: 2x (Factor)
   - deploy_time: 30min (Duration)
3. Extract coverage scale from descriptions:
   - "26,500 students" → user_count: 26500
   - "67 schools" → site_count: 67
4. Build metric parameter catalog

### Step 2: Role Attribute Parameter Extraction

1. Extract influence level from stakeholder listings:
   - "High" → influence_level: high
   - "Medium-High" → influence_level: medium-high
2. Extract priority from stakeholder listings:
   - "High" → priority: high
   - "Priority recommendation" → implied priority for conflicts
3. Infer participation phases from stakeholder roles:
   - IT Director: decision, evaluation, deployment
   - Teacher: acceptance, operations
   - CSM: deployment, operations
4. Infer value focus from expectations
5. Build role attribute parameter catalog

### Step 3: Scenario Parameter Extraction

1. Extract scenario duration from descriptions:
   - "30 minutes deployment" → scenario_duration: 30min
2. Extract actor count from participant descriptions:
   - "26,500 students" → actor_count: 26500
3. Extract success threshold from success criteria:
   - "All learners first-connect success" → success_threshold: 100%
4. Infer action sequence length from scenario complexity
5. Build scenario parameter catalog

### Step 4: Constraint Parameter Extraction

1. Infer budget constraints from purchase factors:
   - "NaaS subscription" → capex_eliminated: true
   - "Capital expenditure approval difficulty" → budget_approval: difficult
2. Extract time constraints from deployment descriptions:
   - "Minimal downtime" → time_constraint: minimal_downtime
3. Infer compliance requirements from industry/context:
   - Healthcare + US → compliance: HIPAA
   - Education + UK → compliance: GDPR, FERPA
4. Extract policy mandates from problem descriptions:
   - "National one-student-one-device goal" → mandate: 1:1_device
5. Extract integration constraints from products:
   - "ServiceNow integration" → integration: ServiceNow
6. Build constraint parameter catalog

### Step 5: Parameter Frequency Analysis

1. Count frequency of each parameter value across documents
2. Build Parameter × Industry matrix
3. Identify common parameters (appearing across industries)
4. Identify industry-specific parameters

### Step 6: Parameter Range/Value Catalog

1. List all possible values for each parameter type:
   - influence_level: [high, medium-high, medium, low]
   - success_rate: range from 50% to 100%
2. Identify typical values per parameter
3. Identify value distributions

---

## Output Format

Follow the template: `parameterization-template.md`

**Required Sections**:

### 1. Metric Parameter Catalog

| Parameter | Type | Typical Values | Frequency | Industries | Source Cases |

### 2. Role Attribute Parameter Catalog

| Parameter | Type | Possible Values | Typical Values | Source Cases |

### 3. Scenario Parameter Catalog

| Parameter | Type | Typical Values | Frequency | Source Cases |

### 4. Constraint Parameter Catalog

| Parameter | Type | Possible Values | Industries | Source Cases |

### 5. Parameter Value Distribution

For each parameter, provide value distribution:

```
Parameter: fault_ticket_reduction
├── Type: Percentage
├── Range: 0% - 100%
├── Typical Values: 100%, 80%, 50%
├── Distribution:
│   ├── 100%: 8 cases (80% of Education)
│   ├── 80%: 2 cases (Manufacturing)
│   └── 50%: 1 case (Healthcare)
└── Source Cases: Education-UK-06, Manufacturing-Portugal-12, ...
```

### 6. Industry × Parameter Matrix

| Industry | Typical Metrics | Typical Constraints | Typical Role Attributes |

### 7. Parameter Template for DSL Input

```
# Metric Parameters
metric_parameters:
  fault_ticket_reduction: { type: percentage, value: 100%, source: Aberdeen }
  coverage_increase: { type: factor, value: 2x, source: Aberdeen }
  deploy_time: { type: duration, value: 30min, source: Aberdeen }
  user_count: { type: count, value: 26500, source: Aberdeen }

# Role Attribute Parameters
role_parameters:
  influence_level: { type: enum, values: [high, medium-high, medium, low] }
  priority: { type: enum, values: [high, medium-high, medium, low] }
  participation_phases: { type: enum_set, values: [need_id, eval, decision, deploy, accept, ops] }

# Scenario Parameters
scenario_parameters:
  success_threshold: { type: percentage, value: 100% }
  actor_count: { type: count, value: 26500 }

# Constraint Parameters
constraint_parameters:
  compliance: { type: enum_set, values: [GDPR] }
  mandate: { type: enum, values: [1:1_device] }
  budget_type: { type: enum, values: [public, private] }
```

---

## Traceability Requirements

For each parameter entry, include:
- Source Cases: Case IDs where this parameter value appears
- Original Expression: Original metric/description wording
- Normalization Method: How value was normalized

---

## Quality Checklist

- [ ] All four parameter types are extracted
- [ ] Metric parameters are normalized
- [ ] Role attributes are extracted from stakeholder data
- [ ] Scenario parameters are extracted from operational scenarios
- [ ] Constraint parameters are inferred from context
- [ ] Parameter frequency analysis is complete
- [ ] Value distributions are documented

---

## Example Usage

```
Parameter extraction example:
Original: "100% Reduction in network-related trouble tickets"
→ Parameter: fault_ticket_reduction
→ Type: Percentage
→ Value: 100%
→ Industry: Education
→ Source: Education-UK-06-Aberdeen

Original: "Digital Infrastructure Manager | High influence | High priority"
→ Role Attributes:
  - influence_level: high
  - priority: high
  - participation_phases: [need_id, eval, decision, deploy, accept]
→ Source: Education-UK-06-Aberdeen

Original: "67 schools, 26,500 students, 30 minutes deployment"
→ Scenario Parameters:
  - site_count: 67
  - user_count: 26500
  - deploy_time: 30min
→ Source: Education-UK-06-Aberdeen

Original: "National one-student-one-device goal | HIPAA compliance"
→ Constraint Parameters:
  - mandate: 1:1_device (Education)
  - compliance: HIPAA (Healthcare)
```