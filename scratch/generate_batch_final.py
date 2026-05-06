import os

supplements = [
    {
        "name": "Luteina",
        "folder": "Luteina",
        "price": "Q199",
        "scientific": "Carotenoide que se deposita en la mácula del ojo, actuando como filtro solar natural contra la luz azul.",
        "benefits": ["Protección contra pantallas y luz LED.", "Mejora la agudeza visual.", "Prevención de cataratas."],
        "hooks": ["¿Ojos cansados por el celular? Protege tu vista con Luteína.", "Tu filtro natural contra la luz azul Q199."]
    },
    {
        "name": "Isoflavonas de Soya",
        "folder": "Isoflavonas_de_Soya",
        "price": "Q259",
        "scientific": "Fitoestrógenos que ayudan a regular el equilibrio hormonal femenino durante la menopausia.",
        "benefits": ["Reducción de sofocos y calores.", "Protección ósea posmenopáusica.", "Bienestar emocional hormonal."],
        "hooks": ["Transiciones suaves, vida plena. El alivio natural para la menopausia.", "Equilibrio hormonal femenino por Q259."]
    },
    {
        "name": "L-Glutathione",
        "folder": "L-Glutathione",
        "price": "Q279",
        "scientific": "El antioxidante maestro del cuerpo, crucial para la desintoxicación celular y el brillo de la piel.",
        "benefits": ["Desintoxicación hepática extrema.", "Aclara y unifica el tono de la piel.", "Refuerzo inmunológico celular."],
        "hooks": ["El secreto de una piel radiante y un cuerpo limpio. Glutatión Q279.", "Desintoxica tu cuerpo al nivel celular más profundo."]
    },
    {
        "name": "Candida Support",
        "folder": "Candida_Support",
        "price": "Q269",
        "scientific": "Mezcla de ácido caprílico, pau d'arco y aceite de orégano para controlar el sobrecrecimiento de levaduras.",
        "benefits": ["Elimina antojos por dulce y niebla mental.", "Equilibrio de la flora intestinal y vaginal.", "Mejora la energía y digestión."],
        "hooks": ["¿Antojos incontrolables de azúcar? Podría ser Cándida. Límpiala ya.", "Recupera tu equilibrio digestivo por Q269."]
    },
    {
        "name": "Cranberry (Arándano Rojo)",
        "folder": "Cranberry",
        "price": "Q199",
        "scientific": "Extracto rico en proantocianidinas que evitan la adhesión de bacterias a las vías urinarias.",
        "benefits": ["Prevención de infecciones urinarias recurrentes.", "Protección renal y de vejiga.", "Antioxidante urinario."],
        "hooks": ["Protección natural y efectiva para tus vías urinarias. Q199.", "Dile adiós a las molestias urinarias de forma natural."]
    },
    {
        "name": "Aceite de Ajo",
        "folder": "Aceite_de_Ajo",
        "price": "Q199",
        "scientific": "Alicina concentrada, un potente compuesto azufrado con efectos antibióticos y cardiovasculares.",
        "benefits": ["Control de la presión arterial y colesterol.", "Antibiótico natural de amplio espectro.", "Mejora la circulación."],
        "hooks": ["El poder del ajo sin el olor. Corazón fuerte e inmunidad total.", "Circulación y defensas por solo Q199."]
    },
    {
        "name": "Vitamina B3 (Niacina)",
        "folder": "Vitamina_B3",
        "price": "Q179",
        "scientific": "Esencial para la producción de energía y el mantenimiento de niveles saludables de lípidos.",
        "benefits": ["Mejora el perfil de colesterol (HDL/LDL).", "Salud de la piel y sistema nervioso.", "Aumento de la circulación periférica."],
        "hooks": ["Energía y salud vascular en cada cápsula. Vitamina B3 Q179.", "El soporte metabólico que tu corazón necesita."]
    },
    {
        "name": "D3 con K2",
        "folder": "D3_con_K2",
        "price": "Q209",
        "scientific": "Dúo dinámico: la D3 absorbe el calcio y la K2 lo dirige a los huesos, evitando que se calcifiquen las arterias.",
        "benefits": ["Huesos de acero y arterias limpias.", "Máxima eficacia inmunológica.", "Salud dental y cardiovascular."],
        "hooks": ["No tomes D3 sin K2. El calcio debe ir a tus huesos, no a tus venas.", "El combo perfecto para tu salud ósea Q209."]
    },
    {
        "name": "Calcio",
        "folder": "Calcio",
        "price": "Q199",
        "scientific": "Mineral estructural fundamental para la densidad ósea y la contracción muscular.",
        "benefits": ["Prevención de osteoporosis.", "Salud de dientes y encías.", "Transmisión nerviosa y muscular."],
        "hooks": ["Huesos fuertes para una vida activa. El soporte que tu estructura necesita.", "Protección ósea garantizada por Q199."]
    },
    {
        "name": "Maca (Lepidium meyenii)",
        "folder": "Maca",
        "price": "Q159",
        "scientific": "Raíz andina adaptógena que equilibra el sistema endocrino y mejora la estamina.",
        "benefits": ["Aumento de energía física y libido.", "Equilibrio hormonal natural.", "Mejora la fertilidad y el ánimo."],
        "hooks": ["El superalimento de los Andes para tu energía diaria. Maca Q159.", "Vitalidad y equilibrio hormonal para hombres y mujeres."]
    },
    {
        "name": "Prenatales",
        "folder": "Prenatales",
        "price": "Q159",
        "scientific": "Multivitamínico completo con ácido fólico, hierro y yodo para el embarazo y lactancia.",
        "benefits": ["Desarrollo óptimo del bebé.", "Prevención de anemia en la madre.", "Soporte nutricional post-parto."],
        "hooks": ["La mejor nutrición para ti y tu bebé desde el primer día.", "Cuidado prenatal completo y accesible Q159."]
    },
    {
        "name": "Ácido Alpha Lipoico 600mg",
        "folder": "Acido_Alpha_lipoico_600mg",
        "price": "Q219",
        "scientific": "Antioxidante universal (agua y grasa) que regenera otros antioxidantes como la Vitamina C y E.",
        "benefits": ["Control de azúcar en sangre.", "Protección contra neuropatía diabética.", "Energía mitocondrial extrema."],
        "hooks": ["El antioxidante universal para tu metabolismo. Q219.", "Protege tus nervios y enciende tu energía celular."]
    },
    {
        "name": "Ácido Alpha Lipoico 300mg",
        "folder": "Acido_Alpha_lipoico_300mg",
        "price": "Q189",
        "scientific": "Dosis de mantenimiento para protección antioxidante diaria y salud metabólica.",
        "benefits": ["Prevención del daño oxidativo.", "Apoyo a la pérdida de peso.", "Desintoxicación celular."],
        "hooks": ["Tu dosis diaria de protección celular. ALA 300mg Q189.", "Salud metabólica al alcance de tu mano."]
    },
    {
        "name": "Centrum Adultos",
        "folder": "Centrum_Adultos",
        "price": "Q499",
        "scientific": "Fórmula completa con 24 micronutrientes clave para el bienestar general del adulto.",
        "benefits": ["Energía diaria y vitalidad.", "Soporte inmunológico.", "Salud de ojos y corazón."],
        "hooks": ["La confianza de la marca #1 en multivitamínicos. Nutrición total.", "Todo lo que tu cuerpo necesita en un solo frasco."]
    },
    {
        "name": "Centrum Men Silver",
        "folder": "Centrum_Men_Silver",
        "price": "Q399",
        "scientific": "Específicamente formulado para hombres mayores de 50 años, con enfoque en próstata y corazón.",
        "benefits": ["Salud prostática e inmunidad.", "Energía mental y física.", "Protección visual."],
        "hooks": ["Nutrición de precisión para el hombre de más de 50 años.", "Sigue activo, sigue fuerte. Centrum Silver Men Q399."]
    },
    {
        "name": "Centrum Woman Silver",
        "folder": "Centrum_Woman_Silver",
        "price": "Q249",
        "scientific": "Fórmula para mujeres 50+, con dosis ajustadas de Calcio, Vitamina D y Magnesio.",
        "benefits": ["Salud ósea y cardiovascular femenina.", "Vitalidad y equilibrio emocional.", "Protección post-menopausia."],
        "hooks": ["Tus mejores años con la mejor nutrición. Centrum Silver Woman.", "Salud ósea y energía para la mujer activa Q249."]
    },
    {
        "name": "DHEA 50mg",
        "folder": "DHEA_50mg",
        "price": "Q199",
        "scientific": "Dehidroepiandrosterona, precursora de hormonas sexuales que declinan con la edad.",
        "benefits": ["Rejuvenecimiento hormonal.", "Mejora del deseo sexual y ánimo.", "Aumento de la densidad ósea."],
        "hooks": ["Recupera tu balance hormonal natural. DHEA 50mg Q199.", "Vitalidad y juventud que se siente."]
    },
    {
        "name": "DHEA 100mg",
        "folder": "DHEA_100mg",
        "price": "Q199",
        "scientific": "Dosis de alta potencia para optimización hormonal bajo supervisión.",
        "benefits": ["Máximo soporte androgénico/estrogénico.", "Energía y masa muscular.", "Protección cognitiva."],
        "hooks": ["Potencia hormonal máxima para tu rendimiento. Q199.", "El precursor maestro para tu vitalidad."]
    },
    {
        "name": "Thyroid Energy",
        "folder": "Thyroid_Energy",
        "price": "Q239",
        "scientific": "Complejo de Yodo, Selenio, Tirosina y Ashwagandha para optimizar la glándula tiroides.",
        "benefits": ["Acelera el metabolismo lento.", "Elimina el cansancio crónico y frío constante.", "Mejora el estado de ánimo."],
        "hooks": ["¿Metabolismo lento? Dale el combustible que tu tiroides necesita.", "Energía y control de peso desde la raíz Q239."]
    },
    {
        "name": "L-Lysina",
        "folder": "L-Lysina",
        "price": "Q179",
        "scientific": "Aminoácido esencial conocido por inhibir la replicación del virus del herpes (fuegos).",
        "benefits": ["Prevención y sanación rápida de fuegos labiales.", "Soporte para la absorción de calcio.", "Formación de colágeno."],
        "hooks": ["Dile adiós a los molestos fuegos labiales para siempre. Q179.", "El aminoácido clave para tu piel e inmunidad."]
    },
    {
        "name": "Picolinato de Cromo",
        "folder": "Picolinato_de_Cromo",
        "price": "Q179",
        "scientific": "Mineral esencial que mejora la acción de la insulina y el metabolismo de carbohidratos.",
        "benefits": ["Control de la ansiedad por dulces.", "Mejora la composición corporal.", "Estabiliza el azúcar en sangre."],
        "hooks": ["El secreto para dejar de picar dulces todo el día. Q179.", "Controla tus antojos y mejora tu metabolismo."]
    },
    {
        "name": "Resveratrol",
        "folder": "Resveratrol",
        "price": "Q189",
        "scientific": "Polifenol encontrado en la uva que activa los genes Sirtuinas de la longevidad.",
        "benefits": ["Potente antienvejecimiento celular.", "Protección cardiovascular y cerebral.", "Imita los beneficios del ayuno."],
        "hooks": ["La molécula de la eterna juventud. Resveratrol puro Q189.", "Protege tu corazón y tus células con el poder de la uva."]
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
