def find_the_difference(word1, word2):
    letters1 = set(word1)
    letters2 = set(word2)

    for letter in letters1:
        letters2.remove(letter)

    return letters2


print(find_the_difference("abcd", "abcde"))