---
name: project-docs
description: "Generate and maintain project documentation for the TINITA HEALTH marketing engine. Covers README, architecture docs, product catalogs, and pipeline documentation. Use when creating, updating, or auditing project documentation."
risk: safe
source: personal
date_added: "2026-05-06"
---

# Project Documentation Generator

## Overview
Comprehensive documentation skill for the TINITA HEALTH automated marketing engine. Ensures all project artifacts, pipelines, and product catalogs are properly documented and maintainable.

## When to Use
- Creating or updating the project README
- Documenting a new product pipeline (Magnesio, Berberina, etc.)
- Generating architecture diagrams for the n8n workflow
- Auditing existing documentation for completeness
- Onboarding a new team member to the project

## Documentation Standards

### File Naming Convention
```
{product_folder}/
├── estrategia_maestra.md      # Master strategy (avatar, positioning, funnel)
├── marketing_plan.md           # 7-hour bonding plan
├── n8n_output/
│   ├── 01_research_positioning.md
│   ├── 02_funnel_persuasion.md
│   ├── 03_story_hooks.md
│   ├── 04_copy_assets.md
│   ├── 05_calendario_editorial.md
│   ├── 06_bonding_hours_content.md
│   ├── 07_deep_dive_content_H1_H2.md
│   └── 08_masterclass_script_60min.md
└── assets/                     # Images, videos, audio
```

### README Template
Every product folder MUST have a `README.md` with:
1. **Product Name and SKU**
2. **Price (Q) and Presentation** (cápsulas, tabletas, etc.)
3. **Avatar Name** and key demographics
4. **Pipeline Status** (which phases are complete)
5. **Links** to generated assets

### Architecture Documentation
Use Mermaid diagrams for:
- Pipeline flow (Webhook → Research → Funnel → Story → Copy → Calendar)
- Product catalog hierarchy
- VPS infrastructure map
- n8n workflow connections

### Language Rules
- All documentation in **Español de Guatemala** unless technical (code comments in English)
- Use **voseo informal** for customer-facing copy
- Use **usted formal** for documentation and guides

## Quality Gates
- [ ] README.md exists in product folder
- [ ] All 5 n8n_output files present
- [ ] Avatar name consistent across all files
- [ ] No placeholder text ("TODO", "TBD", "Lorem ipsum")
- [ ] All file links resolve correctly
- [ ] Architecture diagram is current

## Workflow

### Phase 1: Audit
1. List all product folders
2. Check for missing documentation files
3. Verify avatar consistency
4. Report gaps

### Phase 2: Generate
1. Create missing README files from template
2. Generate architecture diagrams
3. Update master catalog (products_catalog.md)
4. Cross-reference n8n workflow nodes

### Phase 3: Validate
1. Run link checker
2. Verify file sizes (empty files = incomplete generation)
3. Confirm no Lorena/old avatar references remain
4. Update project-level README.md

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
