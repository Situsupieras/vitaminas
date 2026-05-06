---
name: pipeline-monitor
description: "Monitor n8n workflow executions, track product completion status, and alert on failures. Use when checking pipeline health, generating progress reports, or debugging failed executions."
risk: safe
source: personal
date_added: "2026-05-06"
---

# Pipeline Monitor — Execution Tracker

## Overview
Tracks the status of all 82 products through the marketing pipeline, monitors n8n workflow executions, and provides dashboards for progress visibility.

## When to Use
- Checking which products have been processed vs pending
- Debugging a failed n8n execution
- Generating a weekly progress report
- Before starting a batch run (verify capacity)
- After a batch run (verify completeness)

## Product Status Tracking

### Status Definitions
| Status | Meaning | Indicator |
|:---|:---|:---|
| `NOT_STARTED` | No files generated yet | Empty folder or no folder |
| `IN_PROGRESS` | Some files generated, pipeline running | 1-4 files in n8n_output |
| `COMPLETE` | All 5 core files generated | 5 files in n8n_output, each >1KB |
| `VALIDATED` | Passed quality checker | quality_report.json exists with all PASS |
| `PUBLISHED` | Content deployed to social media | published_log.json exists |
| `FAILED` | Pipeline error, needs retry | error_log.txt exists |

### Quick Status Check (Local)
```powershell
# Count files per product folder
Get-ChildItem "c:\proyectos\vitaminas" -Directory | ForEach-Object {
    $count = (Get-ChildItem "$($_.FullName)\n8n_output\*.md" -ErrorAction SilentlyContinue).Count
    $status = switch ($count) {
        0 { "NOT_STARTED" }
        {$_ -lt 5} { "IN_PROGRESS ($count/5)" }
        {$_ -ge 5} { "COMPLETE" }
    }
    [PSCustomObject]@{ Product = $_.Name; Files = $count; Status = $status }
} | Format-Table -AutoSize
```

### n8n Execution Check (VPS)
```powershell
# Check recent executions
ssh sts@148.230.88.220 "docker logs n8n-standalone --tail 20 --since 24h"

# Check for errors
ssh sts@148.230.88.220 "docker logs n8n-standalone --since 24h 2>&1 | Select-String 'ERROR'"
```

## Progress Dashboard

### Product Pipeline Tracker
```markdown
| # | Producto | Research | Funnel | Story | Copy | Calendar | Video | Status |
|---|----------|----------|--------|-------|------|----------|-------|--------|
| 1 | Magnesio | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | COMPLETE |
| 2 | Berberina | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | NOT_STARTED |
| 3 | Ashwagandha | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | NOT_STARTED |
...
```

### Key Metrics
- **Total Products**: 82
- **Completed**: X/82
- **In Progress**: X/82
- **Failed (need retry)**: X/82
- **Average Time per Product**: ~3 min (pipeline) + ~30 min (video)
- **Estimated Completion**: X days at current rate

## Failure Handling

### Common Failures
| Error | Cause | Fix |
|:---|:---|:---|
| `429 Too Many Requests` | OpenRouter rate limit | Wait 60s, retry. Use `--delay` flag |
| `500 Internal Server Error` | LLM temporary failure | Retry same request |
| `Empty response` | Model returned blank | Switch model or increase `max_tokens` |
| `Timeout` | Request took >60s | Split into smaller sections |
| `Connection reset` | Network issue (VPS or local) | Check internet, retry |

### Retry Protocol
1. Check error type in logs
2. If rate limit → wait 2 minutes, retry
3. If empty response → increase temperature to 0.8, retry
4. If persistent failure → switch to backup model (`meta-llama/llama-4-maverick:free`)
5. Log the failure and move to next product
6. Come back to failed products in a dedicated retry batch

## Alerting

### Manual Check (Daily)
```powershell
# Run this daily to check pipeline health
ssh sts@148.230.88.220 "docker exec n8n-standalone n8n list:workflow" | Select-String "TINITA"
ssh sts@148.230.88.220 "docker logs n8n-standalone --since 24h 2>&1 | Select-String 'error' -CaseSensitive:$false"
```

### Future: Automated Alerts (n8n)
Add an Error Trigger node to the TINITA workflow that sends a WhatsApp/Email alert when any execution fails.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Monitoring is currently manual. Automated dashboards require additional n8n configuration.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
