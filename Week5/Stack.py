from Week5.SinglyLinkedList import SinglyLinkedList, Node
class Stack:
    def __init__(self):
        self.list = SinglyLinkedList()
        self.top = None
        self.size = 0

    def push(self, item):
        self.list.add_first(item)
        self.top = self.list.head
        self.size += 1

    def pop(self):
        item = self.list.remove_first()
        self.top = self.list.head
        self.size -= 1
        return item

    def empty(self):
        self.list.clear()

    def is_empty(self) -> bool:
        return self.size == 0

    def print(self):
        self.list.print_list()