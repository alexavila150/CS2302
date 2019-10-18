class Node(object):
    def __init__(self, item=None, left=None, right=None, parent=None):
        self.item = item
        self.left = left
        self.right = right
        self.parent = parent
        self.color = ""

    def set_child(self, direction: str, child):
        if direction is not "left" and direction is not "right":
            return False

        if direction is "left":
            self.left = child
        else:
            self.right = child

        if child is not None:
            child.parent = self
        return True

    def replace_child(self, cur, new):
        if self.left is cur:
            return self.set_child("left", new)
        elif self.right is cur:
            return self.set_child("right", new)
        return False

    def get_grandparent(self):
        if self.parent is None:
            return None

        return self.parent.parent

    def get_uncle(self):
        grandparent = None
        if self.parent is not None:
            grandparent = self.parent.parent

        if grandparent is None:
            return None

        if grandparent.left is self.parent:
            return grandparent.right

        else:
            return grandparent.left


class Tree:
    def __init__(self, item=None):
        self.root = Node(item)

    def rotate_left(self, node):
        right_left_child = node.right.left
        if node.parent is not None:
            node.parent.replace_child(node, node.right)

        else:
            self.root = node.right
            self.root.parent = None

        node.right.set_child("left", node)
        node.set_child("right", right_left_child)

    def rotate_right(self, node):
        left_right_child = node.left.right
        if node.parent is not None:
            node.parent.replace_child(node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        node.left.set_child("right", node)
        node.set_child("left", left_right_child)

    def bst_insert(self, node: Node) -> Node:
        if self.root is None:
            self.root = node
        else:
            cur = self.root
            while cur is not None:
                if node.item < cur.item:
                    if cur.left is None:
                        cur.left = node
                        cur = None
                    else:
                        cur = cur.left
                else:
                    print("item is bigger than cur")
                    if cur.right is None:
                        cur.right = node
                        cur = None
                    else:
                        cur = cur.right
        return node

    def balance(self, node):
        if node.parent is None:
            node.color = "black"
            return

        if node.parent.color is "black":
            return

        parent = node.parent
        grandparent = node.get_grandparent()
        uncle = node.get_uncle()

        if uncle is not None and uncle.color is "red":
            parent.color = uncle.color = "black"
            grandparent.color = "red"
            self.balance(grandparent)
            return

        if node is parent.right and parent is grandparent.left:
            self.rotate_left(parent)
            node = parent
            parent = node.parent

        elif node is parent.left and parent is grandparent.right:
            self.rotate_right(parent)
            node = parent
            parent = node.parent

        parent.color = "black"
        grandparent.color = "red"

        if node is parent.left:
            self.rotate_right(grandparent)
        else:
            self.rotate_right(grandparent)

    def insert(self, item):
        node = Node(item)
        self.bst_insert(node)
        node.color = "red"
        self.balance(node)

    def print(self, node):
        if node is None:
            return

        self.print(node.left)
        print(node.item)
        self.print(node.right)