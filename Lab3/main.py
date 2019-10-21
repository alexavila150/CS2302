import math

from Lab3.AVLTree import Tree as AVLTree
from Lab3.RBTree import Tree as RBTree

avl_tree = AVLTree()

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


def file_to_rb_tree(file_name):
    # Open file to read
    file = open(file_name, 'r')

    # Create AVLTree
    rb_tree = RBTree()

    # add file ids to the tree
    for line in file:
        if not line[0].isalnum(): # First char is no alphabetic or numeric
            continue

        rb_tree.insert(line)

    rb_tree.separate_all_embeddings(rb_tree.root)
    file.close()
    return rb_tree


def similarity(word1: str, word2: str):
    word1_node = avl_tree.bts_search(word1)
    word2_node = avl_tree.bts_search(word2)
    word1_embedding = word1_node.embedding
    word2_embedding = word2_node.embedding

    numerator = 0
    d1 = 0
    d2 = 0
    print("word1_embedding", word1_embedding)
    for i in range(len(word1_embedding)):
        numerator += float(word1_embedding[i]) * float(word2_embedding[i])
        d1 += float(word1_embedding[i]) * float(word1_embedding[i])
        d2 += float(word2_embedding[i]) * float(word2_embedding[i])

    d1 = math.sqrt(d1)
    d2 = math.sqrt(d2)
    denominator = d2 * d1
    return numerator / denominator


def main():
    global avl_tree
    avl_tree = file_to_avl_tree("embeddings_test.txt")
    avl_tree.words_to_file(avl_tree.root)
    print(avl_tree.root.left.embedding)
    print(avl_tree.num_nodes(avl_tree.root))


main()