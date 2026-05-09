---
name: landing-page
description: "Construye landing pages de alta conversión para productos de suplementos TINITA HEALTH. Aplica los frameworks de Russell Brunson (VSL), Gary Bencivenga (Big Idea), y Eugene Schwartz (5 niveles de conciencia). Genera HTML/CSS/JS estático listo para producción."
---

# Landing Page Builder — TINITA HEALTH

## Contexto del Sistema

Cada landing page de TINITA HEALTH:
- Vende **un solo producto** (no distraerse con el catálogo)
- Habla al **avatar específico** definido en `01_research_positioning.md`
- Usa el **hook principal** de `03_story_hooks.md`
- Incluye el **copy de conversión** de `04_copy_assets.md`
- Sigue el **posicionamiento** de `01_research_positioning.md`

## Proceso (Rígido — Seguir Exactamente)

### Fase 1: Recopilar Contexto del Producto

Antes de escribir UNA línea de HTML, lee estos archivos del producto (si existen):

```
<producto>/n8n_output/01_research_positioning.md  → Avatar + posicionamiento
<producto>/n8n_output/03_story_hooks.md            → Hooks + historia de epifanía
<producto>/n8n_output/04_copy_assets.md            → Headlines + bullets + CTAs
<producto>/n8n_output/02_funnel_persuasion.md      → Oferta + precio + garantía
```

Si los archivos no existen, solicita al usuario los datos mínimos:
- Nombre del producto y precio
- Beneficio principal (en 1 oración)
- Para quién es (avatar básico)
- Problema que resuelve

### Fase 2: Elegir la Estructura Según Nivel de Conciencia

Basado en Eugene Schwartz:

| Nivel | Descripción | Estructura de LP |
|-------|-------------|-----------------|
| 1 - Inconsciente | No sabe que tiene el problema | VSL largo > educación > oferta |
| 2 - Consciente del problema | Sabe el problema, no la solución | Big Idea > historia > solución |
| 3 - Consciente solución | Busca soluciones, no tu marca | Comparación > beneficios > prueba |
| 4 - Consciente del producto | Conoce tu producto | Features > precio > urgencia |
| 5 - Más consciente | Listo para comprar | Oferta directa > bonuses > CTA |

**Default para suplementos TINITA**: Nivel 2-3. Estructura:
1. Hook / Headline principal
2. Identificación del problema (agitación)
3. Historia de epifanía / Solución revelada
4. El producto como vehículo
5. Ingredientes + mecanismo único
6. Testimonios / Prueba social
7. Oferta + precio + garantía
8. CTA principal + urgencia
9. FAQ (eliminar objeciones)
10. CTA final

### Fase 3: Diseño y Colores

**Paleta TINITA HEALTH**:
```css
--color-primary: #1B4F72;      /* Azul marino confiable */
--color-accent: #2ECC71;       /* Verde salud */
--color-warm: #F39C12;         /* Naranja urgencia/CTA */
--color-dark: #1A1A2E;         /* Fondo oscuro hero */
--color-text: #2C3E50;         /* Texto principal */
--color-light: #F8F9FA;        /* Fondos claros */
```

**Tipografía** (Google Fonts):
- Headlines: `Montserrat` (700, 800)
- Body: `Open Sans` (400, 600)
- Accent/testimonios: `Lora` italic

**Estilo Visual**:
- Hero oscuro con gradiente (credibilidad + profesionalismo)
- Secciones alternas claro/oscuro
- Cards con sombra suave y bordes redondeados
- Íconos SVG inline (no depender de librerías externas)
- Imágenes del producto en mockup elegante

### Fase 4: Estructura del Archivo

Genera un **único archivo HTML** auto-contenido:

```
<producto>/landing/index.html
```

Incluye TODO inline:
- CSS en `<style>` (no archivos externos excepto Google Fonts)
- JS en `<script>` al final del body
- SVG íconos inline
- Fuentes desde Google Fonts CDN

### Fase 5: Elementos Obligatorios

#### Hero Section
```html
<!-- OBLIGATORIO en hero: -->
- Headline principal (el hook más fuerte)
- Subheadline (amplifica la promesa)
- Imagen del producto (prominente, alta calidad)
- CTA principal visible sin scroll
- Social proof rápido (ej: "★★★★★ 2,847 clientes satisfechos")
```

#### Sección de Problema
```html
<!-- Agitación — usar lenguaje del avatar -->
- Lista de síntomas/dolores que SÍ reconoce
- "¿Te identificas con esto?" (espejo)
- Consecuencias de NO actuar
```

#### Sección de Solución
```html
<!-- Revelación + mecanismo único -->
- La historia de descubrimiento (Epiphany Bridge)
- Cómo funciona el ingrediente activo
- Por qué TINITA es diferente (posicionamiento)
- Infografía simple del mecanismo
```

#### Ingredientes + Prueba
```html
<!-- Credibilidad científica -->
- Tabla de ingredientes con dosis
- Referencias a estudios (si hay)
- Certifications badges (si aplica)
```

#### Testimonios
```html
<!-- Prueba social — 3 mínimo -->
- Foto + nombre + ciudad
- Resultado específico y medible
- Historia creíble (no exagerada)
```

#### Oferta + CTA
```html
<!-- La decisión final -->
- Precio tachado (si hay descuento)
- Precio actual destacado
- Qué incluye (lista de bonos)
- Garantía (número de días + logo)
- Botón CTA naranja/brillante
- Urgencia real (stock limitado / precio temporal)
- Iconos de pago seguro
```

#### FAQ
```html
<!-- Eliminar las 5 objeciones principales -->
1. ¿Es seguro? / ¿Tiene efectos secundarios?
2. ¿Cuánto tiempo tarda en hacer efecto?
3. ¿Qué pasa si no me funciona? (garantía)
4. ¿Es para mí? (quién sí / quién no)
5. ¿Cómo lo tomo?
```

### Fase 6: Optimizaciones Técnicas

#### SEO Básico
```html
<title>[Producto] | [Beneficio Principal] | TINITA HEALTH</title>
<meta name="description" content="[Hook 160 chars]">
<meta property="og:image" content="[foto producto]">
<!-- Schema.org Product markup -->
```

#### Performance
- Google Fonts con `display=swap`
- Imágenes con lazy loading
- CSS crítico inline (above-the-fold)
- Sin jQuery, sin Bootstrap — vanilla JS

#### Conversión
- Botón flotante sticky en móvil
- Progress indicator en scroll
- Exit-intent popup (opcional)
- WhatsApp button flotante (Guatemala market)

### Fase 7: Animaciones y Micro-interactions

```css
/* Entrada suave de elementos */
.animate-in {
  animation: fadeInUp 0.6s ease forwards;
}

/* Botón CTA — pulso para llamar atención */
.btn-cta {
  animation: pulse 2s infinite;
}

/* Counter animado para social proof */
/* Scroll reveal para testimonios */
```

## Checklist de Completitud

Antes de entregar, verifica:

- [ ] Hero visible en mobile sin scroll (375px width)
- [ ] CTA button color `#F39C12` o más brillante
- [ ] Headline en máximo 10 palabras impactantes
- [ ] Al menos 3 testimonios con foto y nombre
- [ ] Precio claramente visible (no hay que buscar)
- [ ] Garantía mencionada al menos 2 veces
- [ ] FAQ responde las 5 objeciones clave
- [ ] Página carga en < 3s (sin imágenes pesadas externas)
- [ ] WhatsApp button presente (mercado Guatemala)
- [ ] No hay errores de HTML (estructura semántica correcta)

## Estructura de Directorios

```
<producto>/
  landing/
    index.html          # Landing page completa (todo inline)
    assets/             # Solo si hay imágenes del producto
      product-hero.webp
      product-detail.webp
```

## Notas de Estilo para el Mercado Guatemalteco

- Usar precios en **Quetzales (Q)** primero, después USD si aplica
- Mencionar **envío a domicilio en Guatemala** explícitamente
- Números de WhatsApp local para consultas
- Testimonios de clientes guatemaltecos cuando sea posible
- Evitar jerga de otros países (usar "suplemento", no "complemento")

## Limitaciones

- No generar páginas con claims médicos que no estén respaldados
- No inventar testimonios — usar solo los que existen en los archivos del producto
- No usar imágenes de stock de terceros — usar las fotos del producto real o generadas
- Si el precio real no está disponible, dejar `[PRECIO]` como placeholder visible
