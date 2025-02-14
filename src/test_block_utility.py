import unittest
from block_utility import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_basic_functionality(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]
        output = markdown_to_blocks(markdown)
        self.assertEqual(expected, output)

    def test_extra_white_space(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.


* This is the first list item in a list block
* This is a list item
* This is another list item"""
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]
        output = markdown_to_blocks(markdown)
        # print(output)
        self.assertEqual(expected, output)

    def test_single_block(self):
        markdown = "Single line text"
        expected = ["Single line text"]
        output = markdown_to_blocks(markdown)
        self.assertEqual(expected, output)

    def test_single_block_trailing_newlines(self):
        markdown = "\nSingle line text\n\n\n"
        expected = ["Single line text"]
        output = markdown_to_blocks(markdown)
        self.assertEqual(expected, output)

    def test_only_blank_lines(self):
        markdown = "\n\n"
        expected = []
        output = markdown_to_blocks(markdown)
        self.assertEqual(expected, output)

    def test_only_no_blank_lines(self):
        markdown = "This is a heading\nThis is a paragraph"
        expected = ["This is a heading\nThis is a paragraph"]
        output = markdown_to_blocks(markdown)
        self.assertEqual(expected, output)