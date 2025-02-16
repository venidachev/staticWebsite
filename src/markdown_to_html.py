from parentnode import ParentNode
from leafnode import LeafNode
from block_utility import markdown_to_blocks, block_to_block_type
from inline_utility import text_to_textnodes, text_node_to_html_node

def markdown_to_html_node(markdown: str) -> ParentNode:
    # parent node's children
    html_node_children: list[ParentNode] = []
    # parent node
    html_node = ParentNode(tag="div", children=html_node_children)
    
    blocks: list[str] = markdown_to_blocks(markdown)

    for block in blocks:
        block_type: str = block_to_block_type(block)

        match block_type:
            case "paragraph":
                html_node_children.append(handle_paragraph(block))
            case "quote":
                html_node_children.append(handle_quote(block))
            case "unordered_list":
                html_node_children.append(handle_unordered_list(block))
            case "ordered_list":
                html_node_children.append(handle_ordered_list(block))
            case "code":
                html_node_children.append(handle_code(block))
            case "heading":
                html_node_children.append(handle_heading(block))
            case _:
                raise ValueError(f"invalid block type: {block_type}")
    return html_node

        

def handle_paragraph(text: str) -> ParentNode:
    return ParentNode("p", children=text_to_children(text))

def handle_quote(block: str) -> ParentNode:
    lines = [line[1:] for line in block.split("\n") if len(line) > 1]
    text = "\n".join(lines)
    return ParentNode("blockquote", children=text_to_children(text.strip()))
    
def handle_unordered_list(block: str) -> ParentNode:
    children: list[ParentNode] = []
    node = ParentNode(tag="ul", children=children)
    # Extract list items
    lines = [line[2:] for line in block.split("\n") if len(line) > 2]
    for text in lines:
        children.append(ParentNode("li", children=text_to_children(text.strip())))
    return node

def handle_ordered_list(block: str) -> ParentNode:
    children: list[ParentNode] = []
    node = ParentNode(tag="ol", children=children)
    # Extract list items
    lines = [line.split(". ", 1)[1] for line in block.split("\n") if ". " in line]
    for text in lines:
        children.append(ParentNode("li", children=text_to_children(text.strip())))
    return node
    

def handle_code(block: str) -> ParentNode:
    # Example input: ```Code!```
    text = block.strip("```").strip()
    child = LeafNode("code", text)
    return ParentNode("pre", children=[child])

def handle_heading(block: str) -> ParentNode:
    # Example input: ### Heading
    # Where # 1-6
    # Split into hashes and 
    hashes, text = block.split(" ", 1)
    tag = f"h{len(hashes)}"
    return ParentNode(tag, children=text_to_children(text.strip()))
   
def text_to_children(text: str) -> list[ParentNode]:
    nodes: list[ParentNode] = []
    text_nodes_list = text_to_textnodes(text.strip())
    for text_node in text_nodes_list:
        nodes.append(text_node_to_html_node(text_node))
    return nodes
    