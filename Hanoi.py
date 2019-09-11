class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def get(self):
        return self.items

    def print_stack(self):
        print(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

class ActivationRecord:
    def __init__(self, disks, source, spare, dest, address):
        self.disks = disks
        self.source = source
        self.spare = spare
        self.dest = dest
        self.address = address

    def __str__(self):
        string = (self.disks,
                  self.source,
                  self.spare,
                  self.dest,
                  self.address)

        return str(string)


def hanoi(disks, source, spare, dest):
    activation_record = ActivationRecord(disks, source, spare, dest, -1)
    stack = Stack()
    stack.push(activation_record)
    location = 0;

    #run until there are no more activation records
    while not stack.is_empty():
        print("AR: ", stack.peek().__str__())
        if stack.peek().disks > 1 and location == 0:
            print("disk:", stack.peek().disks)
            print("location == 0")
            print("create AR")
            stack.push(ActivationRecord(stack.peek().disks - 1,
                                        stack.peek().source,
                                        stack.peek().dest,
                                        stack.peek().spare,
                                        1))

        #Location 1
        elif stack.peek().disks > 1 and location is 1:
            print("disk:", stack.peek().disks)
            print("location == 1")
            print("Move disk from ", stack.peek().source, " to ", stack.peek().dest)
            print("create AR")
            stack.push(ActivationRecord(stack.peek().disks - 1,
                                        stack.peek().spare,
                                        stack.peek().source,
                                        stack.peek().dest,
                                        2))

        elif stack.peek().disks > 1 and location is 2:
            print("location == 2")
            location = stack.pop().address
            print("Go to location ", location)

        else:
            print("disk is 1")
            print("Move disk from ", stack.peek().source, " to ", stack.peek().dest)
            location = stack.pop().address
            print("Go to location: ", location)

print(hanoi(3, 'A', 'B', 'C'))