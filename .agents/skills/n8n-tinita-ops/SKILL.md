---
name: n8n-tinita-ops
description: "Operational guide for managing the TINITA HEALTH n8n workflows on VPS (sts@148.230.88.220). Covers workflow import/export, credential management, monitoring, and safe Docker operations. Use when deploying, debugging, or updating n8n workflows."
risk: critical
source: personal
date_added: "2026-05-06"
---

# n8n Operations for TINITA HEALTH

## Overview
Operational procedures for managing n8n workflows on the production VPS. Follows a strict "do no harm" policy — never restart containers, never modify other services.

## When to Use
- Deploying a new workflow to n8n
- Updating an existing workflow
- Managing credentials (OpenRouter, Gemini, etc.)
- Monitoring workflow executions
- Debugging failed executions
- Exporting workflows for backup

## VPS Infrastructure Map

```
VPS: sts@148.230.88.220
├── n8n-standalone          (n8nio/n8n:latest, port 5678)
├── odoo-19                 (odoo:19.0, port 8069)
├── odoo-postgres           (postgres:16)
├── clinica-gateway-1       (openmrs, port 8040)
├── clinica-frontend-1      (openmrs frontend)
├── clinica-backend-1       (openmrs backend)
├── clinica-db-1            (mariadb:10.11.7)
├── easypanel               (easypanel/easypanel, port 3000)
├── easypanel-traefik       (traefik:3.6.7, ports 80/443)
├── colmenas_beewax-db      (postgres:17)
├── colmenas_beewax-api     (custom, port 8080)
├── cursos_wp_cursos_db     (mariadb:11)
└── objective_aryabhata     (node:18)
```

> [!CAUTION]
> **NEVER** restart, stop, or modify containers other than `n8n-standalone`. Other services (Clínica, Odoo, Colmenas, Cursos) are in production.

## Safe Operations

### Import a Workflow
```powershell
# 1. Copy JSON to VPS
scp workflow.json sts@148.230.88.220:/tmp/workflow.json

# 2. Copy into n8n container
ssh sts@148.230.88.220 "docker cp /tmp/workflow.json n8n-standalone:/tmp/workflow.json"

# 3. Import
ssh sts@148.230.88.220 "docker exec n8n-standalone n8n import:workflow --input=/tmp/workflow.json"

# 4. Clean up
ssh sts@148.230.88.220 "rm /tmp/workflow.json"
```

### Export a Workflow (Backup)
```powershell
ssh sts@148.230.88.220 "docker exec n8n-standalone n8n export:workflow --all --output=/tmp/n8n_backup.json"
scp sts@148.230.88.220:/tmp/n8n_backup.json c:\proyectos\vitaminas\backups\n8n_backup_$(date +%Y%m%d).json
```

### List All Workflows
```powershell
ssh sts@148.230.88.220 "docker exec n8n-standalone n8n list:workflow"
```

### Check n8n Logs
```powershell
ssh sts@148.230.88.220 "docker logs n8n-standalone --tail 50"
```

### Restart n8n ONLY (Safe)
```powershell
ssh sts@148.230.88.220 "docker restart n8n-standalone"
```

## Credential Management

### Via n8n UI
1. Navigate to https://n8n.papa-sts.online
2. Go to Credentials tab
3. Create/Edit credentials

### Current Credentials
| Name | Type | Used By |
|:---|:---|:---|
| OpenRouter API | Header Auth | All HTTP Request nodes (Marketing Pipeline) |

### Adding a New Credential
When adding API keys for new services:
1. Create credential in n8n UI (never hardcode in workflow JSON)
2. Document the credential name and type in this table
3. Assign to relevant workflow nodes

## Monitoring

### Check Recent Executions
```powershell
ssh sts@148.230.88.220 "docker exec n8n-standalone n8n list:workflow"
```

### Via UI
- Navigate to https://n8n.papa-sts.online/home/executions
- Filter by workflow name
- Check for failed executions (red indicators)

## Workflow Naming Convention
```
TINITA HEALTH - [Pipeline Name] ([Description])
```
Example: `TINITA HEALTH - Motor de Marketing (Pipeline 10 Fases)`

## Quality Gates
- [ ] Workflow imported successfully (no errors)
- [ ] Credentials assigned to all HTTP nodes
- [ ] Test execution passes with sample data
- [ ] No hardcoded API keys in workflow JSON
- [ ] Workflow tagged with "TINITA HEALTH"
- [ ] Backup exported before major changes

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
