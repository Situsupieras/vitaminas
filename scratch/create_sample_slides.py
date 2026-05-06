from PIL import Image, ImageDraw, ImageFont
import os

def create_slide(text, subtitle, filename):
    # Dimensions for 1080p (2/3 of 1920 is 1280)
    # But let's just make full 1280x720 slides for simplicity
    width, height = 1280, 720
    background_color = (26, 26, 46) # Azul oscuro profundo de TINITA HEALTH
    
    img = Image.new('RGB', (width, height), color=background_color)
    draw = ImageDraw.Draw(img)
    
    # Try to load a font, fallback to default
    try:
        font_title = ImageFont.truetype("arial.ttf", 60)
        font_subtitle = ImageFont.truetype("arial.ttf", 30)
    except:
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
    
    # Draw Title
    draw.text((100, 250), text, fill=(22, 199, 154), font=font_title) # Verde salud
    # Draw Subtitle
    draw.text((100, 350), subtitle, fill=(245, 230, 202), font=font_subtitle) # Crema cálido
    
    # Draw Logo Placeholder
    draw.rectangle([1100, 600, 1250, 700], outline=(255, 255, 255))
    draw.text((1120, 640), "TINITA", fill=(255, 255, 255))
    
    img.save(filename)
    print(f"Slide saved: {filename}")

output_dir = r"c:\proyectos\vitaminas\scratch\slides"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

create_slide("LA PARADOJA DEL PROFESIONAL", "Recupera tu Mente y Cuerpo con Magnesio Dual", os.path.join(output_dir, "slide1.png"))
create_slide("ANDRÉS CASTILLO: EL CASO", "Arquitecto Senior - Guatemala", os.path.join(output_dir, "slide2.png"))
create_slide("EL MOTOR ENCENDIDO", "Sistema Simpático vs Parasimpático", os.path.join(output_dir, "slide3.png"))
