import unittest
from page_utility import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_functionality(self):
        md = "# Hello"
        expected = "Hello"
        output = extract_title(md)
        self.assertEqual(expected, output)

    def test_empty(self):
        md = ""
        expected = ""
        output = extract_title(md)
        self.assertEqual(expected, output)

    def test_h2(self):
        md = "## Hello"
        expected = ""
        output = extract_title(md)
        self.assertEqual(expected, output)

    def test_2nd_block(self):
        md = "## Hello\n\n#  Hii  "
        expected = "Hii"
        output = extract_title(md)
        self.assertEqual(expected, output)