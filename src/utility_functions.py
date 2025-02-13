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
    return split_nodes_process(old_nodes, "image")

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes_process(old_nodes, "link")

def split_nodes_process(old_nodes: list[TextNode], opt: str) -> list[TextNode]:
    if opt == "link":
        text_type = TextType.LINK
        split_start = "["
        splitter_func = extract_markdown_links
    elif opt == "image":
        text_type = TextType.IMAGE
        split_start = "!["
        splitter_func = extract_markdown_images
    else:
        raise ValueError(f"Invalid split_nodes_process option: {opt}")

    return_list: list[TextNode] = []

    for node in old_nodes:
        split_nodes_list = splitter_func(node.text)
        if len(split_nodes_list) == 0:
            return_list.append(node)
            continue

        text_to_split = node.text
        for split_node in split_nodes_list:
            text = split_node[0]
            url = split_node[1]

            sections = text_to_split.split(f"{split_start}{text}]({url})", 1)

            text_before_link = sections[0]
            text_to_split = sections[1] if len(sections) > 1 else ""

            list_to_extend = []
            if text_before_link:
                list_to_extend.append(TextNode(text_before_link, TextType.TEXT))
            list_to_extend.append(TextNode(text, text_type, url))

            return_list.extend(list_to_extend)
        if text_to_split:
            return_list.append(TextNode(text_to_split, TextType.TEXT))
    return return_list

def extract_markdown_images(text: str) -> list[tuple]:
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text: str) -> list[tuple]:
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)