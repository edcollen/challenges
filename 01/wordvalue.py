from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    word_dict = []
    with open(DICTIONARY,'r') as dict_file:
        word_dict = map(lambda w: filter(lambda c: c.isalpha(),w.strip()),dict_file.readlines())
    return tuple(word_dict)

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(map(lambda c: LETTER_SCORES[c.upper()],word))

DICT_WORDS = load_words()

def max_word_value(words=DICT_WORDS):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(map(lambda w: (calc_word_value(w),w),words),key=lambda e: e[0])[1]

if __name__ == "__main__":
    pass # run unittests to validate
