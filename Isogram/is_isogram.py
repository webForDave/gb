def is_isogram(string):
    """Check if a given word is an Isogram

    :param string: word to be checked
    :return bool: True if string is an isogram otherwise False
    """
    string_lower = string.lower()
    list_of_alphabet = list(map(chr, range(97, 123))) # list of alphabet a-z
    new_string = string_lower

    # checks if each character in new_string is in list_of_alphabet
    for char in new_string:
        if char not in list_of_alphabet:
            new_string = new_string.replace(char, '')

    """if chracter exists more than once in string, appends False to true_false_checker list
    otherwise, appends True"""  
    # true_false_checker = []  
    # for char in new_string:
    #     if new_string.count(char) > 1:
    #         true_false_checker.append(False)
    #     else:
    #         true_false_checker.append(True)
    true_false_checker = [True if new_string.count(char) == 1 else False for char in new_string]

    if False in true_false_checker:
        return False
    else:
        return True


print(is_isogram('dave1212'))