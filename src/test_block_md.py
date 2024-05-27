import unittest

from block_md import (
    markdown_to_blocks,
    markdown_to_html_node,
    block_to_block_type,
    block_type_heading,
    block_type_paragraph,
    block_type_quote,
    block_type_code,
    block_type_unordered_list,
    block_type_ordered_list,
)


class TestBlockMd(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
          This is **bolded** paragraph

          This is another paragraph with *italic* text and `code` here
          This is the same paragraph on a new line

          * This is a list
          * with items
        """

        self.assertEqual(len(markdown_to_blocks(md)), 3)

    def test_markdown_to_blocks_newlines(self):
        md = f"This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items\n"

        self.assertEqual(len(markdown_to_blocks(md)), 3)

    def test_block_to_block_heading(self):
        heading = "###### 123"
        self.assertEqual(block_to_block_type(heading), block_type_heading)

    def test_block_to_block_heading_fail(self):
        heading = "########## 1234"
        self.assertEqual(block_to_block_type(heading), block_type_paragraph)

    def test_block_to_block_quote(self):
        quote = f">This is a quote\n>More of the quote\n>Quote"
        self.assertEqual(block_to_block_type(quote), block_type_quote)

    def test_block_to_block_quote_fail(self):
        quote = f">This is a quote\nMore of the quote\n>Quote"
        self.assertEqual(block_to_block_type(quote), block_type_paragraph)

    def test_block_to_block_code(self):
        code = f"```This is code.\nHere is more code```"
        self.assertEqual(block_to_block_type(code), block_type_code)

    def test_block_to_block_code_fail(self):
        code = f"```This is code. Here is more code``"
        self.assertEqual(block_to_block_type(code), block_type_paragraph)

    def test_block_to_block_unordered_list(self):
        ul_list = f"* This is part of the ul list\n- So is this\n* And this"
        self.assertEqual(block_to_block_type(ul_list), block_type_unordered_list)

    def test_block_to_block_unordered_list_fail(self):
        ul_list = f"* This is part of the ul list\n So is this\n* And this"
        self.assertEqual(block_to_block_type(ul_list), block_type_paragraph)

    def test_block_to_block_ordered_list(self):
        ol_list = f"1. This is an ordered list item\n2. Here's the second item.\n3. And the third"
        self.assertEqual(block_to_block_type(ol_list), block_type_ordered_list)

    def test_block_to_block_ordered_list_fail(self):
        ol_list = f"1. This is an ordered list item\n3. Here's the second item.\n3. And the third"
        self.assertEqual(block_to_block_type(ol_list), block_type_paragraph)

    def test_markdown_to_html(self):
        md_doc = f"# Heading\n\nThis is **some** text right here\nHere's more text\n\n## Heading 2\n\n### Heading 3\n\n#### Heading 4\n\n##### Heading 5\n\n###### Heading 6\n\n```Some code will go here And here```\n\n1. One nice ordered list\n2. With **two** items\n\n* An unordered *italic* list\n- With Different ways to mark it\n- `And a line of code`\n\n>Finished with a nice *quote*\n>From your favorite noobie\n>Me - Newbster McGee".lower()
        html_node = markdown_to_html_node(md_doc)
        html = f"<div><h1>heading</h1><p>this is <b>some</b> text right here here's more text</p><h2>heading 2</h2><h3>heading 3</h3><h4>heading 4</h4><h5>heading 5</h5><h6>heading 6</h6><pre><code>some code will go here and here</code></pre><ol><li>one nice ordered list</li><li>with <b>two</b> items</li></ol><ul><li>an unordered <i>italic</i> list</li><li>with different ways to mark it</li><li><code>and a line of code</code></li></ul><blockquote>finished with a nice <i>quote</i> from your favorite noobie me - newbster mcgee</blockquote></div>"

        self.assertEqual(html_node.to_html(), html)


if __name__ == "__main__":
    unittest.main()
