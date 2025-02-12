import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_empty(self):
        with self.assertRaises(TypeError):
            node = ParentNode()
        
    def test_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, None)

    def test_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", None)

    def test_nested_parents(self):
        i_leaf = LeafNode("i", "italics")
        b_leaf = LeafNode("b", "boold")
        and_leaf = LeafNode(None, " and ")
        paragraph = ParentNode("p", [i_leaf, and_leaf, b_leaf])
        html = ParentNode("html", [paragraph, paragraph], {"lang": "en"})
        self.assertEqual(html.to_html(), '<html lang="en"><p><i>italics</i> and <b>boold</b></p><p><i>italics</i> and <b>boold</b></p></html>')

if __name__ == "__main__":
    unittest.main()