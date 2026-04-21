# Phase {{PHASE_NUMBER}} Progress Report

## Execution Status

- **Phase**: {{PHASE_NUMBER}} - {{PHASE_NAME}}
- **Status**: {{STATUS}} (pending / in_progress / completed / failed)
- **Started**: {{STARTED_AT}}
- **Last Updated**: {{UPDATED_AT}}
- **Duration**: {{DURATION}}

## Progress Summary

| Metric | Count | Notes |
|--------|-------|-------|
| Total Tasks | {{TOTAL_TASKS}} | |
| Completed | {{COMPLETED_COUNT}} | {{COMPLETED_PERCENTAGE}}% |
| Pending | {{PENDING_COUNT}} | |
| Failed | {{FAILED_COUNT}} | See error log |
| In Progress | {{IN_PROGRESS_COUNT}} | Current batch |

## Completed Tasks

| # | Task | Source | Output File | Completed At |
|---|------|--------|-------------|--------------|
{{COMPLETED_TASKS_TABLE_ROWS}}

## Pending Tasks

| # | Task | Source | Expected Output |
|---|------|--------|-----------------|
{{PENDING_TASKS_TABLE_ROWS}}

## Failed Tasks

| # | Task | Source | Error | Suggested Action |
|---|------|--------|-------|------------------|
{{FAILED_TASKS_TABLE_ROWS}}

## Current Batch Status

- **Batch Number**: {{BATCH_NUMBER}}
- **Batch Size**: {{BATCH_SIZE}}
- **Batch Progress**: {{BATCH_PROGRESS}}/{{BATCH_SIZE}}
- **Remaining in Batch**: {{BATCH_REMAINING}}

## Agent Task Distribution

| Agent ID | Assigned Tasks | Completed | Failed | Status |
|----------|----------------|-----------|--------|--------|
{{AGENT_STATUS_TABLE_ROWS}}

## Estimated Completion

- **Remaining Documents**: {{REMAINING_DOCUMENTS}}
- **Estimated Time**: {{ESTIMATED_TIME}}
- **Expected Completion**: {{EXPECTED_COMPLETION_AT}}

## Errors and Alerts

{{ERROR_ALERTS_SECTION}}

## Next Actions

- [ ] Continue pending tasks ({{PENDING_COUNT}} remaining)
- [ ] Handle failed tasks ({{FAILED_COUNT}} items)
- [ ] Proceed to next phase upon completion
- [ ] Update state.json checkpoint

## Checkpoint Information

- **Last Checkpoint**: {{LAST_CHECKPOINT_TIMESTAMP}}
- **Checkpoint Phase**: {{LAST_CHECKPOINT_PHASE}}
- **Checkpoint Action**: {{LAST_CHECKPOINT_ACTION}}
- **State File Updated**: {{STATE_FILE_UPDATED}}

---

*Report generated: {{REPORT_GENERATED_AT}}*
*Phase: {{PHASE_NUMBER}} - {{PHASE_NAME}}*