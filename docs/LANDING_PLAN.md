# Plan de Ejecución: Landing Page "Es Vitamina" v2

## Contexto

Reescribir `landing_esvitamina/index.html` completamente. La v1 es un catálogo genérico que no vende. La v2 debe aplicar los frameworks de marketing de los skills en `.agents/skills/`.

## Archivos de Referencia (LEER ANTES DE EMPEZAR)

1. `brand_esvitamina.md` — Identidad de marca, colores, tono, datos de contacto
2. `.agents/skills/copywriting-master/SKILL.md` — Schwartz, Collier, Masterson
3. `.agents/skills/pattern-disruptor/SKILL.md` — Brendan Kane (Hook Point)
4. `.agents/skills/movement-creator/SKILL.md` — Brunson (Epiphany Bridge), Hoffer
5. `.agents/skills/persuasion-architect/SKILL.md` — Blair Warren, Ariely
6. `.agents/skills/funnel-architect/SKILL.md` — Brunson (Escalera de Valor)
7. `.agents/skills/positioning-strategist/SKILL.md` — April Dunford

## Requisitos Técnicos Globales

- Output: UN solo archivo `landing_esvitamina/index.html`
- CSS en `<style>`, JS en `<script>`, todo inline
- Fonts: Plus Jakarta Sans (600,700,800) + Inter (400,500,600) + Lora (italic 500) via Google Fonts CDN
- Colores: usar EXACTAMENTE los CSS custom properties de `brand_esvitamina.md` sección 2
- Íconos: SVG inline, NO FontAwesome ni librerías externas
- NO Bootstrap, NO jQuery, NO Tailwind — vanilla CSS + JS
- Mobile-first responsive: 375px → 768px → 1024px → 1200px
- IntersectionObserver para animaciones fade-in al scroll
- scroll-behavior: smooth
- HTML semántico (header, main, section, footer)
- Meta SEO + Open Graph completo
- Datos de contacto: ver sección 9 de brand_esvitamina.md

---

## FASE 1: Estructura del DOM (Secciones en orden)

Crear las 12 secciones en este orden exacto. Cada sección tiene un framework de autor asignado.

### Sección 1: Navbar sticky
- Logo "Es Vitamina" a la izquierda (texto, no imagen)
- Links internos: El Problema | Cómo Funciona | Productos | Contacto
- Botón WhatsApp pequeño a la derecha
- Transparente en top, fondo sólido `--brand-deep` al hacer scroll (JS: IntersectionObserver o scroll event)

### Sección 2: Hero — HOOK (Framework: Brendan Kane, Hook Point)
- **Principio**: Los primeros 3 segundos deciden si se quedan o se van. El headline debe invertir un mito.
- Layout: 2 columnas en desktop (texto izq, visual der). 1 columna mobile.
- Pill badge arriba: "🇬🇹 Guatemala · Suplementos Premium"
- **Headline**: "¿Y si tu cansancio no es por falta de sueño?" (pregunta polarizante que invierte el mito)
- **Sub-headline**: "7 de cada 10 guatemaltecos tienen al menos una deficiencia nutricional. Tu cuerpo te manda señales. Es hora de escucharlo."
- CTA dorado: "Descubrí qué necesitás →" (ancla a la sección quiz)
- CTA WhatsApp verde: "Hablá con un asesor gratis"
- Columna derecha: SVG ilustrativo grande (frasco de suplementos estilizado con partículas/círculos animados en CSS puro representando nutrientes)
- Contador animado abajo: "2,847+ personas ya confían en Es Vitamina" (números que suben de 0 al cargar)
- Fondo: gradiente `--bg-hero` a `--brand-deep` con formas radiales sutiles

### Sección 3: Trust Bar
- Fondo `--bg-light`
- 4 items en fila: Envío a domicilio | 80+ productos | Asesoría gratuita | Garantía 30 días
- Cada uno con ícono SVG verde `--brand-primary` + texto corto

### Sección 4: El Pre-Frame (Framework: Brafman, Sway)
- **Principio**: Alterar la percepción ANTES de mostrar la oferta.
- Fondo blanco
- Título: "Lo que nadie te dice sobre tu alimentación"
- Dato impactante grande (tipografía gigante animada): "La comida de hoy tiene 40% menos nutrientes que hace 30 años"
- Subtexto: "Por eso te sentís cansado, dormís mal y te enfermás seguido. No es tu culpa."
- 3 cards de síntomas con checkboxes interactivos (JS):
  - ☐ "Me siento cansado/a todo el día"
  - ☐ "No duermo bien o me despierto sin energía"
  - ☐ "Me enfermo con frecuencia"
- Cuando el usuario marca alguno, aparece un mensaje con fade-in: "Tu cuerpo te está pidiendo algo. Seguí leyendo para descubrir qué." + flecha animada hacia abajo

### Sección 5: Epiphany Bridge (Framework: Russell Brunson, Expert Secrets)
- **Principio**: La gente compra con emoción, justifica con lógica. Contar una historia de descubrimiento.
- Fondo `--bg-warm` (#FFF8F0)
- Estructura de la historia en 4 bloques visuales conectados por una línea SVG vertical:
  1. **El Deseo**: "Queríamos sentirnos bien. Tener energía, dormir profundo, no enfermarnos."
  2. **El Muro**: "Probamos de todo: más ejercicio, más café, remedios caseros. Nada funcionaba realmente."
  3. **La Epifanía**: "Hasta que entendimos algo simple: nuestro cuerpo no estaba fallando — le FALTABA algo. Nutrientes que la comida moderna ya no da."
  4. **El Resultado**: "Cuando empezamos a suplementar con las dosis correctas, todo cambió. Energía real, sueño profundo, menos enfermedades."
- Cierre en bold: "Por eso creamos Es Vitamina. Para que vos no tengás que adivinar."
- Analogía Anti-Technobabble: incluir una frase tipo "Es como recargar la batería de tu celular — si la batería está al 10%, no importa cuántas apps cerrés. Necesitás conectarlo a la corriente."

### Sección 6: La Nueva Oportunidad + Cómo Funciona (Framework: Brunson, Expert Secrets)
- **Principio**: No vender una mejora, vender un NUEVO vehículo. No vendemos vitaminas, vendemos un sistema de bienestar personalizado.
- Fondo blanco
- Título: "No vendemos vitaminas. Te damos un nutricionista de bolsillo."
- Subtítulo: "La diferencia entre comprar suplementos al azar y tener a alguien que analiza tus síntomas y te recomienda exactamente lo que necesitás."
- 3 pasos horizontales (iconos circulares con números conectados por línea):
  1. "Escribinos" — ícono WhatsApp — "Contanos cómo te sentís y qué querés mejorar"
  2. "Te asesoramos gratis" — ícono chat — "Un experto analiza tu caso y te recomienda los suplementos exactos"
  3. "Recibí en tu puerta" — ícono caja — "Te lo enviamos a cualquier punto de Guatemala"
- CTA: "Empezar ahora → WhatsApp"

### Sección 7: Posicionamiento (Framework: April Dunford, Obviously Awesome)
- **Principio**: Mostrar las alternativas reales y por qué Es Vitamina gana.
- Fondo `--bg-light`
- Título: "Compará vos mismo"
- Tabla comparativa visual (3 columnas):
  - Columna 1: "Farmacia genérica" — ✗ Sin asesoría, ✗ Marcas desconocidas, ✗ Precios inflados, ✗ Solo lo que hay en stock
  - Columna 2: "Importar de Amazon" — ✗ Tarda semanas, ✗ Impuestos sorpresa, ✗ No hay asesoría, ✗ Riesgo de que no llegue
  - Columna 3 (destacada con borde dorado): "Es Vitamina" — ✓ Asesoría gratuita, ✓ 80+ productos certificados, ✓ Envío en días, ✓ Precios directos desde Q89
- Debajo: La Palabra Mental (Ries & Trout): "Tu nutricionista de confianza" en tipografía grande

### Sección 8: Categorías por PROBLEMA (Framework: Eugene Schwartz, 5 niveles de conciencia)
- **Principio**: Hablarle al nivel 2 (Problem Aware). La gente busca por PROBLEMA, no por ingrediente. Cada card arranca con el dolor que siente, no con el nombre del producto.
- Fondo blanco
- Título: "¿Qué querés mejorar?"
- Grid responsive de cards. Cada card tiene:
  - Emoji grande
  - Pregunta del problema: "¿Te sentís sin energía?" (no: "Categoría Energía")
  - Texto breve de cómo los suplementos ayudan
  - 3 productos tag (chips): ej. "B12 · CoQ10 · Ginseng"
  - CTA: "Ver soluciones →" apuntando a https://tiendasts.com/vitaminas
- Las 6 categorías principales (las más buscadas primero):
  1. 🧠 "¿Te sentís sin energía?" — B12, CoQ10, Complejo B, Ginseng
  2. 😴 "¿No podés dormir bien?" — Magnesio, Melatonina, Ashwagandha, GABA
  3. 🛡️ "¿Te enfermás seguido?" — Vitamina C, Zinc, Probiótico, Echinacea
  4. ✨ "¿Tu piel o cabello se ven opacos?" — Biotina, Colágeno, Vitamina E
  5. 💪 "¿Te duelen las articulaciones?" — Glucosamina, D3+K2, Colágeno
  6. ❤️ "¿Querés cuidar tu corazón?" — Omega 3, Berberina, CoQ10
- Botón debajo: "Ver las 80+ opciones →" a la tienda
- Card aparte o desplegable con las 5 categorías restantes (Hormonal, Digestión, Visión, Metabólico, Multivitamínicos)

### Sección 9: Mini-Quiz Interactivo (Framework: Brunson, Fórmula Secreta — Cebo)
- **Principio**: El "Cebo" de Brunson. Dar valor GRATIS para captar interés. Un quiz es el lead magnet perfecto.
- Fondo `--bg-warm`
- Título: "¿Qué suplemento necesitás? Descubrilo en 30 segundos"
- Quiz de 3 pasos (JS vanilla, sin dependencias):
  - Paso 1: "¿Cuál es tu edad?" → botones: 18-30 | 31-45 | 46-60 | 60+
  - Paso 2: "¿Qué te preocupa más?" → botones: Energía | Sueño | Inmunidad | Belleza | Articulaciones | Digestión
  - Paso 3: "¿Qué tan urgente lo sentís?" → botones: Leve | Moderado | Necesito ayuda ya
- Al completar: mostrar recomendación personalizada (lógica simple en JS) con:
  - "Tu recomendación: [Producto]" con descripción corta
  - CTA WhatsApp con mensaje pre-armado: "Hola! Hice el quiz y me recomendó [Producto]. Quiero más info."
- Progress bar visual arriba del quiz (paso 1/3, 2/3, 3/3)

### Sección 10: Persuasión (Framework: Blair Warren 5 fuerzas + Dan Ariely pricing)
- **Principio**: Las 5 fuerzas que persuaden a cualquier persona (Warren) + el efecto irracional de "gratis" (Ariely).
- Fondo `--brand-deep` (oscuro)
- Título blanco: "Hacé la cuenta vos mismo"
- Price anchoring (3 cards en fila):
  - Card 1: "💊 Nutricionista" — Q400-Q600/consulta — tachado, opaco
  - Card 2: "🏪 Farmacia" — Q180-Q350/producto — tachado, opaco
  - Card 3 (destacada, borde dorado, escala 1.05): "✓ Es Vitamina" — Desde Q89 + Asesoría GRATIS — color dorado brillante, badge "Tu mejor opción"
- Debajo, las 5 fuerzas de Warren como lista con íconos numerados:
  1. "Imaginate despertar con energía natural, sin alarma, sin café" (animar sueños)
  2. "No es tu culpa. La comida ya no trae lo que tu cuerpo necesita" (justificar fracasos)
  3. "Si no sentís diferencia en 30 días, te devolvemos tu dinero" (disipar miedos)
  4. "Sí, las farmacias cobran de más. Eso se acaba acá." (confirmar sospechas)
  5. "La industria cuenta con que no leas etiquetas. Nosotros contamos con que SÍ las leas." (enemigo común)

### Sección 11: Testimonios (Framework: mini Epiphany Bridge por testimonio)
- **Principio**: Cada testimonio debe contar una mini-historia de transformación, no solo "buen producto".
- Fondo `--bg-warm`
- 3 cards con:
  - ★★★★★ estrellas doradas
  - Cita en Lora italic siguiendo estructura: "Antes [problema]. Probé [alternativa]. Con Es Vitamina [resultado específico]."
  - Inicial en círculo de color + nombre + ciudad guatemalteca + producto que usa
  - Testimonio 1: Energía (B12) — mujer, Ciudad de Guatemala
  - Testimonio 2: Sueño (Magnesio) — hombre, Quetzaltenango
  - Testimonio 3: Inmunidad (Vitamina C + Zinc) — mujer, Antigua Guatemala
- Disclaimer italic: "Experiencias ilustrativas. Los resultados pueden variar."

### Sección 12: CTA Final — Tierra Prometida (Framework: Eric Hoffer, The True Believer)
- **Principio**: Cerrar con la visión esperanzadora del futuro que une a la comunidad.
- Fondo: gradiente `--brand-primary` a `--brand-deep`
- Título grande blanco: "Sentirse bien no debería ser un lujo"
- Subtítulo: "Un Guatemala donde cada persona sabe qué necesita su cuerpo y tiene acceso fácil a ello."
- CTA gigante dorado con pulse: "Empezá tu camino al bienestar" → WhatsApp
- CTA secundario outline: "Ver catálogo completo" → tienda
- Email visible: situsupierasnutricion@gmail.com

### Footer
- Fondo `--brand-deep`
- Logo "Es Vitamina" + tagline breve
- Links: Catálogo | WhatsApp | Email
- Disclaimer legal EXACTO de la sección 10 de brand_esvitamina.md
- "© 2026 Es Vitamina. Todos los derechos reservados."

### Elemento Flotante: WhatsApp
- Botón redondo verde fijo abajo-derecha
- SVG de WhatsApp blanco
- Pulse animation CSS
- Link a: https://wa.me/50230139416?text=Hola!%20Quiero%20asesoría%20sobre%20suplementos

---

## FASE 2: CSS (diseño premium, no genérico)

- Usar TODOS los custom properties del brand bible
- Hero con SVG decorativo animado (partículas/círculos flotantes en CSS puro con @keyframes)
- Cards con micro-interacciones: hover scale + shadow + border-color
- Transiciones suaves en todo (0.3s ease)
- Contadores animados (JS IntersectionObserver + requestAnimationFrame)
- Quiz con transiciones CSS entre pasos (opacity + transform)
- Checkboxes del pre-frame con estado activo visual
- Tabla comparativa con la columna de Es Vitamina visualmente ganadora
- Navbar transition de transparente a sólida

## FASE 3: JavaScript (interactividad)

- IntersectionObserver para fade-in de secciones
- Navbar: cambio de estilo al scroll
- Contadores animados (de 0 a 2847)
- Checkboxes del pre-frame: mostrar mensaje al marcar
- Quiz: lógica de 3 pasos con recomendación
- Smooth scroll para links internos del navbar

---

## FASE 4: Automatización y Cebo (Lead Magnet)

- **Objetivo**: Capturar datos de contacto (Nombre/WhatsApp) antes de entregar el valor.
- **Implementación**:
  1. **Gate en el Quiz**: El usuario completa el quiz y, antes del resultado, aparece un formulario de 2 campos.
  2. **Promesa**: Recibir el resultado personalizado + la "Guía de Síntomas Es Vitamina" (PDF).
  3. **Generación de PDF**: Crear `assets/guia-sintomas-esvitamina.html` optimizado para impresión (A4). El administrador lo guarda como PDF y lo envía manualmente por WhatsApp.
  4. **Llamado a la Acción**: El botón del resultado abre WhatsApp con un mensaje pre-armado pidiendo la guía.
