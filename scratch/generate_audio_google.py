import os
from google.cloud import texttospeech
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def generate_audio():
    input_file = r"c:\proyectos\vitaminas\scratch\masterclass_section1_pro.txt"
    output_file = r"c:\proyectos\vitaminas\Magnesio citrato y glicinato\n8n_output\08_masterclass_section1_google.mp3"
    
    api_key = os.getenv("GOOGLE_TTS_API_KEY")
    
    if not api_key:
        print("Error: GOOGLE_TTS_API_KEY no encontrada en .env")
        return

    if not os.path.exists(input_file):
        print(f"Error: Archivo de entrada {input_file} no encontrado.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    if not text.strip():
        print("Error: El texto está vacío.")
        return

    # Instanciar el cliente usando la API Key a través de client_options
    # Nota: Google Cloud TTS Python SDK soporta api_key en ClientOptions
    from google.api_core.client_options import ClientOptions
    client_options = ClientOptions(api_key=api_key)
    client = texttospeech.TextToSpeechClient(client_options=client_options)

    # Configurar la síntesis
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Voz: es-US-Neural2-B o es-ES-Neural2-F son excelentes.
    # Para Guatemala/Latinoamérica, es-US-Neural2-B (Masculina) es muy natural.
    voice = texttospeech.VoiceSelectionParams(
        language_code="es-US",
        name="es-US-Neural2-B", # Voz masculina premium
        # ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        pitch=0.0,
        speaking_rate=1.0
    )

    print(f"Generando audio con Google Cloud TTS (Neural2)...")
    try:
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # Guardar el resultado
        with open(output_file, "wb") as out:
            out.write(response.audio_content)
            print(f"Audio premium guardado en {output_file}")
    except Exception as e:
        print(f"\n[ERROR] Error al llamar a Google Cloud TTS:")
        print(f"Mensaje: {str(e)}")
        if "API has not been used" in str(e) or "is disabled" in str(e):
            print("\n[!] IMPORTANTE: Debes habilitar la 'Cloud Text-to-Speech API' en tu consola de Google Cloud.")
            print("Enlace para habilitar: https://console.developers.google.com/apis/api/texttospeech.googleapis.com/overview")
        elif "API key not valid" in str(e):
            print("\n[!] IMPORTANTE: La API Key en tu .env parece no ser válida o no tener permisos para TTS.")



if __name__ == "__main__":
    generate_audio()
