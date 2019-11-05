import math

# For all questions, use the following class definitions
class BinaryTreeNode:

    def __init__(self, item=0, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def sum(self):
        return self._sum(self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 7
    # --------------------------------------------------------------------------------------------------------------
    def _sum(self, node):
        if node is None:
            return 0
        return self._sum(node.left) + self._sum(node.right) + node.item

    def sum_at_depth(self, d):
        return self._sum_at_depth(d, self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 8
    # --------------------------------------------------------------------------------------------------------------
    def _sum_at_depth(self, d, node):
        if node is None:
            return 0
        if d == 0:
            return node.item
        return self._sum_at_depth(d - 1, node.left) + self._sum_at_depth(d - 1, node.right)

    def max_val(self):
        return self._max_val(self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 9
    # --------------------------------------------------------------------------------------------------------------
    def _max_val(self, node):
        if node is None:
            return -math.inf
        if node.right is None:
            return node.item
        return self._max_val(node.right)

    def search(self, k):
        return self._search(k, self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 10
    # --------------------------------------------------------------------------------------------------------------
    def _search(self, k, node):
        if node is None:
            return None
        if k > node.item:
            return self._search(k, node.right)
        if k < node.item:
            return self._search(k, node.left)

        return node


