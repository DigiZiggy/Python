"""Generate list of princesses."""


import base64
import re


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
    extracted_line = []
    extracted = re.split(r"\s{2,}", line.strip())
    for each in extracted:
        if each == "":
            continue
        else:
            extracted_line.append(each)
    return extracted_line


def filter_by_status(lines) -> list:
    """
    Filter out non-relevant statuses.

    Statuses to filter: "EATEN", "SAVED", "SLAYED THE DRAGON HERSELF". There is no point to save those.

    :param lines: lines
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
    return first + second + third + forth


def write(read_file):
    """
    Write the sorted lines to the new file 'princesses_to_save.txt'.

    The last princess is NOT followed by a blank line.

    Format:
            Name
            Status
            Place
            Details
            <NEW LINE>
    Example:
            Kathi
            FIGHTS FOR LIFE
            Old Shack
            Sassy
    :param read_file: the file we read from
    :return: None
    """
    line = read(read_file)
    filtered = filter_by_status(line)
    sorted = sort_by_status(filtered)
    to_write = ""
    for each in sorted:
        Name = each[0]
        Status = each[1]
        Place = each[2]
        Details = each[3]
        to_write += "\n{}\n{}\n{}\n{}\n".format(Name, Status, Place, Details)
    with open('princesses_to_save.txt', 'w') as f:
        f.write(str(to_write.strip()))


if __name__ == "__main__":
    write("princesses.txt")
