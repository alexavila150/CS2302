import math


# For all questions, use the following class definitions
class MaxHeap(object):
    # Constructor
    def __init__(self):
        self.tree = []

    # --------------------------------------------------------------------------------------------------------------
    # Problem 19
    # --------------------------------------------------------------------------------------------------------------
    def max_grandpa_gap(self):
        if len(self.tree) < 4:  # TODO: Replace False with your answer
            return -math.inf

        max_grandpa_gap = -math.inf  # TODO: Replace 0 with your answer

        for i in range(3, len(self.tree)):  # TODO: Replace 123 with your answer
            pi = (i - 1)//2
            grandpa_index = (pi - 1)//2  # TODO: Replace 123 with your answer

            grandpa_gap = self.tree[grandpa_index] - self.tree[i]  # TODO: Replace 123 and 456 with your answers

            max_grandpa_gap = max(max_grandpa_gap, grandpa_gap)

        return max_grandpa_gap

    # --------------------------------------------------------------------------------------------------------------
    # Problem 20
    # --------------------------------------------------------------------------------------------------------------
    def is_valid(self):
        for i in range(1, len(self.tree)):  # TODO: Replace 123 with your answer
            if self.tree[i] > self.tree[(i - 1) // 2]:  # TODO: Replace False with your answer
                return False

        return True

    # --------------------------------------------------------------------------------------------------------------
    # Problem 21
    # --------------------------------------------------------------------------------------------------------------
    def try_replace(self, i, val):

        # If i is out of bounds
        if i < 0 or i >= len(self.tree):  # TODO: Replace False with your answer
            return

        parent_index = (i - 1)//2  # TODO: Replace 123 with your answer

        # If i has a parent
        if i > 0:  # TODO: Replace True with your answer

            # If the heap property is broken, return without doing anything
            if self.tree[parent_index] < val:  # TODO Replace == with your answer
                return

        left_child_index = (i * 2) + 1  # TODO: Replace 123 with your answer
        # If i has a left child
        if left_child_index < len(self.tree):  # TODO: Replace True with your answer

            # If the heap property is broken, return without doing anything
            if self.tree[left_child_index] > val:  # TODO Replace == with your answer
                return

        right_child_index = (i * 2) + 2  # TODO: Replace 123 with your answer

        # If i has a right child
        if right_child_index < len(self.tree):  # TODO: Replace True with your answer

            # If the heap property is broken, return without doing anything
            if self.tree[right_child_index] > val:  # TODO Replace == with your answer
                return

        self.tree[i] = val

    # --------------------------------------------------------------------------------------------------------------
    # Problem 22
    # --------------------------------------------------------------------------------------------------------------
    def create_path(self, i):
        path = []
        if i < 0 or i >= len(self.tree):
            return path
        while i > 0:
            path.append(self.tree[i])
            i = (i - 1)//2
        path.append(self.tree[0])
        return path
