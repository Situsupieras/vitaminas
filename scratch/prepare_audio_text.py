import re

def clean_script(text):
    # Remove markdown bold
    text = text.replace("**", "")
    # Remove [Visual: ...] blocks
    text = re.sub(r"\[Visual:.*?\]", "", text, flags=re.DOTALL)
    # Remove (PARENTICAL) blocks
    text = re.sub(r"\(.*?\)", "", text, flags=re.DOTALL)
    # Remove Speaker labels
    text = re.sub(r"NARRADOR.*?:", "", text)
    text = re.sub(r"CONFERENCISTA.*?:", "", text)
    # Remove horizontal rules
    text = text.replace("---", "")
    # Remove extra newlines
    text = "\n".join([line.strip() for line in text.split("\n") if line.strip()])
    return text

input_file = r"c:\proyectos\vitaminas\Magnesio citrato y glicinato\n8n_output\08_masterclass_script_60min.md"
output_file = r"c:\proyectos\vitaminas\scratch\masterclass_section1_clean.txt"

with open(input_file, "r", encoding="utf-8") as f:
    full_content = f.read()

# Extract Section 1 (everything between "## 0-10 min" and "## 10-25 min")
start_marker = "## 0-10 min: La Apertura y la Paradoja del Profesional"
end_marker = "## 10-25 min: La Biologia del Estres (El Motor)"

start_idx = full_content.find(start_marker)
end_idx = full_content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    section1 = full_content[start_idx + len(start_marker):end_idx]
    # Remove the introductory text at the beginning of the section
    intro_end = section1.find("---")
    if intro_end != -1:
        section1 = section1[intro_end + 3:]
    
    clean_text = clean_script(section1)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(clean_text)
    print(f"Clean text saved to {output_file}")
else:
    print("Could not find section markers")
