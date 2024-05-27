import os
import shutil

def copy_static_to_public(source_dir, dest_dir):
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

  for filename in os.listdir(source_dir):
    source = os.path.join(source_dir, filename)
    dest = os.path.join(dest_dir, filename)
    if os.path.isfile(source):
      shutil.copy(source, dest)
      print(f"{source} copied -> {dest}")
    else:
      copy_static_to_public(source, dest)