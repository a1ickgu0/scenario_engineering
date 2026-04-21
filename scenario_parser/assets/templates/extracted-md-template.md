# Extracted Data Document

---

## File Identification

**Generated File Name**: `{{TIMESTAMP}}-{{CONTENT_TYPE}}-{{KEY_IDENTIFIER}}-extracted.md`

| Component | Value |
|-----------|-------|
| **Timestamp** | {{TIMESTAMP}} |
| **Content Type** | {{CONTENT_TYPE}} |
| **Key Identifier** | {{KEY_IDENTIFIER}} |
| **Sequence** | {{SEQUENCE}} |
| **Base Name** | {{TIMESTAMP}}-{{CONTENT_TYPE}}-{{KEY_IDENTIFIER}} |

---

## File Pair Mapping

| Output Type | File Name |
|-------------|-----------|
| **MD Document** | `{{TIMESTAMP}}-{{CONTENT_TYPE}}-{{KEY_IDENTIFIER}}-extracted.md` |
| **JSON Data** | `{{TIMESTAMP}}-{{CONTENT_TYPE}}-{{KEY_IDENTIFIER}}-extracted.json` |
| **Analyzer Output** | `{{TIMESTAMP}}-{{CONTENT_TYPE}}-{{KEY_IDENTIFIER}}-analysis.md` |

---

## Content Classification

| Field | Value | Reason |
|-------|-------|--------|
| **Detected Type** | {{CONTENT_TYPE}} | {{TYPE_REASON}} |
| **Confidence** | {{TYPE_CONFIDENCE}} | Based on matched criteria |
| **Criteria Matched** | {{CRITERIA}} | - |

---

## Source Metadata

| Field | Value |
|-------|-------|
| Source File | {{SOURCE_FILE}} |
| Source Type | {{SOURCE_TYPE}} |
| Language | {{LANGUAGE}} |
| Extracted At | {{EXTRACTED_AT}} |
| Parser Version | 0.1.0 |

---

## Customer Basic Information

| Field | Value | Reference |
|-------|-------|-----------|
| Title | {{DOCUMENT_TITLE}} | {{TITLE_REFERENCE}} |
| Company | {{COMPANY_NAME}} | {{COMPANY_REFERENCE}} |
| Industry | {{INDUSTRY}} | {{INDUSTRY_REFERENCE}} |
| Country | {{COUNTRY}} | {{COUNTRY_REFERENCE}} |
| Year | {{YEAR}} | {{YEAR_REFERENCE}} |

---

## 2. Initial State (应用产品前)

### 整体描述

{{INITIAL_STATE_DESCRIPTION}}

**Reference**: {{INITIAL_STATE_REFERENCE}}

### 关键问题

| Problem | Reference |
|---------|-----------|
| {{PROBLEM_1}} | {{PROBLEM_1_REF}} |
| {{PROBLEM_2}} | {{PROBLEM_2_REF}} |

### 组织背景

{{ORGANIZATIONAL_CONTEXT}}

---

## 3. Final State (应用产品后)

### 整体描述

{{FINAL_STATE_DESCRIPTION}}

**Reference**: {{FINAL_STATE_REFERENCE}}

### 收益成果

| Benefit | Reference |
|---------|-----------|
| {{BENEFIT_1}} | {{BENEFIT_1_REF}} |
| {{BENEFIT_2}} | {{BENEFIT_2_REF}} |

---

## 4. Stakeholder Mentions

| Name | Role Type | Context | Expectation (Raw) | Reference |
|------|-----------|---------|-------------------|-----------|
| {{STAKEHOLDER_1}} | {{ROLE_TYPE_1}} | {{CONTEXT_1}} | {{EXPECTATION_1}} | {{REF_1}} |
| {{STAKEHOLDER_2}} | {{ROLE_TYPE_2}} | {{CONTEXT_2}} | {{EXPECTATION_2}} | {{REF_2}} |

---

## 5. Pain Points Mentions

| Stakeholder | Pain Point | Category | Impact | Reference |
|-------------|------------|----------|--------|-----------|
| {{STAKEHOLDER}} | {{PAIN_POINT}} | {{CATEGORY}} | {{IMPACT}} | {{REFERENCE}} |

**Category Hints**:
- `workflow_bottleneck` - 流程瓶颈
- `efficiency_obstacle` - 效率障碍
- `experience_barrier` - 体验障碍

---

## 6. Product Mentions

| Name | Vendor | Type | Features | Reference |
|------|--------|------|----------|-----------|
| {{PRODUCT_1}} | {{VENDOR_1}} | {{TYPE_1}} | {{FEATURES_1}} | {{REF_1}} |

**Type Hints**:
- `Platform` - 平台（Central, Portal, Dashboard）
- `Product` - 产品（Switch, Router, AP）
- `Service` - 服务（Support, Maintenance）
- `Component` - 组件（License, Module）

---

## 7. Metrics Mentions

| Metric | Value | Unit | Context | Comparison | Reference |
|--------|-------|------|---------|------------|-----------|
| {{METRIC_1}} | {{VALUE_1}} | {{UNIT_1}} | {{CONTEXT_1}} | {{COMPARISON_1}} | {{REF_1}} |

**Type Hints**:
- `efficiency` - 效率指标
- `cost` - 成本指标
- `time` - 时间指标
- `quality` - 质量指标
- `satisfaction` - 满意度指标

---

## 8. Environment Mentions

### Industry Environment

| Constraint | Type | Reference |
|------------|------|-----------|
| {{CONSTRAINT}} | {{TYPE}} | {{REFERENCE}} |

### Regional Environment

| Constraint | Type | Reference |
|------------|------|-----------|
| {{CONSTRAINT}} | {{TYPE}} | {{REFERENCE}} |

### Organizational Environment

| Constraint | Type | Reference |
|------------|------|-----------|
| {{CONSTRAINT}} | {{TYPE}} | {{REFERENCE}} |

### Technical Environment

| Constraint | Type | Reference |
|------------|------|-----------|
| {{CONSTRAINT}} | {{TYPE}} | {{REFERENCE}} |

---

## 9. Raw Quotes

| Quote | Speaker | Role | Topic | Reference |
|-------|---------|------|-------|-----------|
| "{{QUOTE}}" | {{SPEAKER}} | {{ROLE}} | {{TOPIC}} | {{REFERENCE}} |

---

## 10. Scenario Mentions

| Scenario | Participants | Context | Trigger | Outcome | Reference |
|----------|--------------|---------|---------|---------|-----------|
| {{SCENARIO}} | {{PARTICIPANTS}} | {{CONTEXT}} | {{TRIGGER}} | {{OUTCOME}} | {{REFERENCE}} |

---

## 11. Lifecycle Mentions

| Phase | Activities | Duration | Reference |
|-------|------------|----------|-----------|
| {{PHASE}} | {{ACTIVITIES}} | {{DURATION}} | {{REFERENCE}} |

---

## Extraction Validation

### Required Fields Check
- [ ] Title extracted ✓/✗
- [ ] Company extracted ✓/✗
- [ ] Initial state exists ✓/✗
- [ ] Final state exists ✓/✗
- [ ] At least 1 stakeholder ✓/✗
- [ ] At least 1 product ✓/✗

### Optional Fields Check
- [ ] Pain points present ✓/✗
- [ ] Metrics present ✓/✗
- [ ] Quotes present ✓/✗
- [ ] Environment mentions ✓/✗

---

*Extracted by scenario_parser v0.1.0*
*JSON counterpart: {{COMPANY}}-extracted.json*