class Node(object):
   item = -1
   next = None

   def __init__(self, item, next = None):
       self.item = item
       self.next = next

class LinkedList(object):
    head = None
    tail = None
    size = 0

    def __init__(self, node = Node):
        self.head = node
        self.tail = node

    def insert_head(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = Node(data)
            self.size += 1
            return

        curr_node = Node(data)
        curr_node.next = self.head
        self.head = curr_node
        self.size += 1

    def print(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.item)
            curr_node = curr_node.next


# Open both files to read them
activision_file = open('activision.txt', 'r')
vivendi_file = open('vivendi.txt', 'r')

# Linked List files
activision_ids = LinkedList()
vivendi_ids = LinkedList()

# add file ids to the linked lists
for line in activision_file:
    activision_ids.insert_head(line)

for line in vivendi_file:
    vivendi_ids.insert_head(line)


print("number of ids activision:", activision_ids.size)
print("number of ids vivendi:", vivendi_ids.size)


# Close both files
activision_file.close()
vivendi_file.close()
