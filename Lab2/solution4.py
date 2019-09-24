from Lab2.Node import Node
from Lab2.LinkedList import LinkedList


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

def find_duplicates(list: LinkedList):
    #make list to see if the number is duplicate
    is_id_listed = []
    for i in range(list.find_max() + 1):
        is_id_listed.append(False)

    #traverse the id and return numbers that are already on list
    duplicate_ids = []
    curr_node = list.head
    while curr_node is not None:
        # if id is listed already then add it to duplicate list
        if is_id_listed[curr_node.item]:
            duplicate_ids.append(curr_node.item)

        # check id as already visited
        is_id_listed[curr_node.item] = True
        curr_node = curr_node.next

    return duplicate_ids

def main():
    # Linked List files
    activision_ids = file_to_linked_list('activision.txt')
    vivendi_ids = file_to_linked_list('vivendi.txt')

    # combine both lists
    activision_blizzard_ids = activision_ids
    activision_blizzard_ids.append_list(vivendi_ids)

    duplicate_ids = find_duplicates(activision_blizzard_ids)
    print(len(duplicate_ids))

main()
