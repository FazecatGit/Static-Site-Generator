import sys
from textnode import TextNode, TextType
from website_function import delete_content_directory, recursive_copy, generate_page_recursive, generate_page
import os
import shutil


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    delete_content_directory("docs")
    recursive_copy("static", "docs")
    generate_page_recursive("content", "template.html", "docs", basepath="/")
    generate_page("content/index.md", "template.html", "docs/index.html", basepath)

if __name__ == "__main__":
    main()