import asyncio
import edge_tts

async def generate_audio():
    input_file = r"c:\proyectos\vitaminas\scratch\masterclass_section1_pro.txt"
    output_file = r"c:\proyectos\vitaminas\Magnesio citrato y glicinato\n8n_output\08_masterclass_section1_pro.mp3"
    
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Voice for Guatemala
    voice = "es-GT-AndresNeural"
    
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    print(f"Professional audio saved to {output_file}")

if __name__ == "__main__":
    asyncio.run(generate_audio())
