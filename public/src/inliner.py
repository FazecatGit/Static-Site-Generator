import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
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
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        sections = re.split(r'\[([^\]]+)\]\(([^)]+)\)', old_node.text)
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 3 == 0:
                new_nodes.append(TextNode(sections[i], TextType.TEXT))
            elif i % 3 == 1:
                new_nodes.append(TextNode(sections[i], TextType.LINK))
            elif i % 3 == 2:
                new_nodes[-1].url = sections[i]
    return new_nodes
