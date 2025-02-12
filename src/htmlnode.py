from typing import Self
from functools import reduce

class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list[Self] = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        try:
            return reduce(lambda html, key: f'{html} {key}="{self.props[key]}"', self.props, "")
        except TypeError:
            return ""

    def __repr__(self):
        return f"HTMLNode\ntag={self.tag}\nvalue={self.value}\nchildren={self.children}\nprops={self.props}"