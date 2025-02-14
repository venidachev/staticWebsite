import re

def markdown_to_blocks(markdown: str) -> list[str]:
    """Takes a raw Markdown string (representing a full document) as input and returns a list of \"block\" strings."""
    return [block.strip() for block in markdown.split("\n\n") if block.strip()]

def block_to_block_type(block: str) -> str:
    """Takes a single block of markdown text as input and returns a string representing the type of block it is.
    The 6 types being: paragraph, heading, code, quote, unordered_list, ordered_list."""
    # Heading
    regex = r"^#{1,6} "
    if re.match(regex, block):
        return "heading"
    # Code
    if block.startswith("```") and block.endswith("```"):
        return "code"
    # Quote
    if all(line.startswith(">") for line in block.split("\n")):
           return "quote"
    # Unordered list
    if all(line.startswith("* ") or line.startswith("- ") for line in block.split("\n")):
         return "unordered_list"
    # Ordered list
    if all(line.startswith(f"{i}. ") for i, line in enumerate(block.split("\n"), start=1)):
        return "ordered_list"
    # Paragraph
    return "paragraph"