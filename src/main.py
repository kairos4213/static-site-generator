import os
import shutil

from copy_static import copy_static_to_public
from generate_html_page import generate_pages_recursive

static_path = "./static"
public_path = "./public"

index_path = "./content/"
template_path = "./template.html"
destinaton_path = "./public/"


def main():
    print(f"Deleting {public_path}...")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    
    print(f"Beginning to copy {static_path}...")
    copy_static_to_public(static_path, public_path)

    generate_pages_recursive(index_path, template_path, destinaton_path)

main()
