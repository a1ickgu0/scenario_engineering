# Scenario Engineering SKILL

This is a generic INCOSE requirements engineering SKILL focused on extracting requirements and stakeholder information from vendor customer story PDFs or text. It can be used in Claude, other LLM platforms, or manual analysis workflows. Outputs are structured for OpenSCENARIO DSL preparation.

## 📋 Purpose

The goal of this SKILL is to guide analysts in extracting from customer story text:

1. Document title, country, industry, company name, document year
2. Key stakeholders and their roles
3. Purchase elements and business value, evaluated and ranked by business importance
4. Stakeholder expectations/needs, influence and benefits, priority/conflicts, commitment and engagement
5. Operational concept / usage concept
6. Referenced products, services, and solutions
7. **State Model**: Stakeholder, system, and organization states with transitions
8. **Environment Model**: Industry, regional, organizational, and technical constraints
9. **Entity Model**: Organization hierarchy, system composition, external connections
10. **Lifecycle Phases**: Phase sequence with triggers and completion criteria
11. **Parameterization Model**: Structured metrics for OpenSCENARIO DSL

## 🔍 Core Capabilities

### 1. Stakeholder Extraction
- Identify users, customers, operators, maintainers, supporters, regulators, community/public, suppliers, etc.
- Distinguish roles, expectations, values, risks, priorities, and conflicts
- Link lifecycle participation and acceptance
- **Relationship types**: Hierarchical, Collaborative, Conflicting, Dependency

### 2. Purchase Element Analysis
- Extract 3-5 business purchase elements from the customer story
- Evaluate and rank these elements based on business importance to the customer
- Describe from customer perspective "why buy" and "what problem needs solving"
- **Parameterization**: Structured format for quantified metrics

### 3. Operational Concept
- Describe system operation/usage concept
- Extract key usage scenarios, environments, interactions, and success criteria
- **Enhanced structure**: Trigger → Actions → Conditions → Result (State Transition)

### 4. Product & Solution Identification
- Extract products, services, solutions, technologies, or delivery forms from the story
- Map to stakeholder needs
- **Entity hierarchy**: Solution → Products → Services tree structure

### 5. Traceability
- All analysis points must be based on original content
- Provide original text citations, paragraph, or key sentence references

### 6. PDF Processing Support
- Support PDF document text extraction and analysis
- Provide tool integration guides and command examples
- Maintain page and paragraph references for traceability

### 7. State Model (OpenSCENARIO Preparation)
- Stakeholder states: Need Identified → Evaluating → Decided → Satisfied/Dissatisfied
- System states: Not Deployed → Deploying → Running → Upgrading → Fault/Recovering
- Organization states: Problem Identified → Solution Seeking → Procurement → Implementation → Normal Operation
- State transition triggers and conditions

### 8. Environment Model (OpenSCENARIO Preparation)
- Industry environment: Regulations, standards, compliance requirements
- Regional environment: National regulations, cultural characteristics
- Organizational environment: Scale, architecture, budget constraints
- Technical environment: Existing tech stack, integration constraints

### 9. Entity Model (OpenSCENARIO Preparation)
- Organization hierarchy: Company → Department → Team → Role
- System composition: Solution → Products → Services
- External entity connections: Supplier, Regulator, Partner

### 10. Lifecycle Model (OpenSCENARIO Preparation)
- Phase sequence: Need Identification → Evaluation → Decision → Deployment → Acceptance → Operations
- Phase triggers, actions, and completion criteria

### 11. Parameterization Model (OpenSCENARIO Preparation)
- Metric parameters: Quantified indicators with name, type, value, unit
- Role attribute parameters: Influence, priority, participation phase
- Scenario parameters: Deployment time, coverage scale, user count
- Constraint parameters: Budget limit, compliance requirements

## 🛠️ PDF Processing Tool Integration

### Recommended Tools
- **pdftotext**: Linux/Mac native tool, preserves layout
- **pdf2txt.py**: Python PDFMiner tool
- **Online converters**: Browser-based PDF-to-text tools
- **OCR tools**: tesseract for scanned PDFs

### Usage Examples
```bash
# Basic text extraction
pdftotext input.pdf output.txt

# Preserve layout structure
pdftotext -layout input.pdf output.txt

# Specify page range
pdftotext -f 1 -l 5 input.pdf output.txt

# Python approach
python -c "import pdfminer; pdfminer.high_level.extract_text('input.pdf')"
```

### Processing Steps
1. **Extract text**: Convert PDF to plain text format
2. **Add references**: Mark page numbers, section locations
3. **Clean content**: Remove headers, footers, and formatting noise
4. **Validate completeness**: Ensure text is readable and complete

### Traceability Markers
- Page reference: "Page 3, paragraph 2"
- Section marker: "Section 2.1: Customer Challenges"
- Direct quote of original content

## 📁 Directory Structure

```
scenario_analyzer/
├── SKILL.md                # SKILL metadata definition
├── README.md               # This documentation (English)
├── README_zh.md            # Chinese documentation
├── tests/                  # Document validation and test samples
└── assets/
    ├── prompts/            # Core prompts
    │   └── customer-story-analysis.prompt.md
    └── references/         # Analysis guidelines
        └── analysis-guidelines.md
```

## 🚀 Getting Started

1. Copy or convert the vendor customer story PDF text content into readable text for analysis
2. Activate this SKILL and specify the dimensions you need to extract:
   - Purchase elements
   - Stakeholders and expectations
   - Influence and benefits
   - Priority and conflicts
   - Commitment and engagement
   - Operational usage concept
   - Products and solutions
   - **State model** (for OpenSCENARIO)
   - **Environment model** (for OpenSCENARIO)
   - **Entity model** (for OpenSCENARIO)
   - **Lifecycle phases** (for OpenSCENARIO)
   - **Parameterization** (for OpenSCENARIO)
3. Output should be primarily structured tables, with supplementary explanations and original text reference markers

This SKILL is suitable for Claude, other LLM platforms, or manual analysis workflows. Output is structured for downstream processing by `scenario_modeler` SKILL for OpenSCENARIO DSL generation.

## Output Structure

```
## 0. 客户基本信息 (Customer Basic Information)
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

## 🧭 Your First Step

Paste the first vendor customer story text content, or at least provide the first key sentence. We'll start stakeholder extraction and requirements analysis from this real content.

---

## Version History

- **0.2.0** (2026-04-12): Added OpenSCENARIO DSL preparation support - State Model, Environment Model, Entity Model, Lifecycle Phases, Parameterization Model, Relationship Types, enhanced Operational Scenarios with trigger/transition
- **0.1.0** (2026-04-10): Initial customer-story based INCOSE requirements engineering SKILL

---

**[中文版本](README_zh.md)**