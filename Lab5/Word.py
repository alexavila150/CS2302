class Word(object):
    def __init__(self, word, appearances):
        self.word = word
        self.appearances = appearances

    def __eq__(self, other):
        if self.appearances == other.appearances:
            return True
        if self.word == other.word:
            return True
        return False

    def __ne__(self, other):
        if self.appearances != other.appearances:
            return True
        if self.word != other.word:
            return True
        return False

    def __le__(self, other):
        if self.appearances <= other.appearances:
            return True
        elif self.appearances != other.appearances:
            return False
        if self.word <= other.word:
            return True
        return False

    def __lt__(self, other):
        if self.appearances < other.appearances:
            return True
        elif self.appearances != other.appearances:
            return False
        if self.word < other.word:
            return True
        return False

    def __ge__(self, other):
        if self.appearances >= other.appearances:
            return True
        elif self.appearances != other.appearances:
            return False
        if self.word >= other.word:
            return True
        return False

    def __gt__(self, other):
        if self.appearances > other.appearances:
            return True
        elif self.appearances != other.appearances:
            return False
        if self.word > other.word:
            return True
        return False
