import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    print("split_nodes_delimiter input:", [repr(n) for n in old_nodes])
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Text split by delimiter must have an odd number of sections")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    print("split_nodes_DELIMITER output:", new_nodes)
    return new_nodes

def extract_markdown_images(text):
    image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    matches = re.findall(image_pattern, text)
    return matches

def extract_markdown_links(text):
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(link_pattern, text)
    return matches

def split_nodes_images(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if not re.search(r'!\[([^\]]*)\]\(([^)]+)\)', old_node.text):
            new_nodes.append(old_node)
            continue
        sections = re.split(r'!\[([^\]]*)\]\(([^)]+)\)', old_node.text)
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 3 == 0:
                new_nodes.append(TextNode(sections[i], TextType.TEXT))
            elif i % 3 == 1:
                new_nodes.append(TextNode(sections[i], TextType.IMAGE))
            elif i % 3 == 2:
                new_nodes[-1].url = sections[i]
    print("split_nodes_images output:", new_nodes)
    return new_nodes

def split_nodes_links(old_nodes):
    import re
    new_nodes = []
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        matches = list(re.finditer(link_pattern, old_node.text))
        if not matches:
            # Only return the original node once!
            new_nodes.append(old_node)
            continue
        last_index = 0
        for match in matches:
            start, end = match.span()
            if start > last_index:
                new_nodes.append(TextNode(old_node.text[last_index:start], TextType.TEXT))
            new_nodes.append(TextNode(match.group(1), TextType.LINK, match.group(2)))
            last_index = end
        if last_index < len(old_node.text):
            new_nodes.append(TextNode(old_node.text[last_index:], TextType.TEXT))
    return new_nodes


def text_to_textnode(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    print("After BOLD:", [n.text for n in nodes])
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    print("After ITALIC:", [n.text for n in nodes])
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    print("After CODE:", [n.text for n in nodes])
    nodes = split_nodes_images(nodes)
    print("After IMAGES:", [n.text for n in nodes])
    nodes = split_nodes_links(nodes)
    print("After LINKS:", [n.text for n in nodes])
    return nodes