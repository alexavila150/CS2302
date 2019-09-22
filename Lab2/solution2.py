from Lab2.Node import Node
from Lab2.LinkedList import LinkedList

def file_to_linked_list(file_name):
    # Open file to read
    file = open(file_name, 'r')

    # Linked List files
    linked_list = LinkedList()

    # add file ids to the linked lists
    for line in file:
        linked_list.insert_head(int(line))

    file.close()

    return linked_list

def bubble_sort(linked_list):
    #insert temporary node to sort the rest of the list
    linked_list.insert_head(0)

    # Set pointers to keep track of what nodes to switch
    previous_node = linked_list.head
    pointer1 = previous_node.next
    pointer2 = pointer1.next

    while not linked_list.isSorted():
        # Run until it gets to the end of the list
        while pointer2 is not None:
            # if left pointer is bigger switch nodes
            if pointer1.item >= pointer2.item:
                previous_node.next = pointer2
                pointer1.next = pointer2.next
                pointer2.next = pointer1

            previous_node = previous_node.next
            pointer1 = previous_node.next
            pointer2 = pointer1.next

        # Set pointers back to the beginning
        previous_node = linked_list.head
        pointer1 = previous_node.next
        pointer2 = pointer1.next

    linked_list.remove_head()

def find_duplicates(linked_list):
    # if size is 0 or 1 return no duplicates
    if linked_list.size is 0 or linked_list.size is 1:
        return []

    # Set pointers to see if they are duplicates
    pointer1 = linked_list.head
    pointer2 = pointer1.next
    duplicates = []

    # Traverse all the list to find the duplicates
    while pointer2 is not None:
        if pointer1.item == pointer2.item:
            duplicates.append(pointer1.item)
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return duplicates

def main():
    # Linked List files
    activision_ids = file_to_linked_list('activision.txt')
    vivendi_ids = file_to_linked_list('vivendi.txt')

    # combine both lists
    activision_blizzard_ids = activision_ids
    activision_blizzard_ids.append_list(vivendi_ids)

    bubble_sort(activision_blizzard_ids)
    duplicates = find_duplicates(activision_blizzard_ids)

    print(len(duplicates))

main()