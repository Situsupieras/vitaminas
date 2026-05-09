import requests
import os
import subprocess

def download_file(url, dest):
    print(f"Downloading {url}...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(dest, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Saved to {dest}")
        return True
    else:
        print(f"Failed to download. Status code: {response.status_code}")
        return False

def test_piper():
    model_name = "es_MX-carl-medium"
    model_dir = r"c:\proyectos\vitaminas\scratch\piper_models"
    os.makedirs(model_dir, exist_ok=True)
    
    onnx_url = f"https://huggingface.co/rhasspy/piper-voices/resolve/main/es/es_MX/carl/medium/{model_name}.onnx"
    json_url = f"https://huggingface.co/rhasspy/piper-voices/resolve/main/es/es_MX/carl/medium/{model_name}.onnx.json"
    
    onnx_path = os.path.join(model_dir, f"{model_name}.onnx")
    json_path = os.path.join(model_dir, f"{model_name}.onnx.json")
    
    if not os.path.exists(onnx_path):
        if not download_file(onnx_url, onnx_path): return
    if not os.path.exists(json_path):
        if not download_file(json_url, json_path): return

    output_wav = r"c:\proyectos\vitaminas\scratch\piper_test_marco.wav"
    text = "Bienvenidos a Tinita Health. Soy Marco Villagrán y hoy vamos a descubrir el poder del magnesio dual para tu bienestar profesional."
    
    # Piper command line is often the easiest way to use it
    # echo "text" | piper --model model.onnx --output_file output.wav
    
    piper_exe = r"c:\proyectos\vitaminas\.venv_marketing\Scripts\piper.exe"
    
    command = f'echo "{text}" | "{piper_exe}" --model "{onnx_path}" --output_file "{output_wav}"'
    
    print(f"Running: {command}")
    # Using shell=True for echo and piping
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"Audio generated successfully: {output_wav}")
    else:
        print(f"Error generating audio: {result.stderr}")

if __name__ == "__main__":
    test_piper()
