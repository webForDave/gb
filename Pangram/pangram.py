def is_pangram(sentence):
    """Determine if a given sentence/phrase is a pangram

    :param string: sentence to be checked.
    :return bool: True if sentence is a pangram otherwise False
    """
    sentence_lower = sentence.lower().strip()
    list_of_alphabet = list(map(chr, range(97, 123)))
    new_sentence = sentence_lower

    for char in new_sentence:
        if char not in list_of_alphabet:
            new_sentence = new_sentence.replace(char, '')

    sentence_checker = [True if char in new_sentence else False for char in list_of_alphabet]
    
    return False if False in sentence_checker else True



print(is_pangram("The quick brOWn fox jumps over the lazy dog."))