import re

from textnode import text_type_text, TextNode, text_type_image, text_type_link


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError(f"Please check {old_node.text} for missing {delimiter}")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            elif i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text
        img_tuples = extract_markdown_images(old_node.text)

        if not img_tuples:
            new_nodes.append(old_node)
            continue

        for img_tup in img_tuples:
            sections = remaining_text.split(f"![{img_tup[0]}]({img_tup[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Please check image section - Not closed")
            new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(img_tup[0], text_type_image, img_tup[1]))

            remaining_text = sections[1]

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, text_type_text))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text
        link_tups = extract_markdown_links(old_node.text)

        for link_tup in link_tups:
            sections = remaining_text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Please check link sections -- Not closed")
            new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link_tup[0], text_type_link, link_tup[1]))

            remaining_text = sections[1]

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, text_type_text))
    return new_nodes
