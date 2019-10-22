import math

from Lab3.AVLTree import Tree as AVLTree
from Lab3.RBTree import Tree as RBTree

tree = None


# get file name with words and embeddings
# store everything in an AVL Tree
def file_to_avl_tree(file_name):
    # Open file to read
    file = open(file_name, encoding="utf8")

    # Create AVLTree
    avl_tree = AVLTree()

    # add file ids to the tree
    for line in file:
        if not line[0].isalnum() or not line.isascii():  # First char is no alphabetic or numeric
            continue

        avl_tree.insert(line)

    avl_tree.separate_all_embeddings(avl_tree.root)
    file.close()
    return avl_tree


# get file name with words and embeddings
# store everything in a Red Black Tree
def file_to_rb_tree(file_name):
    # Open file to read
    file = open(file_name, encoding="utf8")

    # Create AVLTree
    rb_tree = RBTree()

    # add file ids to the tree
    for line in file:
        if not line[0].isalnum() and not line.isascii():  # First char is no alphabetic or numeric
            continue

        rb_tree.insert(line)

    rb_tree.separate_all_embeddings(rb_tree.root)
    file.close()
    return rb_tree


# Compares 2 words
# return their cosine similarity
def similarity(word1: str, word2: str):
    word1_node = tree.bst_search(word1)
    word2_node = tree.bst_search(word2)

    if word1_node is None:
        return None

    if word2_node is None:
        return None

    word1_embedding = word1_node.embedding
    word2_embedding = word2_node.embedding

    numerator = 0
    d1 = 0
    d2 = 0
    for i in range(len(word1_embedding)):
        numerator += float(word1_embedding[i]) * float(word2_embedding[i])
        d1 += float(word1_embedding[i]) * float(word1_embedding[i])
        d2 += float(word2_embedding[i]) * float(word2_embedding[i])

    d1 = math.sqrt(d1)
    d2 = math.sqrt(d2)
    denominator = d2 * d1
    return numerator / denominator


# gets input file_name
# returns 2D list with pairs
def input_to_list(file_name: str):
    returning_list = []
    file = open(file_name, "r")
    for line in file:
        # Check if it is two words
        words = line.split()
        if len(words) != 2:
            continue

        returning_list.append(words)

    file.close()

    return returning_list


# Gets 2D array of word pairs
# writes the similarity in output.input
def list_to_output(words):
    file = open("output.txt", "w")
    for pair in words:
        file.write(pair[0] + " " + pair[1] + " " + str(similarity(pair[0], pair[1])) + "\n")
    file.close()


def main():
    global tree

    # Ask user for what kind of Tree to be used
    print("what kind of tree do you want to use?")
    print("1. AVL Tree")
    print("2. Red Black Tree")
    num = input("Type the number of the option: ")

    input_chosen = False
    while not input_chosen:
        if num == "1":
            tree = file_to_avl_tree("glove.6B.50d.txt")
            print("words are contained in an AVL Tree")
            input_chosen = True
        elif num == "2":
            tree = file_to_rb_tree("glove.6B.50d.txt")
            print("word are contained in a Red Black Tree")
            input_chosen = True
        else:
            num = input("Choose 1 or 2: ")

    # Reads input file with words to compare
    # Store the similarities in output.txt
    words = input_to_list("input.txt")
    list_to_output(words)
    print("similarities stored in output.txt")


main()