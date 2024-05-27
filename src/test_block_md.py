import unittest

from block_md import (
    markdown_to_blocks,
    block_to_block,
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
        self.assertEqual(block_to_block(heading), block_type_heading)

    def test_block_to_block_heading_fail(self):
        heading = "########## 1234"
        self.assertEqual(block_to_block(heading), block_type_paragraph)

    def test_block_to_block_quote(self):
        quote = f">This is a quote\n>More of the quote\n>Quote"
        self.assertEqual(block_to_block(quote), block_type_quote)

    def test_block_to_block_quote_fail(self):
        quote = f">This is a quote\nMore of the quote\n>Quote"
        self.assertEqual(block_to_block(quote), block_type_paragraph)

    def test_block_to_block_code(self):
        code = f'```This is code.\nHere is more code```'
        self.assertEqual(block_to_block(code), block_type_code)

    def test_block_to_block_code_fail(self):
        code = f"```This is code. Here is more code``"
        self.assertEqual(block_to_block(code), block_type_paragraph)

    def test_block_to_block_unordered_list(self):
        ul_list = f"* This is part of the ul list\n- So is this\n* And this"
        self.assertEqual(block_to_block(ul_list), block_type_unordered_list)

    def test_block_to_block_unordered_list_fail(self):
        ul_list = f"* This is part of the ul list\n So is this\n* And this"
        self.assertEqual(block_to_block(ul_list), block_type_paragraph)

    def test_block_to_block_ordered_list(self):
        ol_list = f"1. This is an ordered list item\n2. Here's the second item.\n3. And the third"
        self.assertEqual(block_to_block(ol_list), block_type_ordered_list)

    def test_block_to_block_ordered_list_fail(self):
        ol_list = f"1. This is an ordered list item\n3. Here's the second item.\n3. And the third"
        self.assertEqual(block_to_block(ol_list), block_type_paragraph)


if __name__ == "__main__":
    unittest.main()
