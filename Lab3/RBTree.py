class Node(object):
    def __init__(self, item=None, left=None, right=None, parent=None):
        self.item = item
        self.left = left
        self.right = right
        self.parent = parent
        self.color = ""
        self.embedding = []

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

    def get_sibling(self):
        if self.parent is not None:
            if self is self.parent.left:
                return self.parent.right
            return self.parent.left
        return None

    def get_predecessor(self):
        cur = self.left
        while cur.right is not None:
            cur = cur.right
        return cur

    def are_both_children_black(self) -> bool:
        if self.left is not None and self.left.color is "red":
            return False
        if self.right is not None and self.right.color is "red":
            return True

    def separate_word_and_embedding(self):
        words = self.item.split()
        self.item = words[0]
        self.embedding = words.pop(0)

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

    def bst_search(self, item):
        cur = self.root
        while cur is not None:
            if item == cur.item:
                return cur
            elif item < cur.item:
                cur = cur.left
            else:
                cur = cur.right
        return None

    def bst_insert(self, node: Node) -> Node:
        if self.root is None or self.root.item is None:
            self.root = node
        else:
            cur = self.root
            while cur is not None:
                if node.item < cur.item:
                    if cur.left is None:
                        cur.left = node
                        node.parent = cur
                        cur = None
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = node
                        node.parent = cur
                        cur = None
                    else:
                        cur = cur.right
        return node

    def bst_remove(self, item):
        par = None
        cur = self.root
        while cur is not None:
            if cur.item == item:
                if cur.left is None and cur.right is None:  # Remove Leaf
                    if par is None:
                        self.root = None
                    elif par.left is cur:
                        par.left = None
                    else:
                        par.right = None

                elif cur.left is not None and cur.right is None: # Remove node with only left child
                    if par is None:
                        self.root = cur.left
                    elif par.left is cur:
                        par.left = cur.left
                    else:
                        par.right = cur.left

                elif cur.left is None and cur.right is not None:
                    if par is None:
                        self.root = cur.right
                    elif par.left is cur:
                        par.left = cur.right
                    else:
                        par.right = cur.right

                else:
                    suc = cur.right
                    while suc.left is not None:
                        suc = suc.left
                    suc_item = suc.item
                    self.bst_remove(suc.item)
                    cur.item = suc_item
                return

            elif cur.item < item:
                par = cur
                cur = cur.right

            else:
                par = cur
                cur = cur.left

        return

    def balance(self, node):
        if node.parent is None:  # Parent is None
            node.color = "black"
            return

        if node.parent.color is "black":  # Parent color is Black
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
            self.rotate_left(grandparent)

    def insert(self, item):
        node = Node(item)
        self.bst_insert(node)
        node.color = "red"
        self.balance(node)

    def is_non_none_and_red(self, node):
        if node is None:
            return False
        return node.color is "red"

    def is_none_or_black(self, node):
        if node is None:
            return True
        return node.color is "black"

    def try_case_1(self, node):
        return node.color is "red" or node.parent is None

    def try_case_2(self, node, sibling):
        if sibling.color is "red":
            node.parent.color = "red"
            sibling.color = "black"
            if node is node.parent.left:
                self.rotate_left(node.parent)
            else:
                self.rotate_right(node.parent)
            return True
        return False

    def try_case_3(self, node, sibling):
        if node.parent.color is "black" and sibling.are_both_children_black():
            sibling.color = "red"
            self.prepare_for_removal(node.parent)
            return True
        return False

    def try_case_4(self, node, sibling):
        if node.parent.color is "red" and sibling.are_both_children_black():
            node.parent.color = "black"
            sibling.color = "red"
            return True
        return False

    def try_case_5(self, node, sibling):
        if (self.is_non_none_and_red(sibling.left)
            and self.is_none_or_black(sibling.right)
            and node is node.parent.left):

            sibling.color = "red"
            sibling.left.color = "black"
            self.rotate_right(sibling)
            return True
        return False

    def try_case_6(self, node, sibling):
        if (self.is_none_or_black(sibling.left)
            and self.is_non_none_and_red(sibling.right)
            and node is node.parent.right):
            sibling.color = "red"
            sibling.right.color = "black"
            self.rotate_left(sibling)
            return True
        return False

    def prepare_for_removal(self, node):
        if self.try_case_1(node):
            return

        sibling = node.get_sibling()
        if self.try_case_2(node, sibling):
            sibling = node.get_sibling()
        if self.try_case_3(node, sibling):
            return
        if self.try_case_4(node, sibling):
            return
        if self.try_case_5(node, sibling):
            sibling = node.get_sibling()
        if self.try_case_6(node, sibling):
            sibling = node.get_sibling()


    def remove_node(self, node):
        if node.left is not None and node.right is not None:
            predecessor_node = node.get_predecessor()
            predecessor_item = predecessor_node.item
            self.remove_node(predecessor_node)
            node.item = predecessor_item
            return
        if node.color is "black":
            self.prepare_for_removal(node)

        self.bst_remove(node.item)

    def remove(self, item):
        node = self.bst_search(item)
        if node is not None:
            self.remove_node(node)


    def print(self, node):
        if node is None:
            return

        print(node.item)
        self.print(node.left)
        self.print(node.right)

    def separate_all_embeddings(self, node: Node):
        if node is None:
            return

        node.separate_word_and_embedding()
        self.separated_all_embeddings(node.left)
        self.separated_all_embeddings(node.right)