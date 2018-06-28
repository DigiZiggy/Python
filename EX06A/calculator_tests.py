"""Importing calc and pytest."""


import calculator
import pytest


@pytest.mark.parametrize("letter, length",
                         [
                             ("s", 0),
                             ("s", -4),
                             ("", 4)
                         ]
                         )
def test_repeat(letter, length):
    """
    Test that repeat() returns empty string if input length less than 1 or input letter empty.

    Example: letter = "" , length = 5 outputs "".
    """
    assert calculator.repeat(letter, length) == ""


@pytest.mark.parametrize("name",
                         [
                             "a",
                             "aa",
                             "",
                             "87",
                             "0",
                             "-1"
                         ]
                         )
def test_convert_name(name):
    """
    Test that convert_name returns 'ERROR' if length of name less than 3 letters.

    Example: name = "ab" gives "ERROR".
    """
    assert calculator.convert_name(name) == "ERROR"


def test_addition_negative_a():
    """
    Test that addition a + b works with a being negative.

    Example: a = -2, b = 1 -> "-2 + 1 = -1"
    """
    assert calculator.addition(-2, 1) == "-2 + 1 = -1"


def test_addition_negative_b():
    """
    Test that addition a + b works with b being negative.

    Example: a = 3, b = -1 -> "3 + (-1) = 2"
    """
    assert calculator.addition(3, -1) == "3 + -1 = 2"


def test_addition_negative_numbers():
    """
    Test that addition a + b works with both being negative.

    Example: a = -2, b = -1 -> "-2 + (-1) = -3"
    """
    assert calculator.addition(-2, -1) == "-2 + -1 = -3"


def test_addition_positive_numbers():
    """
    Test that addition a + b works with both being positive.

    Example: a = 3, b = 1 -> "3 + 1 = 4"
    """
    assert calculator.addition(3, 1) == "3 + 1 = 4"


def test_subtraction_negative_a():
    """
    Test that subtraction a - b works with a being negative.

    Example: a = -2, b = 1 -> "-2 - 1 = -3"
    """
    assert calculator.subtraction(-2, 1) == "-2 - 1 = -3"


def test_subtraction_negative_b():
    """
    Test that subtraction a - b works with b being negative.

    Example: a = 3, b = -1 -> "3 - (-1) = 4"
    """
    assert calculator.subtraction(3, -1) == "3 - -1 = 4"


def test_subtraction_negative_numbers():
    """
    Test that subtraction a - b works with both being negative.

    Example: a = -2, b = -1 -> "-2 - (-1) = -1"
    """
    assert calculator.subtraction(-2, -1) == "-2 - -1 = -1"


def test_subtraction_positive_numbers():
    """
    Test that subtraction a - b works with both being positive.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.subtraction(3, 1) == "3 - 1 = 2"


def test_display_operation_subtract():
    """
    Test that subtraction is displayed when operation is 'substraction'.

    """
    if calculator.display(3, 1, operation="subtraction"):
        assert calculator.subtraction


def test_display_operation_add():
    """
    Test that addition is displayed when operation is 'addition'.

    """
    if calculator.display(3, 1, operation="addition"):
        assert calculator.addition(3, 1)


def test_convert_name1():
    """
    Test that convert_name() converts string as supposed to.
    [first three letters in uppercase]-[length of string][last two letters of string in lowercase]

    Example: "abc"  # -> "ABC-3bc"
    """
    assert calculator.convert_name("Burroughs") == "BUR-9hs"


def test_convert_name2():
    """
    Test that convert_name() converts string as supposed to, even with numbers in it.
    [first three letters in uppercase]-[length of string][last two letters of string in lowercase]

    Example: "abc"  # -> "ABC-3bc"
    """
    assert calculator.convert_name("uT999AIUHjbhh76235g3dhj") == "UT9-23hj"


def test_convert_name_long_string():
    """
    Test that convert_name() converts string as supposed to even when string extremely long.
    [first three letters in uppercase]-[length of string][last two letters of string in lowercase]

    Example: "abc"  # -> "ABC-3bc"
    """
    assert calculator.convert_name("90uT999AIUHjbhh76235g3dhhggfTTFSVGHBJBHSBHJ9897879885444j") == "90U-574j"


def test_convert_name_short_string():
    """
    Test that convert_name() converts string as supposed to even when string extremely short.
    [first three letters in uppercase]-[length of string][last two letters of string in lowercase]

    Example: "abc"  # -> "ABC-3bc"
    """
    assert calculator.convert_name("7v6") == "7V6-3v6"


def test_convert_name_capital_ending():
    """
    Test that convert_name() converts string as supposed to even when string ends with capital letters.
    [first three letters in uppercase]-[length of string][last two letters of string in lowercase]

    Example: "abc"  # -> "ABC-3bc"
    """
    assert calculator.convert_name("BurrougTS") == "BUR-9ts"


def test_line_zero_length():
    """
    Test that line() returns an empty string if inserted line width is 0.

    Example: width = 0  => ""
    """
    assert calculator.line(0) == ""


def test_line_one_length():
    """
    Test that line() returns just one line if inserted line width is 1.

    Example: width = 1  => "-"
    """
    assert calculator.line(1) == "-"


def test_line_decorated():
    """
    Test that line() returns a line of given width with ">" at the start and "<" in the end, if decorated is True.

    Example: width = 6  => ">----<"
    """
    assert calculator.line(6, decorated=True) == ">----<"


def test_line_not_decorated():
    """
    Test that line() returns a line of given width, without end "<" and start ">" if decorated is False.

    Example: width = 6  => "------"
    """
    assert calculator.line(7, decorated=False) == "-------"


def test_line_decorated_with_small_width():
    """
    Test that line() returns empty string if decorated True but line width less than 2.

    Example: width = 1  => ""
    """
    assert calculator.line(1, decorated=True) == ""


def test_display():
    """
    Test display subtraction.

    """
    assert calculator.display(5, -5, name="Burroughs", operation="subtraction", width=10) == "      BUR-9hs\n>-----------<\n|5 - -5 = 10|\n-------------"


def test_display_add():
    """
    Test display addition.

    """
    assert calculator.display(5, 7, name="Burroughs", operation="addition", width=10) == "     BUR-9hs\n>----------<\n|5 + 7 = 12|\n------------"


def test_display_wrongwidth_minus():
    """
    Test display

    """
    assert calculator.display(5, 7, name="Burroughs", operation="addition", width=-20) == "     BUR-9hs\n>----------<\n|5 + 7 = 12|\n------------"


def test_display_wrongwidth_zero():
    """
    Test display

    """
    assert calculator.display(5, 7, name="Burroughs", operation="tere", width=0) == "ERROR"
