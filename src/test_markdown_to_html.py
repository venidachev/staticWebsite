import unittest
from markdown_to_html import markdown_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = "This is **bold** and *italic*."
        html = markdown_to_html_node(md)
        # Test structure: div -> p -> [text, bold, text, italic, text]
        self.assertEqual(html.tag, "div")
        p = html.children[0]
        self.assertEqual(p.tag, "p")
        self.assertEqual(len(p.children), 5)  # Text, bold, text, italic, text nodes
        
    def test_headings(self):
        md = "# Heading 1\n\n## Heading 2"
        html = markdown_to_html_node(md)
        # Test both heading levels
        self.assertEqual(html.children[0].tag, "h1")
        self.assertEqual(html.children[1].tag, "h2")
        
    def test_code_blocks(self):
        md = "```\nprint('hello')\n```"
        html = markdown_to_html_node(md)
        pre = html.children[0]
        self.assertEqual(pre.tag, "pre")
        code = pre.children[0]
        self.assertIsInstance(code, LeafNode)
        self.assertEqual(code.value.strip(), "print('hello')")

    def test_lists(self):
        md = "* Item 1\n* Item 2"
        html = markdown_to_html_node(md)
        ul = html.children[0]
        self.assertEqual(ul.tag, "ul")
        self.assertEqual(len(ul.children), 2)
        self.assertEqual(ul.children[0].tag, "li")