"""Decoder."""


import encoder


def _decrypt_message(encrypted_message, shift):
    """
    Decode the message, using given shift.

    Return decrypted message, Don't use this function outside of decoder module. Works the same as _encrypt_message,
    only in reverse. Uses shift that is not negative, but can be greater than 26.
    :param encrypted_message:
    :param shift:
    :return:
    """
    return encoder._encrypt_message(encrypted_message, -shift)


def get_message(initial_message, shift, decrypt=False):
    """
    Korrekteerib ja krüpteerib argumendina ette antud sõnumi, kasutades ette antud nihet (shift).

    Kui boolean decrypt=False tagastab krüpteeritud sõnumi. Vastasel juhul tagastab dekrüpteeritud sõnumi.
    Algse sõnumi korrastamiseks ja krüpteerimiseks peab kasutama encoder.py moodulis olevat avalikku funktsiooni.
    :param initial_message:
    :param shift:
    :param decrypt:
    :return:
    """
    if decrypt:
        decrypt = _decrypt_message(initial_message, shift)
        return encoder.get_corrected_encrypted_message(decrypt, shift)
    else:
        return encoder.get_corrected_encrypted_message(initial_message, shift)
