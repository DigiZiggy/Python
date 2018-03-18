"""Encoding a message."""


import re
import random as r


def generate(message):
    """
    Generate message.

    :param message:
    :return:
    """
    new_message = ""
    symbols = "\/#$%^&*@1234567890"
    for i in range(len(message)):
        char = message[i]
        new_message += char
        if char.isalpha() and char != " " and i < len(message) - 1 and message[i + 1] != " ":
            for j in range(r.randint(1, 8)):
                new_message += r.choice(symbols)


generate("Hello and welcome to python, pal")


def _correct_message(message):
    """
    Change the encrypted message readable.

    :param message:
    :return: All symbols to be take out are as follows: /#$%^&*@0123456789)
    """
    pattern = "(?<!^)(?<![\/#$%^&*@1234567890 ])([\/#$%^&*@1234567890]+)(?![\/#$%^&*@1234567890 ])(?!$)"
    new_word = re.sub(pattern, "", message)
    return new_word


def _encrypt_message(message, shift):
    """
    The input message will be encrypted, using a certain shift, Caesar shift will be used for encrypting.

    :param message:
    :param shift: Shift is not negative, but can be bigger than 26. (use modulo)
    :return:  All symbols remain the same, but letters will be encrypted.
    """
    key = 'abcdefghijklmnopqrstuvwxyz'
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    if shift > 26:
        shift %= 26
    for l in message:
        if l in upper:
            i = (upper.index(l) + shift) % 26
            result += upper[i]
        elif l in key:
            i = (key.index(l) + shift) % 26
            result += key[i]
        else:
            result += l
    return result


def get_corrected_encrypted_message(initial_message, shift):
    """
    Return the corrected and encrypted original message.

    :param initial_message:
    :param shift:
    :return: Use that function in other modules as well.
    """
    return _encrypt_message(_correct_message(initial_message), shift)
