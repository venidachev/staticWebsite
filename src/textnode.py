from enum import Enum
from typing import Self

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC= "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: Self):
        cond1 = self.text == other.text
        cond2 = self.text_type == other.text_type
        cond3 = self.url == other.url
        return cond1 and cond2 and cond3
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
