"""Tunnikontroll."""


def strpad_a(word: str, left: int, length: int) -> str:
    """
    Return "a" padded word where word starts at position left and total length of result is length.

    length is always enough to fit the word. left >= 0.

    :param word: str to be paddedgdgd
    :param left: start position of word
    :param length: total length of result
    :return: "a" padded word
    """
    left_word = "a" *left + word
    for each in range(length-len(left_word)):
        left_word += "a"
    return left_word


def get_bigger_digit(number: int) -> int:
    """
    Return either the first or the last digit, whichever is bigger.

    :param number: non-negative int
    :return: int (one digit)
    """
    new = str(number)
    if len(new) < 2:
        return int(new)
    if new[0] == new[-1]:
        return int(new[0])
    if new[0] > new[-1]:
        return int(new[0])
    if new[-1] > new[0]:
        return int(new[-1])


def sum_of_tens(numbers: list) -> int:
    """
    Return the sum of all elements divisible by 10.

    :param numbers: list of ints
    :return: int
    """
    sum = 0
    if numbers == []:
        return 0
    for each in numbers:
        if each % 10 == 0:
            sum += each
    return sum


def jump_right(numbers: list) -> list:
    """
    Return "a" padded word where word starts at position left and total length of result is length.

    length is always enough to fit the word. left >= 0.

    :param word: str to be padded
    :param left: start position of word
    :param length: total length of result
    :return: "a" padded word
    """
    if len(numbers) < 2:
        return numbers
    value = numbers[0]
    if value in range(len(numbers)):
        numbers.remove(value)
        numbers.insert(value, value)
    return numbers

if __name__ == '__main__':
    assert strpad_a("hi", 5, 10) == "aaaaahiaaa"
    assert strpad_a("hi", 5, 7) == "aaaaahi"
    assert strpad_a("hi", 0, 7) == "hiaaaaa"

    assert get_bigger_digit(123) == 3
    assert get_bigger_digit(321) == 3
    assert get_bigger_digit(3214) == 4
    assert get_bigger_digit(32143) == 3
    assert get_bigger_digit(7) == 7

    assert sum_of_tens([1, 2, 3]) == 0
    assert sum_of_tens([1, 2, 10, 20]) == 30
    assert sum_of_tens([10, 20, 70]) == 100
    assert sum_of_tens([]) == 0

    assert jump_right([1, 2, 3]) == [2, 1, 3]
    assert jump_right([3, 2, 3, 4]) == [2, 3, 4, 3]
    assert jump_right([7]) == [7]