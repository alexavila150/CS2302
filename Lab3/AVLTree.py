class Node:
    def __init__(self, item=None, left=None, right=None, parent=None):
        self.item = item
        self.left = left
        self.right = right
        self.parent = parent
        self.height = 0

    def set_child(self, direction: str, child):
        if direction is not "left" and direction is not "right":
            return False

        if direction is "left":
            self.left = child
        else:
            self.right = child

        if child is not None:
            child.parent = self

        self.update_height()
        return True

    def replace_child(self, cur, new):
        if self.left is cur:
            return self.set_child("left", new)
        elif self.right is cur:
            return self.set_child("right", new)
        return False

    def update_height(self):
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        self.height = max(left_height, right_height) + 1

    def get_balance(self):
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        return left_height - right_height


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

    def rebalance(self, node):
        node.update_height()
        if node.get_balance() == -2:
            if node.right.get_balance() == 1:
                self.rotate_right(node.right)
            return self.rotate_left(node)

        elif node.get_balance() == 2:
            if node.left.get_balance() == -1:
                self.rotate_left(node.left)
            return self.rotate_right(node)

        return node

    def insert(self, item):
        if self.root is None or self.root.item is None:      # Root is None
            self.root = Node(item)
            return

        cur = self.root
        node = Node(item)
        while cur is not None:
            if item < cur.item:
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

        node = node.parent
        while node is not None:
            self.rebalance(node)
            node = node.parent

    def print(self, node):
        if node is None:
            return


        self.print(node.left)
        self.print(node.right)
        print(node.item)