# TINITA HEALTH — Agentes y Configuración

Este archivo configura los agentes disponibles para **Claude Code**, **OpenAI Codex**, y otros AI coding assistants.

## Agentes Disponibles

### `landing-page-builder`
Construye landing pages de alta conversión para productos TINITA HEALTH.
- **Actívalo cuando**: El usuario pida una landing page, página de ventas, o página web para un producto
- **Skills que usa**: `landing-page`, `copywriting-master`, `positioning-strategist`
- **Output**: `<producto>/landing/index.html`

### `content-pipeline`
Orquesta el pipeline completo de 9 fases de marketing para un producto.
- **Actívalo cuando**: El usuario quiera procesar un producto nuevo o regenerar el contenido
- **Skills que usa**: todos los skills de marketing en `.agents/skills/`
- **Output**: 5 archivos en `<producto>/n8n_output/`

## Skills Disponibles

Los skills están en `.agents/skills/`. Cada uno tiene un `SKILL.md` con instrucciones detalladas.

### Marketing & Copy
- `copywriting-master` — Guiones, ads, emails de conversión
- `funnel-architect` — Embudos y escaleras de valor
- `pattern-disruptor` — Hooks y visuales de alto impacto
- `movement-creator` — Mensaje de marca y movimiento
- `persuasion-architect` — Ofertas y pricing psicológico
- `positioning-strategist` — Diferenciación competitiva
- `content-calendar` — Calendario editorial 30 días
- `marketing-reporter` — Avatar y Dream 100
- `traffic-infiltrator` — Estrategia de tráfico
- `landing-page` — Landing pages de alta conversión ← NUEVO

### Análisis & Estrategia
- `brand-consistency` — Coherencia de marca
- `quality-checker` — Validación de contenido generado
- `seo-audit` — Auditoría SEO
- `programmatic-seo` — SEO a escala
- `competitor-alternatives` — Páginas de comparación

### Tecnología & Operaciones
- `n8n-tinita-ops` — Deploy y debug en VPS
- `video-production` — Pipeline TTS → video
- `venv-manager` — Entorno virtual Python
- `systematic-debugging` — Debug estructurado
- `git-pushing` — Commit y push
- `backup-recovery` — Backups antes de cambios mayores
- `pipeline-monitor` — Monitoreo de ejecuciones n8n

## Slash Commands (Claude Code)

Disponibles en `.claude/commands/`:
- `/landing [producto]` — Genera landing page completa
- `/pipeline [producto]` — Ejecuta pipeline de 9 fases
- `/qa [producto]` — Valida calidad del contenido generado

## Reglas Globales para Todos los Agentes

1. Leer `CLAUDE.md` al inicio de cada sesión para el contexto del proyecto
2. Usar siempre `.venv_marketing\Scripts\python` para ejecutar Python
3. Los outputs de contenido van en español latinoamericano
4. No inventar datos — usar solo información real de los archivos del producto
5. Hacer backup antes de modificar workflows de n8n en producción
