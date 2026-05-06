---
name: brand-consistency
description: "Verify brand voice, visual identity, avatar naming, and tone consistency across all 82 products. Use when auditing multiple products, onboarding a new product, or after batch content generation."
risk: safe
source: personal
date_added: "2026-05-06"
---

# Brand Consistency Guardian

## Overview
Ensures that every piece of content generated for TINITA HEALTH maintains a unified brand identity across all 82 products. Catches inconsistencies in tone, naming, visual identity, and messaging before they reach the public.

## When to Use
- After generating content for a new product (compare vs established products)
- When batch-processing multiple products
- Before launching a new campaign
- During quarterly brand audits
- When onboarding a new team member or contributor

## Brand Standards

### Brand Voice
| Attribute | Correct ✅ | Incorrect ❌ |
|:---|:---|:---|
| **Tono** | Profesional pero cercano, como un amigo experto | Frío, clínico, o demasiado casual |
| **Idioma** | Español de Guatemala (voseo natural) | Español de España ("vosotros", "vale") |
| **Tecnicismo** | Explicar ciencia con analogías cotidianas | Jerga médica sin explicar |
| **Promesas** | Basadas en nutrición y bienestar | Promesas médicas o de cura |
| **Marca** | "TINITA HEALTH" (mayúsculas) | "Tinita health", "tinita", "TH" |

### Visual Identity
| Elemento | Valor | Uso |
|:---|:---|:---|
| **Color Principal** | `#1A1A2E` (Azul profundo) | Fondos de slides, banners |
| **Acento** | `#16C79A` (Verde salud) | Títulos, CTAs, highlights |
| **Texto** | `#F5E6CA` (Crema cálido) | Cuerpo de texto |
| **Alerta** | `#FF6B6B` (Rojo coral) | Mitos, datos impactantes |
| **Logo** | Blanco sobre oscuro | Esquina inferior derecha |
| **Tipografía** | Inter o similar sans-serif | Nunca serif para digital |

### Presenter
| Atributo | Estándar |
|:---|:---|
| **Nombre** | Marco Villagrán |
| **Título** | Especialista en Bienestar de TINITA HEALTH |
| **Nunca usar** | "Dr.", "Médico", "Nutriólogo certificado" |
| **Imagen** | Mismo archivo PNG para todos los videos |

### Content Rules
1. **Nunca prometer curas médicas**: "Puede ayudar a..." ✅ / "Cura el insomnio" ❌
2. **Siempre citar la forma del ingrediente**: "Magnesio Bisglicinato" ✅ / "Magnesio" ❌
3. **Precio siempre en Quetzales**: "Q299" ✅ / "$39" ❌
4. **Contexto guatemalteco**: Mencionar tráfico, Roosevelt, zonas, café ✅ / Referencias genéricas ❌
5. **Cada producto tiene su Palabra Mental**: Definida en `01_research_positioning.md`

## Consistency Checks

### Cross-Product Audit
```
Para cada producto, verificar:
1. ¿El nombre de marca es "TINITA HEALTH" (no variantes)?
2. ¿Los precios están en Quetzales?
3. ¿El tono es consistente con el piloto de Magnesio?
4. ¿El presentador se llama "Marco Villagrán" en todos los videos?
5. ¿Los colores de las slides siguen la paleta?
6. ¿No hay promesas médicas prohibidas?
```

### Avatar Naming Rules
- Cada producto PUEDE tener un avatar diferente (Andrés para Magnesio, María para Berberina)
- Pero DENTRO de un producto, el avatar debe ser el mismo en los 5 archivos
- El avatar nunca debe llamarse igual que el presentador (Marco ≠ Andrés)

### Forbidden Phrases
```
❌ "Cura definitiva para..."
❌ "Garantizado que elimina..."
❌ "Aprobado por la FDA"
❌ "Reemplaza tu medicamento"
❌ "Dr. Marco Villagrán"
❌ "Resultados garantizados"
```

### Required Disclaimers
Cada pieza de contenido público debe incluir al final:
```
"Este producto es un suplemento alimenticio y no sustituye una dieta equilibrada
ni el consejo médico profesional. Consultá a tu médico antes de iniciar
cualquier suplementación."
```

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Brand consistency is a guideline, not a legal review. Consult legal for medical claims.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
