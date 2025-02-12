import unittest
from node_converter import text_node_to_html_node
from textnode import TextNode, TextType
from leafnode import LeafNode

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_type_text(self):
        text_node = TextNode(type=TextType.TEXT, text="Hello, world!")
        result = text_node_to_html_node(text_node)
        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, None)  # No tag for plain text
        self.assertEqual(result.value, "Hello, world!")

    def test_text_type_bold(self):
        text_node = TextNode(type=TextType.BOLD, text="Bold text")
        result = text_node_to_html_node(text_node)
        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, "b")
        self.assertEqual(result.value, "Bold text")

    # Add more tests for other TextTypes...

    def test_invalid_text_type_raises(self):
        text_node = TextNode(type="INVALID_TYPE", text="Invalid")
        with self.assertRaises(Exception):  # Expect an exception
            text_node_to_html_node(text_node)

# Run the tests
if __name__ == "__main__":
    unittest.main()