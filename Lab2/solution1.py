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

def get_duplicate_ids(linked_list):
    # make two pointers to compare nodes
    pointer1 = linked_list.head
    pointer2 = pointer1.next
    duplicate_ids = []

    index1 = 0
    index2 = 1
    #traverse all pointer combinations and find the duplicates
    while pointer1.next is not None:
        while pointer2 is not None:
            if pointer1.item == pointer2.item:
                duplicate_ids.append(pointer1.item)
            pointer2 = pointer2.next
        pointer1 = pointer1.next
        pointer2 = pointer1.next

    # return duplicates
    return duplicate_ids

def main():
    # Linked List files
    activision_ids = file_to_linked_list('activision.txt')
    vivendi_ids = file_to_linked_list('vivendi.txt')

    # combine both lists
    activision_blizzard_ids = activision_ids
    activision_blizzard_ids.append_list(vivendi_ids)

    # add duplicated ids to a list
    duplicated_ids = get_duplicate_ids(activision_blizzard_ids)

    print(len(duplicated_ids))

main()