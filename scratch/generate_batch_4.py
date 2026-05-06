import os

supplements = [
    {
        "name": "5HTP 50mg",
        "folder": "5HTP_50mg",
        "price": "Q159",
        "scientific": "Precursor directo de la serotonina (la hormona de la felicidad), derivado de la semilla de Griffonia simplicifolia.",
        "benefits": ["Mejora el estado de ánimo y reduce la depresión leve.", "Control natural del apetito emocional.", "Mejora la calidad del sueño profundo."],
        "hooks": ["¿Comes por ansiedad o estrés? El 5-HTP ayuda a equilibrar tu saciedad.", "Recupera tu alegría y calma natural por Q159."]
    },
    {
        "name": "5HTP 100mg",
        "folder": "5HTP_100mg",
        "price": "Q189",
        "scientific": "Dosis de mayor potencia para casos de insomnio severo o ansiedad persistente.",
        "benefits": ["Relajación mental profunda.", "Regulación de los ritmos circadianos.", "Alivio de dolores de cabeza por tensión."],
        "hooks": ["Potencia máxima para tu bienestar emocional. 5-HTP 100mg Q189.", "Dile adiós a las noches en vela y al estrés constante."]
    },
    {
        "name": "HGH (Precursores)",
        "folder": "HGH",
        "price": "Q299",
        "scientific": "Mezcla de aminoácidos (Arginina, Ornitina, Lisina) que estimulan la liberación natural de la hormona de crecimiento.",
        "benefits": ["Recuperación muscular acelerada.", "Mejora del tono de la piel y vitalidad general.", "Aumento de la quema de grasa nocturna."],
        "hooks": ["El secreto de la eterna juventud biológica. HGH Natural Q299.", "Mejora tu físico y tu energía mientras duermes."]
    },
    {
        "name": "Zinc para Acné",
        "folder": "Zinc_Acne",
        "price": "Q189",
        "scientific": "Zinc quelado con vitaminas A y C para una regeneración cutánea óptima y control sebáceo.",
        "benefits": ["Reducción de inflamación por acné.", "Regulación de la producción de grasa en la piel.", "Cicatrización rápida sin marcas."],
        "hooks": ["Limpia tu piel desde adentro. El combo perfecto contra el acné Q189.", "Piel radiante y libre de imperfecciones de forma natural."]
    },
    {
        "name": "Echinacea",
        "folder": "Echinacea",
        "price": "Q159",
        "scientific": "Inmunoestimulante natural que activa los macrófagos y linfocitos para combatir infecciones.",
        "benefits": ["Prevención y tratamiento de gripes y virus.", "Refuerzo del sistema linfático.", "Reducción de la duración de infecciones respiratorias."],
        "hooks": ["Tu escudo herbal contra los cambios de clima en Guatemala. Q159.", "Refuerza tus defensas antes de enfermar."]
    },
    {
        "name": "Vinagre de Manzana (Gummies/Caps)",
        "folder": "Vinagre_Manzana",
        "price": "Q189",
        "scientific": "Contiene ácido acético que mejora la sensibilidad a la insulina y el metabolismo de grasas.",
        "benefits": ["Control de peso y reducción de grasa abdominal.", "Mejora la digestión y el pH gástrico.", "Reduce los picos de glucosa."],
        "hooks": ["Todos los beneficios del vinagre de manzana sin el mal sabor. Q189.", "Tu aliado metabólico diario para un abdomen plano."]
    },
    {
        "name": "Saw Palmetto",
        "folder": "Saw_Palmetto",
        "price": "Q199",
        "scientific": "Extracto de baya que bloquea la conversión de testosterona a DHT, protegiendo la próstata.",
        "benefits": ["Salud prostática y flujo urinario normal.", "Prevención de la caída de cabello hormonal.", "Equilibrio hormonal masculino."],
        "hooks": ["Salud masculina preventiva para el hombre de hoy. Saw Palmetto Q199.", "Protege tu próstata y mantiene tu vitalidad."]
    },
    {
        "name": "Ashwagandha",
        "folder": "Ashwagandha",
        "price": "Q179",
        "scientific": "Withania somnifera, el adaptógeno más estudiado para reducir niveles de cortisol (estrés).",
        "benefits": ["Reducción drástica del estrés y ansiedad.", "Mejora de la fuerza física y resistencia.", "Equilibrio de la tiroides y hormonas."],
        "hooks": ["El antídoto natural contra el ritmo de vida acelerado. Ashwagandha Q179.", "Calma mental y fuerza física en una sola raíz."]
    },
    {
        "name": "Ginseng panax",
        "folder": "Ginseng_panax",
        "price": "Q179",
        "scientific": "Ginseng coreano rojo, energizante tradicional que mejora la función cognitiva y física.",
        "benefits": ["Energía inmediata y enfoque láser.", "Mejora de la función eréctil y libido.", "Fortalecimiento inmunológico."],
        "hooks": ["Energía real y legendaria para tus días más largos. Ginseng Panax Q179.", "Enfoque y vitalidad sin el crash de la cafeína."]
    },
    {
        "name": "Ginseng complex",
        "folder": "Ginseng_complex",
        "price": "Q229",
        "scientific": "Mezcla de Ginseng Panax, Americano y Siberiano para un efecto energético completo y equilibrado.",
        "benefits": ["Resistencia física prolongada.", "Adaptación al estrés ambiental.", "Vigor total para hombres y mujeres."],
        "hooks": ["El combo energético definitivo. Triple poder de Ginseng Q229.", "Vitalidad sostenida para los que nunca se detienen."]
    },
    {
        "name": "Cúrcuma (Turmeric)",
        "folder": "Curcuma",
        "price": "Q179",
        "scientific": "Curcumina estandarizada con piperina (pimienta negra) para una absorción 2000% mayor.",
        "benefits": ["Potente antiinflamatorio natural (articulaciones).", "Protección antioxidante para el cerebro.", "Salud digestiva e inmunológica."],
        "hooks": ["Dile adiós al dolor de articulaciones con el oro de la naturaleza. Q179.", "Inflamación bajo control, vida en movimiento."]
    },
    {
        "name": "Triple Omega",
        "folder": "Triple_Omega",
        "price": "Q299",
        "scientific": "Mezcla equilibrada de Omega 3, 6 y 9 provenientes de aceites de pescado, lino y borraja.",
        "benefits": ["Salud integral del corazón y arterias.", "Piel, cabello y uñas radiantes.", "Protección celular y hormonal."],
        "hooks": ["El equilibrio perfecto de grasas saludables para tu cuerpo. Q299.", "Nutrición total para tu cerebro y piel."]
    },
    {
        "name": "Inositol",
        "folder": "Inositol",
        "price": "Q239",
        "scientific": "Mio-inositol, vital para la señalización de insulina y equilibrio de neurotransmisores.",
        "benefits": ["Tratamiento natural para Ovario Poliquístico (SOP).", "Reducción de ansiedad y ataques de pánico.", "Mejora la calidad de los óvulos y fertilidad."],
        "hooks": ["Equilibrio hormonal y paz mental para la mujer. Inositol Q239.", "Tu aliado contra el SOP y la ansiedad metabólica."]
    },
    {
        "name": "Cola de caballo",
        "folder": "Cola_de_caballo",
        "price": "Q169",
        "scientific": "Rica en sílice orgánico, esencial para la síntesis de colágeno y salud renal.",
        "benefits": ["Diurético natural (reduce retención de líquidos).", "Fortalece huesos, uñas y cabello.", "Salud de las vías urinarias."],
        "hooks": ["Dile adiós a la hinchazón y fortalece tu belleza natural. Q169.", "El secreto ancestral para uñas y cabello de acero."]
    },
    {
        "name": "Potasio",
        "folder": "Potasio",
        "price": "Q159",
        "scientific": "Gluconato/Citrato de potasio, electrolito vital para la función muscular y equilibrio hídrico.",
        "benefits": ["Prevención de calambres y debilidad muscular.", "Regulación del ritmo cardíaco.", "Control de la presión arterial."],
        "hooks": ["Evita calambres y fatiga muscular. Potasio esencial Q159.", "El equilibrio eléctrico que tu corazón y músculos necesitan."]
    },
    {
        "name": "Colágeno Piel Uñas Cabello",
        "folder": "Colageno_Piel_Unas_Cabello",
        "price": "Q199",
        "scientific": "Fórmula optimizada con biotina y vitaminas adicionales para la síntesis de colágeno estético.",
        "benefits": ["Piel tersa y luminosa.", "Uñas que no se quiebran.", "Cabello con volumen y fuerza."],
        "hooks": ["Tu rutina de belleza en una cápsula. Colágeno especializado Q199.", "Brilla de adentro hacia afuera."]
    },
    {
        "name": "Melatonina 10mg",
        "folder": "Melatonina_10mg",
        "price": "Q209",
        "scientific": "Dosis de alta potencia para casos de insomnio crónico o Jet Lag severo.",
        "benefits": ["Reseteo del ciclo circadiano.", "Inducción profunda del sueño en casos difíciles.", "Máxima protección antioxidante nocturna."],
        "hooks": ["Para los que han probado de todo y no pueden dormir. Melatonina 10mg.", "Duerme como un bebé, despierta como nuevo."]
    },
    {
        "name": "Glucosamina",
        "folder": "Glucosamina",
        "price": "Q199",
        "scientific": "Componente estructural del cartílago, ayuda a mantener la integridad de las articulaciones.",
        "benefits": ["Reducción de dolor articular por desgaste.", "Mejora de la movilidad y flexibilidad.", "Protección contra la osteoartritis."],
        "hooks": ["Recupera tu movilidad y olvida el dolor articular. Q199.", "Tus rodillas y espalda te lo agradecerán."]
    },
    {
        "name": "Ácido Fólico",
        "folder": "Acido_Folico",
        "price": "Q129",
        "scientific": "Vitamina B9 esencial para la síntesis de ADN y división celular.",
        "benefits": ["Vital para el desarrollo fetal (embarazo).", "Salud del corazón y glóbulos rojos.", "Prevención de anemias."],
        "hooks": ["Nutrición esencial para el inicio de la vida y tu salud diaria. Q129.", "El apoyo fundamental para tu corazón y energía."]
    },
    {
        "name": "Citrato de potasio",
        "folder": "Citrato_de_potasio",
        "price": "Q159",
        "scientific": "Forma altamente absorbible de potasio que ayuda a alcalinizar la orina.",
        "benefits": ["Prevención de cálculos renales.", "Equilibrio ácido-base del cuerpo.", "Salud vascular."],
        "hooks": ["Protege tus riñones y equilibra tu cuerpo. Citrato de Potasio Q159.", "Alcalinidad y salud para tu sistema urinario."]
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
