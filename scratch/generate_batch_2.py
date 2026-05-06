import os

supplements = [
    {
        "name": "B12 sublingual 500mcg",
        "folder": "B12_sublingual_500mcg",
        "price": "Q169",
        "scientific": "Metilcobalamina (B12 activa) en formato sublingual para absorción directa a través de la mucosa bucal, evitando la degradación gástrica.",
        "benefits": ["Aumento inmediato de energía y reducción de fatiga.", "Salud del sistema nervioso y glóbulos rojos.", "Ideal para dietas vegetarianas o con baja absorción intestinal."],
        "hooks": [
            "¿Fatiga constante? Tu cuerpo podría no estar absorbiendo la B12. Prueba la vía sublingual.",
            "Energía que entra directo a tu sistema. Q169."
        ]
    },
    {
        "name": "B12 1000mcg",
        "folder": "B12_1000mcg",
        "price": "Q199",
        "scientific": "Dosis de alta potencia de Cianocobalamina/Metilcobalamina para corrección rápida de deficiencias severas.",
        "benefits": ["Protección cognitiva y prevención de anemia.", "Mantenimiento de la vaina de mielina en neuronas.", "Apoyo al metabolismo de homocisteína."],
        "hooks": [
            "Potencia máxima para tu cerebro y energía. B12 1000mcg Q199.",
            "Recupera tu claridad mental y vitalidad hoy mismo."
        ]
    },
    {
        "name": "Citrato de Magnesio 200mg",
        "folder": "Citrato_de_Magnesio_200mg",
        "price": "Q199",
        "scientific": "Magnesio quelado con ácido cítrico, la forma más popular y equilibrada para absorción y efectos sistémicos.",
        "benefits": ["Relajación muscular y alivio de calambres.", "Mejora del tránsito intestinal.", "Regulación de la presión arterial."],
        "hooks": [
            "El mineral milagroso para el estrés de la ciudad. Citrato de Magnesio Q199.",
            "Duerme mejor, vive más tranquilo. Calidad garantizada."
        ]
    },
    {
        "name": "Citrato de Magnesio 100mg",
        "folder": "Citrato_de_Magnesio_100mg",
        "price": "Q159",
        "scientific": "Dosis moderada para mantenimiento diario o para estómagos sensibles.",
        "benefits": ["Dosis ajustable para niños y adultos mayores.", "Apoyo óseo básico.", "Relajación suave nocturna."],
        "hooks": [
            "La dosis ideal para empezar tu camino al bienestar. Citrato de Magnesio 100mg.",
            "Bienestar accesible para toda la familia por Q159."
        ]
    },
    {
        "name": "Magnesio Complex",
        "folder": "Magnesio_Complex",
        "price": "Q299",
        "scientific": "Mezcla sinérgica de Citrato, Malato y Glicinato para cubrir todas las necesidades del cuerpo en un solo producto.",
        "benefits": ["Energía muscular + Enfoque mental + Salud ósea.", "Máxima biodisponibilidad multiforma.", "Efecto prolongado durante el día."],
        "hooks": [
            "¿Por qué elegir un magnesio si puedes tenerlos todos? Magnesio Complex Q299.",
            "El Rolls-Royce de los magnesios ya está en Guatemala."
        ]
    },
    {
        "name": "Omega 3",
        "folder": "Omega_3",
        "price": "Q239",
        "scientific": "Ácidos grasos esenciales EPA y DHA extraídos de peces de aguas profundas, destilados molecularmente para pureza total.",
        "benefits": ["Reducción de inflamación sistémica.", "Salud cardiovascular y control de triglicéridos.", "Desarrollo y mantenimiento cerebral."],
        "hooks": [
            "Protege tu corazón y enciende tu cerebro. Omega 3 de alta pureza Q239.",
            "El antiinflamatorio natural que tu cuerpo necesita."
        ]
    },
    {
        "name": "Tongkat Ali",
        "folder": "Tongkat_Ali",
        "price": "Q429",
        "scientific": "Eurycoma longifolia, conocida por su capacidad para optimizar los niveles de testosterona libre y reducir el cortisol.",
        "benefits": ["Aumento de vitalidad y libido masculina.", "Mejora de la fuerza y masa muscular.", "Reducción del estrés crónico."],
        "hooks": [
            "Recupera tu vitalidad masculina. El poder del Tongkat Ali en Guatemala.",
            "Más fuerza, más energía, más control. Calidad premium Q429."
        ]
    },
    {
        "name": "Vitamina B6",
        "folder": "B6",
        "price": "Q199",
        "scientific": "Piridoxina, cofactor esencial para la síntesis de neurotransmisores como serotonina y dopamina.",
        "benefits": ["Regulación del estado de ánimo y ciclo del sueño.", "Reducción de síntomas del síndrome premenstrual.", "Apoyo al metabolismo de proteínas."],
        "hooks": [
            "Equilibra tu humor y tus hormonas de forma natural. Vitamina B6 Q199.",
            "El apoyo que tu sistema nervioso central estaba pidiendo."
        ]
    },
    {
        "name": "L-Arginina 1000mg",
        "folder": "L-Arginina_1000mg",
        "price": "Q219",
        "scientific": "Precursor del óxido nítrico, un potente vasodilatador que mejora el flujo sanguíneo.",
        "benefits": ["Mejor oxigenación muscular en el entreno.", "Apoyo a la salud eréctil y vascular.", "Recuperación de tejidos."],
        "hooks": [
            "Potencia tu circulación y tu rendimiento. L-Arginina de alta dosis Q219.",
            "Flujo sanguíneo optimizado para una salud total."
        ]
    },
    {
        "name": "Berberina",
        "folder": "Berberina",
        "price": "Q209",
        "scientific": "Alcaloide natural que activa la enzima AMPK, conocida como el 'interruptor metabólico' del cuerpo.",
        "benefits": ["Control de azúcar en sangre (nivel similar a metformina).", "Pérdida de grasa y mejora metabólica.", "Salud cardiovascular y digestiva."],
        "hooks": [
            "La 'Ozempic natural' para controlar tu azúcar y peso. Berberina Q209.",
            "Optimiza tu metabolismo y recupera tu figura."
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
