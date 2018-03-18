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
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
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
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.convert_name(name) == "ERROR"


def test_addition_negative_a():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.addition(-2, 1) == "-2 + 1 = -1"


def test_addition_negative_b():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.addition(3, -1) == "3 + -1 = 2"


def test_addition_negative_numbers():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.addition(-2, -1) == "-2 + -1 = -3"


def test_addition_positive_numbers():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.addition(3, 1) == "3 + 1 = 4"


def test_subtraction_negative_a():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.subtraction(-2, 1) == "-2 - 1 = -3"


def test_subtraction_negative_b():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.subtraction(3, -1) == "3 - -1 = 4"


def test_subtraction_negative_numbers():
    """
    Assert an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.subtraction(-2, -1) == "-2 - -1 = -1"


def test_subtraction_positive_numbers():
    """
    Assert that an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.subtraction(3, 1) == "3 - 1 = 2"


def test_display_operation_subtract():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    if calculator.display(3, 1, operation="subtraction"):
        assert calculator.subtraction


def test_display_operation_add():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    if calculator.display(3, 1, operation="addition"):
        assert calculator.addition(3, 1)


def test_convert_name1():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.convert_name("Burroughs") == "BUR-9hs"


def test_convert_name2():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.convert_name("uT999AIUHjbhh76235g3dhj") == "UT9-23hj"


def test_convert_name3():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.convert_name("90uT999AIUHjbhh76235g3dhhggfTTFSVGHBJBHSBHJ9897879885444j") == "90U-574j"


def test_convert_name4():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.convert_name("7v6") == "7V6-3v6"


def test_convert_name_2():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.convert_name("BurrougTS") == "BUR-9ts"


def test_line():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.line(0) == ""


def test_line_2():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.line(1) == "-"


def test_line_3():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.line(6, decorated=True) == ">----<"


def test_line_4():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.line(7, decorated=False) == "-------"


def test_line_5():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.line(1, decorated=True) == ""


def test_display():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.display(5, -5, name="Burroughs", operation="subtraction", width=10) == "      BUR-9hs\n>-----------<\n|5 - -5 = 10|\n-------------"


def test_display_add():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.display(5, 7, name="Burroughs", operation="addition", width=10) == "     BUR-9hs\n>----------<\n|5 + 7 = 12|\n------------"


def test_display_wrongwidth():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.display(5, 7, name="Burroughs", operation="addition", width=-20) == "     BUR-9hs\n>----------<\n|5 + 7 = 12|\n------------"


def test_display_wrongwidth2():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert calculator.display(5, 7, name="Burroughs", operation="tere", width=0) == "ERROR"
