import os, requests, json
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"c:\proyectos\vitaminas\.env")

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL")
MODEL = os.getenv("OPENROUTER_MODEL", "meta-llama/llama-4-maverick:free") # Free model
REFERER = os.getenv("OPENROUTER_HTTP_REFERER", "https://n8n.papa-sts.online")

OUTPUT_PATH = r"c:\proyectos\vitaminas\Magnesio citrato y glicinato\n8n_output\08_masterclass_script_60min.md"

AVATAR_INFO = """
Andres Castillo, 45 anos, Arquitecto Senior en Guatemala.
Dolores: Insomnio de motor encendido, tension muscular, irritabilidad familiar.
Anhelos: Paz mental, vitalidad sin cafe, ser un padre presente.
"""

def generate_section(title, instructions, context=""):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": REFERER,
        "Content-Type": "application/json"
    }
    prompt = f"""
    Eres un experto en Copywriting de Respuesta Directa y Marketing Educativo (Chet Holmes style).
    Estamos escribiendo el GUION COMPLETO de una Masterclass de 60 minutos para el Magnesio Dual de TINITA HEALTH.
    
    PRODUCTO: Magnesio Citrato (absorcion muscular) + Glicinato (absorcion cerebral/nerviosa).
    AVATAR: {AVATAR_INFO}
    
    SECCION ACTUAL: {title}
    INSTRUCCIONES: {instructions}
    
    REGLAS:
    - Escribe en Espanol de Guatemala/Latinoamerica, profesional pero cercano.
    - Usa analogias de arquitectura y diseno (planos, cimientos, corto circuitos).
    - Se extremadamente tecnico y educativo (habla de neurotransmisores, bomba sodio-potasio, receptores GABA).
    - El tono debe ser de autoridad medica/cientifica pero empatico.
    
    CONTEXTO PREVIO: {context}
    
    Escribe el guion detallado (incluyendo sugerencias de visuales entre corchetes [Visual: ...]) para esta seccion.
    Debe ser una seccion extensa y profunda.
    """
    
    body = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a master copywriter writing a 60-minute educational script."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 4000,
        "temperature": 0.7
    }
    
    response = requests.post(BASE_URL, headers=headers, json=body)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']

# Secciones
sections = [
    ("0-10 min: La Apertura y la Paradoja del Profesional", "Establece el problema. El insomnio de motor encendido. Valida que no es falta de voluntad. Habla del estilo de vida en GT (carretera a El Salvador, trafico, cafe)."),
    ("10-25 min: La Biologia del Estres (El Motor)", "Explica el sistema simpatico y parasimpatico. La analogia del sistema electrico de un edificio. Por que el estres evapora el magnesio."),
    ("25-40 min: El Fraude del Magnesio Barato", "Desacredita el Oxido de Magnesio. Explica la biodisponibilidad. Por que el citrato solo no basta para el cerebro. Introduce el Glicinato."),
    ("40-50 min: La Solucion Dual - El Blindaje Nervioso", "Presenta el producto de TINITA HEALTH. Explica la sinergia Citrato+Glicinato. Como cruza la barrera hematoencefalica. La sensacion de silencio mental."),
    ("50-60 min: El Protocolo y la Oferta Irresistible", "Instrucciones de uso. El Momento de Oro. Presenta el precio Q299 y el bono de la guia. Cierra con la vision del futuro (Andres despertando con vitalidad).")
]

full_script = "# GUION MAESTRO: La Ingenieria del Descanso (60 Minutos)\n\n"
current_context = ""

print("Generando Masterclass por secciones con OpenRouter (Free Model)...")
for title, instr in sections:
    print(f"  Generando: {title}")
    content = generate_section(title, instr, current_context)
    full_script += f"\n\n## {title}\n\n{content}"
    current_context = content[:1000]

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(full_script)

print(f"\nGuion completo guardado en: {OUTPUT_PATH}")
