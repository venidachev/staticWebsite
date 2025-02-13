import unittest
from utility_functions import text_node_to_html_node, split_nodes_delimiter, extract_markdown_images, extract_markdown_links
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

    def test_invalid_text_type_raises(self):
        text_node = TextNode(type="INVALID_TYPE", text="Invalid")
        with self.assertRaises(Exception):  # Expect an exception
            text_node_to_html_node(text_node)

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_regular(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)
    def test_no_closing_delimiter(self):
        node = TextNode("I failed to *italics this text", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "*", TextType.ITALIC)

    def test_no_closing_delimiters(self):
        node = TextNode("I failed to **bold this text, but I bolded **this one**", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_bold_correct(self):
        node = TextNode("Look at me doing correctly  **bolded** text.", TextType.TEXT)
        expected_nodes = [
            TextNode("Look at me doing correctly  ", TextType.TEXT),
            TextNode("bolded", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, expected_nodes)

    def test_list_of_multiple(self):
        node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("Look at me doing correctly  `coded` text.", TextType.TEXT)
        node3 = TextNode("I AM SO SIDEWAYS", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("Look at me doing correctly  ", TextType.TEXT),
            TextNode("coded", TextType.CODE),
            TextNode(" text.", TextType.TEXT),
            TextNode("I AM SO SIDEWAYS", TextType.ITALIC),
        ]
        new_nodes = split_nodes_delimiter([node1, node2, node3], "`", TextType.CODE)
        self.assertEqual(new_nodes, expected_nodes)

class TestImageAndLinkExtraction(unittest.TestCase):
    def test_image_extraction(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images = extract_markdown_images(text)
        expected_output = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extracted_images, expected_output)

    def test_link_extraction(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_links = extract_markdown_links(text)
        expected_output = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extracted_links, expected_output)

    def test_no_image(self):
        text = "[link 1](url tbh) and [link2](imagine this is also a url)"
        extracted_images = extract_markdown_images(text)
        expected_output = []
        self.assertEqual(extracted_images, expected_output)

    def test_no_link(self):
        text = "here is ![image 1](url tbh) and ![image2](imagine this is also a url)"
        extracted_links = extract_markdown_links(text)
        expected_output = []
        self.assertEqual(extracted_links, expected_output)

    def test_multiple_images(self):
        text = "here is ![image 1](url tbh) and ![image2](imagine this is also a url)"
        extracted_images = extract_markdown_images(text)
        expected_output = [("image 1", "url tbh"), ("image2", "imagine this is also a url")]
        self.assertEqual(extracted_images, expected_output)

    def test_multiple_links(self):
        text = "here is [link 1](url tbh) and [link2](imagine this is also a url)"
        extracted_links = extract_markdown_links(text)
        expected_output = [("link 1", "url tbh"), ("link2", "imagine this is also a url")]
        self.assertEqual(extracted_links, expected_output)

# Run the tests
if __name__ == "__main__":
    unittest.main()