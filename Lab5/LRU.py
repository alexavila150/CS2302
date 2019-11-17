class LRU(object):
    def __init__(self, capacity):
        self.head = Node()
        self.tail = Node()
        self.capacity = capacity
        self.size = 0
        self.node_of_key = dict()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # get node that has the search key
        node = self.node_of_key[key]

        # update node as most recent node

        return node.item

    def put(self, key, value):
        if self.is_full():
            self.remove_last_node()

        self.send_node_to_head(key, value)

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
        self.node_of_key.pop(self.tail.prev, None)

        # remove from linked list
        next_node = self.tail
        prev_node = self.tail.prev.prev
        next_node.prev = prev_node
        prev_node.next = next_node

        # change size of linked list
        self.size += 1

    # inserts node to linked list and dict
    def insert_node_first(self, key, node):
        # insert node to dictionary
        self.node_of_key[key] = node

        # insert node to linked list
        target_node = self.head.next
        prev_node = target_node.prev
        next_node = target_node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        # increment size
        self.size += 1

    def is_full(self):
        return self.capacity == self.size

    def print(self):
        return


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
