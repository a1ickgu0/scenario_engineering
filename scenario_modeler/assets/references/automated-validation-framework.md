# Automated Validation Framework

## Purpose

This framework provides script-based compliance checking for all scenario_modeler outputs. It automates validation of completeness, traceability, and data consistency to ensure high-quality model synthesis results.

---

## Validation Architecture

### Multi-Level Validation

```
Level 1: Syntactic Validation
├── Markdown format validation
├── Table structure validation
├── Section completeness check
└── Template compliance check

Level 2: Semantic Validation
├── Traceability verification
├── Data consistency checks
└── Statistical accuracy validation

Level 3: Cross-Model Validation
├── Inter-model consistency
├── Reference integrity
└── Logical coherence

Level 4: Business Insight Validation
├── Business reasoning chain completeness
├── Decision implication specificity
├── Counter-evidence and confidence quality
└── Recommended action usefulness

Level 5: Delivery Gate
├── Blocking defect review
├── Template deviation log review
├── Strategic advisory model review
└── Final processing report completeness
```

---

## Validation Modules

### Module 1: Industry Model Validator

**Input**: `industry_model.md`

**Validation Checks**:

| Check ID | Check | Rule | Pass Criterion |
|----------|-------|------|----------------|
| IM-01 | Template section completeness | All `industry-model-template.md` `##` headings present | 11/11 sections |
| IM-02 | Industry Classification Table | Has columns for industry, count, percentage | Valid table structure |
| IM-03 | Regional Distribution Matrix | Region × Industry format with totals | Valid matrix |
| IM-04 | Typical Challenges Table | Has frequency, customer, quote columns | All required columns |
| IM-05 | Stakeholder Distribution Matrix | Industry × Category format | Valid matrix |
| IM-06 | Solution Preferences Table | Has solution, frequency, customer columns | All required columns |
| IM-07 | Purchase Factor Synthesis | 3-5 factors per industry | Each industry has factors |
| IM-08 | Customer Name Attribution | Every conclusion has customer name | 100% coverage |
| IM-09 | Original Quote Reference | Every conclusion has quote | 100% coverage |
| IM-10 | Critical Analysis Chapter | Section 9 present and complete | Has credibility rating |
| IM-11 | Total Case Count Verification | Industry total = input case count N | Exact match |
| IM-12 | Statistical Unit Annotation | Each matrix has unit annotation | All matrices annotated |
| IM-13 | Executive Business Insight Summary | Section 0 present before classification tables | Has at least 3 insight rows |
| IM-14 | Industry Decision Playbook | Each major industry has trigger, tension, factor, action | All major industries covered |

**Pass Criteria**: All 14 checks pass (allow 1 warning for optional evidence gaps, not for missing template sections)

### Module 2: Stakeholder Model Validator

**Input**: `stakeholder_model.md`

**Validation Checks**:

| Check ID | Check | Rule | Pass Criterion |
|----------|-------|------|----------------|
| SM-01 | Template section completeness | All `stakeholder-model-template.md` `##` headings present | 7/7 sections |
| SM-02 | Category Definitions Table | Has 6 standard categories | 6 categories |
| SM-03 | Category × Industry Matrix | Complete matrix with totals | Valid structure |
| SM-04 | Category Expectations Table | Has customer, quote columns | All required columns |
| SM-05 | Category Participation Matrix | Phase participation format | Valid matrix |
| SM-06 | Part B: Role Layer | 6 sections present | All present |
| SM-07 | Master Role Catalog | Has category, frequency, industries | All columns present |
| SM-08 | Category → Role Hierarchy | Complete hierarchical tree | Valid structure |
| SM-09 | Role × Industry Matrix | Complete distribution matrix | Valid matrix |
| SM-10 | Role Attributes Table | Has customer, quote, reference | All required columns |
| SM-11 | Part C-E: Final Sections | Insights, Traceability, Critical Analysis | All present |
| SM-12 | Traceability Sub-tables | 4 traceability tables present | All present |
| SM-13 | Credibility Rating | 6 dimensions rated | All dimensions rated |
| SM-14 | Total Stakeholder Count | ≈ N × average stakeholders | ±5% variance allowed |
| SM-15 | Stakeholder Decision System | Part 0 present before category layer | Includes decision owner, evidence owner, blocker, affected user |
| SM-16 | Role-to-Action Specificity | Key insights include recommended engagement action | At least 5 role/action rows |

**Pass Criteria**: All 16 checks pass (allow 1 warning for optional evidence gaps, not for missing template sections)

### Module 3: Purchase Factor Model Validator

**Input**: `purchase_factor_model.md`

**Validation Checks**:

| Check ID | Check | Rule | Pass Criterion |
|----------|-------|------|----------------|
| PFM-01 | Template section completeness | All `purchase-factor-template.md` `##` headings present | 12/12 sections |
| PFM-02 | Business Driver Table | Has frequency, explanation, top 5 | All columns present |
| PFM-03 | Technical Implementation Table | Has linkage to drivers | Linked properly |
| PFM-04 | Quantified Metrics Table | Has metric type, cases | Valid structure |
| PFM-05 | Industry × Driver Matrix | Complete priority matrix | Valid matrix |
| PFM-06 | Solution Chain Table | Factor → Implementation mapping | Valid mapping |
| PFM-07 | Purchase Factor Detailed Analysis | Required detailed section present with evidence and confidence | Section 6 complete |
| PFM-08 | Executive Business Insight Summary | Section 0 present before frequency tables | Has at least 3 conclusions |
| PFM-09 | Traceability Sub-tables | 4 traceability sub-tables present | All present |
| PFM-10 | Stakeholder × Driver Matrix | Category × driver mapping | Valid matrix |
| PFM-11 | Key Insights Section | Contains causal, segmentation, stakeholder, and metric insights | At least 4 insight types |
| PFM-12 | Traceability Summary | 4 traceability tables | All present |
| PFM-13 | Critical Analysis Chapter | Has 6 assessment dimensions | All present |
| PFM-14 | Business Intent Priority | Factors are business intents, not products | Validate terminology |
| PFM-15 | Total Purchase Factor Count | > N (one case multiple factors) | Documented |
| PFM-16 | Business Reasoning Chain | Each top driver has context, pressure, tension, capability, metric, risk, action | Top drivers complete |
| PFM-17 | Counter-Evidence | Major drivers include limitation or alternative interpretation | At least 3 counter-evidence rows |

**Pass Criteria**: All 17 checks pass (allow 1 warning for optional evidence gaps, not for missing template sections)

### Module 4: Cross-Model Consistency Validator

**Inputs**: All three model files

**Validation Checks**:

| Check ID | Check | Rule | Pass Criterion |
|----------|-------|------|----------------|
| CM-01 | Industry Count Consistency | Same industry taxonomy across models | Identical industries |
| CM-02 | Case Count Consistency | Same N across all models | N matches |
| CM-03 | Category Consistency | Same 6 categories across models | Identical categories |
| CM-04 | Purchase Factor Consistency | Same factors across Industry and Purchase models | Identical factors |
| CM-05 | Customer Name Consistency | Same customer names across models | Names match |
| CM-06 | Matrix Totals Consistency | Industry × Role total ≈ stakeholder count | ±5% variance |
| CM-07 | Year Distribution Consistency | Same year distribution where applicable | Consistent |
| CM-08 | Regional Distribution Consistency | Same region distribution where applicable | Consistent |

**Pass Criteria**: All 8 checks pass

### Module 5: Data Consistency Validator

**Input**: All models and matrices

**Validation Checks**:

| Check ID | Check | Rule | Pass Criterion |
|----------|-------|------|----------------|
| DC-01 | Industry × Year Year Total | Σ(year totals) = N | Exact match |
| DC-02 | Industry × Year Industry Total | Σ(industry totals) = N | Exact match |
| DC-03 | Year × Region Year Total | Σ(year totals) = N | Exact match |
| DC-04 | Year × Region Region Total | Σ(region totals) = N | Exact match |
| DC-05 | Industry × Role Role Total | ≈ Stakeholder total M | ±5% variance |
| DC-06 | Statistical Unit Annotation | Every matrix has unit annotation | 100% |
| DC-07 | Total Row/Column Presence | Every matrix has totals | 100% |
| DC-08 | Verification Note Presence | Every matrix has verification note | 100% |
| DC-09 | Multi-Dimension Explanation | Multi-dim matrices explain total > N | 100% |

**Pass Criteria**: All 9 checks pass

### Module 6: Business Insight Quality Validator

**Inputs**: Primary model files

**Validation Checks**:

| Check ID | Check | Rule | Pass Criterion |
|----------|-------|------|----------------|
| BI-01 | Insight-first structure | Primary models begin with business insight summary before inventory tables | All primary models |
| BI-02 | Reasoning chain completeness | Insight rows include context, pressure, tension, factor, capability, metric, risk, action | >=80% of major insights |
| BI-03 | Product-as-factor guard | Product names are not used as purchase factors or business drivers | No critical violations |
| BI-04 | Decision implication | Insights include stakeholder decision or recommended action | >=80% of insights |
| BI-05 | Evidence strength | Insights include HIGH/MEDIUM/LOW confidence and basis | 100% of major insights |
| BI-06 | Counter-evidence | Each primary model includes specific limitations tied to conclusions | >=3 per model |
| BI-07 | Anti-generic language | Generic claims are qualified by segment, trigger, stakeholder, or metric | No unresolved generic claims |

**Pass Criteria**: BI-01 to BI-05 pass, BI-06 has no critical gap, BI-07 has no more than 2 warnings.

### Module 7: Template Compliance Validator

**Inputs**: All generated model files and their bound templates

**Output**: `validation/template_compliance_check.md` generated with `assets/templates/template-compliance-check-template.md`

**Validation Checks**:

| Check ID | Check | Rule | Pass Criterion |
|----------|-------|------|----------------|
| TC-01 | Template binding declared | Every output maps to one required template file | 100% outputs mapped |
| TC-02 | Heading presence | Every `##` heading from the template appears in output | 100% required headings |
| TC-03 | Heading order | Output headings follow template order | No order violations |
| TC-04 | Required table columns | Template table columns are present and not renamed | 100% required columns |
| TC-05 | Placeholder resolution | `[PLACEHOLDER]`, `TBD`, `TODO`, and unsupported `N/A` are replaced or marked as evidence gaps | No unresolved placeholders |
| TC-06 | No section compression | Detailed template sections are not replaced by generic summaries | No compressed required sections |
| TC-07 | Evidence-gap handling | Missing evidence keeps the template section and adds limitation plus validation question | 100% evidence gaps handled |
| TC-08 | Deviation log | Any template deviation lists reason, risk, and corrective action | 100% deviations logged |

**Blocking Defects**:
- Missing required template heading
- Reordered core sections
- Removed or renamed required table columns
- Unresolved placeholders in final output
- Product/factor summary replacing a required detailed template section
- Template deviation without explicit deviation log

**Pass Criteria**: TC-01 to TC-07 pass. TC-08 is required when any deviation exists. Any blocking defect fails delivery.

### Module 8: Gartner-Style Strategic Advisory Validator

**Inputs**: `use_case_fit_model.md`, `critical_capability_model.md`, `buying_committee_model.md`, `competitive_positioning_model.md`

**Validation Checks**:

| Check ID | Check | Rule | Pass Criterion |
|----------|-------|------|----------------|
| GS-01 | Strategic model presence | All four strategic advisory model files exist | 4/4 files |
| GS-02 | Use case boundary | Use Case Fit Model defines market/use-case boundary and exclusions | All major use cases |
| GS-03 | Fit scoring | Use cases include segment fit score and evidence basis | 100% major use cases |
| GS-04 | Critical capability classification | Capabilities are classified as table stakes, differentiator, emerging differentiator, or optional enhancer | 100% major capabilities |
| GS-05 | Capability proof burden | Critical capabilities include MoE/KPI or measurement gap | 100% major capabilities |
| GS-06 | Buying committee influence | Buying Committee Model identifies approve, block, validate, operate, fund, and use roles | All major use cases |
| GS-07 | Stakeholder proof burden | Each key role includes proof required, objection, and engagement action | 100% key roles |
| GS-08 | Competitive alternative | Competitive Positioning Model identifies displaced or compared alternatives | 100% major positioning themes |
| GS-09 | Vendor narrative guard | Vendor narrative is separated from customer evidence and analyst inference | No critical violations |
| GS-10 | Scenario modeling implication | Strategic insights map to scenario actors, states, parameters, or success criteria | >=80% major insights |
| GS-11 | Evidence strength | Strategic conclusions include HIGH/MEDIUM/LOW confidence and evidence basis | 100% major conclusions |
| GS-12 | Counter-evidence | Strategic models include limitations, objections, or measurement gaps | >=3 per strategic model |

**Blocking Defects**:
- Any of the four strategic advisory model files is missing when strategic analysis is requested
- Product names are used as critical capabilities without capability definition
- Competitive positioning claims are not separated from vendor narrative
- Use-case scores lack evidence basis
- Buying committee output lists roles without influence or proof burden

**Pass Criteria**: GS-01 to GS-11 pass. GS-12 must have no critical gap. Any blocking defect fails delivery.

---

## Validation Script Structure

### Main Validation Script (validate_models.sh)

```bash
#!/bin/bash

# Automated Model Validation Script
# Usage: ./validate_models.sh [model_directory] [case_count]

MODEL_DIR="${1:-./outputs/models}"
CASE_COUNT="${2:-0}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Initialize counters
TOTAL_CHECKS=0
PASSED_CHECKS=0
FAILED_CHECKS=0
WARNING_CHECKS=0

# Function to print status
print_status() {
    local status=$1
    local message=$2
    case $status in
        PASS) echo -e "${GREEN}✓${NC} $message"; ((PASSED_CHECKS++)) ;;
        FAIL) echo -e "${RED}✗${NC} $message"; ((FAILED_CHECKS++)) ;;
        WARN) echo -e "${YELLOW}⚠${NC} $message"; ((WARNING_CHECKS++)) ;;
    esac
    ((TOTAL_CHECKS++))
}

# Function to check file exists
check_file() {
    local file=$1
    local name=$2
    if [ -f "$file" ]; then
        print_status PASS "$name file exists"
        return 0
    else
        print_status FAIL "$name file missing: $file"
        return 1
    fi
}

# Function to count sections
count_sections() {
    local file=$1
    local pattern=$2
    local expected=$3
    local name=$4
    local count=$(grep -c "^##" "$file" || echo 0)
    if [ "$count" -ge "$expected" ]; then
        print_status PASS "$name: $count sections (expected ≥$expected)"
        return 0
    else
        print_status FAIL "$name: $count sections (expected ≥$expected)"
        return 1
    fi
}

# Function to check table presence
check_table() {
    local file=$1
    local pattern=$2
    local name=$3
    if grep -q "$pattern" "$file"; then
        print_status PASS "$name table found"
        return 0
    else
        print_status FAIL "$name table missing"
        return 1
    fi
}

# Function to check column presence in table
check_table_columns() {
    local file=$1
    local pattern=$2
    local columns=("${@:3}")
    local name=$4
    local table_content=$(sed -n "/$pattern/,/^$/p" "$file")
    local missing=0
    for col in "${columns[@]}"; do
        if ! echo "$table_content" | grep -q "$col"; then
            echo -e "${RED}✗${NC} Missing column: $col in $name"
            ((missing++))
        fi
    done
    if [ $missing -eq 0 ]; then
        print_status PASS "$name has all required columns"
        return 0
    else
        print_status FAIL "$name missing $missing columns"
        return 1
    fi
}

# Function to check traceability
check_traceability() {
    local file=$1
    local name=$2
    local customer_mentions=$(grep -c "Customer Name\|客户名称" "$file" || echo 0)
    local quote_mentions=$(grep -c "Original Quote\|原文引用" "$file" || echo 0)
    
    if [ "$customer_mentions" -ge 10 ] && [ "$quote_mentions" -ge 10 ]; then
        print_status PASS "$name has adequate traceability ($customer_mentions customers, $quote_mentions quotes)"
        return 0
    else
        print_status WARN "$name limited traceability ($customer_mentions customers, $quote_mentions quotes)"
        return 1
    fi
}

# Function to check critical analysis
check_critical_analysis() {
    local file=$1
    local name=$2
    if grep -q "## 9. Critical Analysis\|## Part E: Critical Analysis\|## 12. Critical Analysis" "$file"; then
        if grep -q "Credibility Rating\|可信度评级" "$file"; then
            print_status PASS "$name has critical analysis with credibility rating"
            return 0
        else
            print_status WARN "$name has critical analysis but missing credibility rating"
            return 1
        fi
    else
        print_status FAIL "$name missing critical analysis chapter"
        return 1
    fi
}

# Function to check matrix totals
check_matrix_totals() {
    local file=$1
    local name=$2
    if grep -q "合计\|Total\|**Total**" "$file"; then
        print_status PASS "$name has total rows/columns"
        return 0
    else
        print_status FAIL "$name missing total rows/columns"
        return 1
    fi
}

# Function to check statistical unit annotation
check_statistical_unit() {
    local file=$1
    local name=$2
    if grep -q "统计口径\|Statistical Scope\|Count\|次数" "$file"; then
        print_status PASS "$name has statistical unit annotation"
        return 0
    else
        print_status WARN "$name missing statistical unit annotation"
        return 1
    fi
}

# Start validation
echo "========================================="
echo "Scenario Modeler Validation Report"
echo "========================================="
echo "Model Directory: $MODEL_DIR"
echo "Case Count: $CASE_COUNT"
echo "========================================="
echo ""

# Validate Industry Model
echo "--- Industry Model Validation ---"
INDUSTRY_FILE="$MODEL_DIR/industry_model.md"
if check_file "$INDUSTRY_FILE" "Industry"; then
    count_sections "$INDUSTRY_FILE" "^## " 11 "Industry Model"
    check_table "$INDUSTRY_FILE" "Industry Classification" "Industry Classification"
    check_table_columns "$INDUSTRY_FILE" "Industry Classification" "Industry" "Count" "Percentage" "Industry Classification"
    check_traceability "$INDUSTRY_FILE" "Industry Model"
    check_critical_analysis "$INDUSTRY_FILE" "Industry Model"
    check_matrix_totals "$INDUSTRY_FILE" "Industry Model"
    check_statistical_unit "$INDUSTRY_FILE" "Industry Model"
fi
echo ""

# Validate Stakeholder Model
echo "--- Stakeholder Model Validation ---"
STAKEHOLDER_FILE="$MODEL_DIR/stakeholder_model.md"
if check_file "$STAKEHOLDER_FILE" "Stakeholder"; then
    count_sections "$STAKEHOLDER_FILE" "^## " 7 "Stakeholder Model"
    check_table "$STAKEHOLDER_FILE" "Category Definitions" "Category Definitions"
    check_table_columns "$STAKEHOLDER_FILE" "Category Definitions" "Category" "Definition" "Frequency" "Category Definitions"
    check_traceability "$STAKEHOLDER_FILE" "Stakeholder Model"
    check_critical_analysis "$STAKEHOLDER_FILE" "Stakeholder Model"
    check_matrix_totals "$STAKEHOLDER_FILE" "Stakeholder Model"
    check_statistical_unit "$STAKEHOLDER_FILE" "Stakeholder Model"
fi
echo ""

# Validate Purchase Factor Model
echo "--- Purchase Factor Model Validation ---"
PURCHASE_FILE="$MODEL_DIR/purchase_factor_model.md"
if check_file "$PURCHASE_FILE" "Purchase Factor"; then
    count_sections "$PURCHASE_FILE" "^## " 12 "Purchase Factor Model"
    check_table "$PURCHASE_FILE" "Business Driver" "Business Driver Layer"
    check_table_columns "$PURCHASE_FILE" "Business Driver Layer" "Business Driver" "Frequency" "Supplementary" "Business Driver Layer"
    check_table "$PURCHASE_FILE" "Executive Business Insight" "Executive Business Insight Summary"
    check_table "$PURCHASE_FILE" "Purchase Factor Detailed Analysis" "Purchase Factor Detailed Analysis"
    check_table "$PURCHASE_FILE" "Traceability Summary" "Traceability Summary"
    check_traceability "$PURCHASE_FILE" "Purchase Factor Model"
    check_critical_analysis "$PURCHASE_FILE" "Purchase Factor Model"
    check_matrix_totals "$PURCHASE_FILE" "Purchase Factor Model"
    check_statistical_unit "$PURCHASE_FILE" "Purchase Factor Model"
fi
echo ""

# Cross-Model Validation
echo "--- Cross-Model Consistency Validation ---"
# Add cross-model checks here
echo "Cross-model checks require advanced parsing - see Python validator"
echo ""

# Summary
echo "========================================="
echo "Validation Summary"
echo "========================================="
echo "Total Checks: $TOTAL_CHECKS"
echo -e "${GREEN}Passed: $PASSED_CHECKS${NC}"
echo -e "${YELLOW}Warnings: $WARNING_CHECKS${NC}"
echo -e "${RED}Failed: $FAILED_CHECKS${NC}"
echo ""

if [ $FAILED_CHECKS -eq 0 ]; then
    echo -e "${GREEN}✓ Validation PASSED${NC}"
    exit 0
elif [ $FAILED_CHECKS -le 3 ]; then
    echo -e "${YELLOW}⚠ Validation PASSED with issues${NC}"
    exit 1
else
    echo -e "${RED}✗ Validation FAILED${NC}"
    exit 2
fi
```

### Python Validator (Advanced Checks)

```python
#!/usr/bin/env python3
"""
Advanced Model Validator
Performs semantic and cross-model validation that requires parsing
"""

import re
import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass, field
from collections import defaultdict

@dataclass
class ValidationResult:
    """Validation result for a single check"""
    check_id: str
    check_name: str
    status: str  # PASS, FAIL, WARN
    message: str
    details: Dict[str, Any] = field(default_factory=dict)

class ModelValidator:
    """Main validator class for scenario_modeler outputs"""
    
    def __init__(self, model_dir: str, case_count: int = 0):
        self.model_dir = Path(model_dir)
        self.case_count = case_count
        self.results: List[ValidationResult] = []
        self.models = {}
        
    def load_models(self):
        """Load all model files"""
        models = {
            'industry': self.model_dir / 'industry_model.md',
            'stakeholder': self.model_dir / 'stakeholder_model.md',
            'purchase': self.model_dir / 'purchase_factor_model.md'
        }
        
        for name, path in models.items():
            if path.exists():
                with open(path, 'r', encoding='utf-8') as f:
                    self.models[name] = f.read()
            else:
                self.results.append(ValidationResult(
                    check_id=f"{name.upper()}-00",
                    check_name=f"{name.capitalize()} model file",
                    status='FAIL',
                    message=f"File not found: {path}"
                ))
    
    def extract_table(self, content: str, start_pattern: str) -> List[List[str]]:
        """Extract table from markdown content"""
        lines = content.split('\n')
        in_table = False
        table = []
        
        for line in lines:
            if start_pattern in line:
                in_table = True
                continue
            if in_table:
                if line.strip() == '' or line.startswith('#'):
                    break
                if '|' in line:
                    row = [cell.strip() for cell in line.split('|')[1:-1]]
                    if row and not all(c.startswith('---') or c == '' for c in row):
                        table.append(row)
        
        return table
    
    def extract_sections(self, content: str) -> Dict[str, str]:
        """Extract sections from markdown"""
        sections = {}
        lines = content.split('\n')
        current_section = None
        current_content = []
        
        for line in lines:
            if line.startswith('##'):
                if current_section:
                    sections[current_section] = '\n'.join(current_content)
                current_section = line.strip()
                current_content = []
            elif current_section:
                current_content.append(line)
        
        if current_section:
            sections[current_section] = '\n'.join(current_content)
        
        return sections
    
    def validate_industry_model(self):
        """Validate industry model"""
        if 'industry' not in self.models:
            return
        
        content = self.models['industry']
        sections = self.extract_sections(content)
        
        # Check section count
        section_count = len([s for s in sections.keys() if s.startswith('##')])
        self.results.append(ValidationResult(
            check_id='IM-01',
            check_name='Section completeness',
            status='PASS' if section_count >= 9 else 'FAIL',
            message=f"Found {section_count} sections (expected ≥9)",
            details={'section_count': section_count}
        ))
        
        # Check for critical analysis
        has_critical_analysis = any('Critical Analysis' in s for s in sections.keys())
        self.results.append(ValidationResult(
            check_id='IM-10',
            check_name='Critical Analysis chapter',
            status='PASS' if has_critical_analysis else 'FAIL',
            message="Critical Analysis chapter present" if has_critical_analysis else "Critical Analysis missing"
        ))
        
        # Check traceability
        customer_count = len(re.findall(r'\|\s*\w+\s*\|', content))
        quote_count = len(re.findall(r'"[^"]*"', content))
        
        self.results.append(ValidationResult(
            check_id='IM-08',
            check_name='Customer name attribution',
            status='PASS' if customer_count > 20 else 'WARN',
            message=f"Found {customer_count} customer references",
            details={'customer_count': customer_count}
        ))
        
        self.results.append(ValidationResult(
            check_id='IM-09',
            check_name='Original quote references',
            status='PASS' if quote_count > 30 else 'WARN',
            message=f"Found {quote_count} quote references",
            details={'quote_count': quote_count}
        ))
    
    def validate_stakeholder_model(self):
        """Validate stakeholder model"""
        if 'stakeholder' not in self.models:
            return
        
        content = self.models['stakeholder']
        sections = self.extract_sections(content)
        
        # Check for Part A, B, C, D, E
        parts = ['Part A', 'Part B', 'Part C', 'Part D', 'Part E']
        missing_parts = [p for p in parts if not any(p in s for s in sections.keys())]
        
        self.results.append(ValidationResult(
            check_id='SM-01',
            check_name='Stakeholder model parts',
            status='PASS' if not missing_parts else 'FAIL',
            message=f"All parts present" if not missing_parts else f"Missing parts: {', '.join(missing_parts)}",
            details={'missing_parts': missing_parts}
        ))
        
        # Check for category definitions
        category_table = self.extract_table(content, 'Category Definitions')
        if category_table:
            category_count = len([row for row in category_table if row])
            self.results.append(ValidationResult(
                check_id='SM-02',
                check_name='Category definitions',
                status='PASS' if category_count >= 6 else 'WARN',
                message=f"Found {category_count} category definitions (expected 6)",
                details={'category_count': category_count}
            ))
    
    def validate_purchase_factor_model(self):
        """Validate purchase factor model"""
        if 'purchase' not in self.models:
            return
        
        content = self.models['purchase']
        sections = self.extract_sections(content)
        
        # Check for template-required sections
        required_sections = [
            'Executive Business Insight Summary',
            'Business Driver Layer Frequency Distribution',
            'Technical Implementation Layer Frequency Distribution',
            'Quantified Metric Patterns',
            'Industry × Business Driver Priority Matrix',
            'Business Driver → Technical Implementation → Solution Chain',
            'Purchase Factor Detailed Analysis Table',
            'Stakeholder × Driver Mapping',
            'Key Insights',
            'Traceability Summary',
            'Critical Analysis',
            'Notes'
        ]
        
        for section_name in required_sections:
            has_section = any(section_name in s for s in sections.keys())
            self.results.append(ValidationResult(
                check_id=f"PFM-TC-{required_sections.index(section_name) + 1:02d}",
                check_name=f'{section_name} section',
                status='PASS' if has_section else 'FAIL',
                message=f"{section_name} present" if has_section else f"{section_name} missing"
            ))
        
        # Check business intent priority (factors are intents, not products)
        business_intent_keywords = ['efficiency', 'experience', 'security', 'compliance', 'cost', 'transformation', 'sustainability']
        product_keywords = ['Wi-Fi', 'AP', 'switch', 'Central', 'ClearPass', 'SD-WAN']
        
        business_driver_table = self.extract_table(content, 'Business Driver Layer')
        if business_driver_table:
            product_mentions = sum(1 for row in business_driver_table for cell in row if any(p in cell for p in product_keywords))
            
            self.results.append(ValidationResult(
                check_id='PFM-14',
                check_name='Business intent priority',
                status='WARN' if product_mentions > 0 else 'PASS',
                message=f"Found {product_mentions} product references in business driver (should be intents)",
                details={'product_mentions': product_mentions}
            ))
    
    def validate_cross_model_consistency(self):
        """Validate consistency across models"""
        if len(self.models) < 2:
            return
        
        # Extract case counts from each model
        case_counts = {}
        for name, content in self.models.items():
            # Look for patterns like "122 cases" or "167 案例数"
            matches = re.findall(r'(\d+)\s*(?:cases?|案例)', content, re.IGNORECASE)
            if matches:
                case_counts[name] = int(matches[0])
        
        if len(case_counts) >= 2:
            unique_counts = set(case_counts.values())
            if len(unique_counts) == 1:
                self.results.append(ValidationResult(
                    check_id='CM-02',
                    check_name='Case count consistency',
                    status='PASS',
                    message=f"All models use case count: {unique_counts.pop()}",
                    details={'case_counts': case_counts}
                ))
            else:
                self.results.append(ValidationResult(
                    check_id='CM-02',
                    check_name='Case count consistency',
                    status='WARN',
                    message=f"Inconsistent case counts: {case_counts}",
                    details={'case_counts': case_counts}
                ))
    
    def validate_data_consistency(self):
        """Validate data consistency within models"""
        for name, content in self.models.items():
            # Check for statistical unit annotations
            has_statistical_unit = any(
                '统计口径' in content or 'Statistical Scope' in content or 'Count' in content
            )
            
            self.results.append(ValidationResult(
                check_id=f'DC-{list(self.models.keys()).index(name) + 1:02d}',
                check_name=f'{name.capitalize()} statistical unit annotation',
                status='PASS' if has_statistical_unit else 'WARN',
                message=f"Statistical unit {'found' if has_statistical_unit else 'missing'}"
            ))
    
    def generate_report(self) -> str:
        """Generate validation report"""
        report = []
        report.append("=" * 50)
        report.append("Scenario Modeler Validation Report")
        report.append("=" * 50)
        report.append(f"Model Directory: {self.model_dir}")
        report.append(f"Case Count: {self.case_count}")
        report.append("=" * 50)
        report.append("")
        
        # Group by status
        passed = [r for r in self.results if r.status == 'PASS']
        failed = [r for r in self.results if r.status == 'FAIL']
        warned = [r for r in self.results if r.status == 'WARN']
        
        report.append(f"Total Checks: {len(self.results)}")
        report.append(f"✓ Passed: {len(passed)}")
        report.append(f"⚠ Warnings: {len(warned)}")
        report.append(f"✗ Failed: {len(failed)}")
        report.append("")
        
        # Detailed results
        report.append("=" * 50)
        report.append("Detailed Results")
        report.append("=" * 50)
        
        for result in self.results:
            symbol = "✓" if result.status == "PASS" else ("✗" if result.status == "FAIL" else "⚠")
            report.append(f"{symbol} [{result.check_id}] {result.check_name}: {result.message}")
        
        report.append("")
        
        # Summary
        if not failed:
            report.append("=" * 50)
            report.append("✓ Validation PASSED")
            report.append("=" * 50)
        elif len(failed) <= 3:
            report.append("=" * 50)
            report.append("⚠ Validation PASSED with issues")
            report.append("=" * 50)
        else:
            report.append("=" * 50)
            report.append("✗ Validation FAILED")
            report.append("=" * 50)
        
        return "\n".join(report)
    
    def run(self):
        """Run all validations"""
        self.load_models()
        self.validate_industry_model()
        self.validate_stakeholder_model()
        self.validate_purchase_factor_model()
        self.validate_cross_model_consistency()
        self.validate_data_consistency()
        
        report = self.generate_report()
        print(report)
        
        # Exit code based on results
        failed = sum(1 for r in self.results if r.status == 'FAIL')
        return 0 if failed == 0 else (1 if failed <= 3 else 2)

def main():
    if len(sys.argv) < 2:
        print("Usage: python validator.py <model_dir> [case_count]")
        sys.exit(1)
    
    model_dir = sys.argv[1]
    case_count = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    
    validator = ModelValidator(model_dir, case_count)
    exit_code = validator.run()
    sys.exit(exit_code)

if __name__ == '__main__':
    main()
```

---

## Usage

### Shell Script (Basic Validation)

```bash
# Validate models in default directory
./validate_models.sh

# Validate with specified directory and case count
./validate_models.sh ./outputs/models 122

# Check exit code
if [ $? -eq 0 ]; then
    echo "Validation passed"
elif [ $? -eq 1 ]; then
    echo "Validation passed with warnings"
else
    echo "Validation failed"
fi
```

### Python Script (Advanced Validation)

```bash
# Validate models with advanced checks
python validator.py ./outputs/models 122

# Save report to file
python validator.py ./outputs/models 122 > validation_report.md
```

---

## Validation Output

### Pass Criteria

- **0 failures**: Full pass
- **1-3 failures**: Pass with issues (requires review)
- **4+ failures**: Fail (requires correction)

### Report Format

Validation report includes:
1. Summary statistics (total, passed, warned, failed)
2. Detailed results per check
3. Specific issues with locations
4. Recommendations for resolution
5. Overall pass/fail determination

---

## Integration with Workflow

### Pre-Synthesis Validation

1. Run input validation on scenario_analyzer outputs
2. Fix identified issues
3. Proceed to model synthesis

### Post-Synthesis Validation

1. Run automated validation on model outputs
2. Review failed/warned checks
3. Correct issues if needed
4. Re-validate until pass
5. Generate final validation report

### Continuous Integration

Add validation to CI/CD pipeline:
```yaml
# Example CI/CD step
- name: Validate Models
  run: |
    python validator.py ./outputs/models ${{ case_count }}
    exit_code=$?
    if [ $exit_code -ne 0 ]; then
      echo "Model validation failed"
      exit 1
    fi
```

---

## Extensibility

### Adding New Checks

1. Define check ID following pattern: `{MODEL}-{NUMBER}`
2. Add validation logic to appropriate validator
3. Update pass criteria
4. Document in this framework

### Custom Validation Rules

Create custom validators by extending the `ModelValidator` class:

```python
class CustomValidator(ModelValidator):
    def validate_custom_rule(self):
        """Custom validation logic"""
        if 'industry' in self.models:
            content = self.models['industry']
            # Your custom validation here
            pass
```

---

## Maintenance

### Version Updates

- Update validation checks when SKILL version changes
- Add new required sections to validators
- Update pass criteria as needed
- Document version-specific requirements

### Threshold Adjustments

- Adjust warning/fail thresholds based on experience
- Update case count expectations
- Modify variance allowances
- Document rationale for changes
