import math

from Lab4.BTrees import BTree

tree = None


# get file name with words and embeddings
# store everything in a BTree
def file_to_b_tree(file_name):
    # Open file to read
    file = open(file_name, encoding="utf8")

    # Create AVLTree
    b_tree = BTree()

    # add file ids to the tree
    for line in file:
        if not line[0].isalnum() or not line.isascii():  # First char is no alphabetic or numeric
            continue

        b_tree.insert(line)

    b_tree.separate_all_embeddings()  # TODO
    file.close()
    return b_tree


# Compares 2 words
# return their cosine similarity
def similarity(word1: str, word2: str):
    word1_embedding = b_tree.get_embedding(word1)
    word2_embedding = b_tree.get_embedding(word2)

    numerator = 0
    d1 = 0
    d2 = 0
    for i in range(len(word1_embedding)):
        print("word1_embedding", word1_embedding)
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
    global b_tree
    b_tree = file_to_b_tree("glove.6B.50d.txt")

    # Reads input file with words to compare
    # Store the similarities in output.txt
    words = input_to_list("input.txt")
    list_to_output(words)
    print("similarities stored in output.txt")
    print("finish")


main()
