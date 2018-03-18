"""Tunnikontroll on tore asi."""


def middle(s):
    """
    Return the middle part of the string.

    When the string has odd number of elements, the middle part is one letter.
    When the string has even number of elements, the middle part is two letters.
    In both cases, there will be equal number of letters to the left and to the right of the "middle" part.
    In case the string is empty, return empty string.
    :param s: string
    :return: string
    """
    if s == "":
        return ""
    if len(s) % 2 == 0:
        return s[int(len(s) / 2) - 1] + s[int(len(s) / 2)]
    if len(s) % 2 == 1:
        return s[int(len(s) / 2)]


def bigger_sum(numbers):
    """
    Find the first index where sum of elements up to that index (itself not included) is bigger than the element.

    If no such element can be found, return -1.

    (bigger_sum([1, 2, 3, 4]))  # => 3
    print(bigger_sum([1, 2, 3]))     # => -1
    print(bigger_sum([2, 1]))       # => 1
    :param numbers: list of non-negative ints
    :return: int
    """
    sum = 0
    for each in range(len(numbers)):
        if numbers[each] < sum:
            return each
        sum += numbers[each]
    return -1


def same_ends(s):
    """
    Return True if the first three letters in the string
    are the same as three last letters reversed.
    The first 3 and last 3 cannot overlap.

    :param s: string
    :return: bool
    """
    if len(s) < 6:
        return False
    if s[0:3] == s[-1:-4:-1]:
        return True
    else:
        return False


def swap_ends(numbers):
    """
    Return list where elements with indices of first element value and last element value are swapped.
    If this cannot be done (both indices must be >= 0), then return original list.
    print(swap_ends([1, 2, 0]))       # [2, 1, 0]
    print(swap_ends([1, 2, 1]))       # [1, 2, 1]
    print(swap_ends([-1, 2, 3, 1]))
    :param numbers: list of ints
    :return: list of ints
    """
    new_list = []
    if len(numbers) == 2:
        if numbers[0] == 0 and numbers[1] == 1 or numbers[0] == 1 and numbers[1] == 0:
            new_list.append(numbers[1])
            new_list.append(numbers[0])
            return new_list
    value = numbers[0]
    if value in range(len(numbers)):
        element = numbers[value]
        second_value = numbers[-1]
        if value == second_value:
            return numbers
        if second_value in range(len(numbers)):
            numbers[second_value] = element
            numbers[value] = value
            return numbers
        return numbers
    return numbers


if __name__ == '__main__':
    print(middle("teeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeere"))  # => er
    print(middle("help"))  # => el
    print(middle("hi"))    # => hi
    print(middle("hey"))   # => e
    print(middle(""))      # => ""

    print(bigger_sum([1, 2, 3, 4]))  # => 3
    print(bigger_sum([1, 2, 3]))     # => -1
    print(bigger_sum([2, 1]))       # => 1
    print(bigger_sum([1, 1]))        # => -1
    print(bigger_sum([]))            # => -1

    print(same_ends("kirik"))    # => False
    print(same_ends("kaakaak"))  # => True
    print(same_ends("tereke"))   # => False

    print(swap_ends([1]))       # [2, 1, 0]
    print(swap_ends([1, 2, 1]))       # [1, 2, 1]
    print(swap_ends([-1, 2, 3, 1]))   # [-1, 2, 3, 1]
    print(swap_ends([2987, 2, 3, -1, 278]))   # [1, 2, 3, -1]
    print(swap_ends([1, 2, 3, 7]))    # [1, 2, 3, 7]
    print(swap_ends([4, 1, 2, 3, 0])) # => [0, 1, 2, 3, 4]