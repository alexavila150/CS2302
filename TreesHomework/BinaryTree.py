class Node(object):
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right


class Tree(object):
    def __init__(self, root):
        self.root = root

    def contains(self, item) -> bool:
        cur = self.root
        while cur is not None:
            if cur.item == item:
                return True
            elif item < cur.item:
                cur = cur.left
            else:
                cur = cur.right
        return False

    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            cur = self.root
            while cur is not None:
                if item < cur.item:
                    if cur.left is None:
                        cur.left = Node(item)
                        cur = None
                    else:
                        cur = cur.left
                else:
                    if cur.left is None:
                        cur.right = Node(item)
                        cur = Node
                    else:
                        cur = cur.right

    def remove(self, item):
        par = None
        cur = self.root
        while cur is not None: # Search for node
            if cur.item == item:
                if cur.left is None and cur.right is None:
                    if par is None:
                        self.root is None
                    elif par.left is cur:
                        par.left = None
                    else:
                        par.right = None
                elif cur.right is None:
                    if par is None:
                        
