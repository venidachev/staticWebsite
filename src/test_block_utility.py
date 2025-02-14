import unittest
from block_utility import markdown_to_blocks, block_to_block_type

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

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a paragraph"
        expected = "paragraph"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)

    def test_heading(self):
        block = "# This is a heading"
        expected = "heading"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)

    def test_heading_no_space(self):
        block = "#This is a heading"
        expected = "paragraph"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)

    def test_heading_6_hashes(self):
        block = "###### This is a heading"
        expected = "heading"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)

    def test_heading_7_hashes(self):
        block = "####### This is a heading"
        expected = "paragraph"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)

    def test_unordered_list_asterisk(self):
        block = """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        expected = "unordered_list"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)

    def test_unordered_list_dash(self):
        block = """- This is the first list item in a list block
- This is a list item
- This is another list item"""
        expected = "unordered_list"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)

    def test_unordered_list_one_invalid(self):
        block = """- This is the first list item in a list block
 This is a list item
- This is another list item"""
        expected = "paragraph"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)

    def test_unordered_list_mixed(self):
        block = """- This is the first list item in a list block
- This is a list item
* This is another list item"""
        expected = "unordered_list"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)

    def test_code(self):
        block = """```- This is the first list item in a list block
- This is a list item
- This is another list item```"""
        expected = "code"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)

    def test_code_unclosed(self):
        block = """```- This is the first list item in a list block
- This is a list item
- This is another list item``"""
        expected = "paragraph"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)

    def test_ordered_list(self):
        block = """1. This is the first list item in a list block
2. This is a list item
3. This is another list item``"""
        expected = "ordered_list"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)
    
    def test_ordered_list_no_dot(self):
        block = """1. This is the first list item in a list block
2 This is a list item
3. This is another list item``"""
        expected = "paragraph"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)

    def test_ordered_list_invalid_start(self):
        block = """2. This is the first list item in a list block
3. This is a list item
4. This is another list item``"""
        expected = "paragraph"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)

    def test_ordered_list_no_space(self):
        block = """1.This is the first list item in a list block
2. This is a list item
3. This is another list item``"""
        expected = "paragraph"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)

    def test_quote(self):
        block = """>This is the first list item in a list block
> This is a list item
>> This is another list item``"""
        expected = "quote"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)

    def test_quote_missed_line(self):
        block = """>This is the first list item in a list block
> This is a list item
This is another list item``"""
        expected = "paragraph"
        output = block_to_block_type(block)
        self.assertEqual(expected, output)