# Extraction Patterns Reference

## Overview

This document defines keyword patterns and extraction rules for scenario_parser.

---

## Role Keyword Patterns

### Decision Maker Keywords

| Role | Keywords (English) | Keywords (Chinese) |
|------|-------------------|-------------------|
| CEO | CEO, Chief Executive, President | 首席执行官, 总裁 |
| CIO | CIO, Chief Information Officer | 首席信息官 |
| CTO | CTO, Chief Technology Officer | 首席技术官 |
| Director | Director, Head of, VP, Vice President | 总监, 副总裁, 部门负责人 |
| CFO | CFO, Chief Financial Officer | 首席财务官 |

### Management Keywords

| Role | Keywords (English) | Keywords (Chinese) |
|------|-------------------|-------------------|
| Manager | Manager, Lead, Supervisor | 经理, 主管, 负责人 |
| IT Manager | IT Manager, Network Manager, System Manager | IT经理, 网络经理, 系统经理 |
| Operations Manager | Operations Manager, Ops Lead | 运维经理, 运营主管 |

### Technical Keywords

| Role | Keywords (English) | Keywords (Chinese) |
|------|-------------------|-------------------|
| IT Team | IT Team, IT Staff, IT Department | IT团队, IT部门, 技术团队 |
| Engineer | Engineer, Network Engineer, System Admin | 工程师, 网络工程师, 系统管理员 |
| Developer | Developer, Software Engineer | 开发人员, 软件工程师 |

### Operations Keywords

| Role | Keywords (English) | Keywords (Chinese) |
|------|-------------------|-------------------|
| Operations | Operations, Support, Maintenance | 运维, 支持, 维护团队 |
| Staff | Staff, Employee, Worker | 员工, 工作人员 |
| Front Desk | Front Desk, Reception | 前台, 接待 |

### User Keywords

| Role | Keywords (English) | Keywords (Chinese) |
|------|-------------------|-------------------|
| Guest | Guest, Visitor, Customer | 客人, 来宾, 顾客 |
| Patient | Patient, Resident | 患者, 病人, 居民 |
| Student | Student, Faculty, Teacher | 学生, 教职工, 老师 |
| Employee | Employee, Staff, Worker | 员工, 职员 |
| Consumer | Consumer, Buyer, Shopper | 消费者, 购买者 |

### External Keywords

| Role | Keywords (English) | Keywords (Chinese) |
|------|-------------------|-------------------|
| Vendor | Vendor, Supplier, Provider | 供应商, 厂商 |
| Partner | Partner, Reseller, Distributor | 合作伙伴, 经销商 |
| Regulator | Regulator, Government, Authority | 监管机构, 政府, 管理部门 |

---

## Pain Point Indicator Patterns

### Workflow Bottleneck Indicators

| English | Chinese |
|---------|---------|
| manual, time-consuming, inefficient | 手动, 耗时, 效率低 |
| bottleneck, slow, delay | 瓶颈, 缓慢, 延迟 |
| complex process, tedious | 复杂流程, 繁琐 |
| manual configuration, manual entry | 手动配置, 手动输入 |

### Efficiency Obstacle Indicators

| English | Chinese |
|---------|---------|
| overhead, burden, workload | 开销, 负担, 工作量大 |
| resource constraint, limited staff | 资源受限, 人员不足 |
| complexity, difficult to manage | 复杂, 管理困难 |
| IT burden, operational burden | IT负担, 运维负担 |

### Experience Barrier Indicators

| English | Chinese |
|---------|---------|
| frustration, dissatisfaction, complaint | 挫败, 不满意, 投诉 |
| poor experience, bad experience | 体验差, 体验不佳 |
| unhappy, disappointed | 不高兴, 失望 |
| complaint, negative feedback | 投诉, 负面反馈 |

---

## Product Type Patterns

### Platform Products

| Keywords |
|----------|
| platform, portal, dashboard, console |
| management platform, cloud platform |
| Central, ClearPass, Unity |

### Hardware Products

| Keywords |
|----------|
| switch, router, access point, AP |
| controller, gateway, firewall |
| Wi-Fi, wireless, network device |

### Service Products

| Keywords |
|----------|
| support, maintenance, managed service |
| consulting, implementation, deployment |
| NaaS, network-as-a-service |

### Component Products

| Keywords |
|----------|
| license, module, feature, add-on |
| subscription, entitlement |
| upgrade, extension |

### Vendor Recognition Patterns

| Vendor | Product Patterns |
|--------|-----------------|
| HPE Aruba | Aruba, Central, ClearPass, AP, switch |
| Cisco | Cisco, Meraki, Catalyst, IOS |
| Juniper | Juniper, Mist, EX, SRX |

---

## Metric Extraction Patterns

### Percentage Patterns

```
Pattern: \d+% | XX percent | improved by X% | reduced by X%

Examples:
- "运维效率提升30%"
- "cost savings of 25%"
- "reduced by 50%"
```

### Count Patterns

```
Pattern: \d+ (users|devices|locations|sites|nodes)

Examples:
- "26500 students"
- "500 access points"
- "12 locations"
```

### Time Patterns

```
Pattern: \d+ (days|hours|minutes|weeks|months)

Examples:
- "deployment in 2 days"
- "reduced from 30 days to 3 days"
- "response time under 5 minutes"
```

### Comparison Patterns

```
Pattern: from X to Y | X → Y | before: X, after: Y

Examples:
- "from 30 days to 3 days"
- "troubleshooting: days → hours"
- "before: 100 tickets, after: 0 tickets"
```

### Metric Type Classification

| Metric Type | Indicators |
|-------------|------------|
| efficiency | 提升, improvement, efficiency, faster |
| cost | 成本, cost, savings, reduce, budget |
| time | 时间, days, hours, faster, quicker |
| quality | 质量, quality, reliability, uptime |
| satisfaction | 满意度, satisfaction, NPS, experience |

---

## Environment Constraint Patterns

### Industry Environment

| Type | Keywords |
|------|----------|
| regulation | HIPAA, GDPR, FERPA, PCI, compliance, regulation |
| standard | ISO, IEC, standard, certification |
| compliance | compliance, regulatory, mandate, requirement |
| practice | industry practice, best practice, common practice |

### Regional Environment

| Type | Keywords |
|------|----------|
| regulation | national regulation, local law, country-specific |
| culture | cultural, local custom, regional characteristic |
| market | market maturity, local market, regional market |

### Organizational Environment

| Type | Keywords |
|------|----------|
| scale | large-scale, small-scale, enterprise, SMB |
| architecture | centralized, distributed, hybrid, cloud |
| budget | budget constraint, cost limitation, financial |
| strategy | strategic, transformation, digitalization |

### Technical Environment

| Type | Keywords |
|------|----------|
| stack | tech stack, technology, infrastructure, legacy |
| integration | integration, interoperability, connectivity |
| standard | technical standard, protocol, specification |
| vendor | vendor relationship, supplier, partner |

---

## Quote Extraction Patterns

### English Quote Patterns

```
Pattern 1: "Quoted text"
Pattern 2: 'Quoted text'
Pattern 3: Speaker said, "Quote text"
Pattern 4: "Quote text," said Speaker
```

### Chinese Quote Patterns

```
Pattern 1: 「引号内容」
Pattern 2: "引号内容"
Pattern 3: XX表示：「内容」
Pattern 4: XX说：「内容」
```

### Speaker Identification

| Pattern | Speaker Position |
|---------|-----------------|
| "Quote," said X | After quote |
| X said, "Quote" | Before quote |
| According to X, "Quote" | Before quote |
| X: "Quote" | Colon separator |

---

## Reference Marker Format

### PDF Sources

```
Format: "Page X, Line Y"

Example:
- "Page 3, Line 25"
- "Page 1-2, Lines 10-30"
```

### Text Sources

```
Format: "Line Y"

Example:
- "Line 45"
- "Lines 100-150"
```

### Section References

```
Format: "Section X.Y: Title"

Example:
- "Section 2.1: Customer Challenges"
- "Paragraph 3"
```

---

## Extraction Rules

### ER-01: Multiple Mentions

If stakeholder/product mentioned multiple times:
- Record each mention separately
- Include all reference locations
- Note context differences

### ER-02: Context Preservation

Extract sufficient context around mentions:
- At least 50 characters before/after
- Preserve original language
- Include surrounding sentences

### ER-03: Reference Precision

Reference must be precise enough to locate:
- Use smallest meaningful unit (line/paragraph)
- If spanning multiple lines, note range
- If unclear, use approximate with "~" marker

### ER-04: Original Language

Extract quotes and context in original language:
- Do not translate
- Maintain original wording
- Note language in document_meta

---

## File Naming Structure

### Basic Format

```
{Timestamp}-{ContentType}-{KeyIdentifier}-{Seq}-extracted.{ext}
```

### Component Definitions

| Component | Definition | Example | Source |
|-----------|------------|---------|--------|
| Timestamp | 提取时间戳 | `20260421T1030` | 执行时间 |
| ContentType | 内容类型 | `Case`, `Report`, `Industry` | 内容分类判断 |
| KeyIdentifier | 关键标识 | `Hospitality-SouthernSun` | 内容提取 |
| Seq | 序列号 | `001`, `002` | 同批同类型多文档（可选） |
| ext | 扩展名 | `md`, `json` | 固定值 |

---

## Content Type Classification（内容类型判断）

根据文档内容自动判断类型：

### CT-01: Case（客户案例）

**判断条件**（满足任意2项）:
- 包含客户公司名
- 包含具体部署场景描述
- 包含"customer story", "case study", "success story"
- 包含初始状态→最终状态的转变描述
- 包含产品使用效果数据

**KeyIdentifier**: `{Industry}-{CustomerNameNormalized}`

**示例**:
```
输入: Southern Sun 酒店网络升级案例
判断: 包含客户名 "Southern Sun" + 部署场景 + 效果数据 → ContentType = Case
Industry = Hospitality
CustomerNameNormalized = SouthernSun
输出: 20260421T1030-Case-Hospitality-SouthernSun-extracted.md
```

### CT-02: Report（行业/市场报告）

**判断条件**（满足任意2项）:
- 标题包含 "Market", "Trends", "Analysis", "Benchmark"
- 包含行业整体数据统计
- 包含多客户案例汇总
- 无单一客户深入描述
- 包含"white paper", "industry report", "market analysis"

**KeyIdentifier**: `{Industry}-{ReportTopic}`

**ReportTopic 判断规则**:
| 标题关键词 | ReportTopic |
|-----------|-------------|
| Market, Trends | MarketTrends |
| White Paper, Guide | WhitePaper |
| Analysis, Overview | IndustryAnalysis |
| Benchmark, Comparison | Benchmark |
| Technology, Tech | TechnologyReport |
| ROI, Value | ROIAnalysis |

**示例**:
```
输入: Hospitality Industry Market Trends 2026
判断: 标题含 "Market" + "Trends" → ContentType = Report
Industry = Hospitality
ReportTopic = MarketTrends
输出: 20260421T1030-Report-Hospitality-MarketTrends-extracted.md
```

### CT-03: Industry（行业概述）

**判断条件**（满足任意2项）:
- 内容聚焦行业特性描述
- 无具体客户或产品
- 包含行业术语、流程、标准
- 包含"industry overview", "sector profile", "industry characteristics"

**KeyIdentifier**: `{Industry}`

**示例**:
```
输入: Healthcare Industry Characteristics and Challenges
判断: 无客户名 + 聚焦行业特性 → ContentType = Industry
Industry = Healthcare
输出: 20260421T1030-Industry-Healthcare-extracted.md
```

### CT-04: Product（产品文档）

**判断条件**（满足任意2项）:
- 内容聚焦单一产品介绍
- 包含产品规格、功能、参数
- 包含产品名称
- 包含"product overview", "technical specification", "datasheet"

**KeyIdentifier**: `{ProductNameNormalized}`

**示例**:
```
输入: Aruba Central Cloud Platform Technical Overview
判断: 聚焦产品 "Aruba Central" + 技术规格 → ContentType = Product
ProductNameNormalized = ArubaCentral
输出: 20260421T1030-Product-ArubaCentral-extracted.md
```

### CT-05: Survey（Survey 输出）

**判断条件**:
- 来自 scenario_survey 的叙事文档
- 文件名包含 "-narrative"
- 包含调研记录格式

**KeyIdentifier**: `{Industry}-{Country}`

**示例**:
```
输入: 来自 scenario_survey 的 Hospitality-Malaysia 调研叙事
判断: Survey 输出 → ContentType = Survey
Industry = Hospitality
Country = Malaysia
输出: 20260421T1030-Survey-Hospitality-Malaysia-extracted.md
```

### CT-06: Mixed（混合/未知）

**判断条件**:
- 无法明确归类到以上类型
- 多类型特征混合
- 内容结构不清晰

**KeyIdentifier**: `{CustomerOrDefault}`

**示例**:
```
输入: 未知结构文档
判断: 无法归类 → ContentType = Mixed
输出: 20260421T1030-Mixed-General-extracted.md

输入: 包含客户名但无案例结构
判断: Mixed，使用客户名
输出: 20260421T1030-Mixed-SouthernSun-extracted.md
```

---

## Timestamp Format Rules（时间戳格式）

### TS-01: 精确时间戳

```
格式: YYYYMMDDTHHMM
示例: 20260421T1030

使用场景:
- 单文档即时处理
- 需要精确追踪处理时间
```

### TS-02: 日期时间戳

```
格式: YYYYMMDD
示例: 20260421

使用场景:
- 批量处理（同批次使用相同日期）
- 不需要精确时间区分
```

### TS-03: 批次时间戳

```
格式: YYYYMMDD-BatchN
示例: 20260421-Batch001, 20260421-Batch002

使用场景:
- 大规模批量处理
- 需要区分不同批次
```

### TS-04: 选择规则

| 处理场景 | 时间戳格式 |
|---------|-----------|
| 单文档处理 | `YYYYMMDDTHHMM` |
| 批量处理（<50文档） | `YYYYMMDD` |
| 大批量处理（≥50文档） | `YYYYMMDD-BatchN` |

---

## KeyIdentifier Normalization（关键标识规范化）

### KI-NR-01: Industry Normalization

使用英文标准行业名：

| 原文关键词 | 标准化 Industry |
|-----------|----------------|
| 酒店, hotel, hospitality | Hospitality |
| 医院, hospital, healthcare, medical | Healthcare |
| 学校, school, education, university | Education |
| 大学, university, college | HigherEducation |
| 物流, logistics, supply chain | Logistics |
| 制造, manufacturing, factory | Manufacturing |
| 零售, retail, store | Retail |
| 服务, services, consulting | Services |
| 体育, sports, entertainment | SportsEntertainment |

### KI-NR-02: Customer Name Normalization

```
规范化步骤:
1. 去除特殊字符: !"#$%&'()*+,./:;<=>?@[\]^_{|}~
2. 空格替换为连字符
3. 保留大小写首字母
4. 多个连字符合并为单个
5. 长度限制: 30 字符以内

Examples:
- "Southern Sun" → "SouthernSun"
- "Aberdeen City Council" → "AberdeenCityCouncil"
- "Royal Devon Healthcare" → "RoyalDevonHealthcare"
- "Moreno Valley USD" → "MorenoValleyUSD"
```

### KI-NR-03: Product Name Normalization

```
规范化步骤:
1. 保留产品正式名称
2. 去除版本号（除非关键）
3. 空格替换为连字符

Examples:
- "Aruba Central" → "ArubaCentral"
- "ClearPass Policy Manager" → "ClearPass"
- "HPE Switch Series" → "HPESwitch"
```

### KI-NR-04: Country Normalization

| 原文关键词 | 标准化 Country |
|-----------|---------------|
| UK, United Kingdom | UK |
| USA, US, United States | US |
| Malaysia | Malaysia |
| Japan | Japan |
| Germany | Germany |
| Australia | Australia |
| Saudi Arabia | SaudiArabia |

---

## Sequence Number Rules（序列号规则）

### SEQ-01: When to Add Sequence

```
条件: 同批次 + 同ContentType + 同KeyIdentifier + 多文档

规则:
- 第1份: 不添加序列号
- 第2份: 添加 -001
- 第3份: 添加 -002
- ...

示例:
20260421T1030-Case-Hospitality-SouthernSun-extracted.md       (第1份)
20260421T1030-Case-Hospitality-SouthernSun-001-extracted.md   (第2份)
20260421T1030-Case-Hospitality-SouthernSun-002-extracted.md   (第3份)
```

---

## Complete File Name Examples

### Case Type Examples

| 内容 | 生成的文件名 |
|------|-------------|
| Southern Sun 酒店案例 | `20260421T1030-Case-Hospitality-SouthernSun-extracted.md` |
| Royal Devon 医院案例 | `20260421T1030-Case-Healthcare-RoyalDevon-extracted.md` |
| Moreno Valley 学校案例 | `20260421T1030-Case-Education-MorenoValleyUSD-extracted.md` |

### Report Type Examples

| 内容 | 生成的文件名 |
|------|-------------|
| Hospitality 市场趋势报告 | `20260421T1030-Report-Hospitality-MarketTrends-extracted.md` |
| Healthcare 行业白皮书 | `20260421T1030-Report-Healthcare-WhitePaper-extracted.md` |
| Education 技术报告 | `20260421T1030-Report-Education-TechnologyReport-extracted.md` |

### Industry Type Examples

| 内容 | 生成的文件名 |
|------|-------------|
| Healthcare 行业概述 | `20260421T1030-Industry-Healthcare-extracted.md` |
| Education 行业特性 | `20260421T1030-Industry-Education-extracted.md` |

### Product Type Examples

| 内容 | 生成的文件名 |
|------|-------------|
| Aruba Central 产品介绍 | `20260421T1030-Product-ArubaCentral-extracted.md` |
| ClearPass 技术文档 | `20260421T1030-Product-ClearPass-extracted.md` |

### Batch Processing Examples

| 批次 | 文件名示例 |
|------|-----------|
| 批次1文档1 | `20260421-Batch001-Case-Hospitality-SouthernSun-extracted.md` |
| 批次1文档2 | `20260421-Batch001-Case-Healthcare-RoyalDevon-extracted.md` |
| 批次2文档1 | `20260421-Batch002-Case-Education-MorenoValleyUSD-extracted.md` |

---

## Analyzer Output Correlation

Parser 和 Analyzer 输出文件名保持相同前缀：

```
Parser:  {Timestamp}-{ContentType}-{KeyIdentifier}-extracted.{ext}
Analyzer: {Timestamp}-{ContentType}-{KeyIdentifier}-analysis.md

示例:
Parser:  20260421T1030-Case-Hospitality-SouthernSun-extracted.md/json
Analyzer: 20260421T1030-Case-Hospitality-SouthernSun-analysis.md
```

---

## JSON File Name Metadata Structure

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
      "type_reason": "Contains customer name and deployment story",
      "classification_criteria_matched": [
        "customer_name_present",
        "deployment_scenario",
        "outcome_data"
      ]
    }
  }
}
```

---

*Reference: Extraction Patterns v0.2.0*