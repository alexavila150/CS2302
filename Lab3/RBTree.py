class Node():
    def __init__(self, item = None, left = None, right = None, parent = None):
        self.item = item
        self.left = left
        self.right = right
        self.parent = parent


class Tree():
    def __init__(self, item = None):
        self.root = Node(item)

    def insert(self, item):
        if self.root is None:      # Root is None
            self.root = Node(item)
            self.parent = None
            return



