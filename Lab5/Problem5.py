from Lab5.Heaps import MaxHeap
from Lab5.Word import Word


def most_frequent_words(words, k):
    appearances_of_word = dict()
    for word in words:
        if word not in appearances_of_word.keys():
            appearances_of_word[word] = 0
        appearances_of_word[word] += 1

    heap = MaxHeap()
    for word in appearances_of_word.keys():
        heap.insert(Word(word, appearances_of_word[word]))

    if k > len(appearances_of_word.keys()):
        k = len(appearances_of_word.keys())

    for i in range(k):
        print(heap.extract_max().word)


words = ["la", "la", "po", "la", "po", "po", "po", "me", "do", "me", "fi", "la"]
most_frequent_words(words, 3)
