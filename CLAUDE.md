# TINITA HEALTH — Marketing Engine · Claude Code Config

## Proyecto

Motor automatizado de marketing para **82 productos de suplementos**. Genera avatares, estrategias de posicionamiento, guiones de video, emails y calendarios editoriales usando LLMs + n8n.

- **VPS**: `ssh sts@148.230.88.220`
- **n8n UI**: https://n8n.papa-sts.online
- **Stack**: Python 3.12, OpenRouter API, Google TTS, n8n, FFmpeg

## Instrucciones de Contexto para Agentes

1. **Lee siempre el README.md** antes de cualquier tarea nueva para entender el pipeline completo.
2. **Entorno virtual**: Usa siempre `.venv_marketing\Scripts\python` — nunca el Python global.
3. **Secretos**: Lee `.env` para API keys. Nunca hardcodees keys en scripts.
4. **Outputs**: Todos los archivos generados van dentro de `<producto>\n8n_output\`.
5. **Idioma de outputs**: Los outputs de contenido van en **español latinoamericano**. El código y comentarios técnicos pueden ser en inglés.

## Skills Disponibles (usar con el comando `Skill`)

Los skills están en `.agents/skills/`. Úsalos ANTES de responder cuando apliquen:

### 🎯 Marketing & Copywriting
| Skill | Cuándo usarlo |
|-------|---------------|
| `copywriting-master` | Redactar guiones, ads, emails de conversión |
| `funnel-architect` | Diseñar embudos, escaleras de valor |
| `pattern-disruptor` | Crear hooks para redes sociales |
| `movement-creator` | Construir el mensaje de marca y movimiento |
| `persuasion-architect` | Optimizar offers, pricing, psicología de compra |
| `positioning-strategist` | Definir diferenciación competitiva |
| `content-calendar` | Planificar calendario editorial 30 días |
| `marketing-reporter` | Investigar avatar y Dream 100 |
| `traffic-infiltrator` | Estrategia de tráfico orgánico/pago |

### 🏗️ Tecnología & Operaciones
| Skill | Cuándo usarlo |
|-------|---------------|
| `landing-page` | Crear landing pages para productos |
| `n8n-tinita-ops` | Deploy, debug o actualizar workflows de n8n en VPS |
| `video-production` | Pipeline TTS → slides → video MP4 |
| `venv-manager` | Gestionar entorno virtual Python |
| `systematic-debugging` | Debuggear cualquier error o comportamiento inesperado |
| `git-pushing` | Commit y push de cambios al repositorio |
| `backup-recovery` | Backups antes de cambios mayores |
| `pipeline-monitor` | Monitorear estado de ejecuciones n8n |

### 📊 Análisis & Estrategia
| Skill | Cuándo usarlo |
|-------|---------------|
| `brand-consistency` | Auditar coherencia de marca entre productos |
| `quality-checker` | Validar calidad del contenido generado |
| `seo-audit` | Auditar SEO de páginas o contenido |
| `programmatic-seo` | Estrategia SEO a escala |
| `competitor-alternatives` | Páginas de comparación competitiva |

## Agentes Disponibles

En `.agents/`:
- `landing-page-builder` — Construye landing pages de alta conversión para productos TINITA HEALTH
- `content-pipeline` — Ejecuta el pipeline completo de 9 fases para un producto

## Convenciones del Proyecto

### Nomenclatura de Carpetas
```
<NombreProducto>/          # Nombre exacto como aparece en tienda
  n8n_output/              # Outputs del pipeline (nunca modificar manualmente)
  assets/                  # Imágenes del producto
```

### Scripts en `scratch/`
- `n8n_simulator.py` — Simulador local del pipeline completo
- `generate_batch_*.py` — Generación en lote de múltiples productos

### Variables de Entorno Clave
```
OPENROUTER_API_KEY     — Para LLM (modelos Claude/GPT/Gemini)
OPENROUTER_MODEL       — Modelo actual (ej: google/gemini-2.5-flash)
GOOGLE_API_KEY         — Para TTS de Google Cloud
```

## Reglas Críticas

- **NUNCA** subir `.env` al repositorio git
- **NUNCA** usar `pip install` sin el venv activado
- **SIEMPRE** hacer backup antes de modificar workflows de n8n en producción
- **SIEMPRE** validar el output de contenido contra `quality-checker` antes de publicar
