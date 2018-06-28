"""Sort the strings in ascending order."""


def get_min_len_word(string_list):
    """
    Function to find and return the minimum length word in string_list.

    If two Strings are the same length, the String appearing first must also
    be returned first.

    :param string_list: List of Strings to look through.
    :return: Smallest length String from string_list.
    """
    if string_list == []:
        return None
    else:
        from_small_to_big = min(string_list, key=len)
        return from_small_to_big


def sort_list(string_list):
    """
    Function to sort string_list by the length of it's elements.

    This function must utilize get_min_len_word().

    :param string_list: List of Strings to be sorted.
    :return: Sorted list of Strings.
    """
    from_small_to_big = []
    if string_list == []:
        return []
    if len(string_list) == 1:
        return string_list
    for word in range(len(string_list)):
        word = get_min_len_word(string_list)
        from_small_to_big.append(word)
        string_list.remove(word)
    return from_small_to_big


print(get_min_len_word(["bskjdbasjk,sd", "jsxbjxsjsn;"]))
print(get_min_len_word(['Hello', 'there']))
print(get_min_len_word(['b', 'have', 'a', 'little', 'lamb']))
print(sort_list([]))
print(sort_list(['Hello', 'there']))
print(sort_list(['Mary', 'have', 'a', 'little', 'lamb']))
