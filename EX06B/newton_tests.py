"""Importing newton file."""


import newton


def test_negative_iteration():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(89, -9) is None


def test_number_iteration_related():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(5, 5) == 2.236


def test_big_iteration_number():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(19, 12875) == 4.359


def test_low_iteration():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(58.78464, 1) == 15.696


def test_no2_iteration():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(763, 2) == 97.865


def test_small_iteration():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(58.78464, 1) == 15.696


def test_limit_iteration():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(98843, 4) == 3099.462


def test_limit2_iteration():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(98987843, 6) == 773385.179


def test_no3_iteration():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(98236, 3) == 6144.999


def test_high_iteration():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(58.78464, 9) == 7.667


def test_float_input():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(4.90, 3) == 2.214


def test_normal_simple_numbers():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(98.467896, 200) == 9.923


def test_negative_numbers():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(-4, 1) is None


def test_both_negative_numbers():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(-14, -31) is None


def test_number_is1():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(1, 98) == 1.0


def test_both_small():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(1.8926, 1.965) == 1.473


def test_both_small2():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(1, 1) == 1.25


def test_both_Xsmall():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(0.008383, 0.0045) == 0.004


def test_number_small():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(1.987432, 2875) == 1.41


def test_numberandite_small():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(0.0000065, 3) == 0.25


def test_number_is_zero():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(0, 9) is None


def test_iteri_is_zero():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(9985.6567, 0.98) == 4992.828


def test_iteri_equal_zero():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(8635, 0) == 4317.5


def test_both_zero():
    """
    Return an expression that subtracts b from a.

    Example: a = 3, b = 1 -> "3 - 1 = 2"
    """
    assert newton.square_root_with_newton_method(0, 0) is None
