"""Importing Acronymator."""


from acronymator import acronymize


"""Main module."""


def get_reversed_acronym(message: str) -> str:
    """
    The main method of the program.

    :param message: initial text
    :return: reversed acronym of the given message
    """
    return acronymize(message)


if __name__ == '__main__':
    print(get_reversed_acronym("That wa-s quite easy, huh?"))  # --> EQT
    print(get_reversed_acronym("Hello, my name is Karen"))  # --> KNH
    print(get_reversed_acronym("Hello,!.#)"))  # --> ""
    print(get_reversed_acronym(".,212 A 13 he,,.llo to me"))  # --> ""
    print(get_reversed_acronym("Light amplification by the stimulated emission of radiation."))  # --> RESAL
    print(get_reversed_acronym("Self-contained underwater breathing apparatus."))  # --> ABUS
    print(get_reversed_acronym("   Spaces     are    irrelevant   "))  # --> IS
