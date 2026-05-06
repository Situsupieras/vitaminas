import os

supplements = [
    {
        "name": "Clorofila",
        "folder": "Clorofila",
        "price": "Q229",
        "scientific": "La clorofila es el pigmento verde de las plantas, conocido como la 'sangre vegetal'. Su estructura es casi idéntica a la hemoglobina humana, sustituyendo el hierro por magnesio.",
        "benefits": ["Desintoxicación profunda del hígado y sangre.", "Oxigenación celular y aumento de energía.", "Desodorizante natural interno."],
        "hooks": [
            "¿Te sientes pesado después de un almuerzo en la calle? La Clorofila es tu detox natural.",
            "Limpia tu cuerpo desde adentro. Menos toxinas, más energía. Clorofila Q229."
        ]
    },
    {
        "name": "Vegetales en cápsula",
        "folder": "Vegetales_en_capsula",
        "price": "Q149",
        "scientific": "Concentrado fitonutriente de vegetales de hoja verde y crucíferas, procesados a bajas temperaturas para preservar enzimas y antioxidantes.",
        "benefits": ["Aporte masivo de micronutrientes en una toma.", "Apoyo al sistema inmunológico.", "Alcalinización del cuerpo."],
        "hooks": [
            "¿No tienes tiempo de cocinar vegetales? Aquí tienes el poder de una ensalada gigante en una cápsula.",
            "Nutrición real para gente con prisa en Guate. Q149."
        ]
    },
    {
        "name": "L Theanina",
        "folder": "L_Theanina",
        "price": "Q219",
        "scientific": "Aminoácido encontrado en el té verde que promueve la relajación sin causar somnolencia. Aumenta las ondas alfa en el cerebro.",
        "benefits": ["Reducción de ansiedad aguda.", "Enfoque mental 'calmado' (ideal para el trabajo).", "Mejora la calidad del sueño."],
        "hooks": [
            "Elimina el 'temblor' del café. L-Teanina: Enfoque puro sin ansiedad.",
            "Paz mental en medio del tráfico. Relajación consciente por Q219."
        ]
    },
    {
        "name": "Malato de Magnesio",
        "folder": "Malato_de_Magnesio",
        "price": "Q239",
        "scientific": "Combinación de magnesio con ácido málico, un componente clave del ciclo de Krebs (energía celular).",
        "benefits": ["Ideal para fatiga crónica y fibromialgia.", "Apoyo directo a la producción de ATP (energía).", "Menos laxante que otras formas de magnesio."],
        "hooks": [
            "¿Te despiertas cansado a pesar de dormir? Te falta Malato de Magnesio.",
            "Energía real, no estimulante. Vive tu día al 100%."
        ]
    },
    {
        "name": "L Carnitina",
        "folder": "L_Carnitina",
        "price": "Q239",
        "scientific": "Transportador de ácidos grasos hacia la mitocondria para ser quemados como energía.",
        "benefits": ["Acelera la quema de grasa durante el ejercicio.", "Mejora el rendimiento atlético.", "Protección cardiovascular."],
        "hooks": [
            "Convierte tu grasa en combustible. Dale poder a tu entreno.",
            "Más energía, menos grasa. El secreto de los atletas en Guate."
        ]
    },
    {
        "name": "Coenzima CoQ10",
        "folder": "Coenzima_CoQ10",
        "price": "Q199",
        "scientific": "Antioxidante liposoluble vital para la producción de energía en el corazón y órganos con alta demanda metabólica.",
        "benefits": ["Salud cardiovascular y presión arterial.", "Antienvejecimiento celular.", "Recuperación post-ejercicio."],
        "hooks": [
            "Dale un respiro a tu corazón. CoQ10: Energía vital para tus órganos.",
            "El antioxidante maestro para tu salud cardíaca. Q199."
        ]
    },
    {
        "name": "Rhodiola",
        "folder": "Rhodiola",
        "price": "Q249",
        "scientific": "Adaptógeno potente que ayuda al cuerpo a resistir el estrés físico, químico y ambiental.",
        "benefits": ["Resistencia al estrés mental y agotamiento.", "Mejora el estado de ánimo.", "Aumenta la estamina física."],
        "hooks": [
            "El escudo contra el Burnout. Rhodiola: Tu adaptógeno para días pesados.",
            "No dejes que el estrés te gane. Control total por Q249."
        ]
    },
    {
        "name": "Colágeno Hidrolizado",
        "folder": "Colageno_Hydrolizado",
        "price": "Q329",
        "scientific": "Proteína estructural principal del cuerpo, procesada para máxima absorción por los tejidos conectivos.",
        "benefits": ["Salud de articulaciones y tendones.", "Elasticidad de la piel y reducción de arrugas.", "Fortalecimiento de cabello y uñas."],
        "hooks": [
            "Belleza y salud que nace desde adentro. Colágeno puro Q329.",
            "Tus rodillas y tu piel te lo agradecerán. Calidad premium."
        ]
    },
    {
        "name": "Probiótico",
        "folder": "Probiotico",
        "price": "Q279",
        "scientific": "Cepas bacterianas beneficiosas que restauran el microbioma intestinal y el sistema inmunológico.",
        "benefits": ["Digestión perfecta y fin del estreñimiento/inflamación.", "80% de tu inmunidad nace en el intestino.", "Mejora el estado de ánimo (eje intestino-cerebro)."],
        "hooks": [
            "Tu segundo cerebro está en tu intestino. Cuídalo con probióticos reales.",
            "Adiós a la inflamación después de comer. Salud digestiva total."
        ]
    },
    {
        "name": "Nutra Visión",
        "folder": "Nutra_Vision",
        "price": "Q199",
        "scientific": "Complejo de luteína, zeaxantina y antioxidantes específicos para la protección de la mácula y retina.",
        "benefits": ["Protección contra la luz azul de pantallas.", "Prevención de degeneración macular.", "Mejora la agudeza visual nocturna."],
        "hooks": [
            "¿Pasas todo el día frente a la compu? Protege tus ojos de la luz azul.",
            "Mira el mundo con claridad. Nutrición específica para tu visión."
        ]
    }
]

template = """# Plan de Contenido de 7 Horas: {name} ({price})

## 🧬 Perfil Científico (Basado en Evidencia)
{scientific}

### Beneficios Clave:
{benefits_list}

---

## 🕒 Hoja de Ruta: "7 Horas de Valor Educativo"

### Hora 1: Fundamentos y Biología (Masterclass)
- **Concepto**: Explicar por qué el cuerpo necesita {name}.
- **Temas**: Mecanismo de acción, señales de deficiencia y absorción.

### Hora 2: Contexto Local y Estilo de Vida en Guatemala
- **Concepto**: Cómo {name} soluciona problemas específicos de la audiencia local.
- **Temas**: Estrés urbano, dieta guatemalteca (exceso de carbohidratos/grasas), clima y energía.

### Hora 3: Mitos, Mentiras y Seguridad
- **Concepto**: Desmitificar información falsa y dar seguridad al comprador.
- **Temas**: Contraindicaciones, dosis seguras, por qué nuestra calidad es superior.

### Hora 4: Sinergias y Biohacking (Combinaciones)
- **Concepto**: Cómo potenciar el efecto combinándolo con otros productos.
- **Temas**: {name} + Magnesio, {name} + Omega 3, etc.

### Hora 5: Guía Práctica de Uso
- **Concepto**: Cuándo y cómo tomarlo para máxima eficacia.
- **Temas**: Ayunas vs con comida, mañana vs noche, ciclos de descanso.

### Hora 6: Testimonios y Casos de Uso Reales
- **Concepto**: Prueba social aplicada al contexto local.
- **Temas**: Historias de éxito de profesionales, madres y atletas.

### Hora 7: Q&A y Taller de Selección de Suplementos
- **Concepto**: Resolución de dudas frecuentes.
- **Temas**: Respuestas a las 10 preguntas más comunes de redes sociales.

---

## 🪝 Marketing Hooks (Alta Conversión)
{hooks_list}

---

## 📂 Recursos y Referencias
- [Investigación en PubMed relacionada](https://pubmed.ncbi.nlm.nih.gov/)
- [Guía de dosificación clínica sugerida]
"""

for s in supplements:
    benefits_str = "\n".join([f"- {b}" for b in s["benefits"]])
    hooks_str = "\n".join([f"{i+1}. \"{h}\"" for i, h in enumerate(s["hooks"])])
    content = template.format(
        name=s["name"],
        price=s["price"],
        scientific=s["scientific"],
        benefits_list=benefits_str,
        hooks_list=hooks_str
    )
    
    path = os.path.join("c:\\proyectos\\vitaminas", s["folder"], "marketing_plan.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {path}")
