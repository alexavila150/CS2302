class HashTable:
    # Builds a hash table of size 'size'
    def __init__(self, size):
        self.table = [[] for i in range(size)]

    def hash(self, k):
        return k % len(self.table)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 15
    # --------------------------------------------------------------------------------------------------------------
    def insert(self, k):
        loc = self.hash(k)
        bucket = self.table[loc]
        if k in bucket:
            return
        bucket.append(k)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 16
    # --------------------------------------------------------------------------------------------------------------
    def contains(self, k):
        loc = self.hash(k)
        bucket = self.table[loc]
        return k in bucket

    # --------------------------------------------------------------------------------------------------------------
    # Problem 17
    # --------------------------------------------------------------------------------------------------------------
    def get_longest_list(self):
        longest_list = 0
        for bucket in self.table:
            if len(bucket) > longest_list:
                longest_list = len(bucket)
        return longest_list

    # --------------------------------------------------------------------------------------------------------------
    # Problem 18
    # --------------------------------------------------------------------------------------------------------------
    def reset_table(self):
        self.table = [[] for i in range(len(self.table))]