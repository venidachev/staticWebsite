from block_utility import markdown_to_blocks
from markdown_to_html import markdown_to_html_node
import os

def extract_title(markdown: str):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.strip().startswith("# "):
            return block[2:].strip()
    return ""

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
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

def generate_page_recursive(dir_path: str, template_path: str, dest_dir_path: str) -> None:

    dir_content = os.listdir(dir_path)

    for file in dir_content:
        file_path = os.path.join(dir_path, file)
        new_dest_dir_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(file_path) and file_path.endswith(".md"):

            generate_page(file_path, template_path, new_dest_dir_path.replace(".md", ".html"))

        if os.path.isdir(file_path):
            os.mkdir(new_dest_dir_path)
            generate_page_recursive(file_path, template_path, new_dest_dir_path)