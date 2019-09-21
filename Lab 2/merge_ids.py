import linked_list
import node

def file_to_linked_list(file_name):
    # Open file to read
    file = open(file_name, 'r')

    # Linked List files
    linked_list = linked_list.LinkedList()

    # add file ids to the linked lists
    for line in activision_file:
        activision_ids.insert_head(line)

    file.close()

def main():
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

    # combine both lists
    activision_blizzard_ids = activision_ids
    activision_blizzard_ids.append_list(vivendi_ids)

    # add duplicated ids to a list
    duplicated_ids = []
    ids_copy = activision_blizzard_ids.copy_list()

    for i in range(activision_blizzard_ids.size):
        for j in range(activision_blizzard_ids.size):

    # Close both files
    activision_file.close()
    vivendi_file.close()

main()
