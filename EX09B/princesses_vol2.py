"""Generate list of princesses."""


import base64


statuses = [
    "INJURED", "BORED", "EATEN", "SAVED",
    "IN PANIC", "SLAYED THE DRAGON HERSELF",
    "FIGHTS FOR LIFE"
]


places_danger = [
    "Dark Cave", "Dungeon", "Old Shack",
    "High Mountain", "Abandoned Prison",
    "Misty Swamp", "Ancient Ruins"
]


places_safe = [
    "Castle", "Pub", "Town Hall", "Office",
    "Library"
]


places_afterlife = [
    "Underworld", "Heaven"
]


details = [
    "Pretty", "Can cook", "Likes books", "Programmer",
    "Will rule the kingdom", "Afraid of spiders",
    "Sassy", "None"
]


def read(read_file) -> list:
    """
    Read, decrypt and save information from the given file.

    :param file: the file we read from
    :exception: Exception
    :return: lines
    """
    princess_list = []
    try:
        with open(read_file, encoding='utf-8', mode='r') as file:
            for line in file:
                princess_list.append(line)
    except Exception:
        print("File not found!")
        raise Exception("File not found!")
    each_princess = []
    for line in princess_list:
        decoded = decode(line)
        princess_info = extract_information(decoded)
        if "None" in princess_info[0:3] or None in princess_info[0:3]:
            raise InvalidPrincessException("Invalid princess!")
        each_princess.append(princess_info)
    return each_princess[3:-1]


def decode(line: str) -> str:
    """
    Decode each line.

    Hint: base64.
    :param line: line from the encoded file.
    :return: same decoded line. String.
    """
    decoded = base64.b64decode(line)
    returns_decoded = decoded.decode('utf8')
    return str(returns_decoded)


def extract_information(line: str) -> list:
    """
    Extract information from each line (without spaces or extra tabulation symbols).

    Example output: ['Helen-elizabeth', 'IN PANIC', 'Ancient Ruins', None]
    Example output: ['Julianne', 'EATEN', 'Heaven', 'Will rule the kingdom'].
    Obviously, she won't rule anything, however. How sad.
    :param line: decrypted line from the file.
    :return: information about single princess
    """
    name = ""
    status = []
    place = []
    detail = []
    for each in statuses:
        if each in line:
            status.append(each)
    for each in places_safe:
        if each in line:
            place.append(each)
            break
    for each in places_danger:
        if each in line:
            place.append(each)
            break
    for each in places_afterlife:
        if each in line:
            place.append(each)
            break
    for each in details:
        if each in line:
            detail.append(each)
            break
    for each in statuses:
        if each in line:
            name = line[:line.index(each)].rstrip()
            break
    result = [name] + status + place + detail
    return result


def filter_by_status(lines) -> list:
    """
    Filter out non-relevant statuses.

    Statuses to filter: "EATEN", "SAVED", "SLAYED THE DRAGON HERSELF". There is no point to save those.

    :param lines: lines tere
    :return: list
    """
    to_filter = ["EATEN", "SAVED", "SLAYED THE DRAGON HERSELF"]
    needs_saving = []
    for each in lines:
        if each[1] not in to_filter:
            needs_saving.append(each)
    return needs_saving


def sort_by_status(filtered_lines) -> list:
    """
    Sort lines by pattern FIGHTS FOR LIFE > INJURED > IN PANIC > BORED.

    FIGHTS FOR LIFE comes before INJURED etc.

    :param filtered_lines:
    :return: sorted lines.
    """
    first = []
    second = []
    third = []
    forth = []
    for each in filtered_lines:
        if each[1] == "FIGHTS FOR LIFE":
            first.append(each)
        if each[1] == "INJURED":
            second.append(each)
        if each[1] == "IN PANIC":
            third.append(each)
        if each[1] == "BORED":
            forth.append(each)
    result = first + second + third + forth
    return result


def sort_by_place(sorted_lines):
    """
    Sorting sorted list by places.

    :param sorted_lines:
    :return:
    """
    first = []
    second = []
    third = []
    forth = []
    for each in sorted_lines:
        print(each)
        if "None" in each[:3] or None in each[:3]:
            raise InvalidPrincessException("Invalid princess!")
        if each[1] == "SAVED" or each[1] == "EATEN" or each[1] == "SLAYED THE DRAGON HERSELF":
            raise InvalidPrincessException("The princess is already {}!".format(each[1]))
        if each[1] == "FIGHTS FOR LIFE":
            first.append(each)
        if each[1] == "INJURED":
            second.append(each)
        if each[1] == "IN PANIC":
            third.append(each)
        if each[1] == "BORED":
            forth.append(each)
    first_sorted = []
    second_sorted = []
    third_sorted = []
    forth_sorted = []
    for each in first:
        if first_sorted.count(each) == 0:
            for real_element in first:
                if real_element[2] == each[2]:
                    first_sorted.append(real_element)
    for each in second:
        if second_sorted.count(each) == 0:
            for real_element in second:
                if real_element[2] == each[2]:
                    second_sorted.append(real_element)
    for each in third:
        if third_sorted.count(each) == 0:
            for real_element in third:
                if real_element[2] == each[2]:
                    third_sorted.append(real_element)
    for each in forth:
        if forth_sorted.count(each) == 0:
            for real_element in forth:
                if real_element[2] == each[2]:
                    forth_sorted.append(real_element)
    result = first_sorted + second_sorted + third_sorted + forth_sorted
    return result


def write(read_file):
    """
    Write the sorted lines to the new file 'princesses_to_save.txt'.

    The last princess is NOT followed by a blank line.
    :param read_file: the file we read from
    :return: None
    """
    line = read(read_file)
    filtered = filter_by_status(line)
    sorted = sort_by_status(filtered)
    sorted_by_place = sort_by_place(sorted)
    to_write = ""
    for each in sorted_by_place:
        width = 20
        Name = each[0]
        Status = each[1]
        Place = each[2]
        Details = each[3]
        to_write += "{}{}{}{}\n".format(Name.ljust(width), Status.ljust(width), Place.ljust(width), Details)
    with open('princesses_to_save.txt', 'w') as f:
        f.write("NAME                STATUS              PLACE               DETAILS\n\
====================================================================\n\n")
        f.write(str(to_write.strip()))


class InvalidPrincessException(Exception):
    """
    Invalid Exception class.

    :param Exception:
    :return:
    """

    pass


if __name__ == '__main__':
    sort_by_place([['Minnie', 'EATEN', 'Dungeon', 'Will rule the kingdom']])
    write("princesses.txt")
