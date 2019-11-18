class LRU(object):
    def __init__(self, capacity):
        self.head = Node(0)
        self.tail = Node(0)
        self.capacity = capacity
        self.size = 0
        self.node_of_key = dict()
        self.keys = set()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.keys:
            return -1

        # get node that has the search key
        node = self.node_of_key[key]
        # update node as most recent node
        self.send_node_to_head(key, node)
        return node.value

    def put(self, key, value):
        # if key is in LRU then update the value
        if key in self.keys:
            node = self.node_of_key[key]
            node.value = value
            return

        if self.is_full():
            self.remove_last_node()

        node = Node(key, value)
        self.insert_node_first(key, node)

    def size(self):
        return self.size

    def max_capacity(self):
        return self.capacity

    def send_node_to_head(self, key, node):
        self.remove_node(node)
        self.insert_node_first(key, node)

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size = 0

    def remove_last_node(self):
        # remove node from dictionary
        last_key = self.tail.prev.key
        self.keys.remove(last_key)
        self.node_of_key.pop(self.tail.prev.key, None)

        # remove from linked list
        next_node = self.tail
        prev_node = self.tail.prev.prev
        next_node.prev = prev_node
        prev_node.next = next_node

        # change size of linked list
        self.size -= 1

    # inserts node to linked list and dict
    def insert_node_first(self, key, node):
        # insert node to dictionary
        self.keys.add(key)
        self.node_of_key[key] = node

        # insert node to linked list
        prev_node = self.head
        next_node = prev_node.next
        prev_node.next = node
        node.prev = prev_node
        next_node.prev = node
        node.next = next_node

        # increment size
        self.size += 1

    def is_full(self):
        return self.capacity == self.size

    def __str__(self):
        result = ""
        curr = self.head.next
        while curr is not self.tail:
            result += str(curr.value) + " "
            curr = curr.next
        return result


class Node(object):
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


my_lru = LRU(5)
my_lru.put("Alex", 19)
my_lru.put("Turin", 29)
my_lru.put("Arturo", 57)
my_lru.put("Irvin", 18)
my_lru.put("Ivonne", 15)
my_lru.put("Ivonne", 15)
my_lru.put("Karen", 14)
my_lru.put("Cynthia", 23)
my_lru.put("Carlos", 15)
my_lru.get("Cynthia")
print(my_lru.get("Alex"))
print(my_lru)
