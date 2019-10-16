class StudentInformation:
    last_name = "Avila"
    first_name = "Alex"
    utep_id = "80631370"


class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def sum_all(self, node=None):  # Quiz Problem 1
        if node is None:
            return 0

        return self.sum_all(node.left) + self.sum_all(node.right) + node.item

    def min_at_depth(self, depth, node=None):  # Quiz Problem 2
        if node is None:
            return float("inf")

        if depth == 0:
            return node.item

        return min(self.min_at_depth(depth - 1, node.left), self.min_at_depth(depth - 1, node.right))

        return 0

    def count_smaller_than_k(self, k, node=None):  # Quiz Problem 3
        if node is None:
            return 0

        if node.item < k:
            return 1 + self.count_smaller_than_k(k, node.left) + self.count_smaller_than_k(k, node.right)

        return self.count_smaller_than_k(k, node.left) + self.count_smaller_than_k(k, node.right)

def main():
    tree = BinaryTree(Node(1))
    root = tree.root
    root.left = Node(2)
    root.right = Node(5)
    root.left.right = Node(4)
    root.left.left = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(3)

    print(tree.count_smaller_than_k(6, root))

if __name__=="__main__":
    main()
