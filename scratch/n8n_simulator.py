import os, json, requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"c:\proyectos\vitaminas\.env")

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL")
MODEL = os.getenv("OPENROUTER_MODEL", "google/gemini-2.5-flash")
REFERER = os.getenv("OPENROUTER_HTTP_REFERER", "https://n8n.papa-sts.online")
SKILLS_DIR = r"c:\proyectos\vitaminas\.agents\skills"
OUTPUT_DIR = r"c:\proyectos\vitaminas\Magnesio citrato y glicinato\n8n_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

ANDRES_CONTEXT = """
AVATAR FIJO (NO generes otro avatar, USA este):
- Nombre: Andres Castillo, 45 anos, Casado, 3 hijos (Ramiro 15, Elena 12, Sofi 6).
- Profesion: Arquitecto Senior, socio en firma de diseno constructivo. Gana Q35,000/mes. Vive en Carretera a El Salvador, Guatemala.
- Dolores: Insomnio de "motor encendido", tension muscular cronica (calambres, cuello), irritabilidad con su familia.
- Anhelos: Paz mental absoluta, despertar con vitalidad sin cafe, paciencia para disfrutar a sus hijos.
- Frustraciones pasadas: Melatonina (pesadillas), infusiones (ineficaces), magnesio de supermercado (diarrea).
"""

PRODUCT = "Magnesio Citrato y Glicinato de TINITA HEALTH. 60 capsulas. Citrato 500mg + Glicinato 500mg. 169mg de magnesio elemental. Precio: Q299. Guatemala 2026."

def read_skill(name):
    path = os.path.join(SKILLS_DIR, name, "SKILL.md")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def call_llm(system_prompt, user_prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": REFERER,
        "Content-Type": "application/json"
    }
    body = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "max_tokens": 4096,
        "temperature": 0.7
    }
    resp = requests.post(BASE_URL, headers=headers, json=body, timeout=120)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]

def save(filename, content):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Guardado: {filename}")

# === NODO 2: Investigacion + Posicionamiento ===
print("[Nodo 2] Investigacion + Posicionamiento...")
sys2 = read_skill("marketing-reporter") + "\n\n" + read_skill("positioning-strategist")
usr2 = f"{ANDRES_CONTEXT}\n\nProducto: {PRODUCT}\n\nGenera el reporte de investigacion completo, Dream 100, Oceano Azul y posicionamiento. USA EL AVATAR DE ANDRES proporcionado arriba, no inventes otro. Toda la salida debe ser en espanol."
research = call_llm(sys2, usr2)
save("01_research_positioning.md", research)

# === NODO 3: Embudo + Persuasion ===
print("[Nodo 3] Embudo + Persuasion...")
sys3 = read_skill("funnel-architect") + "\n\n" + read_skill("persuasion-architect")
usr3 = f"{ANDRES_CONTEXT}\n\nInvestigacion previa:\n{research}\n\nProducto: {PRODUCT}\n\nGenera la Escalera de Valor, el embudo, la regla de Kennedy (CAC), la alianza Joyner, la formula de Blair Warren y la oferta irracional de Ariely. Toda la salida en espanol."
funnel = call_llm(sys3, usr3)
save("02_funnel_persuasion.md", funnel)

# === NODO 4: Storytelling + Ganchos ===
print("[Nodo 4] Storytelling + Ganchos...")
sys4 = read_skill("movement-creator") + "\n\n" + read_skill("pattern-disruptor")
usr4 = f"{ANDRES_CONTEXT}\n\nInvestigacion:\n{research}\n\nEmbudo:\n{funnel}\n\nProducto: {PRODUCT}\n\nCrea el Puente de la Epifania, el Personaje Atractivo, la Tierra Prometida (Hoffer), la analogia anti-technobabble, 5 hooks textuales, 3 hooks visuales y el pre-frame de Brafman. Todo para ANDRES. Salida en espanol."
story = call_llm(sys4, usr4)
save("03_story_hooks.md", story)

# === NODO 5: Copywriting ===
print("[Nodo 5] Copywriting...")
sys5 = read_skill("copywriting-master")
usr5 = f"{ANDRES_CONTEXT}\n\nInvestigacion:\n{research}\n\nEmbudo:\n{funnel}\n\nHistoria y Ganchos:\n{story}\n\nProducto: {PRODUCT}\n\nGenera: 3 guiones de TikTok/Reels (60s cada uno con Hook/Retencion/Solucion/CTA), 2 Facebook Ads (1 trafico frio Story Lead, 1 retargeting Offer Lead), y 3 emails Soap Opera Sequence. Todo dirigido a ANDRES. Salida en espanol."
copy_assets = call_llm(sys5, usr5)
save("04_copy_assets.md", copy_assets)

# === NODO 6: Calendario Editorial ===
print("[Nodo 6] Calendario Editorial...")
sys6 = read_skill("content-calendar")
usr6 = f"Guiones y Ads:\n{copy_assets}\n\nHistoria y Ganchos:\n{story}\n\nProducto: {PRODUCT}\n\nCrea un calendario editorial de 30 dias para el Magnesio Dual de Tinita Health. Aplica la regla 3:1 de Gary Vee. Distribuye los 3 emails Soap Opera. Incluye plataforma, formato, hora de vinculo y tipo (JAB o RIGHT HOOK) para cada dia. Salida en espanol."
calendar = call_llm(sys6, usr6)
save("05_calendario_editorial.md", calendar)

print("\nSimulacion completada. Todos los archivos en:", OUTPUT_DIR)
