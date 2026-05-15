# Recovery Guidelines

## Overview

This document defines the recovery mechanism for scenario_engineering execution, enabling continuation from interruption points.

## Recovery Principles

### RR-01: Forward Recovery Only

- No rollback to previous phases
- Only continue from current checkpoint
- If earlier output is invalid, start new project

### RR-02: Skip Completed Work

- Check `processed_files` before each task
- Do not re-process completed items
- Efficient resource utilization

### RR-03: Preserve State

- Update `state.json` after each batch
- Maintain checkpoint history
- Keep error log for debugging

### RR-04: User Control

- User can choose to retry or skip failed items
- User can override resume behavior
- Explicit confirmation for recovery decisions

---

## State File Discovery

When resuming, locate `state.json` in this order:

```
1. Current working directory
   → If found: Use this state file

2. Most recent project-* directory
   → If found: Switch to that directory

3. User-specified path
   → If provided: Use specified state.json

4. No state file found
   → Prompt user to specify or start new project
```

---

## Recovery Workflow

### Step 1: Load State

```javascript
// Read state.json
const state = JSON.parse(readFile('state.json'));

// Validate state structure
validateStateStructure(state);
```

### Step 2: Determine Resume Point

```javascript
// Get current phase
const currentPhase = state.progress.current_phase;

// Get phase status
const phaseStatus = state.progress.phase_status;

// Find resume action
const resumeAction = state.resume_info.resume_action;

// Build pending file list
const pendingFiles = state.progress.phase_details[`phase${currentPhase}`].pending_files;
```

### Step 3: Execute Recovery

| Resume Scenario | Action |
|-----------------|--------|
| `phase0_init` pending | Complete initialization, create directories |
| `phase1_survey` in_progress | Continue questionnaire/narrative generation |
| `phase2_parser` in_progress | Skip processed, continue pending documents |
| `phase3_analyzer` in_progress | Skip processed, continue pending analyses |
| `phase4_model` pending | Collect phase3 reports, start synthesis |
| `phase5_final` pending | Generate final reports |
| Crash mid-batch | Continue from last checkpoint document |

### Step 4: Update State

After each batch:
```javascript
// Update processed/pending lists
state.progress.phase_details.phaseX.processed_files.push(completedFiles);
state.progress.phase_details.phaseX.pending_files = remainingFiles;

// Update counts
state.progress.phase_details.phaseX.processed += batchCount;
state.progress.phase_details.phaseX.pending -= batchCount;

// Add checkpoint
state.checkpoints.push({
  timestamp: new Date().toISOString(),
  phase: currentPhase,
  action: 'batch_complete'
});

// Write updated state
writeFile('state.json', JSON.stringify(state));
```

---

## Checkpoint Frequency

| Phase | Default Frequency | Configurable |
|-------|-------------------|--------------|
| Phase 0 | Once (at completion) | No |
| Phase 1 | After each questionnaire | Yes |
| Phase 2 | Every 5 documents | Yes (config.checkpoint_frequency) |
| Phase 3 | Every 5 analyses | Yes (config.checkpoint_frequency) |
| Phase 4 | After each model | Yes |
| Phase 5 | Once (at completion) | No |

---

## Failed Document Handling

### Decision Matrix

| Failure Type | Default Action | User Options |
|--------------|----------------|--------------|
| PDF corrupted | Skip with warning | Retry with re-acquired file |
| Content missing | Mark as insufficient | Skip / Supplement manually |
| Parse error | Skip with warning | Retry with preprocessing |
| Timeout | Retry once | Skip / Increase timeout |

### Failed File Tracking

```json
{
  "failed_files": [
    {
      "file": "inputs/raw/doc-003.pdf",
      "reason": "PDF corrupted",
      "timestamp": "2026-04-21T12:00:00Z",
      "action_taken": "skipped",
      "suggested_action": "Re-acquire original document"
    }
  ]
}
```

---

## Resume Mode Detection

### Auto-Detection Logic

```
if (state.json exists) {
  if (state.progress.phase_status contains "in_progress") {
    → Auto-resume from interruption
  } else if (state.progress.phase_status all "completed") {
    → Project complete, prompt user
  } else {
    → Unknown state, prompt user for action
  }
} else {
  → No state, start new project
}
```

### User Override Options

```
--resume              Force resume (even if state shows complete)
--from-phase 2        Skip phases 0-1, start from phase 2
--new                 Ignore existing state, start fresh
--validate            Check outputs, do not resume execution
```

---

## Error Recovery Procedures

### E-01: State File Corrupted

```
Symptoms: JSON parse error, missing required fields
Action:
  1. Check archive/state-final.json for backup
  2. If backup exists, restore from backup
  3. If no backup, prompt user to:
     - Start new project
     - Manually reconstruct state
```

### E-02: Output Files Missing

```
Symptoms: Output file referenced in state.json not found
Action:
  1. Mark as failed in state
  2. Add to failed_files with reason "file_missing"
  3. Regenerate in next batch if possible
```

### E-03: Checkpoint Not Found

```
Symptoms: Last checkpoint timestamp older than expected
Action:
  1. Scan output directory for completed files
  2. Rebuild processed_files list from actual outputs
  3. Update state.json with reconstructed state
```

---

## State Update Protocol

### After Each Batch

1. Append completed files to `processed_files`
2. Remove completed files from `pending_files`
3. Update counters (processed, pending, failed)
4. Add checkpoint entry
5. Update `updated_at` timestamp
6. Write state.json atomically

### After Phase Completion

1. Set phase status to "completed"
2. Record `completed_at` timestamp
3. Set next phase status to "pending"
4. Update `current_phase`
5. Set `resume_action` for next phase
6. Clear `resume_files` (no pending)
7. Write state.json

### Atomic Write

```javascript
// Write atomically to prevent corruption
writeFile('state.json.tmp', JSON.stringify(state));
renameFile('state.json.tmp', 'state.json');
```

---

## Validation Before Resume

```
Check 1: State file structure valid
Check 2: Referenced directories exist
Check 3: Input files still available
Check 4: Output files referenced exist
Check 5: Phase transition is valid

If any check fails:
  → Log error
  → Prompt user for action
  → Do not auto-resume
```

---

*Reference: Recovery Guidelines v1.0*
