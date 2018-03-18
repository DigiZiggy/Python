"""Turn a phrase into acronym."""


def acronymize(message: str) -> str:
    """
    Turn the input text into the acronym and reverse it, if the text is not too long.

    :param message: initial text
    :return: reversed acronym
    """
    new_message = ""
    message = message.split()
    if check_message_length(message) is True:
        for each_word in message:
            if check_word(each_word) is True:
                new_message += each_word[0]
        return reverse(new_message.upper())
    else:
        return "Sorry, the input's just too long!"


def check_word(word: str) -> bool:
    """
    Check if the word is long enough and does not contain special symbols.

    The word should be more than 3 chars long (without symbols).
    :param word: word
    :return: bool
    """
    new_word = ""
    word_symbols = ""
    symbol = "()1234567890!?_@#$%^&*.,'"
    bad_symbols = "`~=+:;{}[]\"/><"
    if word[0] in symbol:
        return False
    for letter in word:
        if letter in symbol:
                word_symbols += letter
                new_letter = letter.replace(letter, "")
                new_word += new_letter
        if letter in bad_symbols:
            return False
        if letter == "-":
            new_word += letter
        elif letter not in symbol:
            new_word += letter
    if new_word + word_symbols == word:
        if len(new_word) >= 4:
            return True
        else:
            return False
    else:
        return False


def check_message_length(words: list) -> bool:
    """
    Check if the initial text length is OK (does not contain more than 50 words).

    :param words: list of words
    :return: bool
    """
    if len(words) <= 50:
        return True
    else:
        return False


def reverse(message: str) -> str:
    """
    Reverse the given message.

    :param message: acronym
    :return: reversed message
    """
    reversed_message = message[::-1]
    return reversed_message
