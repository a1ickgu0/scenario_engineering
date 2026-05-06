---
name: scenario_parser
description: "Document extraction SKILL for parsing customer story PDFs and narratives into structured intermediate data. Outputs dual-format files (MD + JSON) containing extracted customer info, stakeholder mentions, pain points, products, metrics, and raw quotes with full traceability references. Designed to feed scenario_analyzer for analysis generation."
tags:
  - document-extraction
  - pdf-parsing
  - data-extraction
  - intermediate-output
  - traceability-preserving
  - json-output
  - md-output
  - parser
version: "0.1.1"
---

# Scenario Parser SKILL

## Overview

This SKILL extracts structured data from customer story documents (PDFs, texts, narratives) **without performing analysis**. It produces intermediate outputs that feed directly into `scenario_analyzer`.

**Key Positioning**:
- **Role**: Data extraction layer, not analysis
- **Output**: Dual-format (MD + JSON) intermediate files
- **Purpose**: Decouple extraction from analysis, enable batch processing

**Output Flow**:
```
scenario_parser
→ Input: PDF / Text / Narrative
→ Output: {customer}-extracted.md + {customer}-extracted.json
→ Feed: scenario_analyzer
```

## When to Use

- **PDF batch processing**: Extract data from multiple PDFs before analysis
- **Pre-analysis preparation**: Convert raw documents to structured format
- **Data validation**: Review extracted data before analysis generation
- **Pipeline integration**: Part of scenario_engineering Phase 2a
- **Independent execution**: Run parser without immediately triggering analyzer

## Input Sources

| Source Type | Format | Processing |
|-------------|--------|------------|
| PDF files | `.pdf` | pdftotext extraction, structure parsing |
| Survey narratives | `.md` | Direct parsing (from scenario_survey) |
| Independent text | `.txt` | Structure parsing |
| Mixed sources | Multiple | Combined processing |

## Output Format

### File Naming Convention

**命名结构**（时间 + 内容动态生成）:

```
{Timestamp}-{ContentType}-{KeyIdentifier}-{Seq}-extracted.{ext}
```

| 组成部分 | 说明 | 示例 | 来源 |
|---------|------|------|------|
| Timestamp | 提取时间戳 | `20260421T1030`, `20260421` | 提取执行时间 |
| ContentType | 内容类型标识 | `Case`, `Report`, `Industry`, `Product` | 内容分类判断 |
| KeyIdentifier | 关键内容标识 | `Hospitality`, `SouthernSun`, `ArubaCentral` | 基于内容提取 |
| Seq | 序列号（可选） | `001`, `002` | 同批次同类型多文档 |
| ext | 文件扩展名 | `md`, `json` | 固定值 |

---

### Content Type Classification（内容类型判断）

根据文档内容自动判断类型：

| ContentType | 判断依据 | KeyIdentifier 来源 | 命名示例 |
|-------------|----------|-------------------|----------|
| `Case` | 包含客户名、公司名、具体案例故事 | `Industry-CustomerName` | `20260421T1030-Case-Hospitality-SouthernSun-extracted.md` |
| `Report` | 行业分析报告、市场报告、白皮书 | `Industry-ReportTopic` | `20260421T1030-Report-Hospitality-MarketTrends-extracted.md` |
| `Industry` | 行业概述、行业特性文档 | `Industry` | `20260421T1030-Industry-Healthcare-extracted.md` |
| `Product` | 产品介绍、技术文档、规格说明 | `ProductName` | `20260421T1030-Product-ArubaCentral-extracted.md` |
| `Survey` | Survey 输出的叙事文档 | `Industry-Customer` | `20260421T1030-Survey-Hospitality-Malaysia-extracted.md` |
| `Mixed` | 多类型混合或无法判断 | `CustomerOrDefault` | `20260421T1030-Mixed-General-extracted.md` |

---

### KeyIdentifier Generation Rules（关键标识生成规则）

**KI-01: Case 类型** - 客户案例故事

```
KeyIdentifier = {Industry}-{CustomerNameNormalized}

Examples:
- Hospitality 案例，客户 Southern Sun → KeyIdentifier: "Hospitality-SouthernSun"
- Healthcare 案例，客户 Royal Devon → KeyIdentifier: "Healthcare-RoyalDevon"
- Education 案例，客户 Moreno Valley USD → KeyIdentifier: "Education-MorenoValleyUSD"
```

**KI-02: Report 类型** - 行业/市场报告

```
KeyIdentifier = {Industry}-{ReportTopic}

ReportTopic 判断:
- 标题包含 "Market" → MarketTrends
- 标题包含 "White Paper" → WhitePaper
- 标题包含 "Analysis" → IndustryAnalysis
- 标题包含 "Benchmark" → Benchmark

Examples:
- Hospitality 市场趋势报告 → KeyIdentifier: "Hospitality-MarketTrends"
- Healthcare 行业白皮书 → KeyIdentifier: "Healthcare-WhitePaper"
```

**KI-03: Industry 类型** - 行业概述文档

```
KeyIdentifier = {Industry}

Examples:
- Healthcare 行业概述 → KeyIdentifier: "Healthcare"
- Education 行业特性 → KeyIdentifier: "Education"
- Hospitality 行业标准 → KeyIdentifier: "Hospitality"
```

**KI-04: Product 类型** - 产品文档

```
KeyIdentifier = {ProductNameNormalized}

Examples:
- Aruba Central 产品介绍 → KeyIdentifier: "ArubaCentral"
- ClearPass 技术文档 → KeyIdentifier: "ClearPass"
- HPE Switch 规格 → KeyIdentifier: "HPESwitch"
```

**KI-05: Survey 类型** - Survey 输出

```
KeyIdentifier = {Industry}-{Country}

Examples:
- Hospitality-Malaysia 调研 → KeyIdentifier: "Hospitality-Malaysia"
- Healthcare-UK 调研 → KeyIdentifier: "Healthcare-UK"
```

---

### Timestamp Format Rules（时间戳格式）

| 格式 | 使用场景 | 示例 |
|------|----------|------|
| `YYYYMMDDTHHMM` | 精确时间（单文档处理） | `20260421T1030` |
| `YYYYMMDD` | 日期（批量处理同批次） | `20260421` |
| `YYYYMMDD-BatchN` | 批次标识 | `20260421-Batch001` |

**时间戳选择规则**:
- 单文档即时处理：使用精确时间戳 `YYYYMMDDTHHMM`
- 批量处理（同批多文档）：使用日期 + 批次号 `YYYYMMDD-Batch001`
- 所有同批次文档使用相同时间戳前缀

---

### Complete Naming Examples（完整命名示例）

| 情况 | ContentType | KeyIdentifier | 文件名 |
|------|-------------|---------------|--------|
| 酒店客户案例 | Case | Hospitality-SouthernSun | `20260421T1030-Case-Hospitality-SouthernSun-extracted.md` |
| 医院客户案例 | Case | Healthcare-RoyalDevon | `20260421T1030-Case-Healthcare-RoyalDevon-extracted.json` |
| 酒店市场报告 | Report | Hospitality-MarketTrends | `20260421T1030-Report-Hospitality-MarketTrends-extracted.md` |
| 教育行业白皮书 | Report | Education-WhitePaper | `20260421T1030-Report-Education-WhitePaper-extracted.md` |
| 医疗行业概述 | Industry | Healthcare | `20260421T1030-Industry-Healthcare-extracted.md` |
| Aruba 产品文档 | Product | ArubaCentral | `20260421T1030-Product-ArubaCentral-extracted.md` |
| Survey 输出 | Survey | Hospitality-Malaysia | `20260421T1030-Survey-Hospitality-Malaysia-extracted.md` |
| 批量处理第1批 | Case | Hospitality-SouthernSun | `20260421-Batch001-Case-Hospitality-SouthernSun-extracted.md` |
| 同类型同批次多文档 | Case | Hospitality-SouthernSun | `20260421-Batch001-Case-Hospitality-SouthernSun-001-extracted.md` |

---

### Analyzer Output Correlation（Analyzer 输出关联）

| Parser Output | Analyzer Output |
|---------------|-----------------|
| `20260421T1030-Case-Hospitality-SouthernSun-extracted.md/json` | `20260421T1030-Case-Hospitality-SouthernSun-analysis.md` |

保持相同的前缀（Timestamp-ContentType-KeyIdentifier），仅替换后缀：
- `-extracted.{ext}` → `-analysis.md`

---

### Normalization Rules（规范化规则）

| 规则编号 | 内容 |
|---------|------|
| NR-01 | 时间戳精确到分钟或日期 |
| NR-02 | ContentType 使用预定义类型（Case/Report/Industry/Product/Survey/Mixed） |
| NR-03 | KeyIdentifier 基于内容自动提取，不手动指定 |
| NR-04 | 所有名称组件去除特殊字符，空格→连字符 |
| NR-05 | KeyIdentifier 各部分用连字符连接 |
| NR-06 | 文件名总长度不超过120字符 |
| NR-07 | 同批次同类型多文档添加序列号 `-001`, `-002` |

---

### JSON File Name Metadata

```json
{
  "document_meta": {
    "generated_file_name": {
      "timestamp": "20260421T1030",
      "content_type": "Case",
      "key_identifier": "Hospitality-SouthernSun",
      "sequence": null,
      "base_name": "20260421T1030-Case-Hospitality-SouthernSun",
      "md_file": "20260421T1030-Case-Hospitality-SouthernSun-extracted.md",
      "json_file": "20260421T1030-Case-Hospitality-SouthernSun-extracted.json",
      "analyzer_output": "20260421T1030-Case-Hospitality-SouthernSun-analysis.md"
    },
    "content_classification": {
      "detected_type": "Case",
      "type_confidence": "high",
      "type_reason": "Contains customer name 'Southern Sun' and specific deployment story"
    }
  }
}
```

### Dual Output Files

For each input document, generate two files with identical base name:

1. **MD 文档** (`{...}-extracted.md`)
   - 原文内容（带行号标记）
   - 提取的原始信息片段
   - 人类可读，用于审查追溯

2. **JSON 数据** (`{...}-extracted.json`)
   - 结构化数据对象
   - 机器可读，供 Analyzer 直接读取

### Output Directory Structure

```
outputs/phase2-parser/
├── extracted/
│   ├── Hospitality-Malaysia-Southern-Sun-2026-extracted.md
│   ├── Hospitality-Malaysia-Southern-Sun-2026-extracted.json
│   ├── Healthcare-UK-Royal-Devon-Healthcare-2024-extracted.md
│   ├── Healthcare-UK-Royal-Devon-Healthcare-2024-extracted.json
│   └── ...
├── progress/
│   └── phase2a-parser-progress.md
└── problems/
    └── problem-documents-list.md
```

### Analyzer File Name Correlation

Analyzer 输出文件名保持一致的结构：

| Parser Output | Analyzer Output |
|---------------|-----------------|
| `Hospitality-Malaysia-Southern-Sun-2026-extracted.md/json` | `Hospitality-Malaysia-Southern-Sun-2026-analysis.md` |

文件名转换：`{base-name}-extracted.{ext}` → `{base-name}-analysis.md`

## JSON Data Structure

```json
{
  "document_meta": {
    "source_file": "doc-001.pdf",
    "source_type": "pdf",
    "extracted_at": "2026-04-21T10:00:00Z",
    "parser_version": "0.1.0",
    "language": "English",
    "page_count": 5,
    "line_count": 150,
    "generated_file_name": {
      "base_name": "Hospitality-Malaysia-Southern-Sun-2026",
      "md_file": "Hospitality-Malaysia-Southern-Sun-2026-extracted.md",
      "json_file": "Hospitality-Malaysia-Southern-Sun-2026-extracted.json",
      "analyzer_output": "Hospitality-Malaysia-Southern-Sun-2026-analysis.md"
    }
  },
  "customer_info": {
    "title": "Document title from first page or metadata",
    "country": "Malaysia",
    "industry": "Hospitality",
    "company": "Southern Sun",
    "year": "2026",
    "reference": {
      "title": "Page 1, Line 5",
      "company": "Page 1, Line 10"
    }
  },
  "initial_state": {
    "description": "原文描述的问题状态和背景...",
    "key_problems": [
      {
        "problem": "原文问题描述",
        "reference": "Page 1, Line 15"
      }
    ],
    "organizational_context": "原文组织背景描述...",
    "reference": "Page 1-2, Lines 10-30"
  },
  "final_state": {
    "description": "原文描述的最终效果和收益...",
    "benefits": [
      {
        "benefit": "原文收益描述",
        "reference": "Page 4, Line 45"
      }
    ],
    "reference": "Page 4-5, Lines 40-60"
  },
  "stakeholder_mentions": [
    {
      "name": "Guests",
      "role_type": "User",
      "context": "原文上下文片段...",
      "expectations_raw": "期望原文表达...",
      "influence_hint": "原文提及的影响力线索...",
      "reference": "Page 2, Line 25"
    },
    {
      "name": "IT Director",
      "role_type": "Decision Maker",
      "context": "...",
      "expectations_raw": "...",
      "influence_hint": "...",
      "reference": "Page 1, Line 20"
    }
  ],
  "pain_points_mentions": [
    {
      "stakeholder": "IT Team",
      "pain_point": "原文痛点描述...",
      "category_hint": "workflow_bottleneck | efficiency_obstacle | experience_barrier",
      "impact": "原文提及的影响...",
      "reference": "Page 1, Line 20"
    }
  ],
  "product_mentions": [
    {
      "name": "Aruba Central",
      "vendor": "HPE Aruba",
      "type": "Platform | Product | Service | Component",
      "context": "原文产品上下文...",
      "features": ["原文提及的功能..."],
      "reference": "Page 3, Line 35"
    }
  ],
  "metrics_mentions": [
    {
      "metric_name": "运维效率提升",
      "value": "30",
      "unit": "%",
      "context": "运维效率提升30%",
      "comparison": "before vs after if mentioned",
      "type_hint": "efficiency | cost | time | quality | satisfaction",
      "reference": "Page 4, Line 50"
    }
  ],
  "environment_mentions": {
    "industry": [
      {
        "constraint": "原文行业约束描述",
        "type": "regulation | standard | compliance | practice",
        "reference": "Page 1, Line 15"
      }
    ],
    "regional": [
      {
        "constraint": "原文地域约束描述",
        "type": "regulation | culture | market",
        "reference": "..."
      }
    ],
    "organizational": [
      {
        "constraint": "原文组织约束描述",
        "type": "scale | architecture | budget | strategy",
        "reference": "..."
      }
    ],
    "technical": [
      {
        "constraint": "原文技术约束描述",
        "type": "stack | integration | standard | vendor",
        "reference": "..."
      }
    ]
  },
  "raw_quotes": [
    {
      "quote": "Guest experience is everything",
      "speaker": "CIO",
      "speaker_role": "Decision Maker",
      "context": "原文上下文...",
      "topic": "guest_experience",
      "reference": "Page 1, Line 18"
    }
  ],
  "scenario_mentions": [
    {
      "scenario_name": "Guest check-in",
      "participants": ["Guest", "Front desk staff"],
      "context": "原文场景描述...",
      "trigger": "原文触发条件...",
      "outcome": "原文结果...",
      "reference": "Page 2, Lines 20-30"
    }
  ],
  "lifecycle_mentions": [
    {
      "phase": "Deployment",
      "activities": ["原文活动描述..."],
      "duration": "原文提及的时间...",
      "reference": "..."
    }
  ]
}
```

## LLM File Capability Check

**NOT ALL LLM PROVIDERS SUPPORT FILE UPLOAD/READ**

Before processing documents, check LLM file capability:

| LLM Capability | Supports | Action |
|----------------|----------|--------|
| Direct file read | ✅ Yes | LLM can read PDF/Text files directly |
| No file support | ❌ No | Use local Python tools for PDF extraction |

### Check Method

```python
# Pseudo-code for LLM capability check
llm_supports_files = check_llm_capability("file_read")

if llm_supports_files:
    # Direct approach: LLM reads files
    approach = "direct_llm_read"
else:
    # Fallback: Use Python tools
    approach = "local_python_extraction"
```

### Local Python PDF Tools (When LLM No File Support)

**Required Tools**:
```bash
# Install dependencies
pip install PyPDF2 pdfplumber pypdf

# Or use system command
# macOS: brew install poppler
# Linux: apt-get install poppler-utils
```

**Python PDF Extraction Script**:

```python
import pdfplumber
from pathlib import Path

def extract_pdf_to_text(pdf_path: str) -> str:
    """Extract text from PDF with page/line references"""
    text_with_refs = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            lines = text.split('\n')
            for line_num, line in enumerate(lines, start=1):
                text_with_refs.append(f"[Page {page_num}, Line {line_num}] {line}")
    
    return '\n'.join(text_with_refs)

# Usage
pdf_path = "/path/to/document.pdf"
text = extract_pdf_to_text(pdf_path)
```

**Alternative: Using pdftotext (Command Line)**:
```bash
pdftotext -layout input.pdf output.txt
```

### PDF Processing Decision Flow

```
Input: Document
    ↓
Check LLM File Capability
    ├── YES → LLM directly reads file
    │         ├── Parse content
    │         └── Extract structured data
    │
    └── NO  → Use local Python tool
              ├── Extract PDF to text with refs
              ├── Save to intermediate file
              └── LLM processes text
```

### Error Handling

| Error Type | Detection | Recovery |
|------------|-----------|----------|
| LLM cannot read file | File read API error | Fallback to Python tool |
| Python tool missing | Module import error | Auto-install or prompt user |
| PDF corrupted | Extraction fails | Log to problem list |

## Extraction Workflow

```
Step 0: LLM Capability Check
├── Check if LLM supports file upload/read
├── If YES: Proceed with direct file read
└── If NO: Use local Python PDF tool first

Step 1: Source Processing
├── If LLM supports files:
│   └── LLM directly reads PDF/Text file
└── If LLM no file support:
    ├── Use Python pdfplumber or pdftotext
    ├── Extract text with page/line references
    └── Save to intermediate .txt file
├── Add line markers (format: Line N, Page M)
├── Clean headers/footers
└── Validate text completeness
├── Add line markers (format: Line N, Page M)
├── Clean headers/footers
└── Validate text completeness

Step 2: Language Detection
├── Detect primary language
├── Store language in document_meta
└── (English default for vendor case studies)

Step 3: Customer Info Extraction
├── Extract title (first heading or metadata)
├── Extract company name (customer organization)
├── Detect country (geographic references)
├── Detect industry (business type keywords)
├── Estimate year (date references)
└── Add reference markers

Step 4: State Extraction
├── Initial state: problem paragraphs, organizational context
├── Final state: benefit paragraphs, outcome descriptions
├── Extract key problems list
├── Extract benefits list
└── Add reference markers

Step 5: Stakeholder Extraction
├── Role keyword patterns (CEO, CIO, IT Director, Staff, Guest...)
├── Extract role mentions with context
├── Extract expectations_raw (原文期望表达)
├── Extract influence hints (决策权、预算控制等线索)
└── Add reference markers

Step 6: Pain Points Extraction
├── Problem indicator patterns (challenge, problem, issue, difficulty)
├── Associate with stakeholder
├── Categorize hints (workflow, efficiency, experience)
├── Extract impact descriptions
└── Add reference markers

Step 7: Product Extraction
├── Product name patterns (vendor product names)
├── Extract product type hints
├── Extract feature mentions
├── Add reference markers

Step 8: Metrics Extraction
├── Number + unit patterns (30%, 500 users, 2 days)
├── Extract comparison context (before/after)
├── Categorize type hints
├── Add reference markers

Step 9: Environment Extraction
├── Industry constraint keywords (compliance, regulation, standard)
├── Regional constraint keywords (country-specific, cultural)
├── Organizational constraint keywords (scale, budget, strategy)
├── Technical constraint keywords (integration, legacy system)
└── Add reference markers

Step 10: Quote Extraction
├── Quoted speech patterns ("...", 「...」)
├── Identify speaker and role
├── Extract topic and context
└── Add reference markers

Step 11: Output Generation
├── Generate extracted.md with organized sections
├── Generate extracted.json with structured data
└── Validation check
```

## Extraction Patterns Reference

### Role Keyword Patterns

| Role Category | Keywords |
|---------------|----------|
| Decision Maker | CEO, CIO, CTO, Director, VP, Head of, Chief |
| Management | Manager, Lead, Supervisor, Administrator |
| Technical | IT Team, Network Engineer, System Admin, Developer |
| Operations | Operations, Support, Maintenance, Staff |
| User | Guest, Patient, Student, Employee, Customer, Resident |
| External | Vendor, Partner, Supplier, Regulator |

### Pain Point Indicator Patterns

| Category | Keywords |
|----------|----------|
| Workflow Bottleneck | manual, time-consuming, inefficient, bottleneck, slow |
| Efficiency Obstacle | overhead, complexity, burden, resource constraint |
| Experience Barrier | frustration, dissatisfaction, poor experience, complaint |

### Metric Patterns

| Type | Patterns |
|------|----------|
| Percentage | XX%, reduced by X%, improved X% |
| Count | XX users, XX devices, XX locations |
| Time | XX days, XX hours, XX minutes |
| Comparison | from X to Y, X → Y, before: X, after: Y |

### Product Type Patterns

| Type | Keywords |
|------|----------|
| Platform | platform, portal, dashboard, console |
| Product | switch, router, access point, device |
| Service | support, maintenance, consulting, managed service |
| Component | license, module, feature, add-on |

## Quality Requirements

### Extraction Completeness Check

```
Required Fields:
- [ ] document_meta complete
- [ ] customer_info.title exists
- [ ] customer_info.company exists
- [ ] initial_state.description exists
- [ ] final_state.description exists
- [ ] At least 1 stakeholder_mention
- [ ] At least 1 product_mention

Optional but Recommended:
- [ ] At least 1 pain_points_mention
- [ ] At least 1 metrics_mention
- [ ] At least 1 raw_quote
```

### Traceability Requirements

**Every extracted data item must include reference**:
- Format: `"Page X, Line Y"` or `"Line Y"` for text files
- Location must be precise enough to locate original text
- Multiple locations if extracted from multiple places

### Output Validation

| Validation | Criteria |
|------------|----------|
| JSON Valid | Parseable JSON structure |
| MD Readable | Human-readable formatting |
| Reference Accuracy | Reference locations exist in source |
| Field Coverage | Required fields present |

## Parallel Processing Strategy

| Document Count | Recommended Agents | Strategy |
|----------------|-------------------|----------|
| 1-10 | 1 | Serial processing |
| 11-30 | 2-3 | Small batch parallel |
| 31-50 | 4-5 | Medium batch parallel |
| 50+ | 6-8 | Large batch parallel |

## Progress Report Structure

```
# Phase 2a Parser Progress Report

## Execution Status
- Phase: 2a (Parser)
- Status: in_progress / completed
- Started: YYYY-MM-DD HH:MM:SS
- Last Updated: YYYY-MM-DD HH:MM:SS

## Progress Summary
| Metric | Count |
|--------|-------|
| Total Documents | N |
| Processed | M |
| Pending | P |
| Failed | F |

## Processed Documents
| # | Source | Output MD | Output JSON | Status |

## Pending Documents
| # | Source | Expected Output |

## Failed Documents
| # | Source | Error | Suggested Action |

## Next Actions
- [ ] Continue pending documents
- [ ] Handle failed documents
- [ ] Proceed to Phase 2b (Analyzer)
```

## Integration with scenario_analyzer

### Analyzer Input Requirements

Analyzer expects:
- `extracted.md` for human review and context
- `extracted.json` for structured data input

Analyzer workflow:
```
1. Read extracted.json
2. Read extracted.md for context verification
3. Validate input completeness
4. Generate 12-section analysis report
```

### Data Flow

```
Parser Output → Analyzer Input

extracted.json fields → Analyzer sections:
├── customer_info → Section 0: Customer Basic Information
├── stakeholder_mentions → Section 2: Stakeholder List
├── pain_points_mentions → Section 2: Pain Points sub-section
├── initial_state → Section 0: Initial State
├── final_state → Section 0: Final State
├── metrics_mentions → Section 1: Purchase Elements, Section 11: Parameterization
├── product_mentions → Section 10: Products and Solutions
├── environment_mentions → Section 5: Environment Model
├── scenario_mentions → Section 8: Operational Scenarios
└── raw_quotes → Section 12: Traceability
```

## Recovery Support

Parser outputs are checkpoint files:
- If Parser completes but Analyzer fails: Skip Parser, retry Analyzer
- If Parser partially fails: Re-process failed documents only
- State.json tracks Parser completion separately

## Version History

- **0.1.1** (2026-05-06): Add LLM file capability check
  - LLM capability detection for file upload/read
  - Fallback to local Python PDF tools when LLM no file support
  - Python pdfplumber/pdftotext extraction examples

- **0.1.0** (2026-04-21): Initial scenario_parser SKILL
  - Document extraction from PDF/text/narratives
  - Dual-format output (MD + JSON)
  - Full traceability references
  - Integration with scenario_analyzer