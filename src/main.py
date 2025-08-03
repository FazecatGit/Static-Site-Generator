from textnode import TextNode, TextType
from website_function import delete_content_directory, recursive_copy, generate_page_recursive
import os
import shutil


def main():
    delete_content_directory("public")
    recursive_copy("static", "public")
    generate_page_recursive("content", "template.html", "public")
    
    # Uncomment the line below to generate a single page
    #generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()