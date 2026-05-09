import requests
import base64
import os

def generate_tiktok_tts(text, voice="es_mx_002", output_file="tiktok_test.mp3"):
    # This is a common unofficial endpoint for TikTok TTS
    # If this fails, we can try other methods.
    url = "https://tiktok-tts.weilbyte.dev/api/generate"
    
    payload = {
        "text": text,
        "voice": voice
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            if "data" in data:
                audio_data = base64.b64decode(data["data"])
                with open(output_file, "wb") as f:
                    f.write(audio_data)
                print(f"Audio generated successfully: {output_file}")
                return True
            else:
                print("Error: No data in response")
        else:
            print(f"Error: Status code {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Exception: {str(e)}")
    
    return False

if __name__ == "__main__":
    test_text = "Bienvenidos a Tinita Health. Soy Marco Villagrán y hoy vamos a descubrir el poder del magnesio dual para tu bienestar."
    output_path = r"c:\proyectos\vitaminas\scratch\tiktok_test_marco.mp3"
    
    # Try the most popular Spanish MX voice
    generate_tiktok_tts(test_text, voice="es_mx_002", output_file=output_path)
