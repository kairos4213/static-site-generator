import unittest

from inline import split_nodes_delimiter
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestInline(unittest.TestCase):
    def test_one_node_one_bold(self):
        old_node = [TextNode("This is text with a **bold** word", text_type_text)]
        new_nodes = [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text),
        ]

        self.assertEqual(
            split_nodes_delimiter(old_node, "**", text_type_bold), new_nodes
        )

    def test_multi_nodes_multi_bold(self):
        old_nodes = [
            TextNode(
                "This is text with a **bold word here** and **here**", text_type_text
            ),
            TextNode(
                "This is text with a **bold word here** and **here**", text_type_text
            ),
        ]
        new_nodes = [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold word here", text_type_bold),
            TextNode(" and ", text_type_text),
            TextNode("here", text_type_bold),
            TextNode("This is text with a ", text_type_text),
            TextNode("bold word here", text_type_bold),
            TextNode(" and ", text_type_text),
            TextNode("here", text_type_bold),
        ]

        self.assertEqual(
            split_nodes_delimiter(old_nodes, "**", text_type_bold), new_nodes
        )

    def test_one_node_one_italic(self):
        old_node = [TextNode("This is text with an *italic word*", text_type_text)]
        new_nodes = [
            TextNode("This is text with an ", text_type_text),
            TextNode("italic word", text_type_italic),
        ]

        self.assertEqual(
            split_nodes_delimiter(old_node, "*", text_type_italic), new_nodes
        )

    def test_multi_nodes_multi_italic(self):
        old_nodes = [
            TextNode(
                "This is text with *italic words here* and *here*", text_type_text
            ),
            TextNode(
                "This is text with *italic words here* and *here*", text_type_text
            ),
        ]
        new_nodes = [
            TextNode("This is text with ", text_type_text),
            TextNode("italic words here", text_type_italic),
            TextNode(" and ", text_type_text),
            TextNode("here", text_type_italic),
            TextNode("This is text with ", text_type_text),
            TextNode("italic words here", text_type_italic),
            TextNode(" and ", text_type_text),
            TextNode("here", text_type_italic),
        ]

        self.assertEqual(
            split_nodes_delimiter(old_nodes, "*", text_type_italic), new_nodes
        )

    def test_one_node_one_code(self):
        old_node = [TextNode("This is text with a `code block`", text_type_text)]
        new_nodes = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
        ]

        self.assertEqual(
            split_nodes_delimiter(old_node, "`", text_type_code), new_nodes
        )

    def test_multi_nodes_multi_code(self):
        old_nodes = [
            TextNode(
                "This is text with a `code block here` and `here`", text_type_text
            ),
            TextNode(
                "This is text with a `code block here` and `here`", text_type_text
            ),
        ]
        new_nodes = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block here", text_type_code),
            TextNode(" and ", text_type_text),
            TextNode("here", text_type_code),
            TextNode("This is text with a ", text_type_text),
            TextNode("code block here", text_type_code),
            TextNode(" and ", text_type_text),
            TextNode("here", text_type_code),
        ]

        self.assertEqual(
            split_nodes_delimiter(old_nodes, "`", text_type_code), new_nodes
        )

    def test_not_text_type_only(self):
        old_nodes = [
            TextNode("This is an image", text_type_image, "../image"),
            TextNode("This is a link", text_type_link, "www.google.com"),
        ]
        new_nodes = [
            TextNode("This is an image", text_type_image, "../image"),
            TextNode("This is a link", text_type_link, "www.google.com"),
        ]

        self.assertEqual(
            split_nodes_delimiter(old_nodes, "*", text_type_italic), new_nodes
        )

    def test_not_text_type_with_delimiter(self):
        old_nodes = [
            TextNode("This is an image", text_type_image, "../image"),
            TextNode("This is a link", text_type_link, "www.google.com"),
            TextNode("This is text with an *italic* word", text_type_text),
        ]
        new_nodes = [
            TextNode("This is an image", text_type_image, "../image"),
            TextNode("This is a link", text_type_link, "www.google.com"),
            TextNode("This is text with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word", text_type_text),
        ]

        self.assertEqual(
            split_nodes_delimiter(old_nodes, "*", text_type_italic), new_nodes
        )


if __name__ == "__main__":
    unittest.main()
