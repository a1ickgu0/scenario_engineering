# Parameterization Model Output Template

## Document Information

| Field | Value |
|-------|-------|
| Model Type | Parameterization Model |
| Generation Date | [DATE] |
| Source Document Count | [COUNT] |
| Source Document Range | [CASE_IDS] |

---

## 1. Metric Parameter Catalog

| Parameter | Type | Typical Values | Frequency | Industries | Source Cases |
|-----------|------|----------------|-----------|------------|--------------|
| fault_ticket_reduction | Percentage | 100%, 80%, 50% | [COUNT] | Education, Manufacturing | [CASE_IDS] |
| coverage_increase | Factor | 2x, 3x | [COUNT] | Education, Hospitality | [CASE_IDS] |
| deploy_time | Duration | 30min, 1hr | [COUNT] | Education | [CASE_IDS] |
| user_count | Count | 26500, 31000, 67 schools | [COUNT] | Education | [CASE_IDS] |
| first_connect_success | Percentage | 100% | [COUNT] | Education | [CASE_IDS] |
| uptime | Percentage | 99.9%, 99.99% | [COUNT] | All | [CASE_IDS] |
| resolution_time | Duration | hours→minutes | [COUNT] | Hospitality, IT Services | [CASE_IDS] |
| cost_model | Enum | subscription_monthly, opex | [COUNT] | Hospitality | [CASE_IDS] |
| ... | ... | ... | ... | ... | ... |

---

## 2. Role Attribute Parameter Catalog

| Parameter | Type | Possible Values | Typical Values | Source Cases |
|-----------|------|-----------------|----------------|--------------|
| influence_level | Enum | high, medium-high, medium, low | high (Decision Maker, IT Lead) | [CASE_IDS] |
| priority | Enum | high, medium-high, medium, low | high (User in Education) | [CASE_IDS] |
| participation_phases | Enum Set | need_id, eval, decision, deploy, accept, ops | [need_id, eval, decision, deploy] (IT Lead) | [CASE_IDS] |
| value_focus | Enum | efficiency, cost, security, experience, innovation | efficiency (IT Lead), experience (User) | [CASE_IDS] |
| risk_sensitivity | Enum | high, medium, low | high (Regulator), medium (User) | [CASE_IDS] |

---

## 3. Scenario Parameter Catalog

| Parameter | Type | Typical Values | Frequency | Source Cases |
|-----------|------|----------------|-----------|--------------|
| scenario_duration | Duration | 30min, 1hr, ongoing | [COUNT] | [CASE_IDS] |
| actor_count | Count | 26500, 1, 10 | [COUNT] | [CASE_IDS] |
| success_threshold | Percentage/Count | 100%, 26500 | [COUNT] | [CASE_IDS] |
| action_sequence_length | Count | 3, 5, 7 | [COUNT] | [CASE_IDS] |

---

## 4. Constraint Parameter Catalog

| Parameter | Type | Possible Values | Industries | Source Cases |
|-----------|------|-----------------|------------|--------------|
| budget_limit | Currency | $500000, etc. | All | [CASE_IDS] |
| budget_type | Enum | public, private, mixed | Education (public), Hospitality (private) | [CASE_IDS] |
| time_constraint | Duration | 30days, minimal_downtime | Education | [CASE_IDS] |
| compliance | Enum Set | HIPAA, GDPR, FERPA, APPI | Healthcare (HIPAA), EU (GDPR) | [CASE_IDS] |
| mandate | Enum | 1:1_device, nhs_digital | Education (1:1), Healthcare (NHS) | [CASE_IDS] |
| integration | Enum Set | ServiceNow, ASM_portal, existing_IAM | Hospitality (ASM), IT Services | [CASE_IDS] |
| standard | Enum Set | WiFi6, zero_trust, SD_WAN | All | [CASE_IDS] |

---

## 5. Parameter Value Distribution

### Parameter: fault_ticket_reduction

```
Parameter: fault_ticket_reduction
├── Type: Percentage
├── Range: 0% - 100%
├── Typical Values: 100%, 80%, 50%
├── Distribution:
│   ├── 100%: 8 cases (Education: Aberdeen, Alleyn, etc.)
│   ├── 80%: 2 cases (Manufacturing: Colep)
│   └── 50%: 1 case (Healthcare)
└── Source Cases: Education-UK-06, Manufacturing-Portugal-12, Healthcare-UK-03
```

### Parameter: user_count

```
Parameter: user_count
├── Type: Count
├── Range: 1000 - 50000+
├── Typical Values: 26500, 31000, 67000
├── Distribution:
│   ├── 26500: Aberdeen City Council
│   ├── 31000: (Aberdeen total users)
│   └── range values: various scales
└── Source Cases: Education-UK-06, Education-UK-04
```

### Parameter: deploy_time

```
Parameter: deploy_time
├── Type: Duration
├── Range: 10min - 2hr
├── Typical Values: 30min, 1hr
├── Distribution:
│   ├── 30min: Education cases (Aberdeen, etc.)
│   └── 1hr: Larger deployments
└── Source Cases: Education-UK-06, Education-UK-04
```

---

## 6. Industry × Parameter Matrix

| Industry | Typical Metrics | Typical Constraints | Typical Role Attributes |
|----------|-----------------|--------------------|-------------------------|
| Education | fault_ticket: 100%, coverage: 2x, deploy: 30min, users: 26000+ | mandate: 1:1_device, compliance: GDPR, budget: public | influence: high (IT Lead), priority: high (User) |
| Healthcare | compliance rate, uptime: 99.9% | compliance: HIPAA, budget: mixed | influence: high (Regulator), value: security |
| Hospitality | resolution_time: improved, cost_model: subscription | compliance: APPI/GDPR, budget: private | influence: medium (Partner), value: cost |
| Manufacturing | fault_ticket: 80%, efficiency: 50% | standard: predictive_maintenance, budget: private | influence: high (IT Lead), value: efficiency |
| ... | ... | ... | ... |

---

## 7. Parameter Template for DSL Input

```yaml
# Metric Parameters
metric_parameters:
  fault_ticket_reduction:
    type: percentage
    typical_value: 100%
    industries: [Education, Manufacturing]
    source: [Education-UK-06-Aberdeen]
  
  coverage_increase:
    type: factor
    typical_value: 2x
    industries: [Education]
    source: [Education-UK-06-Aberdeen]
  
  deploy_time:
    type: duration
    typical_value: 30min
    industries: [Education]
    source: [Education-UK-06-Aberdeen]
  
  user_count:
    type: count
    typical_value: 26500
    industries: [Education]
    source: [Education-UK-06-Aberdeen]

# Role Attribute Parameters
role_parameters:
  influence_level:
    type: enum
    values: [high, medium-high, medium, low]
    mapping:
      Decision Maker: high
      IT Lead: high
      Operator: medium-high
      User: medium
      Regulator: high
      Partner: medium
  
  priority:
    type: enum
    values: [high, medium-high, medium, low]
    typical:
      User (Education): high
      IT Lead: high
  
  participation_phases:
    type: enum_set
    values: [need_id, eval, decision, deploy, accept, ops]
    typical:
      IT Lead: [need_id, eval, decision, deploy, accept]
      User: [accept, ops]

# Scenario Parameters
scenario_parameters:
  success_threshold:
    type: percentage
    typical_value: 100%
  actor_count:
    type: count
    typical_value: 26500

# Constraint Parameters
constraint_parameters:
  compliance:
    type: enum_set
    values: [HIPAA, GDPR, FERPA, APPI]
    typical:
      Healthcare (US): [HIPAA]
      Education (UK): [GDPR, FERPA]
  
  mandate:
    type: enum
    values: [1:1_device, nhs_digital]
    typical:
      Education: 1:1_device
  
  budget_type:
    type: enum
    values: [public, private, mixed]
    typical:
      Education (municipal): public
      Hospitality: private
```

---

## 8. Key Insights

### Pattern 1: Metric Normalization

| Aspect | Finding | Interpretation | Business Implication | Source Cases |
|--------|---------|----------------|--------------------|--------------|
| 100% reduction | Most Education cases show 100% | Complete elimination achieved | Complete success positioning | [CASE_IDS] |

### Pattern 2: Industry-Specific Constraints

| Aspect | Finding | Interpretation | Business Implication | Source Cases |
|--------|---------|----------------|--------------------|--------------|
| HIPAA (Healthcare only) | Healthcare-specific compliance | Industry-specific constraint | Industry-specific positioning | [CASE_IDS] |

---

## 9. Traceability Summary

| Parameter Value | Source Cases | Original Expression | Normalization Method |
|-----------------|--------------|---------------------|---------------------|
| [VALUE] | [CASE_IDS] | [ORIGINAL] | [METHOD] |

---

## Notes

- [PARAMETER NORMALIZATION NOTES]
- [VALUE DISTRIBUTION NOTES]