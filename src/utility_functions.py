from textnode import TextNode, TextType
from leafnode import LeafNode
import re

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("invalid text type")
        
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    return_list = []

    for node in old_nodes:
        if node.type != TextType.TEXT:
            return_list.append(node)
            continue
        node_text_split = node.text.split(delimiter)

        if len(node_text_split) > 1 and len(node_text_split) % 3 != 0:
            raise Exception("matching closing delimiter not found")
        
        for i in range(0, len(node_text_split), 3):
            new_nodes = [
                TextNode(node_text_split[i], TextType.TEXT),
                TextNode(node_text_split[i+1], text_type),
                TextNode(node_text_split[i+2], TextType.TEXT)
            ]
            return_list.extend(new_nodes)
    return return_list

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    pass

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    pass

def extract_markdown_images(text: str) -> list[tuple]:
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text: str) -> list[tuple]:
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)