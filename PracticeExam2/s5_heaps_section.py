# For all questions, use the following class definitions
class MaxHeap(object):
    # Constructor
    def __init__(self):
        self.tree = []

    # --------------------------------------------------------------------------------------------------------------
    # Problem 19
    # --------------------------------------------------------------------------------------------------------------
    def get_max_sibling_gap(self):

        max_sib_gp = -1
        i = 0
        while (2 * i) + 2 < len(self.tree):  # TODO: Replace 123 with your answer
            left_sib = (2 * i) + 1
            right_sib = (2 * i) + 2

            sib_gp = right_sib - left_sib  # TODO: Replace 123 with your answer

            if sib_gp > max_sib_gp:
                max_sib_gp = sib_gp  # TODO: Replace 123 with your answer

            i += 1

        return max_sib_gp

    # --------------------------------------------------------------------------------------------------------------
    # Problem 20
    # --------------------------------------------------------------------------------------------------------------
    def is_valid(self):
        for i in range(1, len(self.tree)):  # TODO: Replace 123 with your answer
            if self.tree[i] > self.tree[(i - 1)//2]:  # TODO: Replace False with your answer
                return False

        return True

    # --------------------------------------------------------------------------------------------------------------
    # Problem 21
    # --------------------------------------------------------------------------------------------------------------
    def is_a_node_equal_to_its_parent(self):

        for i in range(1, len(self.tree)):  # TODO: Replace 123 with your answer
            if self.tree[i] == self.tree[(i - 1)//2]:  # TODO: Replace False with your answer
                return True

        return False

    # --------------------------------------------------------------------------------------------------------------
    # Problem 22
    # --------------------------------------------------------------------------------------------------------------
    def print_path(self, i):
        if len(self.tree) == 0:
            return

        while i > 0:
            print(self.tree[i])
            i = (i-1)//2

        print(self.tree[0])