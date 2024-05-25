import unittest

from htmlnode import HTMLNode, LeafNode


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

if __name__ == "__main__":
    unittest.main()
