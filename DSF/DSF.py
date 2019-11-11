class DisjointSetForest:
    def __init__(self, n):
        self.forest = [-1] * n

    # Problem 6 # Problem 7
    def find(self, a):
        nums_in_set = set()
        return self._find(self.forest[a], nums_in_set)

    def _find(self, a, nums_in_set):
        if a < 0 or a >= len(self.forest):
            print("Index out of bounds")
            return -1
        if self.forest[a] < 0:
            return a
        nums_in_set.add(a)
        if self.forest[a] in nums_in_set:
            print("Set has a loop")
            return -1

        return self.find(self.forest[a])

    def union(self, a, b):
        if a == b or self.in_same_set(a, b):
            return

        ra = self.find(a)
        rb = self.find(b)

        self.forest[rb] = ra

    # Problem 2
    def in_same_set(self, a, b) -> bool:
        return self.find(a) == self.find(b)

    # Problem 5
    def num_sets(self):
        num_of_roots = 0
        for num in self.forest:
            if num == -1:
                num_of_roots += 1
        return num_of_roots

    # Problem 9
    def same(self, dsf):
        if len(self.forest) != len(dsf.forest):
            return False


    def __str__(self):
        return str(self.forest)


# Problem 8
def create_evens_odds_dsf(n):
    evens_odds_dsf = DisjointSetForest(n)
    for i in range(2, n, 2):
        evens_odds_dsf.union(0, i)
        evens_odds_dsf.union(1, i - 1)

    return evens_odds_dsf

dsf = DisjointSetForest(7)
print(dsf)
dsf.union(2, 3)
print(dsf)
dsf.union(0, 3)
print(dsf)
dsf.union(4, 5)
print(dsf)
dsf.union(3, 5)
print(dsf)
dsf.union(1, 4)
print(dsf)

print(dsf.in_same_set(1, 2))
print(dsf.num_sets())