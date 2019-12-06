# For all questions, use the following class definitions
class DisjointSetForest:
    def __init__(self, n):
        self.dsf = [-1] * n

    def is_index_valid(self, index):
        return 0 <= index <= len(self.dsf)

    def find(self, a):
        if not self.is_index_valid(a):
            return -1

        if self.dsf[a] < 0:
            return a

        return self.find(self.dsf[a])

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        self.dsf[rb] = ra

    # --------------------------------------------------------------------------------------------------------------
    # Problem 23
    # --------------------------------------------------------------------------------------------------------------
    def get_num_sets(self):
        count = 0

        # Your code goes here

        return count

    # --------------------------------------------------------------------------------------------------------------
    # Problem 24
    # --------------------------------------------------------------------------------------------------------------
    def group_singletons(self):

        # Your code goes here

        return

    # --------------------------------------------------------------------------------------------------------------
    # Problem 25
    # --------------------------------------------------------------------------------------------------------------
    def is_compressed(self):

        # Your code goes here

        return True

    # --------------------------------------------------------------------------------------------------------------
    # Problem 26
    # --------------------------------------------------------------------------------------------------------------
    @staticmethod
    def create_dsf(n, k):
        dsf = []  # Feel free to change this line

        # Your code goes here

        return dsf
