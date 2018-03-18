"""Tunnikontroll on tore asi."""


def count_capitalized_strings(lst):
    """
    Return the count of strings which start with uppercase latin letter.

    :param lst: string
    :return: int
    """
    count = 0
    for each in lst:
        if each[0].isupper():
            count += 1
    return count


def list_of_sums(numbers):
    """
    Replace every element with the sum of all *other* elements.

    :param numbers: list if ints
    :return: list of ints
    """
    new_list = []
    summa = sum(numbers)
    for each in numbers:
        new_list.append(summa - each)
    return new_list


def increment_elements_by_pos(numbers, pos):
    """
    Return numbers where the element at pos
    and the element at the index of value of pos
    are replaced with the sum on those two elements.

    If at least one of the indices is out of the list
    or those both point to the same element, return original list.

    # pos and value at pos point to the same element, return original
    (increment_elements_by_pos([1, 2, 6, 4], 1))  # => [1, 8, 8, 4]
    print(increment_elements_by_pos([1, 3, 6, 4], 1))  # => [1, 7, 6, 7]
    :param numbers: list of ints
    :param pos: int
    :return: list of ints
    """
    if pos in range(len(numbers)):
        if pos == numbers[pos]:
            return numbers
        value = numbers[pos]
        if value in range(len(numbers)):
            element = numbers[value]
            numbers[pos] = value + element
            numbers[value] = element + value
        return numbers
    else:
        return numbers

def reverse_two(s):
    """
    Return string where first two letters are put into end in reverse order.
    If there are no 2 letters, return original string.

    String consists of only latin letters.
    :param s: string
    :return: string
    """
    if len(s) < 2:
        return s
    return s[2:] + s[1] + s[0]


if __name__ == '__main__':

    print(count_capitalized_strings(["abc", "Abc", "ABC"]))   # => 2
    print(count_capitalized_strings(["abc"]))   # => 0
    print(count_capitalized_strings(["abc"]))   # => 0
    print(count_capitalized_strings(["aBc", "A", "1A"]))   # => 1

    print(list_of_sums([1, 2, 3])) # => [5, 4, 3]
    print(list_of_sums([2, 7, 9])) # => [16, 11, 9]
    print(list_of_sums([]))        # => []
    print(list_of_sums([1]))       # => [0]
    print(list_of_sums([1, 2]))    # => [2, 1]

    # pos and value at pos point to the same element, return original
    print(increment_elements_by_pos([0, 1], 1))  # => [0, 1]

    print(increment_elements_by_pos([1, 1], 0))  # => [1, 5, 5, 4]
    print(increment_elements_by_pos([1, 2, 3, 4], 2))  # => [1, 2, 7, 7]
    print(increment_elements_by_pos([1, 2, 6, 4], 1))  # => [1, 8, 8, 4]
    print(increment_elements_by_pos([1, 3, 6, 4], 1))  # => [1, 7, 6, 7]
    print(increment_elements_by_pos([1, 3, 6, 4], 2))  # => [1, 3, 6, 4]
    print(increment_elements_by_pos([-1, 3, 6, 4], 0)) # => [-1, 3, 6, 4]
    print(increment_elements_by_pos([-1, 3, 6, 1], -1)) # => [-1, 3, 6, 1]

    print(reverse_two("tere"))  # => reet
    print(reverse_two("ter"))  # => ret
    print(reverse_two("te"))  # => et
    print(reverse_two("t"))  # => t
    print(reverse_two(""))  # => ""