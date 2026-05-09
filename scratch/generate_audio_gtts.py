from gtts import gTTS
import os

def generate_audio():
    input_file = r"c:\proyectos\vitaminas\scratch\masterclass_section1_pro.txt"
    output_file = r"c:\proyectos\vitaminas\Magnesio citrato y glicinato\n8n_output\08_masterclass_section1_pro.mp3"
    
    if not os.path.exists(input_file):
        print(f"Input file {input_file} not found.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    if not text.strip():
        print("Text is empty.")
        return

    # Generate audio
    tts = gTTS(text=text, lang='es', tld='com.mx') # Mexican Spanish for better proximity to GT
    tts.save(output_file)
    print(f"Audio saved to {output_file}")

if __name__ == "__main__":
    generate_audio()
