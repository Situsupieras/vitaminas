---
name: venv-manager
description: "Manage Python virtual environments for project isolation. Use when installing dependencies, running scripts, or setting up new development environments. Enforces best practices: always use venv, pin versions, keep requirements.txt updated."
risk: safe
source: personal
date_added: "2026-05-06"
---

# Python Virtual Environment Manager

## Overview
Enforces virtual environment best practices for all Python operations in the TINITA HEALTH marketing engine. Prevents global pip pollution and ensures reproducible environments.

## When to Use
- Before running ANY `pip install` command
- When setting up a new development environment
- When adding a new dependency to the project
- When running Python scripts (simulators, generators, etc.)
- When deploying to VPS or CI/CD

## Rules (MANDATORY)

### Rule 1: Never Install Globally
```
❌ pip install moviepy
✅ c:\proyectos\vitaminas\.venv_marketing\Scripts\pip install moviepy
```

### Rule 2: Always Activate or Use Full Path
```powershell
# Option A: Activate first
c:\proyectos\vitaminas\.venv_marketing\Scripts\Activate.ps1
pip install moviepy

# Option B: Use full path (preferred for scripts)
c:\proyectos\vitaminas\.venv_marketing\Scripts\python script.py
```

### Rule 3: Pin Versions in requirements.txt
After every `pip install`, update requirements.txt:
```powershell
c:\proyectos\vitaminas\.venv_marketing\Scripts\pip freeze > c:\proyectos\vitaminas\requirements.txt
```

### Rule 4: One venv Per Project
```
c:\proyectos\vitaminas\
├── .venv_marketing/        # Virtual environment (gitignored)
├── requirements.txt        # Pinned dependencies
├── .gitignore              # Must include .venv_marketing/
└── scratch/                # Scripts use venv Python
```

## Setup Workflow

### New Environment
```powershell
# 1. Create
python -m venv c:\proyectos\vitaminas\.venv_marketing

# 2. Install dependencies
c:\proyectos\vitaminas\.venv_marketing\Scripts\pip install -r c:\proyectos\vitaminas\requirements.txt

# 3. Verify
c:\proyectos\vitaminas\.venv_marketing\Scripts\pip list
```

### Adding a Dependency
```powershell
# 1. Install in venv
c:\proyectos\vitaminas\.venv_marketing\Scripts\pip install new-package

# 2. Update requirements
c:\proyectos\vitaminas\.venv_marketing\Scripts\pip freeze > c:\proyectos\vitaminas\requirements.txt

# 3. Commit requirements.txt
git add requirements.txt && git commit -m "deps: add new-package"
```

### Running Scripts
```powershell
# Always use venv Python
c:\proyectos\vitaminas\.venv_marketing\Scripts\python c:\proyectos\vitaminas\scratch\n8n_simulator.py
```

## VPS Deployment
When deploying scripts to the VPS (sts@148.230.88.220):
```bash
# On VPS
python3 -m venv /opt/tinita/venv
source /opt/tinita/venv/bin/activate
pip install -r requirements.txt
```

## Quality Gates
- [ ] `.venv_marketing/` is in `.gitignore`
- [ ] `requirements.txt` exists and is up to date
- [ ] No global pip installs in session history
- [ ] All scratch scripts use venv Python path

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
