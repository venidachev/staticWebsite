import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_print_none(self):
        html = HTMLNode()
        self.assertEqual(repr(html), "HTMLNode\ntag=None\nvalue=None\nchildren=None\nprops=None")

    def test_print_props_to_html(self):
        html = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank"
        })
        self.assertEqual(' href="https://www.google.com" target="_blank"', html.props_to_html())

    def test_print_props_to_html_none(self):
        html = HTMLNode()
        self.assertEqual("", html.props_to_html())

if __name__ == "__main__":
    unittest.main()