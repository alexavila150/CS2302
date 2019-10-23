def most_common_word(sentence):
    num_of_appearances = dict()
    max = 0
    words = sentence.split()
    for word in words:
        if not word in num_of_appearances:
            num_of_appearances[word] = 0
        else:
            num_of_appearances[word] += 1
            if num_of_appearances[word] > max:
                max = num_of_appearances[word]


    for word in words:
        if max == num_of_appearances[word]:
            return word

    return False

print(most_common_word("hello world hello hello world hi"))

