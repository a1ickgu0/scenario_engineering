# Scenario Engineering SKILL

This is a generic INCOSE requirements engineering SKILL focused on extracting requirements and stakeholder information from vendor customer story PDFs or text. It can be used in Claude, other LLM platforms, or manual analysis workflows.

## 📋 Purpose

The goal of this SKILL is to guide analysts in extracting from customer story text:

1. Document title, country, industry, company name, document year
2. Key stakeholders and their roles
3. Purchase elements and business value, evaluated and ranked by business importance
4. Stakeholder expectations/needs, influence and benefits, priority/conflicts, commitment and engagement
5. Operational concept / usage concept
6. Referenced products, services, and solutions

## 🔍 Core Capabilities

### 1. Stakeholder Extraction
- Identify users, customers, operators, maintainers, supporters, regulators, community/public, suppliers, etc.
- Distinguish roles, expectations, values, risks, priorities, and conflicts
- Link lifecycle participation and acceptance

### 2. Purchase Element Analysis
- Extract 3-5 business purchase elements from the customer story
- Evaluate and rank these elements based on business importance to the customer
- Describe from customer perspective "why buy" and "what problem needs solving"

### 3. Operational Concept
- Describe system operation/usage concept
- Extract key usage scenarios, environments, interactions, and success criteria

### 4. Product & Solution Identification
- Extract products, services, solutions, technologies, or delivery forms from the story
- Map to stakeholder needs

### 5. Traceability
- All analysis points must be based on original content
- Provide original text citations, paragraph, or key sentence references

### 6. PDF Processing Support
- Support PDF document text extraction and analysis
- Provide tool integration guides and command examples
- Maintain page and paragraph references for traceability

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
scenario_engine/
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
3. Output should be primarily structured tables, with supplementary explanations and original text reference markers

This SKILL is suitable for Claude, other LLM platforms, or manual analysis workflows.

## 🧭 Your First Step

Paste the first vendor customer story text content, or at least provide the first key sentence. We'll start stakeholder extraction and requirements analysis from this real content.

---

**[中文版本](README_zh.md)**