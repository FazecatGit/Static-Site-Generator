import os
import shutil
from blocks import markdown_to_html_node, extract_title


def delete_content_directory(dst="public"):
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

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} using template {template_path} to {dest_path}")
    

    with open(from_path, 'r') as f:
        content = f.read()

    with open(template_path, 'r') as f:
        template = f.read()

    html_node = markdown_to_html_node(content)
    html_content = html_node.to_html()

    extracted_title = extract_title(content)
    html_content = template.replace("{{ Content }}", html_content)
    html_content = html_content.replace("{{ Title }}", extracted_title)

    html_content = html_content.replace('href="/"', f'href="{basepath}"') 
    html_content = html_content.replace('src="/"', f'src="{basepath}"') 

    # Ensure the destination directory exists

    dest_dir_path = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    with open(dest_path, 'w') as f:
        f.write(html_content)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        if os.path.isfile(item_path):
            if item.endswith('.md'):
                dest_path = os.path.join(dest_dir_path, item.replace('.md', '.html'))
                generate_page(item_path, template_path, dest_path)
        elif os.path.isdir(item_path):
            new_dest_dir = os.path.join(dest_dir_path, item)
            generate_page_recursive(item_path, template_path, new_dest_dir)

        