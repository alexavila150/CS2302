def keyboard_row(words):
    valid_words = []
    for word in words:
        if is_word_in_one_row(word):
            valid_words.append(word)

    return valid_words


def is_word_in_one_row(word):
    letters_of_row = {
        "top": {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"},
        "mid": {"a", "s", "d", "f", "g", "h", "j", "k", "l", "A", "S", "D", "F", "G", "H", "J", "K", "L"},
        "bot": {"z", "x", "c", "v", "b", "n", "m", "Z", "X", "C", "V", "B", "N", "M"}
    }

    expected_row = ""
    if word[0] in letters_of_row["top"]:
        expected_row = "top"
    elif word[0] in letters_of_row["mid"]:
        expected_row = "mid"
    elif word[0] in letters_of_row["bot"]:
        expected_row = "bot"
    else:
        return False

    for letter in word:
        if not letter in letters_of_row[expected_row]:
            return False

    return True


print(keyboard_row(["Hello", "Alaska", "Dad", "Peace"]))
