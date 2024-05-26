import unittest

from inline import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)
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

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        extracted = [
            (
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            (
                "another",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png",
            ),
        ]

        self.assertEqual(extract_markdown_images(text), extracted)

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        extracted = [
            ("link", "https://www.example.com"),
            ("another", "https://www.example.com/another"),
        ]

        self.assertEqual(extract_markdown_links(text), extracted)

    def test_split_nodes_image(self):
        old_nodes = [
            TextNode("This is text", text_type_text),
            TextNode(
                "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                text_type_text,
            ),
        ]
        new_nodes = [
            TextNode("This is text", text_type_text),
            TextNode("This is text with an ", text_type_text),
            TextNode(
                "image",
                text_type_image,
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second image",
                text_type_image,
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
            ),
        ]

        self.assertEqual(split_nodes_image(old_nodes), new_nodes)

    def test_split_nodes_link(self):
        old_nodes = [
            TextNode("this is text", text_type_text),
            TextNode(
                "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
                text_type_text,
            ),
        ]
        new_nodes = [
            TextNode("this is text", text_type_text),
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://www.example.com"),
            TextNode(" and ", text_type_text),
            TextNode("another", text_type_link, "https://www.example.com/another"),
        ]

        self.assertEqual(split_nodes_link(old_nodes), new_nodes)

    def test_text_to_textnodes(self):
        mkdwn = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        nodes = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode(
                "image",
                text_type_image,
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]

        self.assertEqual(text_to_textnodes(mkdwn), nodes)


if __name__ == "__main__":
    unittest.main()
