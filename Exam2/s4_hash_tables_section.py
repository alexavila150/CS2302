import math


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
    def search(self, k):
        loc = self.hash(k)
        bucket = self.table[loc]
        if k in bucket:
            return bucket
        return None

    # --------------------------------------------------------------------------------------------------------------
    # Problem 17
    # --------------------------------------------------------------------------------------------------------------
    def min_key (self):
        min_key = math.inf
        for bucket in self.table:
            bucket_min = math.inf
            if bucket is not None and len(bucket) > 0:
                bucket_min = min(bucket)
            min_key = min(min_key, bucket_min)

        return min_key

    # --------------------------------------------------------------------------------------------------------------
    # Problem 18
    # --------------------------------------------------------------------------------------------------------------
    def load_factor(self):
        num_keys = 0
        for bucket in self.table:
            num_keys += len(bucket)
        return num_keys / len(self.table)
