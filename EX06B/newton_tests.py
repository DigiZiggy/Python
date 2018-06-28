"""Importing newton file."""


import newton


def test_negative_iteration():
    """
    Test case of iterations being less than 1 returns None.

    """
    assert newton.square_root_with_newton_method(89, -9) is None


def test_number_iteration_related():
    """
    Test case of iterations and number being the same value.

    """
    assert newton.square_root_with_newton_method(5, 5) == 2.236


def test_big_iteration():
    """
    Test case of iterations being an extremely large value.

    """
    assert newton.square_root_with_newton_method(19, 12875) == 4.359


def test_small_iteration():
    """
    Test case of iterations being an extremely small value.

    """
    assert newton.square_root_with_newton_method(58.78464, 1) == 15.696


def test_large_number():
    """
    Test case of the number being a large value.

    """
    assert newton.square_root_with_newton_method(763, 2) == 97.865


def test_very_large_number():
    """
    Test case of the number being a extremely large value.

    """
    assert newton.square_root_with_newton_method(98843, 4) == 3099.462


def test_xlarge_number():
    """
    Test case of the number being a VERY extremely large value.

    """
    assert newton.square_root_with_newton_method(98987843, 6) == 773385.179


def test_float_number():
    """
    Test case

    """
    assert newton.square_root_with_newton_method(58.78464, 9) == 7.667


def test_float_input():
    """
    Test case

    """
    assert newton.square_root_with_newton_method(4.90, 3) == 2.214


def test_float_number_large_iterations():
    """
    Test case

    """
    assert newton.square_root_with_newton_method(98.467896, 200) == 9.923


def test_negative_number():
    """
    Test case of number being less than 1 returns None.

    """
    assert newton.square_root_with_newton_method(-4, 1) is None


def test_both_negatives():
    """
    Test case of the number and iterations both being less than 1 returns None.

    """
    assert newton.square_root_with_newton_method(-14, -31) is None


def test_number_is1():
    """
    Test case of the number being 1, whatever the iterations, returns 1 always.

    """
    assert newton.square_root_with_newton_method(1, 98) == 1.0


def test_both_small_floats():
    """
    Test case

    """
    assert newton.square_root_with_newton_method(1.8926, 1.965) == 1.473


def test_both_num1():
    """
    Test case

    """
    assert newton.square_root_with_newton_method(1, 1) == 1.25


def test_both_Xsmall():
    """
    Test case

    """
    assert newton.square_root_with_newton_method(0.008383, 0.0045) == 0.004


def test_number_small_float_iterations_big():
    """
    Test case

    """
    assert newton.square_root_with_newton_method(1.987432, 2875) == 1.41


def test_number_xsmall():
    """
    Test case

    """
    assert newton.square_root_with_newton_method(0.0000065, 3) == 0.25


def test_number_is_zero():
    """
    Test case

    """
    assert newton.square_root_with_newton_method(0, 9) is None


def test_iter_is_less_zero():
    """
    Test case

    """
    assert newton.square_root_with_newton_method(9985.6567, 0.98) == 4992.828


def test_iter_equal_zero():
    """
    Test case

    """
    assert newton.square_root_with_newton_method(8635, 0) == 4317.5


def test_both_zero():
    """
    Test case

    """
    assert newton.square_root_with_newton_method(0, 0) is None
