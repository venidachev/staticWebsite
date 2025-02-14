def markdown_to_blocks(markdown: str) -> list[str]:
    """Takes a raw Markdown string (representing a full document) as input and returns a list of \"block\" strings."""
    return [block.strip() for block in markdown.split("\n\n") if block.strip()]