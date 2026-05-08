# Pipeline Quality Check Framework

## Overview

This document defines the comprehensive quality assurance framework for the SKILL pipeline, ensuring Input validation, Output verification, and Integrity Review across all stages.

---

## 1. Entry Point Validation

### 1.1 Entry Point → Input Source Mapping

| Entry Point | Required Input | Input Validation Rules | Proceed Condition |
|-------------|----------------|---------------------|-------------------|
| **survey** | Industry + Country | - Industry in template list<br>- Country in language mapping table<br>- Neither null/empty | Proceed only if valid |
| **parser** | PDF/Text/Narrative files | - File exists and is readable<br>- Content type classification succeeds | Proceed only if valid |
| **analyzer** | extracted.md + extracted.json | - Both files exist<br>- extracted.json is parseable<br>- extracted.md exists for context | Proceed only if valid |
| **modeler** | Multiple *-analysis.md files | - Minimum 3 analysis files<br>- Files are in same language/format<br>- Sufficient count for synthesis | Proceed only if valid |

### 1.2 Input Quality Validation

#### survey Input Validation

| Field | Validation Rule | Error Condition | Recovery Action |
|-------|---------------|-----------------|---------------|
| **Industry** | Must match template name in `assets/templates/` | Invalid industry → Use generic-template.md |
| **Country** | Must support language generation | Unmapped country → Use English |
| **Both Provided** | Ensure country matches industry region | Language mismatch → Use primary language |

#### parser Input Validation

| Field | Validation Rule | Error Condition | Recovery Action |
|-------|---------------|-----------------|---------------|
| **File Exists** | File path must resolve | File not found → Check alternate paths |
| **File Readable** | PDF must have text layer | Encrypted/corrupted → Try alternative extraction tools |
| **File Size** | Reasonable size (< 50MB) | Oversized → Extract in chunks |

#### analyzer Input Validation

| Field | Validation Rule | Error Condition | Recovery Action |
|-------|---------------|-----------------|---------------|
| **extracted.md Exists** | Required for context | Missing → Skip to JSON-only analysis |
| **extracted.json Valid** | Required for structure | JSON parse error → Report parse error, skip to next |
| **File Pair Consistency** | Base names must match | Mismatch → Identify correct pair |
| **Reference Integrity** | MD references must map to JSON | Broken → Re-extract if possible |

#### modeler Input Validation

| Field | Validation Rule | Error Condition | Recovery Action |
|-------|---------------|-----------------|---------------|
| **File Count** | Minimum 3 analyses required | Insufficient (1-2) → Require more analyses |
| **Format Consistency** | All files must follow template | Mixed formats → Re-analyze uniformly |
| **Language Uniformity** | Same analysis language | Mixed → Require re-analysis in primary language |

---

## 2. SKILL-Level Output Validation

### 2.1 scenario_parser Output Validation

| Validation Type | Rule | Check Method | Pass Criteria |
|---------------|------|---------|----------------|
| **Completeness** | All required fields present | Field check list | All pass |
| **Traceability** | Every item has reference | Reference scan | Any missing → Add reference marker |
| **Format Integrity** | JSON is parseable | JSON validate | Parse error → Regenerate |
| **Type Consistency** | Content type classification confidence | Low confidence → Review classification |

### 2.2 scenario_analyzer Output Validation

| Validation Type | Rule | Check Method | Pass Criteria |
|---------------|------|---------|----------------|
| **Section Completeness** | All 12 sections (0-12) present | Section scan | All pass |
| **Traceability** | Every key point has source reference | Reference scan | Any missing → Add reference marker |
| **Consistency** | Stakeholder counts match | Count verify | Mismatch → Investigate |
| **Structure Adherence** | Tables follow format spec | Format scan | Violations → Reformat |

### 2.3 scenario_modeler Output Validation

| Validation Type | Rule | Check Method | Pass Criteria |
|---------------|------|---------|----------------|
| **Model Completeness** | All 3 models complete | Model scan | All pass |
| **Traceability** | Source case citations complete | Citation scan | Any missing → Add citation |
| **Credibility** | Critical analysis present | Credibility scan | Missing → Add critical chapter |
| **Statistical Consistency** | Matrices sum to source count | Count verify | Mismatch → Recalculate |

---

## 3. Cross-SKILL Integrity Review

### 3.1 Parser → Analyzer Consistency Check

| Check Type | Purpose | Validation Method |
|-----------|---------|-------------------|---------------|
| **Reference Mapping** | Extracted fields map to Analyzer sections | Table scan | Any unmapped field → Document mapping |
| **Data Integrity** | JSON content matches MD structure | Cross-verify | Corruption detected → Re-extract |
| **Quote Preservation** | All raw quotes preserved | Quote scan | Lost in translation → Restore from source |

### 3.2 Analyzer → Modeler Traceability Chain

| Check Type | Purpose | Validation Method |
|-----------|---------|-------------------|---------------|
| **Citation Coverage** | Source case IDs in conclusions | Citation scan | Uncovered cases → Investigate |
| **Customer Attribution** | Names consistent across models | Attribution scan | Inconsistent → Standardize |
| **Quote Accuracy** | Original text preserved | Quote scan | Paraphrasing detected → Restore original |

---

## 4. Error Handling and Recovery

### 4.1 Error Classification

| Error Category | Examples | Severity | Recovery Strategy |
|---------------|---------|---------|-------------------|
| **Input Validation Error** | Invalid industry, missing file, unreadable PDF | HIGH | Stop processing, report error, suggest fix |
| **Extraction Error** | PDF corrupted, extraction timeout | HIGH | Log as failed, skip, try alternative tools |
| **Analysis Error** | Missing required section, incomplete traceability | MEDIUM | Report missing section, continue with warning |
| **Synthesis Error** | Insufficient analyses for modeler, statistical mismatch | HIGH | Stop synthesis, require minimum 3 analyses |
| **Output Format Error** | Malformed JSON, template violation | MEDIUM | Regenerate output, validate format |

### 4.2 Recovery Mechanisms

| Recovery Type | Trigger | Action | Rollback Support |
|------------|---------|---------|--------------|--------------|
| **Partial Completion** | Phase completed with errors | Continue remaining, don't reprocess completed items |
| **Checkpoint Resume** | Previous session interrupted | Load checkpoint, skip to next pending item |
| **Quality Gate** | Phase 2a complete but quality check failed | Hold for Phase 2b until validated |
| **Fallback to Previous SKILL** | Current SKILL input invalid | Re-process with previous SKILL output |

---

## 5. Implementation Recommendations

### 5.1 Immediate Actions (Priority 1)

1. **Add Input Validation to all SKILLs**
   - Each SKILL should validate inputs before processing
   - Add validation rules to SKILL.md
   - Create validation checklists

2. **Add Output Validation to all SKILLs**
   - Each SKILL should validate outputs before completion
   - Add output checklists to SKILL.md

3. **Create Cross-SKILL Verification Rules**
   - Add mapping tables to scenario_engineering
   - Define traceability chain validation
   - Require consistency checks between Parser → Analyzer → Modeler

### 5.2 Medium-Term Improvements (Priority 2)

1. **Create Central Quality Check Module**
   - Shared validation logic in scenario_engineering/assets/references/
   - SKILLs import validation functions
   - Consistent validation across pipeline

2. **Add Reference Markers to Extraction**
   - Enforce reference requirements in scenario_parser
   - Add reference markers to scenario_analyzer
   - Require citation formats in scenario_modeler

3. **Enhance Progress Reporting**
   - Add quality gate status to phase progress reports
   - Show validation pass/fail in execution summary
   - Track quality metrics (completeness, accuracy, traceability)

### 5.3 Long-Term Architecture Changes (Priority 3)

1. **State Machine Extension**
   - Add quality metrics to state.json structure
   - Track validation results across phases
   - Enable quality-based checkpointing

2. **Validation Report Generation**
   - Generate comprehensive quality report at phase completion
   - Document all validation checks performed
   - List quality issues found
   - Provide recommendations for improvement

---

## 6. Version History

| Version | Date | Changes | Author |
|---------|---------|---------|---------|
| 1.0.0 | 2026-05-06 | Initial quality framework draft | Created comprehensive Input/Output validation and integrity review system |

---

## 7. References

This framework aligns with:
- **scenario_engineering/SKILL.md** - Phase validation and recovery mechanisms
- **scenario_parser/SKILL.md** - Extraction completeness and traceability requirements
- **scenario_analyzer/SKILL.md** - 12-section completeness and output validation
- **scenario_modeler/SKILL.md** - Model synthesis and statistical consistency requirements