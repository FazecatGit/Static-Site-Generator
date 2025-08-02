from src.textnode import TextNode, TextType
from website_function import *

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    recursive_copy("static", "public")

if __name__ == "__main__":
    main()