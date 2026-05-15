# Cross-Model Consistency Framework

## Purpose

This framework defines consistency checks between Industry, Stakeholder, and Purchase Factor models to ensure data alignment and logical coherence across all scenario_modeler outputs.

---

## Consistency Dimensions

### Dimension 1: Case Count Consistency

**Definition**: All models must reference the same total number of input cases.

**Check**: `N_industry = N_stakeholder = N_purchase = N_input`

**Validation Rule**:
```
For each model, extract total case count from:
- Industry Model: Sum of industry totals
- Stakeholder Model: Explicit case count or inferred from coverage
- Purchase Factor Model: Explicit case count

All must equal the input case count N.
```

**Tolerance**: 0% (exact match required)

**Failure Impact**: CRITICAL - Reject all models and re-generate

### Dimension 2: Industry Taxonomy Consistency

**Definition**: All models must use identical industry classifications.

**Check**: `Industries_industry = Industries_stakeholder = Industries_purchase`

**Validation Rule**:
```
1. Extract industry lists from each model
2. Compare sets for exact match
3. Check for:
   - Missing industries in any model
   - Extra industries in any model
   - Naming differences (case, spacing)
```

**Tolerance**: 0% (exact match required)

**Failure Impact**: HIGH - Must reconcile taxonomy

### Dimension 3: Stakeholder Category Consistency

**Definition**: All models must use identical stakeholder categories.

**Check**: `Categories_industry = Categories_stakeholder = Categories_purchase`

**Validation Rule**:
```
1. Extract category lists from each model
2. Verify 6 standard categories present:
   - Decision Maker
   - IT Lead
   - Operator
   - User
   - Regulator
   - Partner
3. Check for category naming consistency
```

**Tolerance**: 0% (exact match required)

**Failure Impact**: HIGH - Must reconcile categories

### Dimension 4: Purchase Factor Definition Consistency

**Definition**: Purchase factors must be defined identically across models.

**Check**: `Factors_industry = Factors_purchase`

**Validation Rule**:
```
1. Extract purchase factor lists from Industry and Purchase models
2. Compare:
   - Factor names (exact match)
   - Factor definitions (semantic equivalence)
   - Factor groupings (if hierarchical)
3. Check for:
   - Divergent naming
   - Missing factors
   - Extra factors
```

**Tolerance**: 0% for core factors, allow optional variations

**Failure Impact**: MEDIUM - Document variations, flag for review

### Dimension 5: Customer Name Consistency

**Definition**: Customer names must be spelled identically across all models.

**Check**: `Customers_industry = Customers_stakeholder = Customers_purchase`

**Validation Rule**:
```
1. Extract all customer name references from each model
2. Create sets of unique names
3. Compare for:
   - Exact matches
   - Case differences (e.g., "Aberdeen" vs "aberdeen")
   - Spacing differences
   - Abbreviations (e.g., "ARC" vs "Austrian Red Cross")
```

**Tolerance**: Allow case differences, but require consistent usage

**Failure Impact**: MEDIUM - Document variations, standardize

### Dimension 6: Matrix Total Consistency

**Definition**: Matrix totals must be mathematically consistent within and across models.

**Checks**:

| Matrix | Consistency Check | Formula |
|--------|-------------------|---------|
| Industry × Year | Year total = N | Σ(year_totals) = N |
| Industry × Year | Industry total = N | Σ(industry_totals) = N |
| Year × Region | Year total = N | Σ(year_totals) = N |
| Year × Region | Region total = N | Σ(region_totals) = N |
| Industry × Role | Role total ≈ M | Σ(role_totals) ≈ M (±5%) |
| Industry × Role | Industry total ≈ M | Σ(industry_totals) ≈ M (±5%) |

**Tolerance**: 0% for case count matrices, ±5% for stakeholder matrices

**Failure Impact**: HIGH - Must recalculate and correct

### Dimension 7: Year Distribution Consistency

**Definition**: Year distributions must be consistent where they appear across models.

**Check**: Year distribution in Industry Model ≈ Year distribution in Purchase Factor Model

**Validation Rule**:
```
1. Extract year distributions from both models
2. Compare distributions:
   - Total cases per year
   - Percentage per year
3. Allow for slight variations due to:
   - Different aggregation methods
   - Missing data handling
   - Rounding differences
```

**Tolerance**: ±5% per year

**Failure Impact**: MEDIUM - Document variations, investigate cause

### Dimension 8: Regional Distribution Consistency

**Definition**: Regional distributions must be consistent across models.

**Check**: Regional distribution in Industry Model ≈ Regional distribution in Year × Region matrix

**Validation Rule**:
```
1. Extract regional distributions from relevant matrices
2. Compare total cases per region
3. Check for:
   - Missing regions in any matrix
   - Total count mismatches
   - Percentage discrepancies
```

**Tolerance**: ±5% per region

**Failure Impact**: MEDIUM - Document variations, investigate cause

### Dimension 9: Cross-Reference Integrity

**Definition**: Cross-references between models must be valid and consistent.

**Checks**:

| Reference Type | Source | Target | Validation |
|----------------|--------|--------|------------|
| Industry → Purchase Factors | Industry Model | Purchase Factor Model | All industries reference valid factors |
| Category → Roles | Stakeholder Model | Stakeholder Model | All categories map to valid roles |
| Industry → Roles | Industry Model | Stakeholder Model | Role distribution matches industry patterns |
| Purchase Factor → Industry | Purchase Factor Model | Industry Model | Factor priorities align with industry needs |

**Tolerance**: 100% (all cross-references must be valid)

**Failure Impact**: HIGH - Must correct invalid references

### Dimension 10: Logical Coherence

**Definition**: Relationships between data elements must be logically consistent.

**Checks**:

| Logical Relationship | Validation Rule |
|---------------------|-----------------|
| Industry × Purchase Factor | High-priority factors in an industry should appear in that industry's section |
| Category × Influence | Categories with high influence should have more traceability citations |
| Purchase Factor × Quantification | Frequently mentioned factors should have more quantified cases |
| Industry × Stakeholder | Industries with more cases should have more diverse stakeholder roles |

**Tolerance**: Qualitative assessment, flag significant anomalies

**Failure Impact**: MEDIUM - Document anomalies, investigate

---

## Consistency Check Implementation

### Python Consistency Checker

```python
#!/usr/bin/env python3
"""
Cross-Model Consistency Checker
Validates consistency across Industry, Stakeholder, and Purchase Factor models
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
from dataclasses import dataclass, field
from collections import Counter, defaultdict

@dataclass
class ConsistencyCheck:
    """Result of a single consistency check"""
    check_id: str
    check_name: str
    dimension: str
    status: str  # PASS, FAIL, WARN
    message: str
    details: Dict[str, Any] = field(default_factory=dict)
    severity: str = "MEDIUM"  # CRITICAL, HIGH, MEDIUM, LOW

class CrossModelConsistencyChecker:
    """Performs consistency checks across all models"""
    
    def __init__(self, model_dir: str, input_case_count: int = 0):
        self.model_dir = Path(model_dir)
        self.input_case_count = input_case_count
        self.models = {}
        self.checks: List[ConsistencyCheck] = []
        
    def load_models(self) -> bool:
        """Load all model files"""
        model_files = {
            'industry': 'industry_model.md',
            'stakeholder': 'stakeholder_model.md',
            'purchase': 'purchase_factor_model.md'
        }
        
        for name, filename in model_files.items():
            path = self.model_dir / filename
            if path.exists():
                with open(path, 'r', encoding='utf-8') as f:
                    self.models[name] = f.read()
            else:
                self.checks.append(ConsistencyCheck(
                    check_id=f"CM-LOAD-{name.upper()}",
                    check_name=f"{name.capitalize()} model file",
                    dimension="File Loading",
                    status="FAIL",
                    message=f"Model file not found: {filename}",
                    severity="CRITICAL"
                ))
                return False
        return True
    
    def extract_case_count(self, content: str, model_name: str) -> int:
        """Extract total case count from model content"""
        # Look for patterns like "122 cases", "167 案例数", etc.
        patterns = [
            r'(\d+)\s*(?:cases?|案例)',
            r'(\d+)\s*(?:customers?|客户)',
            r'total[^:]*:\s*(\d+)',
            r'合计[^\d]*(\d+)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                return int(matches[0])
        
        # Try to sum from tables
        table_totals = re.findall(r'\|\s*\*\*Total\*\*\s*\|\s*(\d+)', content, re.IGNORECASE)
        if table_totals:
            return int(table_totals[0])
        
        return 0
    
    def extract_industries(self, content: str) -> Set[str]:
        """Extract industry names from content"""
        # Look for industry classification table
        industry_pattern = r'\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|'
        
        # Context: Industry Classification section
        industries = set()
        in_industry_section = False
        
        for line in content.split('\n'):
            if 'Industry Classification' in line:
                in_industry_section = True
                continue
            if in_industry_section and line.strip() == '':
                break
            if in_industry_section and '|' in line:
                match = re.search(industry_pattern, line)
                if match:
                    industry = match.group(1).strip()
                    if industry and not industry.lower() in ['industry', 'count', 'percentage', 'total']:
                        industries.add(industry)
        
        return industries
    
    def extract_categories(self, content: str) -> Set[str]:
        """Extract stakeholder categories from content"""
        # Standard categories
        standard_categories = {
            'Decision Maker', 'IT Lead', 'Operator', 'User', 'Regulator', 'Partner'
        }
        
        # Check for standard categories in content
        found_categories = set()
        for category in standard_categories:
            if category.lower() in content.lower():
                found_categories.add(category)
        
        return found_categories
    
    def extract_purchase_factors(self, content: str) -> Set[str]:
        """Extract purchase factor names from content"""
        # Look for purchase factor / business driver tables
        factors = set()
        
        # Pattern: Business Driver / Purchase Factor table rows
        factor_pattern = r'\|\s*\*\*([^|]+?)\*\*\s*\|'
        
        for line in content.split('\n'):
            if 'Business Driver' in line or 'Purchase Factor' in line:
                continue
            if '---' in line or line.strip() == '':
                continue
            if '|' in line:
                matches = re.findall(factor_pattern, line)
                for match in matches:
                    factor = match.strip()
                    if factor and len(factor) > 3:  # Exclude short headers
                        factors.add(factor)
        
        return factors
    
    def extract_customer_names(self, content: str) -> Set[str]:
        """Extract customer names from content"""
        # Look for patterns like "Aberdeen City Council", "Southern Sun", etc.
        # This is heuristic - may need refinement based on actual content
        
        customers = set()
        
        # Pattern: Capitalized names with multiple words
        name_pattern = r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\b'
        
        # Filter out common non-customer words
        non_customer_words = {
            'Section', 'Chapter', 'Part', 'Table', 'Matrix', 'Model',
            'Customer', 'Name', 'Quote', 'Original', 'Industry',
            'Purchase', 'Factor', 'Stakeholder', 'Role', 'Category',
            'Total', 'Sum', 'Count', 'Percentage', 'Frequency'
        }
        
        matches = re.findall(name_pattern, content)
        for match in matches:
            if match not in non_customer_words:
                customers.add(match)
        
        return customers
    
    def check_case_count_consistency(self):
        """Check CM-02: Case count consistency"""
        case_counts = {}
        for name, content in self.models.items():
            count = self.extract_case_count(content, name)
            case_counts[name] = count
        
        # Compare all counts
        unique_counts = set(case_counts.values())
        
        if len(unique_counts) == 1:
            count = unique_counts.pop()
            self.checks.append(ConsistencyCheck(
                check_id="CM-02",
                check_name="Case count consistency",
                dimension="Case Count",
                status="PASS",
                message=f"All models use case count: {count}",
                details={'case_counts': case_counts},
                severity="CRITICAL"
            ))
        else:
            self.checks.append(ConsistencyCheck(
                check_id="CM-02",
                check_name="Case count consistency",
                dimension="Case Count",
                status="FAIL",
                message=f"Inconsistent case counts: {case_counts}",
                details={'case_counts': case_counts},
                severity="CRITICAL"
            ))
    
    def check_industry_taxonomy_consistency(self):
        """Check CM-01: Industry taxonomy consistency"""
        industry_sets = {}
        for name, content in self.models.items():
            industries = self.extract_industries(content)
            industry_sets[name] = industries
        
        # Compare industry sets
        all_industries = set().union(*industry_sets.values())
        missing = {}
        extra = {}
        
        for name, industries in industry_sets.items():
            missing[name] = all_industries - industries
            extra[name] = industries - all_industries
        
        if all(not missing[name] and not extra[name] for name in industry_sets):
            self.checks.append(ConsistencyCheck(
                check_id="CM-01",
                check_name="Industry taxonomy consistency",
                dimension="Industry Taxonomy",
                status="PASS",
                message=f"All models use identical industry taxonomy ({len(all_industries)} industries)",
                details={'industries': sorted(all_industries)},
                severity="HIGH"
            ))
        else:
            self.checks.append(ConsistencyCheck(
                check_id="CM-01",
                check_name="Industry taxonomy consistency",
                dimension="Industry Taxonomy",
                status="FAIL",
                message="Industry taxonomy differs across models",
                details={'missing': missing, 'extra': extra, 'all_industries': sorted(all_industries)},
                severity="HIGH"
            ))
    
    def check_category_consistency(self):
        """Check CM-03: Stakeholder category consistency"""
        category_sets = {}
        for name, content in self.models.items():
            categories = self.extract_categories(content)
            category_sets[name] = categories
        
        # Check for 6 standard categories
        standard_categories = {
            'Decision Maker', 'IT Lead', 'Operator', 'User', 'Regulator', 'Partner'
        }
        
        all_found = set().union(*category_sets.values())
        missing_categories = standard_categories - all_found
        
        if not missing_categories:
            self.checks.append(ConsistencyCheck(
                check_id="CM-03",
                check_name="Stakeholder category consistency",
                dimension="Category Consistency",
                status="PASS",
                message="All 6 standard categories present across models",
                details={'categories': sorted(all_found)},
                severity="HIGH"
            ))
        else:
            self.checks.append(ConsistencyCheck(
                check_id="CM-03",
                check_name="Stakeholder category consistency",
                dimension="Category Consistency",
                status="WARN",
                message=f"Missing standard categories: {missing_categories}",
                details={'found': sorted(all_found), 'missing': sorted(missing_categories)},
                severity="HIGH"
            ))
    
    def check_purchase_factor_consistency(self):
        """Check CM-04: Purchase factor definition consistency"""
        factor_sets = {}
        for name in ['industry', 'purchase']:
            if name in self.models:
                factors = self.extract_purchase_factors(self.models[name])
                factor_sets[name] = factors
        
        if len(factor_sets) < 2:
            # Skip if insufficient models
            return
        
        # Compare factor sets
        all_factors = set().union(*factor_sets.values())
        missing = {}
        extra = {}
        
        for name, factors in factor_sets.items():
            missing[name] = all_factors - factors
            extra[name] = factors - all_factors
        
        if all(not missing[name] and not extra[name] for name in factor_sets):
            self.checks.append(ConsistencyCheck(
                check_id="CM-04",
                check_name="Purchase factor definition consistency",
                dimension="Purchase Factor",
                status="PASS",
                message=f"Purchase factors consistent ({len(all_factors)} factors)",
                details={'factors': sorted(list(all_factors)[:10])},  # Show first 10
                severity="MEDIUM"
            ))
        else:
            self.checks.append(ConsistencyCheck(
                check_id="CM-04",
                check_name="Purchase factor definition consistency",
                dimension="Purchase Factor",
                status="WARN",
                message="Purchase factor definitions differ across models",
                details={'missing_count': {k: len(v) for k, v in missing.items()},
                        'extra_count': {k: len(v) for k, v in extra.items()}},
                severity="MEDIUM"
            ))
    
    def check_customer_name_consistency(self):
        """Check CM-05: Customer name consistency"""
        customer_sets = {}
        for name, content in self.models.items():
            customers = self.extract_customer_names(content)
            customer_sets[name] = customers
        
        # Compare customer sets
        all_customers = set().union(*customer_sets.values())
        
        # Check for case variations
        case_variations = defaultdict(set)
        for customer in all_customers:
            lower = customer.lower()
            case_variations[lower].add(customer)
        
        variations = {k: v for k, v in case_variations.items() if len(v) > 1}
        
        if not variations:
            self.checks.append(ConsistencyCheck(
                check_id="CM-05",
                check_name="Customer name consistency",
                dimension="Customer Names",
                status="PASS",
                message=f"Customer names consistent ({len(all_customers)} unique)",
                details={'customer_count': len(all_customers)},
                severity="MEDIUM"
            ))
        else:
            self.checks.append(ConsistencyCheck(
                check_id="CM-05",
                check_name="Customer name consistency",
                dimension="Customer Names",
                status="WARN",
                message=f"Found {len(variations)} customer name case variations",
                details={'variations': {k: list(v) for k, v in list(variations.items())[:5]}},
                severity="MEDIUM"
            ))
    
    def check_matrix_total_consistency(self):
        """Check DC-01 to DC-05: Matrix total consistency"""
        # Extract and validate matrix totals
        for name, content in self.models.items():
            # Look for matrices with totals
            total_matches = re.findall(r'\|\s*\*\*Total\*\*\s*\|\s*(\d+)', content, re.IGNORECASE)
            
            if total_matches:
                # Check if totals are consistent
                totals = [int(t) for t in total_matches]
                unique_totals = set(totals)
                
                if len(unique_totals) == 1:
                    self.checks.append(ConsistencyCheck(
                        check_id=f"DC-{name.upper()}-TOTAL",
                        check_name=f"{name.capitalize()} model matrix totals",
                        dimension="Matrix Totals",
                        status="PASS",
                        message=f"Matrix totals consistent: {unique_totals.pop()}",
                        details={'totals': totals},
                        severity="HIGH"
                    ))
                else:
                    self.checks.append(ConsistencyCheck(
                        check_id=f"DC-{name.upper()}-TOTAL",
                        check_name=f"{name.capitalize()} model matrix totals",
                        dimension="Matrix Totals",
                        status="WARN",
                        message=f"Matrix totals vary: {min(totals)}-{max(totals)}",
                        details={'totals': totals},
                        severity="HIGH"
                    ))
    
    def run_all_checks(self):
        """Run all consistency checks"""
        if not self.load_models():
            return
        
        self.check_case_count_consistency()
        self.check_industry_taxonomy_consistency()
        self.check_category_consistency()
        self.check_purchase_factor_consistency()
        self.check_customer_name_consistency()
        self.check_matrix_total_consistency()
    
    def generate_report(self) -> str:
        """Generate consistency check report"""
        report = []
        report.append("=" * 60)
        report.append("Cross-Model Consistency Check Report")
        report.append("=" * 60)
        report.append(f"Model Directory: {self.model_dir}")
        report.append(f"Input Case Count: {self.input_case_count}")
        report.append("=" * 60)
        report.append("")
        
        # Summary by dimension
        by_dimension = defaultdict(list)
        for check in self.checks:
            by_dimension[check.dimension].append(check)
        
        for dimension, checks in sorted(by_dimension.items()):
            report.append(f"## {dimension}")
            report.append("")
            
            for check in checks:
                symbol = "✓" if check.status == "PASS" else ("✗" if check.status == "FAIL" else "⚠")
                report.append(f"{symbol} [{check.check_id}] {check.check_name}: {check.message}")
                
                if check.details:
                    for key, value in check.details.items():
                        if isinstance(value, (list, set)):
                            report.append(f"  - {key}: {len(value)} items")
                        else:
                            report.append(f"  - {key}: {value}")
                
                report.append("")
        
        # Overall summary
        report.append("=" * 60)
        report.append("Summary")
        report.append("=" * 60)
        
        passed = sum(1 for c in self.checks if c.status == "PASS")
        failed = sum(1 for c in self.checks if c.status == "FAIL")
        warned = sum(1 for c in self.checks if c.status == "WARN")
        
        report.append(f"Total Checks: {len(self.checks)}")
        report.append(f"✓ Passed: {passed}")
        report.append(f"✗ Failed: {failed}")
        report.append(f"⚠ Warnings: {warned}")
        report.append("")
        
        # Severity breakdown
        by_severity = defaultdict(int)
        for check in self.checks:
            by_severity[check.severity] += 1
        
        report.append("By Severity:")
        for severity in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
            count = by_severity.get(severity, 0)
            status = "✓" if (severity == "CRITICAL" and count == 0) else ("✗" if count > 0 else "")
            report.append(f"  {status} {severity}: {count}")
        
        report.append("")
        
        # Final assessment
        critical_failed = sum(1 for c in self.checks if c.status == "FAIL" and c.severity == "CRITICAL")
        high_failed = sum(1 for c in self.checks if c.status == "FAIL" and c.severity == "HIGH")
        
        if critical_failed > 0:
            report.append("=" * 60)
            report.append("✗ CONSISTENCY CHECK FAILED (Critical issues)")
            report.append("=" * 60)
        elif high_failed > 0:
            report.append("=" * 60)
            report.append("⚠ CONSISTENCY CHECK FAILED (High severity issues)")
            report.append("=" * 60)
        elif failed > 0:
            report.append("=" * 60)
            report.append("⚠ CONSISTENCY CHECK PASSED WITH ISSUES")
            report.append("=" * 60)
        else:
            report.append("=" * 60)
            report.append("✓ CONSISTENCY CHECK PASSED")
            report.append("=" * 60)
        
        return "\n".join(report)

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python cross_model_consistency.py <model_dir> [input_case_count]")
        sys.exit(1)
    
    model_dir = sys.argv[1]
    input_case_count = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    
    checker = CrossModelConsistencyChecker(model_dir, input_case_count)
    checker.run_all_checks()
    
    report = checker.generate_report()
    print(report)
    
    # Exit code based on critical failures
    critical_failed = sum(1 for c in checker.checks if c.status == "FAIL" and c.severity == "CRITICAL")
    sys.exit(1 if critical_failed > 0 else 0)

if __name__ == '__main__':
    main()
```

---

## Usage

### Running Consistency Checks

```bash
# Basic usage
python cross_model_consistency.py ./outputs/models

# With input case count for validation
python cross_model_consistency.py ./outputs/models 122

# Save report to file
python cross_model_consistency.py ./outputs/models 122 > consistency_report.md
```

### Integration with Validation Pipeline

```bash
# Complete validation pipeline
echo "=== Running Model Validation ==="
./validate_models.sh ./outputs/models 122

echo ""
echo "=== Running Cross-Model Consistency ==="
python cross_model_consistency.py ./outputs/models 122

echo ""
echo "=== Validation Complete ==="
```

---

## Consistency Report Example

```
============================================================
Cross-Model Consistency Check Report
============================================================
Model Directory: ./outputs/models
Input Case Count: 122
============================================================

## Case Count
✓ [CM-02] Case count consistency: All models use case count: 122
  - case_counts: {'industry': 122, 'stakeholder': 122, 'purchase': 122}

## Industry Taxonomy
✓ [CM-01] Industry taxonomy consistency: All models use identical industry taxonomy (9 industries)
  - industries: ['Education', 'Government', 'Healthcare', 'Hospitality', 'Logistics', 'Manufacturing', 'Retail', 'Services', 'Sports/Entertainment']

## Category Consistency
✓ [CM-03] Stakeholder category consistency: All 6 standard categories present across models
  - categories: ['Decision Maker', 'IT Lead', 'Operator', 'Partner', 'Regulator', 'User']

## Purchase Factor
⚠ [CM-04] Purchase factor definition consistency: Purchase factor definitions differ across models
  - extra_count: {'industry': 2, 'purchase': 3}
  - missing_count: {'industry': 3, 'purchase': 2}

## Customer Names
⚠ [CM-05] Customer name consistency: Found 5 customer name case variations
  - variations: {'aberdeen city council': {'Aberdeen City Council', 'aberdeen city council'}, ...}

## Matrix Totals
✓ [DC-industry-TOTAL] Industry model matrix totals: Matrix totals consistent: 122
✓ [DC-stakeholder-TOTAL] Stakeholder model matrix totals: Matrix totals consistent: 1074
✓ [DC-purchase-TOTAL] Purchase model matrix totals: Matrix totals consistent: 695

============================================================
Summary
============================================================
Total Checks: 6
✓ Passed: 4
✗ Failed: 0
⚠ Warnings: 2

By Severity:
  ✓ CRITICAL: 0
  ✓ HIGH: 0
  ⚠ MEDIUM: 2
  ✓ LOW: 0

============================================================
✓ CONSISTENCY CHECK PASSED WITH ISSUES
============================================================
```

---

## Resolution Guidelines

### Resolving Inconsistencies

| Issue Type | Resolution Method | Priority |
|------------|-------------------|----------|
| Case count mismatch | Re-generate affected model(s) | CRITICAL |
| Industry taxonomy mismatch | Standardize taxonomy across all models | HIGH |
| Category missing | Add missing category to affected model(s) | HIGH |
| Purchase factor divergence | Review and reconcile factor definitions | MEDIUM |
| Customer name case variations | Standardize naming convention | MEDIUM |
| Matrix total mismatch | Recalculate matrix, check formulas | HIGH |

### Prevention Strategies

1. **Shared Taxonomy**: Use common taxonomy file for industries and categories
2. **Standard Templates**: Use consistent output templates across models
3. **Real-time Validation**: Validate during model generation, not just after
4. **Automated Checks**: Run consistency checks as part of CI/CD pipeline
5. **Version Control**: Track model versions together, not independently

---

## Maintenance

### Regular Updates

- Add new consistency checks as needed
- Update extraction patterns based on actual content
- Adjust tolerance thresholds based on experience
- Improve pattern matching accuracy

### Framework Evolution

- Extend to support additional models
- Add semantic similarity checks for definitions
- Implement machine learning for better extraction
- Create visual consistency reports