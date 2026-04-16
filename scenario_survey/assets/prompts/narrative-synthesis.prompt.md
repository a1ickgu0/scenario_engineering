---
name: narrative-synthesis
description: "Synthesize pre-sales survey/interview results into structured customer requirements narrative ready for scenario_analyzer analysis. Transforms collected expectations and requirements into narrative format, preserving original quotes and target data."
---

# Narrative Synthesis Prompt

## Task Description

Convert **pre-sales survey** or interview results into a structured customer requirements narrative document. The output must:

1. Follow narrative format suitable for scenario_analyzer input
2. Preserve original quotes and target expectations
3. Use customer's own language and expressions
4. Structure information in logical flow (expectations, not outcomes)
5. Include traceability markers where possible

## Key Positioning

- **Timing**: Pre-sales stage (before solution decision)
- **Content**: Customer expectations, requirements, targets - not achieved outcomes
- **Language**: Use same language as source survey (default English)

## Input Requirements

The input should contain collected pre-sales survey materials including:
- Basic company information
- Current challenges and pain points
- Decision factors and expectations
- Stakeholder information and expectations
- Expected usage scenarios
- Target expectations and success criteria
- Quote materials from stakeholders

## Output Format Template (English - Default)

```
# [Project Name] Customer Requirements Narrative

> Based on pre-sales survey/interview collection
> Survey Date: [Date]
> Survey Participant: [Participant information]

---

## 1. Basic Information

| Project Information | Content |
|--------------------|---------|
| Project Name | [Name] |
| Company Name | [Company] |
| Industry | [Industry] |
| Country | [Country] |
| Company Scale | [Employee count/location count] |
| Project Timeline Expectation | [Expected timeline] |
| Current Status | [Considering/Planning/Early discussion] |

---

## 2. Current Challenges

### Business Pain Points

[Describe current core challenges facing the customer]

- **Pain Point 1**: [Specific problem description]
  > Original quote: "[Direct quote]"

- **Pain Point 2**: [Specific problem description]
  > Original quote: "[Direct quote]"

### Impact on Business

[Describe actual impact on business]

- [Impact description 1]
  > Quantification: [Specific numbers if available]

- [Impact description 2]

### Previous Attempts

[Describe other approaches previously tried]

- [Attempt 1]: [Result description]
- [Attempt 2]: [Result description]

---

## 3. Decision Factors & Expectations

### Solutions Under Consideration

[Describe solutions/approaches being considered]

- **Option A**: [Description and characteristics]
- **Option B**: [Description and characteristics]
- **Primary Interest**: [Which option seems preferred and why]
  > Original quote: "[Direct quote]"

### Decision Factors (By Priority)

| Priority | Factor | Business Value | Why Important |
|----------|--------|----------------|---------------|
| 1 | [Most important factor] | [What problem it solves] | [Original quote or explanation] |
| 2 | [Second important factor] | [What problem it solves] | [Original quote or explanation] |
| 3 | [Third important factor] | [What problem it solves] | [Original quote or explanation] |

### Expected Trade-offs

[Describe potential conflicting factors and expected balance]

- **Different views**: [What different opinions exist]
- **Expected resolution**: [How customer expects to balance]
  > Original quote: "[Direct quote]"

---

## 4. People Involved

### Decision & Management Level

| Role | Person/Department | Expectations/Concerns | Influence |
|------|------------------|----------------------|-----------|
| [Decision maker] | [Specific person] | [Expectation content] | High |
| [Manager] | [Specific person] | [Expectation content] | High |

### Execution & Usage Level

| Role | Person/Department | Expectations/Concerns | Influence |
|------|------------------|----------------------|-----------|
| [Executor] | [Specific department] | [Expectation content] | Medium |
| [User] | [Specific group] | [Expectation content] | Medium |

### External Parties

| Role | Party | Expectations/Requirements | Relationship Type |
|------|-------|--------------------------|-------------------|
| [Customer/service user] | [Specific party] | [Expectation content] | Beneficiary |
| [Partner] | [Specific party] | [Expectation content] | Collaborator |
| [Regulator] | [Specific party] | [Compliance requirements] | Constraint |

### Interest & Concern Mapping

- **Beneficiaries**: [Who would benefit, what benefit]
- **Affected parties**: [Whose work would change]
- **Supporters**: [Who actively supports]
- **Concerned parties**: [Who has concerns]

---

## 5. Expected Usage

### Typical Usage Scenarios

#### Scenario 1: [Scenario Name]

**Trigger condition**: [When would this be used]

**User roles**: [Who would participate]

**Expected steps**:
1. [What step 1 would be]
2. [What step 2 would be]
3. [What step 3 would be]

**Prerequisites**: [What preparation would be needed]

**Success criteria**: [How would success be judged]

**Original description**:
> "[Direct quote of expected usage scenario]"

#### Scenario 2: [Scenario Name]

[Same structure as above]

### Different Role Usage

| Role | Usage Method | Expected Frequency | Key Operations |
|------|--------------|-------------------|----------------|
| [Role A] | [How would use] | [Frequency] | [Key operations] |
| [Role B] | [How would use] | [Frequency] | [Key operations] |

### Peak & Exception Situations

- **Peak periods**: [When would usage be highest]
  - [Peak period characteristics]

- **Exception handling**: [How would problems be handled]
  - [Exception situation description]
  - [Expected handling approach]
  > Original quote: "[Direct quote]"

---

## 6. Industry & Environment

### Industry Requirements

[Industry-specific regulations, standards, certification requirements]

- **Regulation 1**: [Specific content]
- **Standard 1**: [Specific standard]
- **Certification requirement**: [Required certifications]

### Company Situation

- **Scale**: [Employee count, location count, coverage]
- **Distribution**: [Geographic distribution]
- **Existing systems**: [Current systems/equipment]

### Technical Environment

- **Network environment**: [Network conditions]
- **Equipment situation**: [Equipment types and quantities]
- **Integration needs**: [Systems to integrate]

---

## 7. Target Expectations

### Quantified Targets

| Dimension | Current Situation | Target Expectation | Improvement Goal |
|-----------|------------------|-------------------|------------------|
| [Metric 1] | [Current value] | [Target value] | [Percentage or multiplier] |
| [Metric 2] | [Current value] | [Target value] | [Percentage or multiplier] |
| [Metric 3] | [Current value] | [Target value] | [Percentage or multiplier] |

> Data source: [Note data source, e.g., participant statement, estimation]

### Problem Resolution Expectations

[Describe how customer expects problems to be resolved]

- **Pain point 1 resolution**: [Expected resolution and outcome]
- **Pain point 2 resolution**: [Expected resolution and outcome]

### Stakeholder Satisfaction Expectations

[Describe expected feedback and satisfaction]

- **Decision maker expectation**: [Expected feedback]
  > Original quote: "[Direct quote]"

- **User expectation**: [Expected feedback]
  > Original quote: "[Direct quote]"

- **External party expectation**: [Expected feedback]
  > Original quote: "[Direct quote]"

---

## 8. Key Success Factors Summary

### Core Success Factors (By Priority)

1. **[Most important factor]**
   - Business value: [What core problem would be solved]
   - Success definition: [What success would look like]
   > Original quote: "[Direct quote]"

2. **[Second important factor]**
   - Business value: [What problem would be solved]
   - Success definition: [What success would look like]

3. **[Third important factor]**
   - Business value: [What problem would be solved]
   - Success definition: [What success would look like]

### Insights & Expectations

[Participant's summary of expectations or insights]

> Original quote: "[Direct quote]"

---

## 9. Quote Materials

### Key Quotes

| Speaker | Quote Content | Context |
|---------|---------------|---------|
| [Person A] | "[Original words]" | [In what context said] |
| [Person B] | "[Original words]" | [In what context said] |

### Related Materials

- [Document name]: [Brief description]
- [Photo/screenshot]: [Brief description]
- [Reference material]: [Brief description]

---

## 10. Notes

- This narrative based on pre-sales survey/interview collection
- Quotes preserved as original words, with brackets for clarification
- Quantified targets marked as "estimate" if estimated
- Inferred conclusions marked as "inferred" with basis explained

---

*Narrative synthesis date: [Date]*
*Synthesized by: [Synthesizer information]*