def break_words(stuff):
    """This function will break up words for us."""
    # splits up words by a space specified with ' '
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return (sorted(words))

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """This function will print the first and last words of a sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """This function will sort, then print the first and last words of a sentence"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


