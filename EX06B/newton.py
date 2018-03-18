"""Calculate square root with Newton method."""


def square_root_with_newton_method(number, iterations):
    """
    Calculate the given number's approximate square root.

    :param number: number from which the square root will be calculated.
    :param iterations: number of formula cycles, highest integer not bigger than the value (1.9 => 1).
    :return: approximate square root. In the case of non-positive number or negative iterations, return None.
    """
    # Inital value of g.
    # Cycle based on the iterations number.
    # Formula in the cycle.
    # Return the rounded final result.
    gList = []
    x = number
    g = x / 2
    iterations = int(iterations)
    if x <= 0 or iterations < 0:
        return None
    if iterations == 0:
        gList.append(int((g * 1000) + 0.5) / 1000.0)
        return gList[0]
    for i in range(iterations):
        g = (g + x / g) / 2
        gList.append(int((g * 1000) + 0.5) / 1000.0)
    return gList[-1]


if __name__ == '__main__':
    print(square_root_with_newton_method(98987843, 6))
