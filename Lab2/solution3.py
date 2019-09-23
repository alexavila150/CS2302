from Lab2.LinkedList import LinkedList
from Lab2.Node import Node

def file_to_linked_list(file_name: str) -> LinkedList:
    # Open file to read
    file = open(file_name, 'r')

    # Linked List files
    linked_list = LinkedList()

    # add file ids to the linked lists
    for line in file:
        linked_list.insert_head(int(line))

    file.close()

    return linked_list

def merge_sorted_lists(a: Node, b: Node) -> Node:
    # if a is empty, return b which is already sorted
    if a is None:
        return b

    # if b is empty, return a which is already sorted
    if b is None:
        return a

    # if a is smaller, a.next is the sorted list of a.next and b
    if a.item < b.item:
        a.next = merge_sorted_lists(a.next, b)
        return a
    else:
        b.next = merge_sorted_lists(a, b.next)
        return b

def split_list(head: Node, partition_heads):
    if head is None:
        return

    if head.next is None:
        partition_heads[0] = head
        partition_heads[1] = head
        return


    pointer1 = head
    pointer2 = pointer1.next

    # Pointer2 advances 2 steps and pointer 1 advances 1 step
    # until pointer 2 gets to the end of the array
    while pointer2 is not None:
        pointer2 = pointer2.next
        if pointer2 is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

    partition_heads[0] = head
    partition_heads[1] = pointer1.next
    pointer1.next = None

def merge_sort(head: Node) -> Node:
    #list to store heads of the splited list
    partition_heads = [None, None]
    # Split the list into two
    split_list(head, partition_heads)
    left_head = partition_heads[0]
    right_head = partition_heads[1]

    #if split_list is size one return
    if left_head == right_head:
        return left_head

    left_head = merge_sort(left_head)
    right_head = merge_sort(right_head)

    merge_sorted_list = merge_sorted_lists(left_head, right_head)
    return merge_sorted_list

def merge_sort_list(list: LinkedList):
    head = merge_sort(list.head)
    list.empty_list()
    list.add_multi_nodes(head)

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

    #sort and find duplicates
    merge_sort_list(activision_blizzard_ids)

main()



