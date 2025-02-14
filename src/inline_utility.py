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
        node_text_split = node.text.split(delimiter)
        if node.type != TextType.TEXT or len(node_text_split) == 1:
            return_list.append(node)
            continue
        
        if len(node_text_split) > 1 and len(node_text_split) % 2 == 0:
            raise Exception("matching closing delimiter not found")
        
        if node_text_split[0]:
            return_list.append(TextNode(node_text_split.pop(0), TextType.TEXT))
        
        for i in range(0, len(node_text_split), 2):
            new_nodes = []
            new_nodes.append(TextNode(node_text_split[i], text_type))
            if node_text_split[i+1]:
                new_nodes.append(TextNode(node_text_split[i+1], TextType.TEXT))
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

def text_to_textnodes(text: str) -> list[TextNode]:
    initial_node = TextNode(text, TextType.TEXT)
    result_list: list[TextNode] = []
    result_list = split_nodes_delimiter([initial_node], "**", TextType.BOLD) # bold
    result_list = split_nodes_delimiter(result_list, "*", TextType.ITALIC) # italic
    result_list = split_nodes_delimiter(result_list, "`", TextType.CODE) # code
    result_list = split_nodes_link(result_list) # links
    result_list = split_nodes_image(result_list) # images
    return result_list


def extract_markdown_images(text: str) -> list[tuple]:
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text: str) -> list[tuple]:
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)