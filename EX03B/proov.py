def ends_with_pair(s):
    """

    :param a:
    :return:
    """
    if len(s) == 0: return -1
    if len(s) == 1: return 0
    if s[-1] == s[-2]:
        return len(s) - 2
    else:
        return len(s) - 1
    pass


print(ends_with_pair("tere"))
print(ends_with_pair("terteuiii"))


def swap_pos(numbers, pos):
    """

    :param numbers:
    :param pos:
    :return:
    """
    a = pos
    if a < 0 or a >= len(numbers): return numbers
    b = numbers[pos]
    if b < 0 or b >= len(numbers): return numbers
    numbers[a], numbers[b] = numbers[b], numbers[a]
    return numbers



def new_list(list):
    """

    :param list:
    :return:
    """
    new_list = []
    for i in range(min(len(a), len(b))):
        new_list.append(a[i])
        new_list.append(b[i])
    return new_list


def say_hello(jaan):
    print("hello", "jaan")


say_hello("mari")