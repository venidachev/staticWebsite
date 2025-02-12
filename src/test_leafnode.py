import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_paragraph(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        html = "<p>This is a paragraph of text.</p>"
        self.assertEqual(leaf.to_html(), html)

    def test_props(self):
        leaf = LeafNode("a", "Link!", {
            "href": "https://www.google.com",
            "target": "_blank"
        })
        html = '<a href="https://www.google.com" target="_blank">Link!</a>'
        self.assertEqual(leaf.to_html(), html)

    def test_no_tag(self):
        leaf = LeafNode(None, "Some", {"href": "localhost:8888"})
        html = "Some"
        self.assertEqual(leaf.to_html(), html)

    def test_no_value(self):
        with self.assertRaises(ValueError):
            leaf = LeafNode("p", None)

if __name__ == "__main__":
    unittest.main()