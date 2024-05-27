import os
import shutil

from copy_static import copy_static_to_public

static_path = "./static"
public_path = "./public"


def main():
    print(f"Deleting {public_path}...")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    
    print(f"Beginning to copy {static_path}...")
    copy_static_to_public(static_path, public_path)


main()
