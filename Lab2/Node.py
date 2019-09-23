class Node(object):
    item = -1
    next = None

    def __init__(self, item = -1, next = None):
        self.item = item
        self.next = next

    def print_list(self):
        curr = self
        while curr is not None:
            print(curr.item)
            curr = curr.next