from random import sample

# Do not modify or remove this

    WORD_LIST = ["banana","apple","orange","fraise","dog","cat"]

def random_word():
    return random_words(1)[0]

def random_words(length):
    return sample(WORD_LIST, length)
