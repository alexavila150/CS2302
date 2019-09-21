import node

class LinkedList(object):
    head = None
    tail = None
    size = 0

    def __init__(self, node = None):
        self.head = node
        self.tail = node

    def insert_head(self, data):
        if self.head is None:
            self.head = node.Node(data)
            self.tail = self.head
            self.size += 1
            return


        curr_node = node.Node(data)
        curr_node.next = self.head
        self.head = curr_node
        self.size += 1

    def append_list(self, list):
        # if added list is empty return
        if list.size is 0:
            return

        # if self is empty return
        if self.size is 0:
            return

        # combine both sizes
        self.size += list.size

        # add list to the tail of self
        self.tail.next = list.head
        self.tail = list.tail

    def copy_list(self):
        copy = LinkedList()
        copy.head = node.Node(self.head.item)
        curr_copy = copy.head
        curr_self = self.head

        # Copy every node from self to copy
        for i in range(1, self.size):
            curr_copy.next = node.Node()
            curr_copy = curr_copy.next
            curr_self = curr_self.next
            curr_copy.item = curr_self.item

        # Set tail and size
        copy.tail = curr_copy
        copy.size = self.size
        return copy


    def print(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.item)
            curr_node = curr_node.next