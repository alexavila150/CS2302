from Lab5.Node import Node


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    # Inserts item at the beginning of the list
    def insert(self, item):
        if self.head is None:  # empty list
            self.head = Node(item)
            return

        node = Node(item)
        node.next = self.head
        self.head.prev = node
        self.head = node

    def __str__(self):
        list_str = ""
        curr = self.head
        while curr is not None:
            list_str += str(curr.item) + " "
            curr = curr.next
        return list_str


my_list = DoubleLinkedList()
my_list.insert(1)
my_list.insert(2)
my_list.insert(3)
print(my_list)