class HashTable:
    # Builds a hash table of size 'size'
    def __init__(self, size):
        self.table = [[] for i in range(size)]

    def hash(self, k):
        return k % len(self.table)

    # Inserts k in the appropriate bucket if k is not already there
    def insert(self, k):
        loc = self.hash(k)
        bucket = self.table[loc]

        if not k in bucket:
            bucket.append(k)

    # Removes k if it is in the table. If k is not in the table, an Exception is raised
    def remove(self, k):
        loc = self.hash(k)
        bucket = self.table[loc]
        if k in bucket:
            bucket.remove(k)
        else:
            raise ValueError('hashtable.remove(k): k is not in the table')

    def find(self, k):
        # Returns bucket and index where k is stored in the table
        # If k is not in table, return None and -1 as the bucket and index
        loc = self.hash(k)
        bucket = self.table[loc]

        if k in bucket:
            index = bucket.index(k)
            return bucket, index

        return None, -1

    def __str__(self):
        s = ""
        for i in range(len(self.table)):
            bucket = self.table[i]
            s += str(i) + ": "
            s += str(bucket)
            s += "\n"
        return s

    def load_factor(self):  # Problem 2
        num_elements = 0
        for bucket in self.table:
            num_elements += len(bucket)
        return num_elements / len(self.table)

    def size_longest_list(self):  # Problem 3
        max_size = 0
        for bucket in self.table:
            if len(bucket) > max_size:
                max_size = len(bucket)
        return max_size

    def is_valid(self):  # Problem 4
        for i in range(len(self.table)):
            i = self.table.index(self.table[i])
            for key in self.table[i]:
                if not key % len(self.table) == i:
                    return False
        return True

    def insert_asc(self, k):  # Problem 5
        loc = self.hash(k)
        bucket = self.table[loc]

        if len(bucket) == 0:
            bucket.append(k)
            return

        for i in range(len(bucket)):
            if k == bucket[i]:
                return

            if k < bucket[i]:
                bucket.insert(i, k)
                return

        bucket.append(k)

    def largest_key(self):  # Problem 6
        max_key = float("-inf")
        for bucket in self.table:
            if len(bucket) > 0 and max(bucket) > max_key:
                max_key = max(bucket)

        return max_key

    def resize(self, size):  # Problem 7
        new_hash = HashTable(size)
        new_hash.table = [[] for i in range(size)]
        for bucket in self.table:
            for key in bucket:
                new_hash.insert_asc(key)
        self.table = new_hash.table

    def contains(self, k):
        loc = self.hash(k)
        bucket = self.table[loc]
        return k in bucket

    def is_equal(self, hash_table):  # Problem 8
        for bucket in self.table:
            for key in bucket:
                if not hash_table.contains(key):
                    return False
        return True



table = HashTable(7)
table.insert(3)
table.insert(17)
table.insert(5)
table.insert(6)
table.insert_asc(10)
table.insert_asc(19)
table.insert_asc(12)
table.insert_asc(4)
table.insert_asc(30)

table2 = HashTable(3)
table2.insert(3)
table2.insert(17)
table2.insert(5)
table2.insert(6)
table2.insert_asc(10)
table2.insert_asc(19)
table2.insert_asc(12)
table2.insert_asc(4)
table2.insert_asc(30)

table.resize(5)
print(table)
print(table.is_equal(table2))

