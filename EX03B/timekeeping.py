"""Converting time from one system to another."""


def convert(current_time, secs_in_minute, new_secs_in_minute):
    """
    User inputs current time, how many seconds are there in a minute of that given time,
    and new amount of seconds in a minute. Finding new time.

    :param current_time: user input of time
    :param secs_in_minute: current time system seconds in minute
    :param new_secs_in_minute: new time system seconds in minute amount
    :return: other function to round the time to proper format
    """
    if current_time == "00:00":
        return current_time
    elif int(current_time[-2:]) >= int(secs_in_minute):
        return None
    all_seconds = secs_in_minute * int(current_time[:2]) + int(current_time[-2:])
    MM = all_seconds // new_secs_in_minute
    SS = all_seconds % new_secs_in_minute
    return rounding(MM, SS)


def rounding(minutes, seconds):
    """
    Giving time a proper format.

    :param minutes: check if smaller than 10
    :param seconds: check if smaller than 10, round and output two first numbers of the value
    :return: properly formatted time
    """
    seconds = int(round(seconds))
    #if smaller than 10, but 0 infront of the number,
    #else round and return two first numbers of the whole value of seconds
    if minutes < 10 and seconds < 10:
        return str(0) + str(minutes) + ":" + str(0) + str(int(str(seconds)[:2]))
    if minutes < 10:
        return str(0) + str(minutes) + ":" + str(int(str(seconds)[:2]))
    if seconds < 10:
        return str(minutes) + ":" + str(0) + str(int(str(seconds)[:2]))
    else:
        return str(minutes) + ":" + str(int(str(seconds)[:2]))


if __name__ == '__main__':
    print(convert("99:00", 1, 100))
    print(convert("10:00", 30, 100))
    print(convert("12:12", 20, 30))
