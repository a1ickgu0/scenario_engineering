# Bilingual Quote Reference Requirement Framework

## Purpose

This framework establishes mandatory requirements for bilingual quote references in scenario_modeler analysis. It ensures all non-Chinese source quotes are provided with Chinese translations, enabling comprehensive traceability and understanding across language barriers.

---

## Core Requirement

**Rule**: For all source quotes that are not in Chinese, both the original language version AND a Chinese translation must be provided.

**Mandatory Scope**:
- All original quotes from source documents
- All stakeholder statements and interviews
- All business driver descriptions
- All quantified metric statements
- All product/solution descriptions
- All challenge and pain point descriptions

---

## Bilingual Quote Format

### Standard Format

```
**Original Quote** ([Language]):
"[Original text in source language]"

**中文翻译**:
"[Chinese translation of the original quote]"
```

### Compact Format (for tables)

```
| English Quote | Chinese Translation |
|--------------|-------------------|
| "[Original text]" | "[中文翻译]" |
```

### Extended Format (with context)

```
**Original Quote** (English):
"[Original text]"

**中文翻译**:
"[中文翻译]"

**Context**: [Additional context about the quote]
**Attribution**: [Who said it, role]
**Source**: [Document, Page X, Line Y]
```

---

## Language Categories and Translation Requirements

### Category 1: English Sources

**Definition**: Original quotes in English from customer stories, case studies, or interviews.

**Translation Requirement**: MANDATORY Chinese translation

**Format**:
```
Original Quote (English):
"The new Wi-Fi 6E deployment has completely transformed our guest experience, with 99% coverage and seamless connectivity."

中文翻译:
"新的Wi-Fi 6E部署彻底改变了我们的客户体验，实现了99%的覆盖率和无缝连接。"
```

---

### Category 2: Other European Languages

**Definition**: Original quotes in German, French, Spanish, Italian, etc.

**Translation Requirement**: MANDATORY Chinese translation

**Format**:
```
Original Quote (German):
"Die 100GbE-Infrastruktur ermöglicht es uns, wettbewerbsfähig zu bleiben und Forschungsprojekte einzuwerben."

中文翻译:
"100GbE基础设施使我们能够保持竞争力并获得研究项目。"
```

---

### Category 3: Asian Languages

**Definition**: Original quotes in Japanese, Korean, Vietnamese, Thai, etc.

**Translation Requirement**: MANDATORY Chinese translation

**Format**:
```
Original Quote (Japanese):
「新しいネットワークインフラにより、運用効率が30%向上しました」

中文翻译:
"通过新的网络基础设施，运营效率提升了30%。"
```

---

### Category 4: Chinese Sources

**Definition**: Original quotes already in Chinese (Simplified or Traditional).

**Translation Requirement**: OPTIONAL - Chinese source is sufficient, but consider providing English for international audience

**Format**:
```
Original Quote (Chinese):
"运营效率是我们的主要驱动力，我们正在通过AIOps实现70%的减负。"

English Translation (Optional):
"Operations efficiency is our primary driver, we're achieving 70% burden reduction through AIOps."
```

---

## Translation Quality Standards

### Standard 1: Accuracy (准确性)

**Requirement**: Translation must accurately convey original meaning without distortion.

**Quality Criteria**:
- No significant meaning deviation
- Technical terms translated correctly
- Quantified values preserved exactly
- Context maintained

**Example**:
```
✓ Accurate:
Original: "We achieved a 30% efficiency improvement."
翻译: "我们实现了30%的效率提升。"

✗ Inaccurate:
Original: "We achieved a 30% efficiency improvement."
翻译: "我们的效率有很大提升。" (Lost specific 30% value)
```

---

### Standard 2: Completeness (完整性)

**Requirement**: Translation must include all information from original quote.

**Quality Criteria**:
- No omitted information
- No skipped details
- Complete coverage of original message
- All quantified values included

**Example**:
```
✓ Complete:
Original: "Deployment time reduced from 2 days to 30 minutes, saving us 97.9% of deployment time."
翻译: "部署时间从2天减少到30分钟，为我们节省了97.9%的部署时间。"

✗ Incomplete:
Original: "Deployment time reduced from 2 days to 30 minutes, saving us 97.9% of deployment time."
翻译: "部署时间从2天减少到30分钟。" (Missing 97.9% savings)
```

---

### Standard 3: Terminology Consistency (术语一致性)

**Requirement**: Technical terms and industry jargon must be translated consistently.

**Quality Criteria**:
- Technical terms standardized across translations
- Industry-specific jargon handled appropriately
- Acronyms preserved or explained
- Consistent translation for same term

**Terminology Examples**:

| English Term | Standard Chinese Translation | Notes |
|-------------|--------------------------|-------|
| Wi-Fi 6E | Wi-Fi 6E | Keep technical term |
| AIOps | AIOps / AI运维 | Can use bilingual |
| Zero Trust | 零信任架构 | Standard term |
| SD-WAN | SD-WAN / 软件定义广域网 | Keep acronym, add Chinese |
| HIMSS | HIMSS | Keep certification name |
| CIO | CIO / 首席信息官 | Can use bilingual |

---

### Standard 4: Readability (可读性)

**Requirement**: Translation should be natural and readable in Chinese.

**Quality Criteria**:
- Grammatically correct Chinese
- Natural phrasing and flow
- Appropriate formality level
- Professional business language

**Example**:
```
✓ Natural:
Original: "The CIO has decision-making authority up to $5M."
翻译: "CIO拥有高达500万美元的决策权限。"

✗ Unnatural:
Original: "The CIO has decision-making authority up to $5M."
翻译: "CIO具有决策权威高达500万美元。" (Unnatural phrasing)
```

---

## Bilingual Quote Implementation by Output Section

### Section 1: Business Background Analysis

**Requirement**: All business context statements must have bilingual quotes.

**Format**:
```
## Business Background

### Industry Context
**Original Quote** (English):
"As a higher education institution with research focus, we compete for research grants based on our technical infrastructure."

中文翻译:
"作为一所以研究为重点的高等教育机构，我们根据技术基础设施竞争研究经费。"

**Confidence**: HIGH
**Basis**: Explicit Statement (Page 2, Line 15)
```

---

### Section 2: Stakeholder Analysis

**Requirement**: All stakeholder statements and roles must have bilingual quotes.

**Format**:
```
## Stakeholder Analysis

### CIO Role Description
**Original Quote** (English):
"The CIO has final decision-making authority for IT investments up to $5M, with strategic oversight of all digital initiatives."

中文翻译:
"CIO对高达500万美元的IT投资拥有最终决策权，并对所有数字举措进行战略监督。"

**Confidence**: HIGH
**Basis**: Explicit Statement (Page 5, Line 23)
```

---

### Section 3: Business Driver Analysis

**Requirement**: All business driver descriptions must have bilingual quotes.

**Format**:
```
## Business Driver Analysis

### Primary Driver: Operations Efficiency
**Original Quote** (English):
"Operations efficiency is our primary driver, with IT burden being our biggest challenge. We need to reduce routine tasks by 70%."

中文翻译:
"运营效率是我们的主要驱动力，IT负担是我们最大的挑战。我们需要将日常任务减少70%。"

**Confidence**: HIGH
**Basis**: Direct Citation (Page 3, Line 12)
```

---

### Section 4: Quantified Metrics (MoE)

**Requirement**: All quantified metric statements must have bilingual quotes.

**Format**:
```
## Quantified Metrics

### Efficiency Improvement
**Metric**: 30% operations efficiency improvement
**Original Quote** (English):
"We've achieved a 30% improvement in our operations efficiency through the new network automation."

中文翻译:
"通过新的网络自动化，我们的运营效率提升了30%。"

**Confidence**: HIGH
**Credibility**: HIGH
**Source**: Direct Measurement (Page 8, Line 34)
```

---

### Section 5: Traceability Tables

**Requirement**: All traceability table quotes must have bilingual format.

**Format**:
```
## Traceability Table

| Customer Name | Original Quote (English) | Original Quote (Chinese) | Source Reference |
|--------------|---------------------------|-------------------------|-----------------|
| Austrian Red Cross | "AIOps reduces IT burden by 70%" | "AIOps将IT负担减轻了70%" | Page 5, Line 23 |
| Aberdeen City Council | "Deployment time from 2 days to 30 min" | "部署时间从2天缩短到30分钟" | Page 8, Line 34 |
| University of Illinois | "Research competitiveness enabled" | "研究竞争力得到提升" | Page 2, Line 15 |
```

---

## Bilingual Quote Validation Checklist

### Completeness Check
- [ ] Original quote provided
- [ ] Chinese translation provided (for non-Chinese sources)
- [ ] Source language identified
- [ ] Attribution included (who said it)
- [ ] Context provided (if needed)

### Quality Check
- [ ] Translation accurate (no meaning distortion)
- [ ] Translation complete (no omissions)
- [ ] Terminology consistent (technical terms)
- [ ] Translation natural (readable Chinese)
- [ ] Quantified values preserved exactly

### Traceability Check
- [ ] Source reference provided (document, page, line)
- [ ] Stakeholder attribution clear
- [ ] Time period/context included (if relevant)
- [ ] Cross-reference to other models (if applicable)

---

## Translation Best Practices

1. **Always Provide Both Versions**: Never omit either original or translation
2. **Identify Source Language**: Clearly state original language
3. **Preserve Technical Terms**: Keep acronyms and technical terms when appropriate
4. **Translate Quantified Values Exactly**: Never approximate numbers
5. **Maintain Professional Tone**: Use appropriate business language
6. **Provide Context**: Add context when quote meaning depends on situation
7. **Use Standard Terminology**: Establish and use consistent Chinese translations
8. **Consider Audience**: Make Chinese accessible to target audience
9. **Verify Accuracy**: Review translations for accuracy and completeness
10. **Flag Uncertain Translations**: Note when translation quality is uncertain

---

## Common Translation Patterns

### Pattern 1: Efficiency Metrics

| English Pattern | Chinese Translation |
|----------------|-------------------|
| "X% efficiency improvement" | "X%的效率提升" |
| "X% reduction in time" | "时间减少X%" |
| "X% burden reduction" | "负担减轻X%" |
| "X% productivity gain" | "生产力提高X%" |

### Pattern 2: Cost Metrics

| English Pattern | Chinese Translation |
|----------------|-------------------|
| "$X cost savings" | "节省$X成本" |
| "X% cost reduction" | "成本降低X%" |
| "X% ROI" | "X%的投资回报率" |
| "X months payback" | "X个月回本" |

### Pattern 3: Deployment Metrics

| English Pattern | Chinese Translation |
|----------------|-------------------|
| "Deployed in X months" | "在X个月内部署完成" |
| "X sites deployed" | "部署了X个站点" |
| "X% coverage achieved" | "实现了X%的覆盖率" |
| "Rollout completed" | "推广完成" |

### Pattern 4: User Experience Metrics

| English Pattern | Chinese Translation |
|----------------|-------------------|
| "X% user satisfaction" | "X%的用户满意度" |
| "Seamless connectivity" | "无缝连接" |
| "X% adoption rate" | "X%的采用率" |
| "Improved experience" | "体验改善" |

### Pattern 5: Compliance Metrics

| English Pattern | Chinese Translation |
|----------------|-------------------|
| "Achieved X certification" | "达成X认证" |
| "X% compliance" | "X%的合规性" |
| "Met X standard" | "符合X标准" |
| "Passed X audit" | "通过X审计" |

---

## Integration with Other Frameworks

This framework integrates with:

1. **Confidence Level Framework**: Apply bilingual quotes to all confidence assessments
2. **MoE Indicators Framework**: All quantified metrics require bilingual quotes
3. **Business Background Driver Priority**: All business driver statements require bilingual quotes
4. **Stakeholder Role Hierarchy**: All stakeholder statements require bilingual quotes
5. **Cross-Model Consistency**: Ensure consistent bilingual format across models
6. **Automated Validation Framework**: Validate bilingual quote completeness

---

## Example: Complete Bilingual Quote Documentation

### Business Driver Example

```
## Primary Business Driver: Operations Efficiency Optimization

### Driver Description
**Original Quote** (English):
"Our primary driver is operations efficiency - we need to reduce the IT team's operational burden from 70% of their time to 20%, enabling them to focus on strategic initiatives rather than routine tasks."

中文翻译:
"我们的主要驱动力是运营效率——我们需要将IT团队的运营负担从其时间的70%降低到20%，使他们能够专注于战略举措而非日常任务。"

### Quantified Metrics
**Original Quote** (English):
"Through Central cloud management and AIOps automation, we've achieved a 70% reduction in IT burden and a 100% elimination of routine network support tickets."

中文翻译:
"通过Central云管理和AIOps自动化，我们实现了IT负担降低70%，并100%消除了常规网络支持工单。"

### Confidence Assessment
- **Confidence Level**: HIGH ★★★★★
- **Basis**: Direct Citation (Page 3, Lines 12-15)
- **Credibility**: HIGH (Direct stakeholder statement)

### Source Traceability
- **Document**: Austrian Red Cross Case Study
- **Section**: Business Drivers and Value
- **Page/Line**: Page 3, Lines 12-15
- **Attribution**: CIO interview
- **Context**: Discussing primary motivations for AIOps deployment
```

---

## Implementation Guidelines

### For Analysts

1. **Always Translate**: Never leave non-Chinese quotes untranslated
2. **Use Standard Format**: Follow the defined bilingual format
3. **Check Quality**: Review translations for accuracy and completeness
4. **Maintain Consistency**: Use consistent terminology throughout
5. **Document Source**: Always provide source references

### For Reviewers

1. **Verify Completeness**: Check that all quotes have translations
2. **Assess Accuracy**: Review translations for meaning accuracy
3. **Check Terminology**: Ensure technical terms are translated consistently
4. **Validate Traceability**: Confirm source references are complete
5. **Flag Issues**: Note any translation quality concerns

### For Validators

1. **Check Compliance**: Verify bilingual format is used consistently
2. **Assess Quality**: Evaluate translation quality against standards
3. **Verify Completeness**: Ensure no quotes are missing translations
4. **Check Traceability**: Confirm source references are complete
5. **Generate Reports**: Report any bilingual quote issues found

---

## Glossary of Standard Chinese Translations

### Technical Terms

| English Term | Standard Chinese | Alternative |
|-------------|------------------|-------------|
| Wi-Fi 6E | Wi-Fi 6E | 第六代Wi-Fi增强版 |
| AIOps | AIOps | AI运维 / 人工智能运维 |
| Zero Trust | 零信任架构 | 零信任 |
| SD-WAN | SD-WAN | 软件定义广域网 |
| Cloud Management | 云管理 | 中央云管理 |
| Network Automation | 网络自动化 | 自动化网络 |
| Cybersecurity | 网络安全 | 网络安全 / 网络安全 |
| Deployment | 部署 | 部署 |
| Coverage | 覆盖 | 覆盖 |
| Throughput | 吞吐量 | 吞吐量 |
| Latency | 延迟 | 延迟 |

### Business Terms

| English Term | Standard Chinese | Alternative |
|-------------|------------------|-------------|
| ROI (Return on Investment) | ROI | 投资回报率 |
| CAPEX (Capital Expenditure) | CAPEX | 资本支出 |
| OPEX (Operational Expenditure) | OPEX | 运营支出 |
| TCO (Total Cost of Ownership) | TCO | 总体拥有成本 |
| Digital Transformation | 数字化转型 | 数字化转型 |
| Competitive Advantage | 竞争优势 | 竞争优势 |
| Stakeholder | 利益相关者 | 利益相关者 |
| Business Driver | 业务驱动 | 业务驱动力 |
| Pain Point | 痛点 | 痛点 |

---

## Quality Assurance Checklist

### Document-Level Check
- [ ] All non-Chinese quotes have Chinese translations
- [ ] All translations follow standard format
- [ ] Source language identified for each quote
- [ ] All quotes have attribution
- [ ] All quotes have source references

### Section-Level Check
- [ ] Business Background: All quotes bilingual
- [ ] Stakeholder Analysis: All quotes bilingual
- [ ] Business Drivers: All quotes bilingual
- [ ] MoE Indicators: All quotes bilingual
- [ ] Traceability Tables: All quotes bilingual

### Quality-Level Check
- [ ] Translations are accurate
- [ ] Translations are complete
- [ ] Terminology is consistent
- [ ] Translations are readable
- [ ] Technical terms handled appropriately

---

## Tools and Resources

### Translation Tools
- Professional translation services (recommended for formal documents)
- Machine translation with human review (acceptable for internal use)
- Bilingual glossaries for consistency

### Glossary Maintenance
- Maintain industry-specific glossary
- Update terminology based on stakeholder feedback
- Share glossary across team for consistency
- Version control glossary updates

### Quality Control
- Peer review of translations
- Native speaker verification for critical quotes
- Back-translation check for accuracy
- Terminology consistency check across documents