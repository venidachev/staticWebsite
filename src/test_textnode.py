import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.IMAGE, None)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertEqual(node, node2)
    
    def test_different_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.spikewinn.com")
        self.assertNotEqual(node, node2)

    def test_wrong_text_type(self):
        node = TextNode("This is a text node", "normal", "https://www.spikewinn.com")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.spikewinn.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()