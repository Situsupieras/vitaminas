# Blueprint del Workflow de n8n: La Fábrica de Contenido

Este documento sirve como la arquitectura técnica para configurar los nodos en tu instancia de n8n. Utilizaremos el modelo LLM proporcionado por OpenRouter.ai (ej. `google/gemini-flash-1.5` o un modelo Llama gratuito) a través del nodo de HTTP Request o los Nodos de AI de n8n.

## Variables Globales del Workflow
- `Product_Name`: "Magnesio Citrato y Glicinato"
- `Product_Path`: `C:\proyectos\vitaminas\Magnesio citrato y glicinato`

---

## 🔀 Nodos y Estructura

### Nodo 1: Webhook / Trigger
- **Tipo**: Webhook / Manual Trigger.
- **Payload**: JSON con el nombre del producto, ingredientes y carpeta.

### Nodo 2: Agente Investigador & Estratega (HTTP Request a OpenRouter)
- **Rol**: Fusiona los `SKILL.md` de *marketing-reporter* y *positioning-strategist*.
- **Prompt (System)**: [Contenido de los SKILL.md combinados].
- **Prompt (User)**: "Genera el reporte de investigación, Dream 100 y posicionamiento para: {{ $json.Product_Name }}".
- **Output**: Guarda como variable `Research_Data`.

### Nodo 3: Arquitecto de Embudos & Persuasión (HTTP Request)
- **Rol**: Fusiona *funnel-architect* y *persuasion-architect*.
- **Prompt (System)**: [Contenido de los SKILL.md].
- **Prompt (User)**: "Usando esta investigación: {{ $node["Nodo 2"].json.Research_Data }}, genera la Escalera de Valor, el Embudo y la optimización de persuasión de Blair Warren".
- **Output**: Guarda como variable `Funnel_Data`.

### Nodo 4: Creador de Movimientos & Ganchos (HTTP Request)
- **Rol**: Fusiona *movement-creator* y *pattern-disruptor*.
- **Prompt (User)**: "Crea el puente de la epifanía y los 5 ganchos disruptivos para: {{ $json.Product_Name }}".
- **Output**: Guarda como variable `Story_Data`.

### Nodo 5: El Redactor Maestro (HTTP Request)
- **Rol**: El nuevo agente `copywriting-master`.
- **Prompt (System)**: "Eres un Copywriter maestro basado en Eugene Schwartz y Robert Collier..."
- **Prompt (User)**: "Usa toda la información recolectada:
  1. Investigación: {{ $node["Nodo 2"].json.Research_Data }}
  2. Historia y Ganchos: {{ $node["Nodo 4"].json.Story_Data }}
  Genera 3 Guiones de TikTok, 2 Ads de Facebook y 1 Email Soap Opera."
- **Output**: `Copy_Assets`.

### Nodo 6: Generador de Prompts Visuales (HTTP Request)
- **Rol**: Prompt Engineer de Midjourney/DALL-E.
- **Prompt (User)**: "Basado en los anuncios generados en el Nodo 5, crea 3 prompts hiperrealistas en inglés para Midjourney que sirvan como imágenes para los anuncios de Facebook."
- **Output**: `Visual_Prompts`.

### Nodo 7: Guardar en Disco (Write/Read File Node)
- **Acción**: Crea archivos `.md` en la carpeta `{{ $json.Product_Path }}\n8n_output\`.
- Archivo 1: `estrategia_persuasion.md` (Output Nodos 2 y 3).
- Archivo 2: `guiones_y_ads.md` (Output Nodos 4 y 5).
- Archivo 3: `prompts_visuales.md` (Output Nodo 6).

---

## 🛠️ Configuración de OpenRouter en n8n
Para hacer las peticiones al LLM gratuito, usa el nodo **HTTP Request** con la siguiente configuración:
- **Method**: POST
- **URL**: `https://openrouter.ai/api/v1/chat/completions`
- **Headers**:
  - `Authorization`: `Bearer TU_API_KEY`
  - `HTTP-Referer`: `http://localhost:5678` (tu instancia n8n)
- **Body Parameters (JSON)**:
  ```json
  {
    "model": "google/gemini-2.5-flash", // O el modelo Llama gratuito que prefieras
    "messages": [
      { "role": "system", "content": "EL CONTENIDO DEL SKILL.MD" },
      { "role": "user", "content": "EL PROMPT CON VARIABLES" }
    ]
  }
  ```
