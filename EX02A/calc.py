"""Importing math. And calculate the value of z."""


import math


def value_of_z(ex, x, y):
    """
    Calculate the value of z with given x and y with given mathematical expression.

    :param ex: exercise number
    :param x: number
    :param y: number
    :return: float
    """
    if ex == 1:
        # Power to
        return(x ** y + y ** x)
    elif ex == 2:
        # x divided with value minus y divided with value
        return(x / 5.6 - y / 6.5)
    elif ex == 3:
        # Using square roots and logaritms
        return(x / 5 * (y ** 4) * math.log(5)) / (7 * math.sqrt(x ** 2 + y ** 2) + 1)
    else:
        # if ex does not exist
        print("This mathematical expression does not exict!")
        return None


print(value_of_z(1, 10, 10))
