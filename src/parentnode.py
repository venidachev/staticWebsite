from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        if tag is None:
            raise ValueError("parent node missing tag")
        if children is None:
            raise ValueError("parent node missing children")
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        html = ""
        # opening tag
        html += f"<{self.tag}{self.props_to_html()}>"
        # children
        for child in self.children:
            html += child.to_html()
        #closing tag
        html += f"</{self.tag}>"
        return html