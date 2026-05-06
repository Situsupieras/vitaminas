import os

supplements = [
    {
        "name": "Melatonina 5mg",
        "folder": "Melatonina_5mg",
        "price": "Q159",
        "scientific": "Hormona pineal que regula el ritmo circadiano. Dosis de 5mg ideal para conciliar el sueño en entornos urbanos ruidosos.",
        "benefits": ["Inducción rápida del sueño.", "Mejora del descanso profundo.", "Efecto antioxidante neuronal."],
        "hooks": ["¿Vueltas en la cama? Melatonina 5mg para un descanso real. Q159.", "Apaga tu mente, enciende tu descanso."]
    },
    {
        "name": "Ginkgo Biloba",
        "folder": "Ginkgo_Biloba",
        "price": "Q169",
        "scientific": "Extracto estandarizado que mejora la microcirculación cerebral y periférica.",
        "benefits": ["Mejora la memoria y concentración.", "Alivio de vértigo y tinnitus.", "Protección contra el deterioro cognitivo."],
        "hooks": ["Potencia tu memoria y enfoque mental. Ginkgo Biloba Q169.", "Circulación cerebral óptima para rendir al máximo."]
    },
    {
        "name": "Gastro Comfort",
        "folder": "Gastro_Comfort",
        "price": "Q349",
        "scientific": "Fórmula avanzada con PepZin GI (Zinc-Carnosina) para reparar la mucosa gástrica.",
        "benefits": ["Alivio de gastritis y acidez crónica.", "Protección contra H. pylori.", "Reparación del revestimiento del estómago."],
        "hooks": ["¿Gastritis por el estrés del trabajo? Gastro Comfort es la solución definitiva.", "Come tranquilo de nuevo. Protección gástrica premium Q349."]
    },
    {
        "name": "Blood Sugar Specific",
        "folder": "Blood_Sugar_Specific",
        "price": "Q249",
        "scientific": "Mezcla de Cromo, Vanadio y hierbas tradicionales para sensibilizar los receptores de insulina.",
        "benefits": ["Control de picos de glucosa post-comida.", "Reducción de antojos por azúcar.", "Estabilidad de energía durante el día."],
        "hooks": ["Domina tus niveles de azúcar de forma natural. Q249.", "Sin picos, sin caídas. Energía estable todo el día."]
    },
    {
        "name": "Vitamina E",
        "folder": "Vitamina_E",
        "price": "Q149",
        "scientific": "Mezcla de tocoferoles naturales, potente antioxidante liposoluble.",
        "benefits": ["Protección cardiovascular.", "Salud de la piel y cicatrización.", "Fertilidad y equilibrio hormonal."],
        "hooks": ["Juventud para tus células. Vitamina E natural Q149.", "El escudo antioxidante que tu cuerpo necesita."]
    },
    {
        "name": "Vitamina D3 5000 IU",
        "folder": "Vitamina_D3_5000IU",
        "price": "Q179",
        "scientific": "Colecalciferol de alta dosis, vital para la función inmune y absorción de calcio.",
        "benefits": ["Refuerzo inmunológico masivo.", "Salud ósea y muscular.", "Mejora del estado de ánimo (vitamina del sol)."],
        "hooks": ["Aunque vivas en el país de la eterna primavera, podrías tener deficiencia de D3.", "Tus defensas al máximo por solo Q179."]
    },
    {
        "name": "Vitamina C 500mg",
        "folder": "Vitamina_C_500mg",
        "price": "Q159",
        "scientific": "Ácido ascórbico con escaramujo (rose hips) para liberación prolongada.",
        "benefits": ["Producción de colágeno natural.", "Defensa antioxidante diaria.", "Absorción de hierro de la dieta."],
        "hooks": ["Protección diaria para toda la familia. Vitamina C Q159.", "Salud y colágeno en cada cápsula."]
    },
    {
        "name": "Vitamina C 1000mg",
        "folder": "Vitamina_C_1000mg",
        "price": "Q199",
        "scientific": "Dosis terapéutica para periodos de alto estrés o enfermedad.",
        "benefits": ["Recuperación rápida de gripes y resfriados.", "Protección contra el daño solar en la piel.", "Apoyo a las glándulas suprarrenales."],
        "hooks": ["Potencia inmunológica total. Vitamina C 1000mg Q199.", "No dejes que una gripe te detenga."]
    },
    {
        "name": "Glicinato de magnesio",
        "folder": "Glicinato_de_magnesio",
        "price": "Q219",
        "scientific": "Magnesio unido al aminoácido glicina, la forma más relajante y suave para el estómago.",
        "benefits": ["Paz mental y alivio de ansiedad.", "Sueño reparador y profundo.", "Sin efectos laxantes."],
        "hooks": ["El magnesio que relaja tu mente. Adiós a la ansiedad. Q219.", "Descanso profundo sin molestias estomacales."]
    },
    {
        "name": "Enzimas digestivas de Papaya",
        "folder": "Enzimas_digestivas_Papaya",
        "price": "Q199",
        "scientific": "Papaína y proteasas naturales para desglosar proteínas y carbohidratos complejos.",
        "benefits": ["Elimina la pesadez estomacal inmediata.", "Mejor absorción de nutrientes.", "Alivio de gases y eructos."],
        "hooks": ["¿Comiste de más? Las enzimas de papaya son tu mejor aliado.", "Digestión ligera y rápida por Q199."]
    },
    {
        "name": "Zinc",
        "folder": "Zinc",
        "price": "Q139",
        "scientific": "Mineral traza esencial para la división celular y la función inmunitaria.",
        "benefits": ["Acorta la duración de resfriados.", "Salud de la próstata y niveles de testosterona.", "Cicatrización de heridas."],
        "hooks": ["El guardián de tus defensas y tu salud hormonal. Q139.", "Inmunidad básica y potente para el día a día."]
    },
    {
        "name": "Melena de Leon con Ginkgo",
        "folder": "Melena_de_Leon_con_Ginkgo",
        "price": "Q209",
        "scientific": "Hericium erinaceus (hongo nootrópico) potenciado con Ginkgo para neurogénesis.",
        "benefits": ["Crecimiento de nuevas neuronas (BDNF).", "Memoria fotográfica y enfoque láser.", "Protección contra el estrés oxidativo mental."],
        "hooks": ["Dale superpoderes a tu cerebro. Melena de León + Ginkgo Q209.", "El combo definitivo para estudiantes y profesionales."]
    },
    {
        "name": "GABA",
        "folder": "GABA",
        "price": "Q229",
        "scientific": "Ácido gamma-aminobutírico, el principal neurotransmisor inhibidor del sistema nervioso.",
        "benefits": ["Freno natural para la ansiedad.", "Relajación muscular profunda.", "Apoyo a la hormona de crecimiento natural."],
        "hooks": ["Ponle freno al estrés. GABA: El calmante natural de tu cerebro.", "Paz instantánea en cápsulas por Q229."]
    },
    {
        "name": "Biotin 5000mcg",
        "folder": "Biotin_5000mcg",
        "price": "Q159",
        "scientific": "Vitamina B7 en dosis óptima para el mantenimiento de la queratina.",
        "benefits": ["Cabello más grueso y brillante.", "Uñas fuertes que no se quiebran.", "Salud de la piel."],
        "hooks": ["Belleza real desde la raíz. Biotin 5000mcg Q159.", "Cabello y uñas envidiables de forma natural."]
    },
    {
        "name": "Biotin 10000mcg",
        "folder": "Biotin_10000mcg",
        "price": "Q179",
        "scientific": "Dosis de máxima potencia para casos de caída de cabello severa o uñas muy débiles.",
        "benefits": ["Recuperación capilar acelerada.", "Metabolismo de grasas y energía.", "Resultados visibles en menos tiempo."],
        "hooks": ["Potencia máxima para tu belleza. Biotin 10000mcg Q179.", "Resultados profesionales para tu cabello y piel."]
    },
    {
        "name": "Selenio",
        "folder": "Selenio",
        "price": "Q179",
        "scientific": "Mineral esencial y antioxidante que protege las células del daño por radicales libres.",
        "benefits": ["Salud de la tiroides y metabolismo.", "Protección contra metales pesados.", "Fortalecimiento inmunológico."],
        "hooks": ["El protector invisible de tu tiroides y células. Q179.", "Defensa antioxidante de precisión."]
    },
    {
        "name": "Aceite de Orégano",
        "folder": "Aceite_de_Oregano",
        "price": "Q169",
        "scientific": "Carvacrol y timol concentrados con potentes propiedades antimicrobianas naturales.",
        "benefits": ["Antibiótico y antifúngico natural.", "Eliminación de cándida y parásitos.", "Salud respiratoria."],
        "hooks": ["El antibiótico de la naturaleza. Aceite de Orégano Q169.", "Limpia tu cuerpo de bacterias y hongos dañinos."]
    },
    {
        "name": "Cardo Mariano",
        "folder": "Cardo_Mariano",
        "price": "Q299",
        "scientific": "Silimarina concentrada para la regeneración y protección de los hepatocitos (hígado).",
        "benefits": ["Desintoxicación hepática profunda.", "Regeneración del hígado dañado por alcohol o grasas.", "Piel más clara (reflejo de un hígado sano)."],
        "hooks": ["Dale un reset a tu hígado. Cardo Mariano premium Q299.", "El seguro de vida para tu órgano depurador principal."]
    },
    {
        "name": "Complejo B",
        "folder": "Complejo_B",
        "price": "Q199",
        "scientific": "Mezcla equilibrada de todas las vitaminas del grupo B en sus formas más absorbibles.",
        "benefits": ["Energía física y mental sostenida.", "Salud del sistema nervioso.", "Metabolismo eficiente de los alimentos."],
        "hooks": ["Toda la energía que necesitas en un solo complejo. Q199.", "El combustible diario para tu sistema nervioso."]
    },
    {
        "name": "NAD",
        "folder": "NAD",
        "price": "Q499",
        "scientific": "Nicotinamida Adenina Dinucleótido, coenzima esencial para la reparación del ADN y longevidad celular.",
        "benefits": ["Reversión del envejecimiento biológico.", "Claridad mental extrema.", "Energía mitocondrial pura."],
        "hooks": ["Invierte en tu juventud celular. El secreto de la longevidad. Q499.", "Rendimiento cognitivo de otro nivel."]
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
