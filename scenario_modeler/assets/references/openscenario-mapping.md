# OpenSCENARIO Mapping Reference

## Purpose

This document provides mapping guidance from scenario_modeler outputs to OpenSCENARIO DSL concepts, enabling preparation of structured inputs for DSL-based scenario modeling.

---

## OpenSCENARIO Concept Mapping

### Core Concept Correspondence

| OpenSCENARIO Concept | Original Purpose | scenario_modeler Mapping |
|----------------------|------------------|--------------------------|
| Actors/Entities | Vehicles, pedestrians, traffic participants | Stakeholder roles, Organizations, User groups |
| Actions | Speed change, lane change, trajectory | Stakeholder behaviors, System operations |
| Events | Triggers, state changes | Phase transitions, Lifecycle triggers |
| Conditions | Distance, time, parameter conditions | Purchase factors, Constraints, Success criteria |
| Storyboard | Init → Act → StopTrigger | Lifecycle phases, State transitions |
| Environment | Road network, weather, time | Industry/Regional/Organizational context |
| Parameters | Configurable parameter declarations | Metric parameters, Role attributes |
| Catalogs | Reusable component library | Industry templates, Role templates |

---

## Actor Mapping

### Stakeholder → Actor

| Stakeholder Category | Actor Type | Actor Attributes | Example |
|----------------------|------------|------------------|---------|
| Decision Maker | decision_actor | influence: high, role: decision | CEO, CIO |
| IT Lead | technical_actor | influence: high, role: technical_lead | IT Director, DIM |
| Operator | operation_actor | influence: medium, role: operator | IT Ops Team |
| User | user_actor | influence: medium, role: user | Teacher, Student group |
| Regulator | constraint_actor | influence: constraint, role: regulator | Government, NHS |
| Partner | external_actor | influence: medium, role: partner | CSM, Vendor |

### Actor Definition Template

```yaml
actor:
  id: "ACT001"
  name: "Digital Infrastructure Manager"
  type: "technical_actor"
  category: "IT Lead"
  attributes:
    influence_level: "high"
    priority: "high"
    participation_phases: ["need_id", "eval", "decision", "deploy", "accept"]
    value_focus: "efficiency"
    source_case: "Education-UK-06-Aberdeen"
```

---

## Action Mapping

### Behavior → Action

| Action Type | OpenSCENARIO Action Category | scenario_modeler Mapping | Example |
|-------------|------------------------------|--------------------------|---------|
| Assess | PrivateAction | Evaluate current state | Assess network capacity |
| Configure | PrivateAction | Set system parameters | Configure network |
| Deploy | PrivateAction | Install system | Deploy new network |
| Test | PrivateAction | Validate functionality | Run acceptance tests |
| Approve | PrivateAction | Authorize decision | Approve budget |
| Monitor | PrivateAction | Observe system status | Monitor performance |
| Communicate | PrivateAction | Exchange information | Report to management |
| Use | PrivateAction | Operate system | Use Wi-Fi |

### Action Definition Template

```yaml
action:
  id: "ACT001_deploy"
  name: "Deploy Network"
  type: "PrivateAction"
  actor_ref: "ACT001"  # IT Team
  parameters:
    duration: "30min"
    target: "network_system"
  conditions:
    pre: "deployment_approved"
    post: "network_configured"
```

---

## Event Mapping

### Trigger → Event

| Event Type | OpenSCENARIO Event Category | scenario_modeler Mapping | Example |
|------------|------------------------------|--------------------------|---------|
| Phase Start | StartTrigger | Lifecycle phase entry | Evaluation phase start |
| Phase End | StopTrigger | Lifecycle phase completion | Deployment phase end |
| Decision Made | Event | Decision point | Purchase decision |
| Acceptance Pass | Event | Validation event | Acceptance completed |
| Issue Detected | Event | Problem event | Network fault detected |

### Event Definition Template

```yaml
event:
  id: "EVT001_decision"
  name: "Purchase Decision Made"
  type: "Event"
  trigger:
    condition: "evaluation_complete AND budget_approved"
  actions:
    - "contract_signed"
    - "deployment_scheduled"
  priority: "high"
```

---

## Condition Mapping

### Constraint → Condition

| Condition Type | OpenSCENARIO Condition Category | scenario_modeler Mapping | Example |
|----------------|---------------------------------|--------------------------|---------|
| Success Criteria | ByValueCondition | Quantified metrics | first_connect_success = 100% |
| Budget Limit | ByValueCondition | Constraint parameter | budget_max = $500000 |
| Compliance | ByValueCondition | Constraint parameter | compliance = HIPAA |
| Phase Complete | ByEntityCondition | State transition | system_state = running |
| User Satisfied | ByEntityCondition | Stakeholder state | stakeholder_state = satisfied |

### Condition Definition Template

```yaml
condition:
  id: "COND001_success"
  name: "First Connect Success"
  type: "ByValueCondition"
  parameter_ref: "first_connect_success"
  value: "100%"
  rule: "equalTo"
```

---

## Storyboard Mapping

### Lifecycle → Storyboard

| Storyboard Element | OpenSCENARIO Structure | scenario_modeler Mapping |
|--------------------|------------------------|--------------------------|
| Init | Initial state | Pre-deployment state, Initial conditions |
| Story/Act | Scenario phases | Lifecycle phases (Need Id → Operations) |
| StartTrigger | Phase entry trigger | Phase start conditions |
| StopTrigger | Phase exit trigger | Phase completion criteria |
| ManeuverGroup | Actor actions | Action sequences per phase |

### Storyboard Definition Template

```yaml
storyboard:
  init:
    entities:
      - actor: "ACT001"  # IT Lead
        state: "need_identified"
      - system: "SYS001"  # Network
        state: "not_deployed"
    environment:
      industry: "Education"
      region: "UK"
      constraints: ["1:1_device_mandate", "GDPR"]
  
  stories:
    - name: "Network Deployment Story"
      acts:
        - name: "Need Identification Act"
          start_trigger: "capacity_gap_detected"
          maneuver_groups:
            - actors: ["ACT001"]
              maneuvers:
                - action: "assess_current_state"
                - action: "document_requirements"
          stop_trigger: "requirements_documented"
        
        - name: "Deployment Act"
          start_trigger: "contract_signed"
          maneuver_groups:
            - actors: ["ACT002"]  # IT Team
              maneuvers:
                - action: "deploy_network"
                  parameters: { duration: "30min" }
                - action: "configure_settings"
          stop_trigger: "network_running"
```

---

## Environment Mapping

### Context → Environment

| Environment Dimension | OpenSCENARIO Environment Element | scenario_modeler Mapping |
|-----------------------|----------------------------------|--------------------------|
| Industry Regulations | Environment condition | HIPAA, GDPR, FERPA |
| Regional Culture | Environment attribute | UK digital culture, US innovation |
| Organizational Scale | Environment attribute | 67 schools, 26500 users |
| Budget Constraints | Environment condition | CapEx approval difficulty |
| Technical Standards | Environment condition | Wi-Fi 6/6E, zero-trust |

### Environment Definition Template

```yaml
environment:
  id: "ENV001"
  name: "Education UK Municipal"
  attributes:
    industry: "Education"
    sub_industry: "K-12"
    region: "UK"
    org_scale: "large"
    org_type: "municipal"
    budget_type: "public"
  conditions:
    - type: "policy"
      name: "1:1_device_mandate"
      value: true
    - type: "compliance"
      name: "GDPR"
      value: true
    - type: "technical_standard"
      name: "WiFi6"
      value: true
```

---

## Parameter Mapping

### Configurable Values → Parameters

| Parameter Type | OpenSCENARIO Parameter Declaration | scenario_modeler Mapping |
|----------------|------------------------------------|--------------------------|
| Metric Parameter | ParameterDeclaration | fault_ticket_reduction, coverage_increase |
| Role Attribute | ParameterDeclaration | influence_level, priority |
| Scenario Parameter | ParameterDeclaration | deploy_time, user_count |
| Constraint Parameter | ParameterDeclaration | budget_limit, compliance |

### Parameter Definition Template

```yaml
parameter_declarations:
  - name: "fault_ticket_reduction"
    type: "Percentage"
    default_value: "100%"
    source: "Education-UK-06-Aberdeen"
  
  - name: "deploy_time"
    type: "Duration"
    default_value: "30min"
    source: "Education-UK-06-Aberdeen"
  
  - name: "user_count"
    type: "Integer"
    default_value: 26500
    source: "Education-UK-06-Aberdeen"
  
  - name: "compliance"
    type: "EnumSet"
    values: ["GDPR", "HIPAA", "FERPA"]
    default_value: ["GDPR"]
```

---

## Catalog Mapping

### Templates → Catalogs

| Catalog Type | OpenSCENARIO Catalog Purpose | scenario_modeler Content |
|--------------|------------------------------|--------------------------|
| ActorCatalog | Reusable actor definitions | Role templates per category |
| ActionCatalog | Reusable action definitions | Action templates per type |
| ConditionCatalog | Reusable condition definitions | Condition templates per type |
| EnvironmentCatalog | Reusable environment definitions | Industry/Region environment templates |

### Catalog Definition Template

```yaml
catalog:
  name: "EducationActorCatalog"
  type: "ActorCatalog"
  actors:
    - id: "ACT_template_ITLead"
      name: "IT Lead Template"
      category: "IT Lead"
      typical_phases: ["need_id", "eval", "decision", "deploy"]
      typical_expectations: ["efficiency", "feasibility"]
    
    - id: "ACT_template_User"
      name: "User Template"
      category: "User"
      typical_phases: ["accept", "ops"]
      typical_expectations: ["user_experience", "usability"]
```

---

## DSL Output Preparation Checklist

- [ ] All stakeholders mapped to actors with attributes
- [ ] All actions mapped with actor references
- [ ] All events defined with triggers
- [ ] All conditions defined with parameters
- [ ] Storyboard structure reflects lifecycle phases
- [ ] Environment includes all context dimensions
- [ ] Parameters are declared with types and values
- [ ] Catalogs are prepared for reusable templates

---

## Notes on DSL Preparation

1. **Current scope**: Prepare structured inputs for DSL, not full DSL generation
2. **Output format**: YAML/JSON templates ready for DSL conversion
3. **Traceability**: Maintain source case references in all DSL elements
4. **Completeness**: Ensure all scenario_modeler outputs have DSL mapping
5. **Validation**: Cross-check with OpenSCENARIO specification requirements