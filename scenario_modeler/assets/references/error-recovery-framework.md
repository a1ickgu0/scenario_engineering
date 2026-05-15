# Error Recovery Framework

## Purpose

This framework provides systematic handling of edge cases, missing data, and processing failures in scenario_modeler. It defines clear resolution paths, fallback strategies, and recovery procedures to ensure robust operation.

---

## Error Classification

### Error Severity Levels

| Level | Description | Impact | Action Required | Recovery Time |
|-------|-------------|--------|-----------------|---------------|
| **CRITICAL** | Processing cannot continue | Blocks entire workflow | Immediate intervention | < 1 hour |
| **HIGH** | Major component failure | Partial workflow blocked | Same-day resolution | < 4 hours |
| **MEDIUM** | Data quality issue | Degraded output quality | Review and document | < 24 hours |
| **LOW** | Minor inconsistency | Minimal impact | Track for future | N/A |

### Error Categories

| Category | Sub-Categories | Examples |
|----------|----------------|----------|
| **Input Errors** | Missing files, invalid format, corrupt data | -analysis.md missing, markdown parse errors |
| **Data Quality Errors** | Missing fields, inconsistent data, outliers | Empty required fields, negative year, invalid country |
| **Processing Errors** | Memory limits, timeout, agent failures | OOM, script timeout, agent crashes |
| **Validation Errors** | Check failures, compliance issues | Traceability missing, matrix totals mismatch |
| **Output Errors** | Format errors, incomplete sections | Malformed tables, missing chapters |
| **Consistency Errors** | Cross-model inconsistencies | Case count mismatch, industry taxonomy divergence |

---

## Error Recovery Strategies

### Strategy 1: Retry with Backoff

**Applicable**: Transient failures, network issues, agent timeouts

```
Retry Policy:
├── Initial attempt (no delay)
├── Retry 1: 30 seconds wait
├── Retry 2: 1 minute wait
├── Retry 3: 2 minutes wait
└── Failure: Escalate to recovery handler
```

**Implementation**:
```python
def retry_with_backoff(func, max_retries=3):
    """Execute function with exponential backoff"""
    for attempt in range(max_retries):
        try:
            return func()
        except (TimeoutError, NetworkError) as e:
            if attempt < max_retries - 1:
                wait_time = 30 * (2 ** attempt)
                log_warning(f"Attempt {attempt + 1} failed, retrying in {wait_time}s")
                time.sleep(wait_time)
            else:
                raise
```

### Strategy 2: Graceful Degradation

**Applicable**: Missing optional data, partial failures

**Degradation Levels**:

| Level | Impact | Compensation |
|-------|--------|--------------|
| Full | All data available | Standard processing |
| High | Some data missing | Use imputation, flag affected areas |
| Medium | Key data missing | Skip affected analysis, annotate |
| Low | Major data missing | Partial processing, mark as incomplete |

**Example**:
```python
def process_with_degradation(data):
    """Process data with graceful degradation"""
    if 'quantified_metrics' not in data:
        log_warning("Quantified metrics missing, proceeding with degraded analysis")
        # Proceed without quantified analysis
        # Add credibility downgrade note
    if 'customer_quotes' in data and len(data['customer_quotes']) < 3:
        log_warning("Insufficient customer quotes, traceability reduced")
        # Continue but flag traceability issue
    return process_data(data)
```

### Strategy 3: Fallback Processing

**Applicable**: Processing failures, model generation issues

**Fallback Options**:

| Primary Method | Fallback Method | When to Use |
|----------------|-----------------|-------------|
| Parallel agents | Serial processing | Agent failures, resource constraints |
| Full analysis | Partial analysis | Memory limits, timeout |
| All models | Selected models | Critical sections missing |
| Auto-processed | Manual review | Complex edge cases |

### Strategy 4: Data Imputation

**Applicable**: Missing fields, incomplete records

**Imputation Rules**:

| Missing Field | Imputation Method | Validation |
|---------------|-------------------|------------|
| Year | Median of nearby cases | Check plausibility (2018-2026) |
| Country | Same industry majority | Check regional consistency |
| Purchase Elements | Industry average | Flag for manual review |
| Stakeholder Count | Industry average | Add confidence interval |
| Quantified Metrics | Skip analysis | Mark as "data insufficient" |

**Example**:
```python
def impute_missing_field(cases, field, industry):
    """Impute missing field using industry statistics"""
    industry_cases = [c for c in cases if c['industry'] == industry and field in c]
    if industry_cases:
        values = [c[field] for c in industry_cases]
        return {
            'value': statistics.median(values),
            'method': 'industry_median',
            'confidence': 'medium',
            'flag': 'imputed'
        }
    return None
```

### Strategy 5: Manual Escalation

**Applicable**: Complex edge cases, ambiguous data, critical failures

**Escalation Triggers**:

- 3+ retry attempts failed
- Critical data missing > 50%
- Cross-model inconsistency > 10%
- Validation failure > 5 checks
- Unrecoverable parsing error

---

## Error Recovery Procedures

### Procedure 1: Input File Recovery

**Error**: Input file missing or corrupt

**Steps**:

```
1. Detect error
   └── Check file existence and readability

2. Identify root cause
   ├── File deleted/moved → Check backup/archive
   ├── Corrupt format → Try alternate parser
   └── Wrong path → Check directory structure

3. Attempt recovery
   ├── Check backup location: ./archive/inputs/
   ├── Search for similar filename patterns
   ├── Request re-upload if needed
   └── Document recovery attempt

4. Update processing state
   ├── Mark file as recovered or missing
   ├── Update inventory and counts
   └── Continue with available files

5. Report outcome
   ├── Log recovery actions
   ├── Flag for data completeness review
   └── Generate recovery report
```

### Procedure 2: Missing Required Field Recovery

**Error**: Required field empty or missing

**Steps**:

```
1. Validate field presence
   └── Check required fields list

2. Identify missing fields
   ├── List all missing required fields
   ├── Check for partial matches (similar names)
   └── Determine criticality

3. Recovery options
   ├── Infer from context (if reliable)
   ├── Use industry default (if applicable)
   ├── Mark as "N/A" with explanation
   └── Reject document (if critical)

4. Update validation status
   ├── Update validation report
   ├── Document imputation decisions
   └── Flag for manual review

5. Proceed or stop
   ├── If recoverable: mark warning, continue
   └── If critical: reject, stop processing
```

### Procedure 3: Model Generation Failure Recovery

**Error**: Model generation fails mid-process

**Steps**:

```
1. Detect failure point
   └── Identify which section/agent failed

2. Check available partial output
   ├── Determine what was generated
   ├── Assess completeness of partial output
   └── Check if partial output is usable

3. Recovery strategy selection
   ├── If >80% complete: Salvage partial, complete manually
   ├── If 50-80% complete: Resume from checkpoint
   └── If <50% complete: Restart with different approach

4. Implement recovery
   ├── Save partial output as draft
   ├── Create recovery checkpoint
   ├── Resume or restart processing
   └── Log recovery actions

5. Final validation
   ├── Validate recovered output
   ├── Check for consistency issues
   └── Update processing state
```

### Procedure 4: Validation Failure Recovery

**Error**: Validation checks fail

**Steps**:

```
1. Identify failed checks
   └── List all failed validation checks

2. Categorize failures
   ├── Critical (must fix): Sections missing, traceability missing
   ├── High (should fix): Data inconsistencies, format errors
   ├── Medium (review): Edge cases, outliers
   └── Low (document): Minor inconsistencies

3. Recovery by category
   ├── Critical: Stop processing, fix issue, re-run
   ├── High: Fix issue, re-validate specific check
   ├── Medium: Document as known limitation, continue
   └── Low: Log issue, no action required

4. Update validation report
   ├── Document fixes applied
   ├── Update status for each check
   ├── Add rationale for acceptance if any
   └── Generate revised report

5. Final decision
   ├── All critical fixed: Accept output
   ├── Critical remaining: Reject output
   └── Medium/low issues: Accept with notes
```

### Procedure 5: Cross-Model Inconsistency Recovery

**Error**: Data inconsistent across models

**Steps**:

```
1. Detect inconsistency
   ├── Compare case counts across models
   ├── Compare industry taxonomies
   ├── Compare purchase factor definitions
   └── Identify specific inconsistencies

2. Investigate root cause
   ├── Check source data for discrepancies
   ├── Review aggregation logic
   ├── Verify calculation formulas
   └── Identify processing differences

3. Resolution options
   ├── Correct the model with error (if clear)
   ├── Use consensus value (if small difference)
   ├── Flag as "known inconsistency" (if minor)
   └── Regenerate all models (if systematic)

4. Apply resolution
   ├── Document the decision logic
   ├── Update affected models
   ├── Re-run validation
   └── Update traceability

5. Update documentation
   ├── Add note to model outputs
   ├── Update processing log
   └── Create inconsistency report
```

---

## Checkpoint System

### Checkpoint Definition

**Checkpoint**: Saved state at critical processing milestones

### Checkpoint Locations

```
Processing Milestones:
├── Phase 0: Input Validation Complete
│   └── Checkpoint: input_validation_done.json
├── Phase 1: Industry Model Complete
│   └── Checkpoint: industry_model_complete.json
├── Phase 2: Stakeholder Model Complete
│   └── Checkpoint: stakeholder_model_complete.json
├── Phase 3: Purchase Factor Model Complete
│   └── Checkpoint: purchase_factor_model_complete.json
└── Phase 4: All Models Complete
    └── Checkpoint: all_models_complete.json
```

### Checkpoint Content Structure

```json
{
  "checkpoint_id": "industry_model_complete",
  "timestamp": "2026-05-07T14:30:00Z",
  "processing_stage": "phase_1",
  "files_generated": [
    "industry_model.md"
  ],
  "statistics": {
    "input_cases": 122,
    "processing_time_seconds": 180,
    "memory_used_mb": 512
  },
  "validation_status": "passed",
  "next_stage": "stakeholder_model",
  "resume_point": "stakeholder_model_start"
}
```

### Resume Processing

**Usage**: When processing is interrupted or fails

```
Resume Workflow:
1. Load latest checkpoint
2. Check checkpoint validity
3. Determine resume point
4. Resume from identified point
5. Continue processing
6. Generate final report with recovery notes
```

---

## Error Logging and Reporting

### Error Log Structure

```json
{
  "error_id": "ERR-2026-05-07-001",
  "timestamp": "2026-05-07T14:35:22Z",
  "error_type": "DATA_QUALITY",
  "severity": "MEDIUM",
  "stage": "input_validation",
  "description": "Missing required field 'Year' in 3 documents",
  "affected_documents": [
    "customer1-analysis.md",
    "customer2-analysis.md",
    "customer3-analysis.md"
  ],
  "recovery_action": "imputed_median_year",
  "recovery_result": "success",
  "processing_impact": "minor",
  "manual_review_required": false,
  "resolved": true
}
```

### Error Summary Report

```
# Error Recovery Summary Report

## Processing Information
- **Processing Date**: 2026-05-07
- **Input Files**: 122
- **Processing Time**: 3 hours 15 minutes

## Error Statistics
| Severity | Count | Resolved | Unresolved |
|----------|--------|----------|-----------|
| CRITICAL | 0 | 0 | 0 |
| HIGH | 1 | 1 | 0 |
| MEDIUM | 3 | 3 | 0 |
| LOW | 8 | 6 | 2 |
| **Total** | 12 | 10 | 2 |

## Error Details

### ERR-2026-05-07-001 (MEDIUM) - RESOLVED
- **Type**: DATA_QUALITY
- **Description**: Missing required field 'Year' in 3 documents
- **Recovery**: Imputed median year (2024) from industry
- **Impact**: Minor
- **Manual Review**: Not required

### ERR-2026-05-07-002 (HIGH) - RESOLVED
- **Type**: PROCESSING
- **Description**: Agent-Industry timeout during synthesis
- **Recovery**: Retried with serial processing
- **Impact**: Processing delayed by 15 minutes
- **Manual Review**: Not required

### ERR-2026-05-07-003 (LOW) - UNRESOLVED
- **Type**: VALIDATION
- **Description**: Minor traceability gap in section 5
- **Recovery**: Documented as known limitation
- **Impact**: Minimal
- **Manual Review**: Recommended

## Recovery Success Rate
- **Total Errors**: 12
- **Resolved**: 10
- **Unresolved**: 2
- **Success Rate**: 83.3%

## Recommendations
1. Review unresolved errors for potential fixes
2. Improve data collection to prevent missing years
3. Increase timeout threshold for agent processing
4. Add traceability validation step

## Quality Assessment
- **Overall Quality**: HIGH
- **Data Completeness**: 97.5%
- **Validation Status**: PASSED with 2 warnings
```

---

## Preventive Measures

### Input Quality Prevention

| Prevention Measure | Implementation |
|-------------------|----------------|
| Input validation before processing | Run input validation framework |
| Data quality checks | Validate all fields during parsing |
| Error-tolerant parsing | Continue processing minor format issues |
| Backup retention | Keep original input files |

### Processing Reliability Prevention

| Prevention Measure | Implementation |
|-------------------|----------------|
| Resource monitoring | Track memory and CPU usage |
| Timeout handling | Graceful timeout with retry |
| Checkpoint system | Save state at critical points |
| Parallel processing control | Limit concurrent agents |

### Output Quality Prevention

| Prevention Measure | Implementation |
|-------------------|----------------|
| Real-time validation | Validate during generation |
| Automated checks | Run validation framework |
| Manual review process | Review flagged items |
| Version control | Keep output versions |

---

## Recovery Scripts

### Recovery Manager Script

```python
#!/usr/bin/env python3
"""
Error Recovery Manager
Handles systematic error recovery for scenario_modeler
"""

import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any

class ErrorRecoveryManager:
    """Manages error recovery for model processing"""
    
    def __init__(self, log_dir: str = "./logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        self.error_log = []
        self.checkpoints = {}
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_dir / 'recovery.log'),
                logging.StreamHandler()
            ]
        )
        
    def log_error(self, error_type: str, severity: str, description: str, 
                 affected_items: List[str] = None, recoverable: bool = True) -> str:
        """Log an error for recovery tracking"""
        error_id = f"ERR-{datetime.now().strftime('%Y-%m-%d-%H%M%S')}"
        
        error_entry = {
            "error_id": error_id,
            "timestamp": datetime.now().isoformat(),
            "error_type": error_type,
            "severity": severity,
            "description": description,
            "affected_items": affected_items or [],
            "recoverable": recoverable,
            "resolved": False
        }
        
        self.error_log.append(error_entry)
        
        # Log to file
        logging.error(f"{error_id}: {description}")
        
        # Save checkpoint
        self.save_checkpoint()
        
        return error_id
    
    def resolve_error(self, error_id: str, recovery_action: str, 
                    result: str, impact: str = "minor") -> None:
        """Mark an error as resolved"""
        for error in self.error_log:
            if error["error_id"] == error_id:
                error["recovery_action"] = recovery_action
                error["recovery_result"] = result
                error["processing_impact"] = impact
                error["resolved"] = True
                break
        
        logging.info(f"{error_id}: Resolved with action '{recovery_action}'")
        self.save_checkpoint()
    
    def save_checkpoint(self, stage: str = None) -> None:
        """Save recovery checkpoint"""
        checkpoint = {
            "timestamp": datetime.now().isoformat(),
            "stage": stage,
            "error_count": len(self.error_log),
            "resolved_count": sum(1 for e in self.error_log if e["resolved"]),
            "unresolved_count": sum(1 for e in self.error_log if not e["resolved"])
        }
        
        checkpoint_file = self.log_dir / "recovery_checkpoint.json"
        with open(checkpoint_file, 'w') as f:
            json.dump(checkpoint, f, indent=2)
    
    def load_checkpoint(self) -> Optional[Dict]:
        """Load recovery checkpoint if exists"""
        checkpoint_file = self.log_dir / "recovery_checkpoint.json"
        if checkpoint_file.exists():
            with open(checkpoint_file, 'r') as f:
                return json.load(f)
        return None
    
    def generate_report(self) -> str:
        """Generate error recovery summary report"""
        total = len(self.error_log)
        resolved = sum(1 for e in self.error_log if e["resolved"])
        unresolved = total - resolved
        
        report = []
        report.append("# Error Recovery Summary Report")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        report.append("## Statistics")
        report.append(f"- Total Errors: {total}")
        report.append(f"- Resolved: {resolved}")
        report.append(f"- Unresolved: {unresolved}")
        report.append(f"- Success Rate: {(resolved/total*100):.1f}%" if total > 0 else "0%")
        report.append("")
        
        report.append("## Error Details")
        for error in self.error_log:
            status = "✓ RESOLVED" if error["resolved"] else "✗ UNRESOLVED"
            report.append(f"### {error['error_id']} [{error['severity']}] - {status}")
            report.append(f"- Type: {error['error_type']}")
            report.append(f"- Description: {error['description']}")
            if error["recovery_action"]:
                report.append(f"- Recovery: {error['recovery_action']}")
            report.append("")
        
        return "\n".join(report)
    
    def can_proceed(self) -> bool:
        """Determine if processing can proceed with current state"""
        critical_unresolved = sum(1 for e in self.error_log 
                              if e["severity"] == "CRITICAL" and not e["resolved"])
        return critical_unresolved == 0

# Usage example
if __name__ == '__main__':
    manager = ErrorRecoveryManager()
    
    # Log an error
    err_id = manager.log_error(
        error_type="DATA_QUALITY",
        severity="MEDIUM",
        description="Missing required field 'Year' in 3 documents",
        affected_items=["doc1.md", "doc2.md", "doc3.md"]
    )
    
    # Resolve the error
    manager.resolve_error(
        error_id=err_id,
        recovery_action="imputed_median_year",
        result="success",
        impact="minor"
    )
    
    # Generate report
    print(manager.generate_report())
```

---

## Integration with Workflow

### Pre-Processing Integration

```
Workflow: scenario_modeler

1. Input Validation
   └── Run input-validation-framework
   └── Log any errors to recovery manager

2. Error Handling
   └── For each error: determine recovery strategy
   └── Apply recovery: impute/retry/skip/escalate
   └── Update recovery status

3. Proceed to Processing
   └── If can_proceed(): continue
   └── Else: stop and request manual intervention
```

### During Processing Integration

```
Processing Loop with Recovery:

For each processing step:
├── Try to execute step
├── If success: continue to next step
├── If failure:
│   ├── Log error
│   ├── Determine recovery strategy
│   ├── Apply recovery
│   ├── Save checkpoint
│   └── Retry or continue based on result
└── After all steps: generate recovery report
```

### Post-Processing Integration

```

After Model Generation:

1. Run validation framework
2. Check for validation failures
3. For each failure:
   ├── Log as validation error
   ├── Determine if critical
   ├── Apply recovery if possible
   └── Flag for manual review if needed
4. Generate final report with recovery summary
```

---

## Best Practices

1. **Log Everything**: All errors and recovery actions must be logged
2. **Save Checkpoints**: Regularly save processing state
3. **Prioritize Critical Issues**: Address critical/high severity first
4. **Document Decisions**: Always document recovery rationale
5. **Track Patterns**: Identify recurring errors for prevention
6. **Manual Review Flag**: Know when to escalate to manual review
7. **Quality vs Speed**: Balance recovery completeness with processing time
8. **Transparent Reporting**: Report all recovery actions in final output

---

## Maintenance

### Regular Review

- Review error logs monthly
- Identify patterns and recurring issues
- Update prevention measures
- Adjust recovery strategies based on experience

### Framework Updates

- Add new error types as discovered
- Update recovery strategies based on patterns
- Enhance prevention measures
- Improve documentation and examples