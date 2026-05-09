import re
import os

def final_clean(text):
    # 1. Remove [Visual: ...] blocks (multiline)
    text = re.sub(r"\[Visual:.*?\]", "", text, flags=re.DOTALL)
    # 2. Remove (Parenthetical) blocks (multiline)
    text = re.sub(r"\(.*?\)", "", text, flags=re.DOTALL)
    # 3. Remove Markdown bold/italics
    text = text.replace("**", "").replace("_", "")
    # 4. Remove horizontal rules
    text = text.replace("---", "")
    # 5. Remove Speaker labels
    text = re.sub(r"NARRADOR.*?:", "", text)
    text = re.sub(r"CONFERENCISTA.*?:", "", text)
    # 6. Cleanup quotes
    text = text.replace('"', "")
    # 7. Remove empty lines and fix spacing
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return " ".join(lines)

input_file = r"c:\proyectos\vitaminas\Magnesio citrato y glicinato\n8n_output\08_masterclass_script_60min.md"
output_file = r"c:\proyectos\vitaminas\scratch\masterclass_section1_pro.txt"

with open(input_file, "r", encoding="utf-8") as f:
    full_text = f.read()

# Extract only section 1 for the demo
start_pattern = "MASTERCLASS: LA FÓRMULA TINITA HEALTH"
end_pattern = "## 10-25 min:"

start_idx = full_text.find(start_pattern)
end_idx = full_text.find(end_pattern)

if start_idx != -1 and end_idx != -1:
    section_text = full_text[start_idx:end_idx]
    cleaned = final_clean(section_text)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(cleaned)
    print("Text cleaned successfully.")
else:
    print("Section markers not found.")
