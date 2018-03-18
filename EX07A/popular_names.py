"""Order names by popularity."""


from collections import OrderedDict


def read_from_file() -> list:
    """
    Create the list of all the names.

    :return: list
    """
    names = []
    with open("popular_names.txt", encoding='utf-8') as file:
        for line in file:
            names.append(line.strip())
    return names


def to_dictionary(names: list) -> dict:
    """
    Make a dictionary from a list of names.

    :param names: list of all the names
    :return: dictionary {"name:sex": number}
    """
    di = dict()
    for w in names:
        if w in di:
            di[w] = di[w] + 1
        else:
            di[w] = 1
    return di


def to_sex_dicts(names_dict: dict) -> tuple:
    """
    Divide the names by sex to 2 different dictionaries.

    :param names_dict: dictionary of names
    :return: two dictionaries {"name": number}, {"name": number}
    first one is male names, seconds is female names.
    """
    males = [k for k, v in names_dict.items() if ':M' in k]
    male_values = [v for k, v in names_dict.items() if ':M' in k]
    male_keys = []
    for name in males:
        male_keys.append(name.split(':')[0])
    male_names = dict(zip(male_keys, male_values))
    females = [k for k, v in names_dict.items() if ':F' in k]
    values = [v for k, v in names_dict.items() if ':F' in k]
    female_keys = []
    for name in females:
        female_keys.append(name.split(':')[0])
    female_names = dict(zip(female_keys, values))
    return male_names, female_names


def most_popular(names_dict: dict) -> str:
    """
    Find the most popular name in the dictionary.

    If the dictionary is empty, return "Empty dictionary."
    :param names_dict: dictionary of names
    :return: string
    """
    if names_dict == {}:
        return "Empty dictionary."
    else:
        return max(names_dict, key=names_dict.get)


def number_of_people(names_dict: dict) -> int:
    """
    Calculate the number of people in the dictionary.

    :param names_dict: dictionary of names
    :return: int
    """
    people = sum(names_dict.values())
    return people


def names_by_popularity(names_dict: dict) -> str:
    r"""
    Create a string used to print the names by popularity.

    Format:
        1. name: number of people + "\n"
        ...

    Example:
        1. Kati: 100
        2. Mati: 90
        3. Nati: 80
        ...

    :param names_dict: dictionary of the names
    :return: string
    """
    d_sorted_by_value = OrderedDict(sorted(names_dict.items(), key=lambda x: x[1], reverse=True))
    new = '\n'.join(['%s: %s' % (key, value) for (key, value) in d_sorted_by_value.items()])
    lst = new.split("\n")
    pop = ""
    line_num = 1
    if names_dict == {}:
        return ""
    for line in lst:
        popularity = "{}. {}".format(line_num, line)
        line_num += 1
        pop += popularity + "\n"
    return pop


if __name__ == '__main__':
    example_names = ("Kati:F\n" * 1000 + "Lauri:M\n" * 900 + "Mati:M\n" * 1400 + "Mari:F\n" * 600).rstrip("\n").split("\n")
    people = to_dictionary(example_names)
    print(people)  # -> {'Kati:F': 1000, 'Mati:M': 800, 'Mari:F': 600, 'Tõnu:M': 400}
    male_names, female_names = to_sex_dicts(people)
    print(male_names)  # -> {'Mati': 800, 'Tõnu': 400}
    print(female_names)  # -> {'Kati': 1000, 'Mari': 600}
    print(most_popular(male_names))  # -> "Mati"
    print(number_of_people(people))  # -> 2800
    print(names_by_popularity(male_names))  # ->   1. Mati: 800
