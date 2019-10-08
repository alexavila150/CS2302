class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_last(self, item):
        if self.head is None:
            self.head = Node(item)
            return

        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next

        pointer.next = Node(item)
        return

    def add_first(self, item):
        return

    def add(self, index, item):

        return

    def clear(self):
        return

    def contains(self, item):
        if self.head is None:
            return False

        pointer = self.head
        while pointer is not None:
            if item == pointer.item:
                return True
            pointer = pointer.next

        return False

    def index_of(self, item):
        return

    def get(self, index: int):
        if self.head is None:
            return None

        curr_index = 0
        pointer = self.head
        while pointer is not None:
            if curr_index == index:
                return pointer.item
            curr_index += 1
            pointer = pointer.next

        return None

    def get_first(self):
        return

    def get_last(self):
        return

    def remove(self, index):
        return

    def remove_first(self):
        return

    def remove_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return

        pointer = self.head
        while pointer.next.next is not None:
            pointer = pointer.next

        pointer.next = None

        return

    def size(self):
        return

    def is_empty(self):
        return

    def print_list(self):
        curr = self.head

        while curr is not None:
            print(curr.item)
            curr = curr.next


def main():
    print("You can test here")
    list = SinglyLinkedList()
    #list.add_last(5)
    #list.add_last(6)
    #list.add_last(1)
    list.remove_last()
    list.print_list()
    print(list.get(3))



if __name__ == "__main__":
    main()
