import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "this is a hyperlink",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        html_props = f' href="https://www.google.com" target="_blank"'

        self.assertEqual(node.props_to_html(), html_props)

    def test_leaf_node_no_props(self):
        node = LeafNode("p", "this is a paragraph")
        html = "<p>this is a paragraph</p>"

        self.assertEqual(node.to_html(), html)

    def test_leaf_node_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        html = f'<a href="https://www.google.com">Click me!</a>'

        self.assertEqual(node.to_html(), html)

    def test_leaf_node_no_tag(self):
        node = LeafNode(None, "this is a paragraph")
        html = "this is a paragraph"

        self.assertEqual(node.to_html(), html)

    def test_parent_node_no_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        html = f"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"

        self.assertEqual(node.to_html(), html)

    def test_parent_node_with_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"href": "https://www.google.com", "target": "_blank"},
        )
        html = f'<p href="https://www.google.com" target="_blank"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'

        self.assertEqual(node.to_html(), html)

    def test_parent_node_with_parent_nodes(self):
        node = ParentNode(
            "ul",
            [
                ParentNode("li", [LeafNode("i", "Italic text")]),
                ParentNode("li", [LeafNode("i", "Italic text")]),
                ParentNode("li", [LeafNode("i", "Italic text")]),
            ],
        )
        html = f"<ul><li><i>Italic text</i></li><li><i>Italic text</i></li><li><i>Italic text</i></li></ul>"

        self.assertEqual(node.to_html(), html)

    def test_three_layer_parent_node_with_props(self):
        node = ParentNode(
            "ul",
            [
                ParentNode(
                    "li",
                    [
                        LeafNode("h3", "Some Heading"),
                        ParentNode(
                            "ol",
                            [
                                LeafNode(
                                    "a", "link to boot.dev", {"href": "www.boot.dev"}
                                ),
                                LeafNode(
                                    "a", "link to google", {"href": "www.google.com"}
                                ),
                                LeafNode(
                                    "a", "link to youtube", {"href": "www.youtube.com"}
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )
        html = f'<ul><li><h3>Some Heading</h3><ol><a href="www.boot.dev">link to boot.dev</a><a href="www.google.com">link to google</a><a href="www.youtube.com">link to youtube</a></ol></li></ul>'

        self.assertEqual(node.to_html(), html)


if __name__ == "__main__":
    unittest.main()
