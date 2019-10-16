class StudentInformation:
    last_name = "Avila"
    first_name = "Alex"
    utep_id = "80631370"


class MultipleChoice:
    @staticmethod
    def get_problem_1_answer():
        return 1  # If you think the answer is option n, return n

    @staticmethod
    def get_problem_2_answer():
        return 0  # If you think the answer is option n, return n


class BTreeNode:
    # Constructor
    def __init__(self, keys=[], children=[], is_leaf=True, max_num_keys=5):
        self.keys = keys
        self.children = children
        self.is_leaf = is_leaf
        if max_num_keys < 3:  # max_num_keys must be odd and greater or equal to 3
            max_num_keys = 3
        if max_num_keys % 2 == 0:  # max_num_keys must be odd and greater or equal to 3
            max_num_keys += 1
        self.max_num_keys = max_num_keys

    def is_full(self):
        return len(self.keys) >= self.max_num_keys


class BTree:
    # Constructor
    def __init__(self, max_num_keys=5):
        self.max_num_keys = max_num_keys
        self.root = BTreeNode(max_num_keys=max_num_keys)

    def search_at_depth(self, k, d, node=None) -> BTreeNode:  # Quiz question 3
        if node is None:
            return None

        if d.keys.contains(k) and d == 0:
            return d

        search = None
        for child in node.children:
            if search is not None:
                return search
            search = self.search_at_depth(k, d - 1, child)

        return search

    def height(self, node=None):  # Quiz question 4
        if node is None:
            return -1

        height = 0
        cur = node
        while cur.children is not None:
            cur = cur.children[0]
            height += 1

        return height

    def count_even(self, node=None):  # Quiz question 5
        if node is None:
            return 0

        node_evens = 0
        for key in node.keys:
            if key % 2 == 0:
                node_evens += 1

        evens_in_children = 0
        for child in node.children:
            evens_in_children += self.count_even(child)

        return node_evens + evens_in_children



def main():
    tree = BTree()



if __name__=="__main__":
    main()
