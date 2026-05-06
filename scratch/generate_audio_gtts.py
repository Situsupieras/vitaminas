from gtts import gTTS
import os

input_file = r"c:\proyectos\vitaminas\scratch\masterclass_section1_clean.txt"
output_file = r"c:\proyectos\vitaminas\Magnesio citrato y glicinato\n8n_output\08_masterclass_section1_gtts.mp3"

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# Generate audio with Spanish (Latin American accent is not directly selectable in gTTS, but 'es' works)
tts = gTTS(text=text, lang='es')
tts.save(output_file)

print(f"Audio saved to {output_file}")
