---
name: scenario_engine
description: "INCOSE requirements engineering SKILL for extracting stakeholder, usage, and solution information from vendor customer story PDFs or narratives. Designed for use in Claude, other LLM workflows, or manual analyst processes, with table-first structured output and traceability references. Outputs are structured for OpenSCENARIO DSL preparation."
tags:
  - incose
  - requirements-engineering
  - customer-story
  - stakeholder-analysis
  - pdf-analysis
  - traceability
  - openscenario-preparation
version: "0.2.0"
---

# Scenario Engineering SKILL

## Overview

This SKILL is designed for generic INCOSE requirements engineering work that begins from a vendor customer story in PDF or text format. It is suitable for Claude, other LLM environments, or manual analyst workflows. The primary goal is to extract and structure:

1. Stakeholder information and expectations
2. Operational concept / run scenarios
3. Products and solutions described in the story

The analysis must preserve original wording and support traceability to the source text.

The generated reports should use the local language. If the local language cannot be determined, default to Chinese for report generation.

> Note: Generated analysis reports are demo outputs for validation. The actual requirements and output rules should be defined and maintained in this SKILL.

## When to Use

- **Customer story analysis**: When a vendor customer story is provided in PDF or text form
- **Stakeholder mapping**: When you need to identify users, customers, operators, maintainers, regulators, suppliers, and other stakeholder groups
- **Expectation capture**: When different stakeholder needs, values, risks and conflicts must be surfaced
- **Operational scenarios**: When you want to define how the solution is expected to be used and operated
- **Solution discovery**: When you need to identify actual products, services and technical solutions referenced in the story
- **Generic workflow**: When output should be structured and reusable beyond a single tool or platform
- **Traceability**: When the analysis must be tied back to specific sections or wording from the original story

## Key Capabilities

### Stakeholder Extraction
Identify and classify stakeholder groups, purchase elements, expectations, influences, conflicts, and lifecycle participation.

### Customer Story Traceability
Link each analysis item back to the original customer story text or PDF section, preserving wording and context.

### Operational Scenarios Capture
Produce a structured view of how the customer expects the system to be used, including use contexts, operating scenarios, and success conditions.

### Product & Solution Identification
Extract the product, service, and solution elements that are described or implied by the customer story, and map them to stakeholder needs.

### PDF Processing Tools
When direct PDF reading is not available, use external PDF processing tools to extract text content before analysis. Recommended tools include:
- PDF text extraction utilities (pdftotext, pdf2txt)
- Online PDF converters
- OCR tools for scanned PDFs
- Manual text extraction and copying

## Analysis Requirements

For each customer story, the SKILL should produce:

### Core Information
- **Customer basic information**: document title, country, industry, company name, and document year
- **Initial state description**: problems before solution deployment, organizational context
- **Final state description**: overall benefits and outcomes after solution deployment

### Purchase Analysis
- **Purchase elements**: 3-5 business-level buying factors described in the story, evaluated and ranked by business importance. Prioritize elements that align with the customer's core business needs, strategic objectives, and value propositions. Focus on what drives the fundamental business decisions rather than just technical features. For each purchase element, include quantified assessment information, detailing how the customer quantifies the value of this element across different dimensions, including before-and-after changes (e.g., cost reduction from X to Y, time savings of Z%, efficiency improvements).

### Stakeholder Analysis
- **Stakeholder listing**: Who the stakeholders are and their roles
- **Expectations/needs**: What each stakeholder expects or requires from the system
- **Influence and value**: How stakeholders influence the system or are affected by it, including value and risk
- **Relationship types**: Hierarchical, Collaborative, Conflicting, or Dependency relationships between stakeholders
- **Priority and conflict**: Conflicting expectations, relative priorities, and potential risks
- **Engagement and commitment**: Suggested stakeholder involvement in decision, evaluation, acceptance, and lifecycle activities

### State Model (for OpenSCENARIO)
- **Stakeholder states**: Initial state → Evaluation → Decision → Acceptance → Satisfied/Dissatisfied
- **System states**: Not Deployed → Deploying → Running → Upgrading → Fault/Recovering
- **Organization states**: Problem Identified → Solution Seeking → Procurement → Implementation → Normal Operation
- **State transition triggers**: Conditions that trigger state changes

### Environment Model (for OpenSCENARIO)
- **Industry environment**: Regulations, standards, compliance requirements, industry policies
- **Regional environment**: National regulations, cultural characteristics, market maturity
- **Organizational environment**: Scale, architecture type, budget constraints, strategic direction
- **Technical environment**: Existing tech stack, integration constraints, technical standards

### Entity Model (for OpenSCENARIO)
- **Organization entity hierarchy**: Company → Department → Team → Role tree structure
- **System entity composition**: Solution → Products → Services tree structure
- **External entity connections**: Supplier, Regulator, Partner relationships

### Lifecycle Model (for OpenSCENARIO)
- **Lifecycle phases**: Need Identification → Evaluation → Decision → Deployment → Acceptance → Operations
- **Phase triggers**: Start conditions for each phase
- **Phase actions**: Key activities per phase
- **Phase completion criteria**: End conditions for each phase

### Operational Scenarios
- **Running scenarios**: Key usage flows with trigger conditions, execution conditions, and state transitions
- **Scenario structure**: Trigger → Actions → Conditions → Result (State Transition)
- **Environmental assumptions**: Contextual constraints and prerequisites

### Product/Solution View
- **Product/solution identification**: The products, services, and solution elements referenced or implied
- **Entity mapping**: Map products/solutions to entity hierarchy

### Parameterization Model (for OpenSCENARIO)
- **Metric parameters**: Quantified metrics with name, type, value, unit structure
- **Role attribute parameters**: Influence level, priority, participation phase attributes
- **Scenario parameters**: Deployment time, coverage scale, user count parameters
- **Constraint parameters**: Budget limit, time constraints, compliance requirements

## Required Output Format

The output should be structured with tables as the primary format and supplemental narrative explanation for key findings. Each analysis item should include a reference marker for traceability.

### Output Structure

```
## 0. 客户基本信息
   - 基本信息 table
   - 应用产品与方案之前的问题 (Initial State)
   - 整体使用效果/收益综述 (Final State)

## 1. 购买要素 (Purchase Elements with Parameterization)

## 2. 利益相关者清单 (Stakeholder List with Relationship Types)

## 3. 冲突与优先级 (Conflicts and Priority)

## 4. 状态模型 (State Model)
   - 利益相关者状态表
   - 系统状态表
   - 组织状态表
   - 状态转换路径图

## 5. 环境模型 (Environment Model)
   - 行业环境表
   - 地域环境表
   - 组织环境表
   - 技术环境表

## 6. 实体层级模型 (Entity Model)
   - 组织实体层级树
   - 系统实体组成树
   - 外部实体连接图

## 7. 生命周期阶段 (Lifecycle Phases)
   - 阶段序列表 (触发器/动作/完成标准)

## 8. 运行场景 (Operational Scenarios with Trigger/Transition)

## 9. 承诺与参与建议 (Engagement and Commitment)

## 10. 产品与解决方案 (Products and Solutions)

## 11. 参数化模型 (Parameterization Model)
   - 量化指标参数表
   - 角色属性参数表
   - 场景参数表
   - 约束参数表

## 12. 追溯与备注 (Traceability and Notes)
```

### Traceability Format

Each analysis item should include a reference marker such as:
- quoted text snippet
- page/section indication
- direct phrasing from the customer story

Example:
- Stakeholder: Operations Team
  - Expectation: "快速完成系统部署" (source: page 4, paragraph 2)

## Workflow Example

1. User provides PDF customer story or extracted text
2. **If PDF format**: Use PDF processing tools to extract readable text content
   - Convert PDF to text using pdftotext, pdf2txt, or online converters
   - Preserve page/section references for traceability
   - Clean extracted text for analysis
3. Use an LLM or analyst process to extract the relevant passages
4. Organize stakeholders and expectations into structured tables
5. Identify conflicting goals and recommend priority
6. Summarize product/solution concepts and usage scenarios

## PDF Processing Integration

### Tool Requirements
- **Text Extraction**: pdftotext, pdf2txt, or online PDF-to-text converters
- **OCR Support**: For scanned PDFs, use OCR tools like tesseract
- **Text Cleaning**: Remove formatting artifacts and preserve readable content

### Processing Steps
1. **Extract Text**: Convert PDF to plain text format
2. **Add References**: Mark page numbers, sections, or paragraph locations
3. **Clean Content**: Remove headers, footers, and formatting noise
4. **Validate**: Ensure extracted text is readable and complete

### Example Commands
```bash
# Using pdftotext (Linux/Mac)
pdftotext -layout input.pdf output.txt

# Using pdf2txt (Python)
pdf2txt.py -o output.txt input.pdf

# With page numbers
pdftotext -f 1 -l 10 input.pdf output.txt
```

### Traceability Preservation
- Include page references: "Page 3, paragraph 2"
- Section markers: "Section 2.1: Customer Challenges"
- Direct quotes with context

```
/scenario_engine
# Activate customer-story extraction and stakeholder analysis workflow
```

## Version History

- **0.2.0** (2026-04-11): Added OpenSCENARIO DSL preparation support - State Model, Environment Model, Entity Model, Lifecycle Phases, Parameterization Model, Relationship Types, enhanced Operational Scenarios with trigger/transition
- **0.1.0** (2026-04-10): Initial customer-story based INCOSE requirements engineering SKILL draft
