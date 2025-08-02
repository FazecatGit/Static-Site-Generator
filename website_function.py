import os
import shutil

def delete_static_directory(src="static", dst="public"):
    if os.path.exists(dst):
        print(f"Deleting existing '{dst}' directory...")
        shutil.rmtree(dst)


def recursive_copy(src_path, dst_path):
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)

    for item in os.listdir(src_path):
        src_item_path = os.path.join(src_path, item)
        dst_item_path = os.path.join(dst_path, item)

        if os.path.isfile(src_item_path):
            shutil.copy(src_item_path, dst_item_path)
            print(f"Copied file: {src_item_path} -> {dst_item_path}")
        elif os.path.isdir(src_item_path):
            recursive_copy(src_item_path, dst_item_path)