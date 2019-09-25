from Lab2.Node import Node

class LinkedList(object):
    head = None
    tail = None
    size = 0

    def __init__(self, node: Node = None):
        if node is None:
            self.head = None
            self.tail = None
            self.size = 0
            return

        if node.next is None:
            self.head = node
            self.tail = node
            self.size = 1

    def insert_head(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return


        curr_node = Node(data)
        curr_node.next = self.head
        self.head = curr_node
        self.size += 1

    def add_multi_nodes(self, node: Node):
        if node is None:
            self.empty_list()
            return

        if node.next is None:
            self.insert_head(node)
            return

        self.head= node
        self.size = 0
        curr_node = node
        while curr_node is not None:
            self.size += 1
            curr_node = curr_node.next

        self.tail = curr_node

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

    def remove_head(self):
        if self.head is None:
            self.size = 0
            return

        # If there is 1 node, empty list
        if self.size is 1:
            self.empty_list()
            return

        self.head = self.head.next
        self.size -= 1


    def empty_list(self):
        self.head = None
        self.tail = None
        self.size = 0

    def copy_list(self):
        copy = LinkedList()
        copy.head = Node(self.head.item)
        curr_copy = copy.head
        curr_self = self.head

        # Copy every node from self to copy
        for i in range(1, self.size):
            curr_copy.next = Node()
            curr_copy = curr_copy.next
            curr_self = curr_self.next
            curr_copy.item = curr_self.item

        # Set tail and size
        copy.tail = curr_copy
        copy.size = self.size
        return copy

    def isSorted(self):
        # return true if list has 1 or 0 elements
        if self.head is None or self.size is 1:
            return True

        # Set pointers to see if list is sorted
        pointer1 = self.head
        pointer2 = pointer1.next

        while pointer2 is not None:
            if pointer1.item > pointer2.item:
                return False

            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return True
    
    def find_max(self) -> int:
        if self.head is None:
            return -1

        #set pointer and max variable
        max_num = self.head.item
        curr_node = self.head

        # find max item on the list
        while curr_node is not None:
            if curr_node.item > max_num:
                max_num = curr_node.item
            curr_node = curr_node.next

        return max_num

    def print(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.item)
            curr_node = curr_node.next
            
    