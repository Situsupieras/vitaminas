# TINITA HEALTH — Motor de Marketing Automatizado

> **Versión**: 3.1.0 · **Build**: 2026-05-09
> **Última actualización**: Mayo 2026

---

## 🎯 ¿Qué es esto?

Un sistema automatizado que genera **todo el material de marketing** para los 82 productos de TINITA HEALTH: avatar del cliente, estrategia de posicionamiento, guiones de video, emails, calendario editorial de 30 días y video educativo de 60 minutos.

**Tiempo por producto**: ~30 minutos (automatizado) vs ~2 semanas (manual).

---

## 📋 Requisitos Previos

Antes de empezar, asegurate de tener:

| Requisito | Cómo verificar | Instalación |
|:---|:---|:---|
| Python 3.12+ | `python --version` | [python.org](https://python.org) |
| Git | `git --version` | [git-scm.com](https://git-scm.com) |
| Entorno Virtual | Verificar `.venv_marketing/` | `python -m venv .venv_marketing` |
| API Key OpenRouter | Verificar `.env` línea 25 | [openrouter.ai](https://openrouter.ai) |
| API Key Google | Verificar `.env` línea 4 | [aistudio.google.com](https://aistudio.google.com) |
| SSH al VPS | `ssh sts@148.230.88.220` | Pedir acceso al admin |

### Instalación rápida (primera vez)
```powershell
# 1. Clonar el repositorio
git clone <repo-url> c:\proyectos\vitaminas
cd c:\proyectos\vitaminas

# 2. Crear entorno virtual
python -m venv .venv_marketing

# 3. Instalar dependencias
.venv_marketing\Scripts\pip install -r requirements.txt

# 4. Configurar secretos
# Copiar .env.example a .env y llenar las API keys
copy .env.example .env
notepad .env
```

---

## 🚀 Guía Rápida: Crear Contenido para un Producto Nuevo

### Paso 1: Preparar la Carpeta del Producto

Creá una carpeta con el nombre del producto:
```powershell
mkdir "c:\proyectos\vitaminas\Berberina"
mkdir "c:\proyectos\vitaminas\Berberina\n8n_output"
```

Colocá dentro:
- La **foto del producto** (`.jpeg` o `.png`)
- La **foto de información nutricional** (`.jpeg` o `.png`)

### Paso 2: Configurar el Simulador

Abrí el archivo `scratch\n8n_simulator.py` y cambiá estas 3 variables:

```python
# Línea ~11: Carpeta de salida
OUTPUT_DIR = r"c:\proyectos\vitaminas\Berberina\n8n_output"

# Línea ~14: Contexto del avatar (dejá que el LLM lo genere o ponelo fijo)
ANDRES_CONTEXT = """
Avatar: María López, 52 años, Contadora...
"""

# Línea ~22: Descripción del producto
PRODUCT = "Berberina de TINITA HEALTH. 60 cápsulas. Precio: Q209..."
```

### Paso 3: Ejecutar el Pipeline

```powershell
.venv_marketing\Scripts\python scratch\n8n_simulator.py
```

**Tiempo estimado**: 2-3 minutos.

**Resultado**: 5 archivos en la carpeta `n8n_output/`:

| Archivo | Contenido |
|:---|:---|
| `01_research_positioning.md` | Avatar + Dream 100 + Posicionamiento + Palabra Mental |
| `02_funnel_persuasion.md` | Escalera de Valor + CAC + Oferta Irracional |
| `03_story_hooks.md` | Puente de la Epifanía + 5 Hooks + Pre-frame |
| `04_copy_assets.md` | 3 Guiones TikTok + 2 Facebook Ads + 3 Emails |
| `05_calendario_editorial.md` | Calendario de 30 días (ratio Gary Vee 3:1) |

### Paso 4: Revisar y Ajustar

Abrí cada archivo y verificá:
- ✅ El avatar tiene sentido para el producto
- ✅ Los dolores y anhelos son realistas
- ✅ Los guiones de video tienen hooks fuertes
- ✅ El calendario tiene la distribución correcta (21 días valor + 9 días venta)

### Paso 5: Generar el Video (Opcional)

```powershell
# Generar el guion extendido de la Masterclass (60 min)
.venv_marketing\Scripts\python scratch\generate_masterclass.py

# Limpiar texto para audio
.venv_marketing\Scripts\python scratch\prepare_audio_text.py

# Generar audio
.venv_marketing\Scripts\python scratch\generate_audio_gtts.py

# Crear slides
.venv_marketing\Scripts\python scratch\create_sample_slides.py

# Componer video final
.venv_marketing\Scripts\python scratch\compose_video.py
```

**Resultado**: Un video MP4 de ~10 minutos con el presentador Marco Villagrán + slides educativas + narración.

---

## 🌐 Usar n8n (Producción)

Si preferís usar n8n en el VPS en lugar del simulador local:

### Opción A: Ejecutar vía Webhook
```powershell
curl -X POST https://n8n.papa-sts.online/webhook/tinita-marketing `
  -H "Content-Type: application/json" `
  -d '{
    "product_name": "Berberina",
    "ingredients": "Berberina HCl 500mg",
    "price": "Q209",
    "avatar_context": "Mujer, 52 años, contadora..."
  }'
```

### Opción B: Ejecutar desde la UI de n8n
1. Entrá a **https://n8n.papa-sts.online**
2. Abrí el workflow **"TINITA HEALTH - Motor de Marketing (Pipeline 10 Fases)"**
3. Hacé clic en **"Execute Workflow"**
4. Ingresá los datos del producto en el nodo de Webhook

---

## 📁 Estructura del Proyecto

```
c:\proyectos\vitaminas\
├── .agents\                        # Specs de agentes IA
│   ├── content-pipeline.md         # Agente: pipeline completo 9 fases
│   ├── landing-page-builder.md     # Agente: construcción de landing pages
│   └── skills\                     # Skills usables con el comando Skill
│       ├── landing-page\SKILL.md
│       ├── video-production\SKILL.md
│       └── ... (39 skills total)
├── landing_esvitamina\             # Landing page Es Vitamina v3.1 ✅
│   ├── index.html                  # HTML limpio (sin inline styles/scripts)
│   ├── css\
│   │   ├── variables.css           # Custom properties + reset + base
│   │   ├── components.css          # Botones, cards, quiz, badges
│   │   ├── sections.css            # Secciones específicas + keyframes
│   │   └── responsive.css          # Media queries (mobile-first)
│   ├── js\
│   │   ├── quiz.js                 # Quiz lógica + lead capture gate
│   │   ├── ui.js                   # Navbar, IntersectionObserver, contadores
│   │   └── smooth.js               # Smooth scroll
│   └── assets\
│       └── guia-sintomas-esvitamina.html  # Lead magnet PDF (10 síntomas)
├── docs\                           # Documentación del proyecto
│   ├── brand_esvitamina.md         # Brand bible + design system
│   ├── LANDING_PLAN.md             # Plan de construcción de landing
│   └── REVISION_VISUAL_V3.md       # Notas de revisión visual v3
├── archive\                        # Versiones anteriores
│   └── index_v2.html               # Landing v2 (backup)
├── scratch\                        # Scripts de automatización
│   ├── n8n_simulator.py            # Simulador local del pipeline
│   ├── prepare_audio_text.py
│   ├── generate_audio_gtts.py      # TTS con Google gTTS
│   ├── generate_audio_google.py    # TTS con Google Cloud
│   ├── generate_audio_edge.py      # TTS con Edge TTS
│   ├── compose_video.py            # Composición final de video
│   └── create_pro_slides.py        # Generación de slides
├── .venv_marketing\                # Entorno virtual Python (NO en git)
├── .env                            # API Keys (NO en git)
├── .gitignore
├── requirements.txt
├── AGENTS.md                       # Guía de agentes para Claude Code
├── ARCHITECTURE.md                 # Arquitectura del sistema
├── CLAUDE.md                       # Config Claude Code (contexto + skills)
│
├── Magnesio citrato y glicinato\   # PILOTO ✅
│   ├── README.md
│   └── n8n_output\                 # 8 archivos generados
│
└── ... (82 productos total)
```

---

## 🌍 Landing Page Es Vitamina

La landing page vive en `landing_esvitamina/`. Arquitectura modular desde v3.1:

| Archivo | Responsabilidad |
|:---|:---|
| `css/variables.css` | Design tokens, reset, tipografía base |
| `css/components.css` | Botones, cards, quiz, badge, phone mockup |
| `css/sections.css` | Hero, nav, CTA, footer + keyframes |
| `css/responsive.css` | Media queries (768px / 1024px / 480px) |
| `js/quiz.js` | 4 pasos + gate de captura de leads (localStorage) |
| `js/ui.js` | Navbar scroll, IntersectionObserver, contadores |
| `js/smooth.js` | Smooth scroll para anclas |
| `assets/guia-sintomas-esvitamina.html` | Lead magnet imprimible (A4, 10 síntomas) |

### Deploy

```powershell
# Servir localmente para preview
cd landing_esvitamina
python -m http.server 8080
# Abrir http://localhost:8080

# Subir al VPS
scp -r landing_esvitamina/ sts@148.230.88.220:/var/www/esvitamina/
```

Los leads capturados por el quiz se guardan en `localStorage['esvitamina_leads']` como array JSON con campos: `name`, `phone`, `goal`, `age`, `urgency`, `timestamp`.

---

## 🧠 Los 9 Agentes de Marketing

Cada producto pasa por estos 9 agentes, cada uno basado en autores de clase mundial:

| # | Agente | Autores | Output |
|:---|:---|:---|:---|
| 0 | **Reportero** | Brunson (Fórmula Secreta), Chet Holmes (Dream 100) | Avatar + Dream 100 |
| 1 | **Posicionamiento** | April Dunford, Al Ries & Trout (Palabra Mental) | Océano Azul + Posicionamiento |
| 2 | **Embudo** | Brunson (Escalera de Valor), Dan Kennedy (CAC), Mark Joyner | Funnel + Oferta |
| 3 | **Storytelling** | Brunson (Epifanía), Eric Hoffer (Tierra Prometida) | Historia + Movimiento |
| 4 | **Tráfico** | Brunson (Traffic Secrets), Gary Vee (3:1), Tim Ferriss | Dream 100 + Pauta |
| 5 | **Disruptor** | Brendan Kane (Hook Point), Brafman (Pre-framing) | 5 Hooks + Visual Hooks |
| 6 | **Copywriting** | Schwartz (5 Niveles), Collier, Masterson | Guiones + Ads + Emails |
| 7 | **Persuasión** | Blair Warren, Dan Ariely, Brafman | Oferta Irracional + Precio |
| 8 | **Calendario** | Gary Vee (Jab/Hook), Brunson (Soap Opera) | 30 días mapeados |

---

## ❓ Preguntas Frecuentes

### ¿Cuánto cuesta operar el sistema?
**$0** si usás modelos gratuitos de OpenRouter y gTTS para audio. Las API keys de Google Gemini tienen tier gratuito generoso.

### ¿Puedo cambiar el avatar?
Sí. Editá la variable `ANDRES_CONTEXT` en `n8n_simulator.py` o dejala vacía para que el LLM genere uno nuevo.

### ¿Puedo usar otro idioma?
Los prompts están en inglés con instrucción de salida en español. Para cambiar el idioma de salida, modificá la línea `output in Spanish` en los system prompts del simulador.

### ¿Cómo agrego un producto nuevo al catálogo?
1. Creá la carpeta con el nombre del producto
2. Agregá las fotos del producto
3. Ejecutá el simulador (Paso 2 y 3 de esta guía)
4. Revisá los outputs (Paso 4)

### ¿Qué hago si el simulador falla?
1. Verificá tu conexión a internet
2. Verificá que la API key en `.env` sea válida
3. Revisá que el modelo en `OPENROUTER_MODEL` sea gratuito y activo
4. Probá con `google/gemini-2.5-flash` como modelo alternativo

### ¿Cómo subo un workflow nuevo a n8n?
Seguí las instrucciones del skill `n8n-tinita-ops`:
```powershell
scp workflow.json sts@148.230.88.220:/tmp/
ssh sts@148.230.88.220 "docker cp /tmp/workflow.json n8n-standalone:/tmp/ && docker exec n8n-standalone n8n import:workflow --input=/tmp/workflow.json"
```

---

## 📞 Soporte

- **VPS**: `ssh sts@148.230.88.220`
- **n8n UI**: https://n8n.papa-sts.online
- **Tienda**: https://tiendasts.com/suplementos (pendiente)
- **Repositorio de Skills**: `c:\proyectos\vitaminas\.agents\skills\`
