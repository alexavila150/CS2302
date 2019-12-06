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

        for i in self.dsf:
            if i == -1:
                count += 1
        return count

    # --------------------------------------------------------------------------------------------------------------
    # Problem 24
    # --------------------------------------------------------------------------------------------------------------
    def group_singletons(self):

        not_singletons = set()
        for i in range(len(self.dsf)):
            if self.dsf[i] != -1:
                not_singletons.add(i)
                not_singletons.add(self.find(i))

        singletons = list()
        for i in range(len(self.dsf)):
            if i not in not_singletons:
                singletons.append(i)

        for i in range(1, len(singletons)):
            self.union(i, i - 1)

        return

    # --------------------------------------------------------------------------------------------------------------
    # Problem 25
    # --------------------------------------------------------------------------------------------------------------
    def is_compressed(self):
        numbers_in_forest = set()
        for i in self.dsf:
            numbers_in_forest.add(self.dsf[i])

        return len(numbers_in_forest) < 3

    # --------------------------------------------------------------------------------------------------------------
    # Problem 26
    # --------------------------------------------------------------------------------------------------------------
    @staticmethod
    def create_dsf(n, k):
        dsf = [k] * n
        dsf[k] = -1
        return dsf
