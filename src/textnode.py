from enum import Enum
from typing import Self

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC= "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, type: TextType, url: str = None):
        self.text = text
        self.type = type
        self.url = url

    def __eq__(self, other: Self):
        cond1 = self.text == other.text
        cond2 = self.type == other.type
        cond3 = self.url == other.url
        return cond1 and cond2 and cond3
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"
