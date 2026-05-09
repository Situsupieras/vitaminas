import requests
import os

def generate_tiktok_tts_pro(text, voice="es_mx_002", output_file="tiktok_pro_test.mp3"):
    # Using the mirrored endpoint identified by the research
    url = "https://tiktokvoice.net/api/generate"
    
    payload = {
        "text": text,
        "voice": voice
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://tiktokvoice.net/",
        "Origin": "https://tiktokvoice.net/"
    }
    
    try:
        print(f"Requesting TTS for: {text[:50]}...")
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success" and "data" in data and "url" in data["data"]:
                audio_url = data["data"]["url"]
                print(f"Downloading audio from: {audio_url}")
                audio_response = requests.get(audio_url)
                if audio_response.status_code == 200:
                    with open(output_file, "wb") as f:
                        f.write(audio_response.content)
                    print(f"Audio saved to: {output_file}")
                    return True
                else:
                    print(f"Failed to download audio file: {audio_response.status_code}")
            else:
                print("Error: Invalid response format or failure status")
                print(data)
        else:
            print(f"Error: Status code {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Exception: {str(e)}")
    
    return False

if __name__ == "__main__":
    test_text = "Esta es la nueva voz de Marco Villagrán para Tinita Health. Mucho mejor que la anterior, ¿verdad?"
    output_path = r"c:\proyectos\vitaminas\scratch\tiktok_pro_test.mp3"
    
    generate_tiktok_tts_pro(test_text, voice="es_mx_002", output_file=output_path)
