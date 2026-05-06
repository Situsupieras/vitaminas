---
name: backup-recovery
description: "Backup and restore procedures for n8n workflows, generated content, and VPS data. Use before major changes, after batch runs, or on a weekly schedule to prevent data loss."
risk: critical
source: personal
date_added: "2026-05-06"
---

# Backup & Disaster Recovery

## Overview
Protects all generated marketing assets, n8n workflows, and configurations from data loss. Covers local backups, VPS backups, and restoration procedures.

## When to Use
- Before making changes to n8n workflows
- After completing a batch of products
- Weekly scheduled backup
- Before updating Docker images on VPS
- When migrating to a new server
- After any system failure

## What to Backup

### Critical Assets (Priority 1 — Irreplaceable)
| Asset | Location | Method |
|:---|:---|:---|
| `.env` (API Keys) | `c:\proyectos\vitaminas\.env` | Manual copy to secure location |
| n8n Workflows | VPS Docker volume | `n8n export:workflow --all` |
| n8n Credentials | VPS Docker volume | `n8n export:credentials --all` |
| Generated Content | `*/n8n_output/*.md` | Git commit + push |

### Important Assets (Priority 2 — Time-consuming to regenerate)
| Asset | Location | Method |
|:---|:---|:---|
| Product folders (82) | `c:\proyectos\vitaminas\*` | Git |
| Skills (39+) | `.agents\skills\*` | Git |
| Scripts | `scratch\*` | Git |
| Avatar images | Various | Copy to `backups/` |
| Audio/Video files | `*/n8n_output/*.mp3, *.mp4` | External storage |

### Recoverable Assets (Priority 3 — Can be regenerated)
| Asset | Location | Recovery Method |
|:---|:---|:---|
| Slide images | `scratch\slides\` | Re-run `create_sample_slides.py` |
| Clean text files | `scratch\*_clean.txt` | Re-run `prepare_audio_text.py` |
| Virtual environment | `.venv_marketing\` | `pip install -r requirements.txt` |

## Backup Procedures

### 1. Local Backup (Git)
```powershell
# Stage all content changes
cd c:\proyectos\vitaminas
git add -A
git commit -m "backup: content generation $(Get-Date -Format 'yyyy-MM-dd')"
git push origin main
```

### 2. n8n Workflow Backup (VPS)
```powershell
# Export all workflows
ssh sts@148.230.88.220 "docker exec n8n-standalone n8n export:workflow --all --output=/tmp/n8n_workflows_backup.json"

# Export all credentials (encrypted)
ssh sts@148.230.88.220 "docker exec n8n-standalone n8n export:credentials --all --output=/tmp/n8n_credentials_backup.json"

# Download to local
$date = Get-Date -Format "yyyyMMdd"
mkdir -Force "c:\proyectos\vitaminas\backups"
scp sts@148.230.88.220:/tmp/n8n_workflows_backup.json "c:\proyectos\vitaminas\backups\n8n_workflows_$date.json"
scp sts@148.230.88.220:/tmp/n8n_credentials_backup.json "c:\proyectos\vitaminas\backups\n8n_credentials_$date.json"

# Cleanup VPS
ssh sts@148.230.88.220 "rm /tmp/n8n_*_backup.json"
```

### 3. Full VPS Docker Backup
```bash
# ON THE VPS (run via SSH)
# Backup n8n data volume
docker run --rm -v n8n_data:/data -v /tmp:/backup alpine tar czf /backup/n8n_data_$(date +%Y%m%d).tar.gz /data

# Download
scp sts@148.230.88.220:/tmp/n8n_data_*.tar.gz c:\proyectos\vitaminas\backups\
```

> [!CAUTION]
> **NEVER** stop the n8n container to make a backup. The export commands work while n8n is running.

## Recovery Procedures

### Restore n8n Workflows
```powershell
# Upload backup to VPS
scp "c:\proyectos\vitaminas\backups\n8n_workflows_YYYYMMDD.json" sts@148.230.88.220:/tmp/restore.json

# Import into n8n
ssh sts@148.230.88.220 "docker cp /tmp/restore.json n8n-standalone:/tmp/restore.json && docker exec n8n-standalone n8n import:workflow --input=/tmp/restore.json"
```

### Restore Generated Content
```powershell
# From git
git checkout main -- "Magnesio citrato y glicinato/n8n_output/"

# Or regenerate from scratch
.venv_marketing\Scripts\python scratch\n8n_simulator.py
```

### Restore Virtual Environment
```powershell
python -m venv .venv_marketing
.venv_marketing\Scripts\pip install -r requirements.txt
```

## Backup Schedule

| Frecuencia | Qué | Cómo |
|:---|:---|:---|
| **Después de cada producto** | Git commit + push | `git add -A && git commit && git push` |
| **Semanal (Lunes)** | n8n workflows + credentials | Procedimiento #2 |
| **Mensual** | Full VPS Docker volume | Procedimiento #3 |
| **Antes de cambios mayores** | Todo | Procedimientos #1 + #2 |

## Quality Gates
- [ ] `.env` está respaldado en ubicación segura (NO en git)
- [ ] Último backup de n8n tiene menos de 7 días
- [ ] `backups/` folder existe y contiene al menos 1 archivo
- [ ] Git está al día (no hay cambios sin commit)
- [ ] Se probó al menos 1 restauración exitosa

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Credential exports are encrypted with n8n's internal key. If the n8n instance is destroyed, credentials must be re-created manually.
- Large media files (MP4, MP3) are NOT backed up via git. Use external storage.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
