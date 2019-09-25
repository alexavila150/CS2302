class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

    def set_item(self, item):
        self.item = item

    def set_next(self, next):
        self.next = next

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

class SinglyLinkedList:
    def __init__(self, head: Node = None):
        self.head = head
        if self.head is None:
            self.size = 0
            return
        self.size = 1

    def add_last(self, item):
        curr_node = self.head
        while curr_node.get_next() is not None:
            curr_node = curr_node.get_next()

        curr_node.set_next(Node(item))
        self.size += 1

    def add_first(self, item):
        self.head = Node(item, self.head)
        self.size += 1

    def add(self, index: int, item):
        if index < 0:
            return

        if index == 0:
            self.add_first(item)
            return

        if index > self.size:
            self.add_last(item)
            return

        curr_node = self.head
        for i in range(index - 1):
            curr_node = curr_node.next

        new_node = Node(item)
        new_node.next = curr_node.next
        curr_node.next = new_node
        self.size += 1

    def clear(self):
        self.head = None
        self.size = None

    def contains(self, item) -> bool:
        curr_node = self.head
        while curr_node is not None:
            if curr_node.item == item:
                return True
            curr_node = curr_node.next

        return False

    def get_index_of_item(self, item) -> int:
        curr_node = self.head
        curr_index = 0
        while curr_node is not None:
            if curr_node.item == item:
                return curr_index

        return -1

    def get(self, index: int):
        if self.head is None:
            return -1

        if index < 0:
            return -1

        if index == 0:
            return self.head.item

        if index >= self.size:
            return -1

        curr_node = self.head
        for i in range(index):
            curr_node = curr_node.next

        return curr_node.item

    def get_first(self):
        return self.head.item

    def get_last(self):
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        return curr_node.item

    def remove_first(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.size -= 1

    def remove_last(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.remove_first()

        curr_node = self.head
        while curr_node.next.next is not None:
            curr_node = curr_node.next

        curr_node.next = curr_node.next.next
        self.size -= 1


    def remove(self, index):
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.remove_first()
            return

        if index == self.size - 1:
            self.remove_last()
            return

        curr_node = self.head

        #look for search node
        search_node = self.head
        for i in range(index):
            search_node = search_node.next

        while curr_node.next is not search_node:
            curr_node = curr_node.next

        curr_node.next = curr_node.next.next
        self.size -= 1

    def size(self):
        return self.size

    def is_empty(self):
        return self.head is None

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.get_item())
            curr_node = curr_node.get_next()

    def reverse_list(self):
        if self.head is None:
            return

        nodes = []
        pointer = self.head
        while pointer is not None:
            nodes.append(pointer)
            pointer = pointer.next

        self.head = nodes.pop()
        pointer = self.head
        while len(nodes) is not 0:
            pointer.next = nodes.pop()
            pointer = pointer.next

        pointer.next = None

    def delete_duplicates(self):
        self.add_first(9)

        previous_node = self.head
        pointer1 = previous_node.next
        pointer2 = pointer1.next
        while pointer2 is not None:
            if pointer1.item == pointer2.item:
                pointer1.next = pointer2.next
                self.size -= 1

            if pointer1.next is None:
                break

            previous_node = previous_node.next
            pointer1 = pointer1.next
            pointer2 = pointer1.next

        self.remove_first()

list = SinglyLinkedList()
list.add_first(0)
list.add_first(0)
list.add_first(1)
list.add_first(2)
list.add_first(2)
list.add_first(3)

list.delete_duplicates()

print("list")
list.print_list()
