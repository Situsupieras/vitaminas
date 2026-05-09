from PIL import Image, ImageDraw, ImageFont
import os

def create_slide(text, title, filename, color_bg=(26, 26, 46), color_text=(245, 230, 202), color_accent=(22, 199, 154)):
    # 1280x1080 (Right 2/3 of a 1920x1080 video)
    width, height = 1280, 1080
    img = Image.new('RGB', (width, height), color=color_bg)
    draw = ImageFont and ImageDraw.Draw(img)
    
    # Draw a border or accent line
    draw.rectangle([0, 0, 10, height], fill=color_accent)
    
    # Try to load a font, fallback to default
    try:
        font_title = ImageFont.truetype("arial.ttf", 60)
        font_body = ImageFont.truetype("arial.ttf", 40)
    except:
        font_title = ImageFont.load_default()
        font_body = ImageFont.load_default()

    # Draw Title
    draw.text((100, 100), title.upper(), font=font_title, fill=color_accent)
    
    # Draw Body Text (with wrapping)
    margin = 100
    y_text = 250
    words = text.split()
    line = ""
    for word in words:
        if len(line + word) < 40:
            line += word + " "
        else:
            draw.text((margin, y_text), line, font=font_body, fill=color_text)
            y_text += 60
            line = word + " "
    draw.text((margin, y_text), line, font=font_body, fill=color_text)
    
    # Add Logo placeholder (bottom right)
    draw.text((width - 300, height - 100), "TINITA HEALTH", font=font_body, fill=(255, 255, 255))
    
    img.save(filename)

output_dir = r"c:\proyectos\vitaminas\scratch\slides"
os.makedirs(output_dir, exist_ok=True)

slides_data = [
    ("Muchos profesionales exitosos viven en una paradoja: tienen éxito afuera, pero su motor interno no se apaga nunca.", "LA PARADOJA DEL PROFESIONAL", "slide1.png"),
    ("Andrés Castillo, como tú, es un experto en su campo. Pero el insomnio y la tensión muscular le roban su paz familiar.", "EL CASO DE ANDRÉS", "slide2.png"),
    ("Tu cerebro es una red eléctrica compleja. Cuando el 'acelerador' (glutamato) no tiene 'freno' (GABA), el sistema colapsa.", "LA BIOLOGÍA DEL ESTRÉS", "slide3.png")
]

for text, title, fname in slides_data:
    create_slide(text, title, os.path.join(output_dir, fname))

print("Professional slides generated.")
