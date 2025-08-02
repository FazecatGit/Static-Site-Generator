import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(tag="div", value="Hello World", props={"class": "greeting"})
        self.assertEqual(node.props_to_html(), ' class="greeting"')

    def test_repr(self):
        node = HTMLNode(tag="span", value="Inline text", props={"style": "color: red"})
        self.assertEqual(repr(node), "HTMLNode(tag=span, value=Inline text, children=None, props={'style': 'color: red'})")

    def test_repr_with_children(self):
        child_node = HTMLNode(tag="span", value="Child text")
        parent_node = HTMLNode(tag="div", children=[child_node], props={"class": "parent"})
        self.assertEqual(repr(parent_node), "HTMLNode(tag=div, value=None, children=[HTMLNode(tag=span, value=Child text, children=None, props=None)], props={'class': 'parent'})")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!")
        self.assertEqual(node.to_html(), '<a>Hello, world!</a>')



    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main(exit=False)
