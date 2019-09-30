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

    def contains(self):
        return

    def index_of(self, item) -> int:
        if self.head is None:
            return -1

        pointer = self.head
        index = 0
        while pointer is not None:
            if pointer.item == item:
                return index
            index += 1
            pointer = pointer.next

        return -1

    def get(self, index):
        return

    def get_first(self):
        return

    def get_last(self):
        if self.head is None:
            return None
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next

        return pointer.item


        return

    def remove(self, index):
        return

    def remove_first(self):
        return

    def remove_last(self):
        return

    def size(self) -> int:
        pointer = self.head
        size = 0
        while pointer is not None:
            size += 1
            pointer = pointer.next
        return size

    def is_empty(self):
        return

    def print_list(self):
        if self.head is None:
            return
        pointer = self.head
        while pointer is not None:
            print(pointer.item)
            pointer = pointer.next


        return


def main():
    print("You can test here")
    list = SinglyLinkedList()
    list.add_last(5)
    list.add_last(6)
    list.add_last(8)
    list.print_list()
    print(list.size())

if __name__ == "__main__":
    main()
