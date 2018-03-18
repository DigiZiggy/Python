"""comparator."""


def comparator(number: float) -> str:
    """Kasutan comparator funktsiooni.

    et võrrelda antud numbrit viiega ja väljastada võrdlusest tulenev vastav sõnum.
    :param num: input number
    :return: message regarding the number value compared to five.
    """
    if number > 5:
        return("The input number is bigger than 5!")
        # Võrdlen kas sisse pandud number on viiest suurem, ja väljastab vastava vastuse siis.
    elif number < 5:
        return("The input number is smaller than 5!")
        # Võrdlen kas sisse pandud number on viiest väiksem, ja väljastab vastava vastuse siis.
    else:
        return("The input number is 5!")
        # Ütlen programmile, et kui eelnev protsess ei viinud kuhugi, siis väljasta selline vastus.


print(comparator(2))
