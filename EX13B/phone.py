"""Phone numbers."""


def how_many_calls(n, cache={0: 1, 1: 1, 2: 2, 3: 4}):
    """
    Return the number of calls made during the current minute.

    Arguments:
    n -- the current minute.
    """
    if n < 0:
        return None
    if n in cache:
        return cache[n]
    cache[n] = how_many_calls(n - 1, cache) + how_many_calls(n - 2, cache) + how_many_calls(n - 3, cache)
    return cache[n]


def how_many_people(n, cache={0: 1, 1: 2, 2: 4, 3: 8}):
    """
    Return the number of people who know after n minutes has passed.

    Arguments:
    n -- how many minutes has passed.
    """
    if n < 0:
        return None
    if n in cache:
        return cache[n]
    cache[n] = (how_many_people(n - 1, cache) * 2) - cache[n - 4]
    return cache[n]


if __name__ == "__main__":
    print(how_many_calls(0))  # -> 2
    print(how_many_calls(4))  # -> 7
    print(how_many_calls(10))  # -> 274
    print(how_many_people(0))  # -> 4
    print(how_many_people(4))  # -> 15
    print(how_many_people(10))  # -> 600
