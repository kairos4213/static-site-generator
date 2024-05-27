from htmlnode import ParentNode
from inline_md import text_to_textnodes
from textnode import text_node_to_html_node

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


def block_to_block_type(markdown_block):
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
    elif len(lines) >= 1 and lines[0].startswith("```") and lines[-1].endswith("```"):
        return block_type_code
    elif markdown_block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    elif markdown_block.startswith("- ") or markdown_block.startswith("* "):
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


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def quote_block_to_html(markdown_block):
    lines = markdown_block.split("\n")
    quote = ""
    for item in lines:
        quote += item.lstrip(">") + " "
    html_node = ParentNode("blockquote", text_to_children(quote.rstrip()))
    return html_node


def ul_block_to_html(markdown_block):
    list_items = markdown_block.split("\n")
    html_list = []
    for item in list_items:
        item = item.lstrip("- ")
        item = item.lstrip("* ")
        html_list.append(ParentNode("li", text_to_children(item)))
    html_node = ParentNode("ul", html_list)
    return html_node


def ol_block_to_html(markdown_block):
    list_items = markdown_block.split("\n")
    html_list = []
    for i in range(len(list_items)):
        incrementor = i + 1
        list_items[i] = list_items[i].lstrip(f"{incrementor}. ")
        html_list.append(ParentNode("li", text_to_children(list_items[i])))
    html_node = ParentNode("ol", html_list)
    return html_node


def code_block_to_html(markdown_block):
    code_text = markdown_block.strip("```")
    children = text_to_children(code_text)
    html_node = ParentNode("pre", [ParentNode("code", children)])
    return html_node


def heading_block_to_html(markdown_block):
    html_node = None
    if markdown_block.startswith("# "):
        text = markdown_block.lstrip("# ")
        children = text_to_children(text)
        html_node = ParentNode("h1", children)
    elif markdown_block.startswith("## "):
        text = markdown_block.lstrip("## ")
        children = text_to_children(text)
        html_node = ParentNode("h2", children)
    elif markdown_block.startswith("### "):
        text = markdown_block.lstrip("### ")
        children = text_to_children(text)
        html_node = ParentNode("h3", children)
    elif markdown_block.startswith("#### "):
        text = markdown_block.lstrip("#### ")
        children = text_to_children(text)
        html_node = ParentNode("h4", children)
    elif markdown_block.startswith("##### "):
        text = markdown_block.lstrip("##### ")
        children = text_to_children(text)
        html_node = ParentNode("h5", children)
    else:
        text = markdown_block.lstrip("###### ")
        children = text_to_children(text)
        html_node = ParentNode("h6", children)
    return html_node


def paragraph_block_to_html(markdown_block):
    lines = markdown_block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    html_node = ParentNode("p", children)
    return html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            children.append(heading_block_to_html(block))
        elif block_type == block_type_code:
            children.append(code_block_to_html(block))
        elif block_type == block_type_ordered_list:
            children.append(ol_block_to_html(block))
        elif block_type == block_type_unordered_list:
            children.append(ul_block_to_html(block))
        elif block_type == block_type_quote:
            children.append(quote_block_to_html(block))
        else:
            children.append(paragraph_block_to_html(block))

    html_node = ParentNode("div", children)
    return html_node


md_doc = f"# Heading\n\nThis is **some** text right here\nHere's more text\n\n## Heading 2\n\n### Heading 3\n\n#### Heading 4\n\n##### Heading 5\n\n###### heading 6\n\n```Some code will go here And here```\n\n1. One nice ordered list\n2. With **two** items\n\n* An unordered *italic* list\n- With Different ways to mark it\n- `And a line of code`\n\n>Finished with a nice *quote*\n>From your favorite noobie\n>Me - Newbster McGee".lower()

node = markdown_to_html_node(md_doc)
print(node.to_html())