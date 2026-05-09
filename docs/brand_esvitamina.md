# ES VITAMINA — Brand Bible

> Documento maestro de identidad de marca. Generado aplicando los frameworks de los 9 agentes de marketing de TINITA HEALTH.
> Última actualización: Mayo 2026

---

## 🧬 1. IDENTIDAD DE MARCA

### Nombre
**Es Vitamina** — un nombre que funciona como declaración. No es una pregunta, es una afirmación: "Lo que necesitás para sentirte bien... es vitamina."

### Tagline
**"Tu cuerpo sabe. Dale lo que pide."**

### Tagline secundario (para ads)
"Más de 80 suplementos premium. Asesoría gratuita. Envío a toda Guatemala."

### Voz de Marca
| Atributo | Cómo suena | Cómo NO suena |
|----------|-----------|---------------|
| Cercana | "Mirá, esto es lo que pasa cuando tu cuerpo no tiene magnesio..." | "La hipomagnesemia causa disfunciones neuromusculares" |
| Confiable | "Cada cápsula tiene exactamente lo que dice la etiqueta" | "¡MILAGROSO! ¡CURA TODO!" |
| Educativa | "Antes de venderte algo, dejame explicarte por qué lo necesitás" | "¡Comprá ya! ¡Oferta!" |
| Empática | "Sabemos lo que se siente no poder dormir bien" | "Si no tomás esto, vas a seguir enfermo" |
| Directa | "Esto funciona. Y si no te funciona, te devolvemos tu dinero" | "Quizás podría ayudar en algunos casos..." |

### Tono por canal
| Canal | Tono | Ejemplo |
|-------|------|---------|
| Landing page | Profesional-cálido, educativo | "Tu cuerpo trabaja las 24 horas por vos. ¿Vos qué hacés por él?" |
| WhatsApp | Amigable, de confianza, como un amigo nutricionista | "Hola! Contame qué síntomas tenés y te sugiero el suplemento ideal 💊" |
| Redes sociales | Disruptivo, sorprendente, educativo | "El 87% de los guatemaltecos tienen deficiencia de Vitamina D. ¿Y vos?" |
| Email | Storytelling, personal, como una carta de un experto | "Te voy a contar algo que descubrí hace 3 años y que cambió mi forma de ver la nutrición..." |

---

## 🎨 2. IDENTIDAD VISUAL

### Paleta de Colores (Psicología aplicada)

```css
:root {
  /* === PRIMARIOS === */
  --brand-deep:        #0A2540;   /* Azul noche — autoridad, ciencia, confianza profunda */
  --brand-primary:     #1A6B4A;   /* Verde bosque — salud natural, vitalidad, vida */
  --brand-accent:      #E8A838;   /* Dorado cálido — premium, energía, calidez humana */

  /* === SECUNDARIOS === */
  --brand-mint:        #3ECFA0;   /* Verde menta — frescura, limpieza, nuevo comienzo */
  --brand-coral:       #FF6B6B;   /* Coral suave — urgencia elegante, CTAs que no gritan */
  --brand-lavender:    #8B7EC8;   /* Lavanda — calma, sueño, bienestar emocional */

  /* === NEUTROS === */
  --bg-hero:           #0D1B2A;   /* Fondo hero — profundo, premium, no genérico */
  --bg-light:          #F7F9FC;   /* Fondo secciones claras — limpio, médico, fresco */
  --bg-warm:           #FFF8F0;   /* Fondo cálido — testimonios, historias, cercanía */
  --text-primary:      #1A1A2E;   /* Texto principal — legible, serio */
  --text-secondary:    #5A6678;   /* Texto secundario — sutil, no compite */
  --text-on-dark:      #E8ECF1;   /* Texto sobre fondos oscuros */
  --border-soft:       #E2E8F0;   /* Bordes sutiles */

  /* === FUNCIONALES === */
  --cta-primary:       #E8A838;   /* Botón principal — dorado que dice "acción" sin gritar */
  --cta-primary-hover: #D4952E;   /* Hover del CTA */
  --cta-whatsapp:      #25D366;   /* WhatsApp verde oficial */
  --success:           #10B981;   /* Confirmaciones */
  --warning:           #F59E0B;   /* Alertas */
  --trust-badge:       #1A6B4A;   /* Badges de confianza */
}
```

### ¿Por qué estos colores?

| Color | Psicología | Uso en la landing |
|-------|-----------|-------------------|
| Azul noche `#0A2540` | Autoridad, ciencia, confianza (como una farmacia premium, no un mercado) | Hero, header, footer |
| Verde bosque `#1A6B4A` | Naturaleza, salud, "esto viene de la tierra" | Badges de confianza, íconos de beneficios, secciones de ingredientes |
| Dorado cálido `#E8A838` | Premium pero accesible, energía, "esto vale oro" | CTAs principales, precios, highlights |
| Verde menta `#3ECFA0` | Frescura, nuevo comienzo, "empezá hoy" | Acentos, checkmarks, indicadores positivos |
| Coral `#FF6B6B` | Urgencia sin agresividad | Precios tachados, stock limitado, timer |
| Lavanda `#8B7EC8` | Calma, sueño, bienestar mental | Categoría de sueño y relajación |

### Tipografía

```css
/* Headlines — impacto + legibilidad */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');

/* Body — claridad + calidez */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

/* Testimonios/citas — humano, personal */
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@1,500&display=swap');
```

| Elemento | Font | Peso | Tamaño |
|----------|------|------|--------|
| H1 (hero) | Plus Jakarta Sans | 800 | 48-56px (mobile: 32-36px) |
| H2 (secciones) | Plus Jakarta Sans | 700 | 36-40px (mobile: 26-28px) |
| H3 (cards) | Plus Jakarta Sans | 600 | 22-24px |
| Body | Inter | 400 | 16-18px |
| Body emphasis | Inter | 600 | 16-18px |
| Citas/testimonios | Lora italic | 500 | 18-20px |
| Labels/badges | Inter | 600 | 12-14px, uppercase, letter-spacing 0.5px |

### Espaciado y Layout

```css
/* Ritmo vertical consistente */
--section-padding: clamp(3rem, 8vh, 6rem);
--container-max: 1200px;
--card-radius: 16px;
--btn-radius: 12px;
--card-shadow: 0 4px 24px rgba(10, 37, 64, 0.08);
--card-shadow-hover: 0 8px 40px rgba(10, 37, 64, 0.15);
```

---

## 🥊 3. POSICIONAMIENTO (April Dunford — Obviously Awesome)

### Alternativas Competitivas Reales
1. **Comprar en farmacias locales** → Marcas desconocidas, sin asesoría, precios inflados
2. **Importar de Amazon/iHerb** → Costoso, tarda semanas, impuestos de importación, riesgo de que no llegue
3. **"No hacer nada"** → Seguir con fatiga, dolores, insomnio, "a ver si se me pasa"

### Atributos Únicos vs Valor

| Atributo (Lo que es) | Valor (Lo que hace por vos) |
|----------------------|---------------------------|
| 80+ productos certificados en un solo lugar | No tenés que buscar en 10 farmacias distintas |
| Asesoría nutricional gratuita por WhatsApp | Alguien que SÍ sabe te dice exactamente qué tomar |
| Envío a domicilio en toda Guatemala | No salís de tu casa, llega a tu puerta |
| Precios directos (sin intermediarios de farmacia) | Pagás menos que en cualquier farmacia del país |
| Fórmulas con dosis reales (no micro-dosis) | Cada cápsula tiene lo que dice. No tirás tu dinero |

### La Palabra Mental (Ries & Trout)
> **"Tu nutricionista de confianza"**
>
> No somos una farmacia. No somos una tienda online más. Somos tu nutricionista personal que te dice exactamente qué tomar, te lo envía a tu casa, y te acompaña en el proceso.

### Declaración de Posicionamiento
> "Para guatemaltecos que están cansados de sentirse cansados, que quieren sentirse bien pero no saben por dónde empezar, **Es Vitamina** ofrece asesoría nutricional personalizada + los suplementos exactos que necesitás, con envío directo a tu puerta. A diferencia de las farmacias o Amazon, acá alguien te escucha, te guía, y te acompaña."

---

## 🚩 4. MOVIMIENTO (Russell Brunson — Expert Secrets + Eric Hoffer)

### Los 3 Pilares del Movimiento

#### El Líder (Personaje Atractivo)
**Arquetipo: El Guía Nutricionista** — No es un doctor frío ni un vendedor agresivo. Es alguien que descubrió que la nutrición celular cambió su vida y ahora quiere compartirlo. Habla como un amigo que sabe de nutrición.

#### La Causa
> **"Liberar a Guatemala de la desinformación nutricional."**
>
> El 70% de los guatemaltecos tiene alguna deficiencia vitamínica y no lo sabe. No porque no les importe su salud, sino porque nadie les ha explicado la conexión entre cómo se sienten y lo que les falta a sus células.

#### La Nueva Oportunidad
No vendemos vitaminas — vendemos **un sistema de bienestar personalizado**. La diferencia entre comprar vitaminas al azar vs tener a alguien que analiza tus síntomas, te recomienda exactamente lo que necesitás, y te da seguimiento.

### El Puente de la Epifanía

1. **El Deseo**: "Quiero dejar de sentirme cansado/a todo el tiempo"
2. **El Muro**: "Ya probé de todo — dormir más, hacer ejercicio, tomar café — y sigo igual"
3. **La Epifanía**: "Descubrí que mi cuerpo no estaba fallando, le FALTABA algo. Un análisis simple mostró que tenía deficiencia de Magnesio y B12. Cuando empecé a suplementar con las dosis correctas, en 2 semanas era otra persona."
4. **El Resultado**: "Ahora duermo profundo, me despierto con energía, y mi mente está clara. No fue magia — fue darle a mi cuerpo lo que necesitaba."

### La Tierra Prometida (Eric Hoffer)
> "Un Guatemala donde cada persona sabe exactamente qué necesita su cuerpo y tiene acceso fácil y económico a ello. Donde 'sentirse bien' no es un lujo, es lo normal."

---

## 🎣 5. HOOKS (Brendan Kane — Hook Point)

### Concepto Contra-intuitivo Central
- **El Mito**: "Las vitaminas son para gente enferma o vieja"
- **La Disrupción**: "Las vitaminas no son para curarte — son para que tu cuerpo haga lo que ya sabe hacer. Si estás cansado, no necesitás más café. Necesitás lo que tu cuerpo te está pidiendo a gritos."

### Los 5 Hooks para la Landing Page
1. **"Tu cuerpo te está mandando señales. ¿Las estás escuchando?"** (Problema → curiosidad)
2. **"El 87% de los guatemaltecos tiene al menos una deficiencia nutricional. ¿Vos sos parte de ese 87%?"** (Estadística → identificación)
3. **"¿Y si tu cansancio no es por falta de sueño?"** (Contra-intuitivo → mente abierta)
4. **"No necesitás 20 suplementos. Necesitás los 2 correctos."** (Simplicidad → alivio)
5. **"Dejá de adivinar. Preguntale a alguien que sí sabe."** (Autoridad → CTA WhatsApp)

---

## 🎭 6. PERSUASIÓN (Blair Warren + Dan Ariely)

### La Fórmula de Blair Warren Aplicada

1. **Animar sus sueños**: "Imaginate despertar sin alarma, con energía natural, y que esa energía te dure todo el día."
2. **Justificar sus fracasos**: "No es tu culpa que estés cansado/a. La comida de hoy ya no tiene los nutrientes que tenía hace 30 años."
3. **Disipar sus miedos**: "Garantía de satisfacción. Si no sentís diferencia en 30 días, te devolvemos tu dinero."
4. **Confirmar sus sospechas**: "Sí, las farmacias cobran de más. Sí, muchas marcas usan dosis ridículamente bajas. Eso se acaba acá."
5. **Arrojar piedras al enemigo**: "La industria de suplementos genéricos cuenta con que vos no leas las etiquetas. Nosotros contamos con que SÍ las leas."

### Anclaje de Precio (Dan Ariely)
- **Ancla**: "Una consulta con nutricionista: Q400-Q600. Un suplemento en farmacia: Q180-Q350."
- **Revelación**: "Con Es Vitamina: asesoría gratuita + suplementos desde Q89. Hacé la cuenta."

### Pre-Frame (Brafman)
Antes de mostrar precio, mostrar: el costo de NO actuar (seguir comprando café, energizantes, doctor tras doctor) vs el costo de un suplemento correcto por día (menos de Q3/día).

---

## 🪜 7. EMBUDO (Russell Brunson — DotCom Secrets)

### Escalera de Valor de Es Vitamina

| Nivel | Oferta | Precio | Objetivo |
|-------|--------|--------|----------|
| 🆓 Gratis | Quiz "¿Qué vitamina necesitás?" + Asesoría WhatsApp | Q0 | Captar contacto |
| 💊 Frontend | 1 producto individual | Q89-Q250 | Primera compra |
| 📦 Middle | Bundle de 3 o suscripción mensual | Q199-Q499 | Aumentar ticket |
| ⭐ Backend | Plan nutricional personalizado + 6 meses de suplementos | Q1,500+ | Máximo valor |

### Tipo de Embudo: Landing → WhatsApp → Venta
1. **Landing page** → Educa, genera confianza, muestra catálogo
2. **CTA WhatsApp** → "¿No sabés qué tomar? Escribinos" → Asesoría personalizada
3. **Link de compra** → Tienda: https://tiendasts.com/vitaminas
4. **Seguimiento** → Email/WhatsApp con tips de uso + recompra

---

## 📐 8. CATEGORÍAS DE PRODUCTO

### Las 11 Categorías con Narrativa de Beneficio

| # | Categoría | Ícono | Narrativa (para la landing) | Productos estrella |
|---|-----------|-------|----------------------------|-------------------|
| 1 | Energía & Rendimiento Mental | 🧠 | "Claridad mental sin café. Energía que dura todo el día." | CoQ10, B12, Complejo B |
| 2 | Sueño & Relajación | 😴 | "Dormí profundo. Despertá renovado/a." | Magnesio, Melatonina, Ashwagandha |
| 3 | Huesos & Articulaciones | 💪 | "Mové tu cuerpo sin dolor. Fortalecé lo que te sostiene." | D3+K2, Colágeno, Glucosamina |
| 4 | Belleza: Piel, Cabello & Uñas | ✨ | "La belleza empieza por dentro." | Biotina, Colágeno, Glutathione |
| 5 | Inmunidad & Defensa | 🛡️ | "Tu escudo invisible contra lo que anda en el ambiente." | Vitamina C, Zinc, Probiótico |
| 6 | Corazón & Circulación | ❤️ | "Cuidá el motor que te mantiene vivo." | Omega 3, Berberina, CoQ10 |
| 7 | Salud Hormonal & Mujer | 🌸 | "Equilibrio natural en cada etapa de tu vida." | Prenatales, Ácido Fólico, DHEA |
| 8 | Digestión & Detox | 🍃 | "Un intestino feliz = un cuerpo feliz." | Probiótico, Enzimas, Cardo Mariano |
| 9 | Visión | 👁️ | "Protegé lo que te conecta con el mundo." | Luteína, Nutra Vision |
| 10 | Control Metabólico | 🎯 | "Equilibrá tu azúcar. Recuperá el control." | Berberina, Picolinato de Cromo |
| 11 | Multivitamínicos | ⭐ | "Todo lo esencial, en una sola cápsula." | Centrum Adultos, Centrum Silver |

---

## 📋 9. DATOS DE CONTACTO Y OPERACIÓN

| Dato | Valor |
|------|-------|
| Marca | Es Vitamina |
| URL Tienda | https://tiendasts.com/vitaminas |
| Email | situsupierasnutricion@gmail.com |
| WhatsApp | +502 3013-9416 |
| Link WhatsApp | https://wa.me/50230139416?text=Hola!%20Quiero%20asesoría%20sobre%20suplementos |
| País | Guatemala 🇬🇹 |
| Moneda | Quetzales (Q) |
| Envío | A domicilio en toda Guatemala |
| Garantía | 30 días de satisfacción |

---

## ⚖️ 10. DISCLAIMER LEGAL

```
Los productos ofrecidos son suplementos alimenticios y no sustituyen una dieta equilibrada ni tratamiento médico. Los resultados pueden variar. Consulte a su médico antes de iniciar cualquier suplementación, especialmente si está embarazada, amamantando, o toma medicamentos. Es Vitamina no hace claims de curar, tratar o prevenir enfermedades.
```

---

## 🚫 REGLAS INQUEBRANTABLES DEL COPY

1. **NUNCA** decir "cura", "trata" o "previene enfermedades" → Usar "apoya", "contribuye a", "puede ayudar a mantener"
2. **NUNCA** inventar testimonios → Solo usar reales o marcar como "ilustrativo"
3. **NUNCA** usar tuteo → Usar "vos" (Guatemala) o formas neutras ("usted" en textos formales)
4. **NUNCA** poner precios en USD sin convertir a Quetzales
5. **SIEMPRE** incluir disclaimer legal en el footer
6. **SIEMPRE** mencionar la asesoría gratuita — es el diferenciador #1
7. **SIEMPRE** incluir WhatsApp como canal principal de contacto
