"""Recursion vs loops."""


def loop_reverse(s: str) -> str:
    """
    Reverse a string using a loop.

    :param s: input string
    :return: reversed input string
    """
    reversed = ""
    for i in s[::-1]:
        reversed += i
    return reversed


def recursive_reverse(s: str) -> str:
    """
    Reverse a string using recursion.

    :param s: input string
    :return: reversed input string
    """
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    return recursive_reverse(s[1:]) + s[0]


def loop_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using a loop.

    :param n: the last number to add to the sum
    :return: sum
    """
    summa = 0
    for each in range(n + 1):
        summa += each
    return summa


def recursive_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using recursion.

    :param n: the last number to add to the sum
    :return: sum
    """
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)


if __name__ == '__main__':
    print(loop_reverse("hello"))  # -> "olleh"
    print(recursive_reverse("Aggghi"))  # -> "A"
    print(recursive_reverse(""))  # -> ""
    print(loop_sum(3))  # -> 6
    print(recursive_sum(95))  # -> 4560
    print(recursive_sum(0))  # -> 0
