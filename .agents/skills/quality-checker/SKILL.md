---
name: quality-checker
description: "Validate that LLM-generated marketing content follows the established frameworks (Schwartz 5 levels, Gary Vee 3:1 ratio, Brunson Epiphany Bridge, etc.). Use after every pipeline execution to ensure output quality before publishing."
risk: safe
source: personal
date_added: "2026-05-06"
---

# Quality Checker — Content Validation Agent

## Overview
Automated quality gate that validates every piece of generated marketing content against the frameworks defined by the 9 core agents. Catches hallucinations, missing sections, and framework violations before content reaches the public.

## When to Use
- After running the n8n pipeline or local simulator for any product
- Before publishing any content to social media or email
- When auditing a batch of products for consistency
- When a new LLM model is introduced (to verify output quality)

## Validation Checklist by File

### 01_research_positioning.md
- [ ] **Avatar completo**: Tiene nombre, edad, profesión, ingresos en Quetzales, estado civil, hijos
- [ ] **3+ Dolores**: Emocionales, no genéricos ("estrés" solo no cuenta, debe ser específico)
- [ ] **3+ Anhelos**: Secretos, no obvios (no solo "sentirse bien")
- [ ] **Dream 100**: Al menos 5 fuentes específicas de Guatemala (no globales genéricas)
- [ ] **Océano Azul**: Tiene Red Ocean vs Blue Ocean claramente diferenciados
- [ ] **Palabra Mental** (Ries/Trout): Una sola palabra definida para posicionar el producto
- [ ] **Sin jerga de IA**: No contiene "¡Excelente!", "¡Claro!", "Como modelo de lenguaje..."

### 02_funnel_persuasion.md
- [ ] **Escalera de Valor**: 4 peldaños mínimo (Free → Frontend → Middle → Backend)
- [ ] **CAC Kennedy**: Cálculo explícito del costo máximo de adquisición
- [ ] **Blair Warren**: Las 5 frases de persuasión adaptadas al producto
- [ ] **Oferta Irracional** (Ariely): Anclaje de precio + trigger de gratuidad
- [ ] **Precio en Quetzales**: No usa dólares ni euros

### 03_story_hooks.md
- [ ] **Puente de la Epifanía**: Historia en 4 pasos (Backstory → Journey → New Opportunity → Framework)
- [ ] **Tierra Prometida** (Hoffer): Visión aspiracional definida
- [ ] **5+ Hooks**: Estilo National Enquirer, contra-intuitivos
- [ ] **3+ Visual Hooks**: Descripciones de acciones visuales para TikTok
- [ ] **Pre-frame** (Brafman): Frase de anclaje para percepción

### 04_copy_assets.md
- [ ] **Análisis de Conciencia** (Schwartz): Nivel identificado (Unaware → Most Aware)
- [ ] **3 Guiones de Video**: Cada uno con Hook → Retención → Solución → CTA
- [ ] **2 Facebook Ads**: Ad 1 = Cold (Story Lead), Ad 2 = Retargeting (Offer Lead)
- [ ] **3 Emails Soap Opera**: Siguiendo la secuencia de Brunson
- [ ] **CTA claros**: Cada pieza tiene un llamado a la acción específico

### 05_calendario_editorial.md
- [ ] **30 días completos**: Tabla con los 30 días, no menos
- [ ] **Ratio 3:1** (Gary Vee): ~21 días JAB + ~9 días RIGHT HOOK
- [ ] **Multi-plataforma**: Usa IG, FB, TikTok, Email, WhatsApp
- [ ] **Emails distribuidos**: Los 3 Soap Opera emails están en los días correctos
- [ ] **Hora de Vínculo**: Cada día indica qué hora de las 7 está cubriendo

## Automated Validation Script

```python
# Uso: python quality_checker.py <product_folder>
# Ejemplo: python quality_checker.py "Magnesio citrato y glicinato"
#
# Output: Reporte con PASS/FAIL por cada criterio
# Exit code 0 = todo OK, Exit code 1 = hay fallos
```

### Validaciones automáticas que el script debe hacer:
1. **Verificar que los 5 archivos existen** y no están vacíos (>1KB)
2. **Buscar la Palabra Mental** en el archivo 01 (debe existir)
3. **Contar los hooks** en el archivo 03 (mínimo 5)
4. **Verificar el ratio JAB/HOOK** en el calendario (contar ocurrencias)
5. **Detectar jerga de IA** ("¡Excelente!", "¡Claro!", "Como modelo de lenguaje")
6. **Verificar consistencia del avatar** (mismo nombre en los 5 archivos)
7. **Verificar moneda** (Q o Quetzales, no USD)

## Red Flags (Rechazo Automático)
- ❌ Avatar sin nombre propio (solo "el cliente" o "el usuario")
- ❌ Dolores genéricos sin contexto guatemalteco
- ❌ Hooks que no son contra-intuitivos (solo descriptivos)
- ❌ Calendario con menos de 25 días
- ❌ Emails sin subject lines
- ❌ Guiones de video sin hook en los primeros 3 segundos

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- This checker validates structure and presence, not creative quality.
- Human review is still required for tone, cultural relevance, and factual accuracy.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
