import os
import shutil

def copy_static_to_public(src="static", dst="public"):
    # Step 1: Delete destination if it exists
    if os.path.exists(dst):
        print(f"Deleting existing '{dst}' directory...")
        shutil.rmtree(dst)

    # Step 2: Recursively copy everything from src to dst
    def recursive_copy(src_path, dst_path):
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)

        for item in os.listdir(src_path):
            src_item_path = os.path.join(src_path, item)
            dst_item_path = os.path.join(dst_path, item)

            if os.path.isfile(src_item_path):
                shutil.copy(src_item_path, dst_item_path)
                print(f"Copied file: {src_item_path} -> {dst_item_path}")
            else:
                # It's a directory, recurse
                recursive_copy(src_item_path, dst_item_path)

    recursive_copy(src, dst)


if __name__ == "__main__":
    copy_static_to_public()