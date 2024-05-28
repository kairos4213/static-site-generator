import os

from block_md import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ")
    raise ValueError("Markdown must contain a single h1 header")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as fp:
        source_contents = fp.read()
    html = markdown_to_html_node(source_contents).to_html()
    page_title = extract_title(source_contents)

    with open(template_path, "r+") as tp:
        template_contents = tp.read()
    template_contents = template_contents.replace("{{ Title }}", page_title)
    template_contents = template_contents.replace("{{ Content }}", html)

    if not os.path.dirname(dest_path):
        os.makedirs(dest_path)
    else:
        with open(dest_path, "w") as page:
            page.write(template_contents)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(dir_path_content):
        source = os.path.join(dir_path_content, filename)
        dest = os.path.join(dest_dir_path, filename)
        if os.path.isfile(source):
            generate_page(source, template_path, f"{dest.rstrip(".md")}.html")
        else:
            generate_pages_recursive(source, template_path, dest)
