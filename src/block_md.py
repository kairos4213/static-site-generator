import re

from htmlnode import HTMLNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    block_list = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        block_list.append(block)
    return block_list


def block_to_block(markdown_block):
    lines = markdown_block.splitlines()

    if (
        markdown_block.startswith("# ")
        or markdown_block.startswith("## ")
        or markdown_block.startswith("### ")
        or markdown_block.startswith("#### ")
        or markdown_block.startswith("##### ")
        or markdown_block.startswith("###### ")
    ):
        return block_type_heading
    elif len(lines) > 1 and lines[0].startswith("```") and lines[-1].endswith("```"):
        print(lines[0], lines[-1])
        return block_type_code
    elif markdown_block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    elif markdown_block.startswith("* ") or markdown_block.startswith("* "):
        for line in lines:
            if not line.startswith("- ") and not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list
    elif markdown_block.startswith("1. "):
        for i in range(len(lines)):
            incrementor = i + 1
            if not lines[i].startswith(f"{incrementor}. "):
                return block_type_paragraph
        return block_type_ordered_list
    else:
        return block_type_paragraph
