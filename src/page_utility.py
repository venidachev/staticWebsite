from block_utility import markdown_to_blocks
from markdown_to_html import markdown_to_html_node

def extract_title(markdown: str):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.strip().startswith("# "):
            return block[2:].strip()
    return ""

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        md_content = "".join(file.readlines())

    with open(template_path) as file:
        template = "".join(file.readlines())
        
    html_content = markdown_to_html_node(md_content).to_html()
    title = extract_title(md_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)

    with open(dest_path, 'w') as file:
        file.write(template)