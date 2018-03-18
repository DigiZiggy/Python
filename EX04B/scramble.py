"""Scramble  words within sentences."""


def scramble_sentence(sentence: str) -> str:
    """
    Function to change all words in sentence using scramble_word() function.

    :param sentence: sentence to scramble
    :return: scrambled sentence
    """
    if sentence == "":
        return ""
    words = sentence.split(" ")
    tulemus = []
    for each_word in words:
        tulemus.append(scramble_word(each_word))
    string_tulemus = " ".join(tulemus)
    return string_tulemus


def scramble_word(word: str) -> str:
    """
    Sort a word alphabetically, keeping only the astrophe, first and last letter as they were.

    If the last letter of a word is a symbol (.,;?!") the second to last letter must remain the same.
    If the length of the word without symbols is greater than 7 or the word can't be changed from the
    original, the initial word must be returned. When sorting, treat every letter as lowercase.

    :param word: input word
    :return: alphabetically scrambled word
    """
    if word == "":
        return ""
    a = ""
    if word[-1] in '.,;?!"':
        a = word[-1]
        word = word[0:-1]
    if len(word) <= 3:
        return word + a
    if len(word) > 7:
        return word + a
    result = ""
    sonas_on_ylakoma = "'" in word
    if sonas_on_ylakoma:
        ylakoma_index = word.find("'")
        word = word[0:ylakoma_index] + word[ylakoma_index + 1:len(word)]
    frstletter = word[0]
    lastletter = word[-1]
    letters1 = list(word)[1:-1]
    letters1.sort(key=lambda s: s.lower())
    result = list(str(frstletter) + "".join(letters1) + str(lastletter) + a)
    if sonas_on_ylakoma:
        result.insert(ylakoma_index, "'")
    result = "".join(result)
    return result


if __name__ == '__main__':
    print(scramble_sentence("Hey, how's it going?"))  # -> Hey, how's it ginog?
    print(scramble_sentence("The phenomenal power of the human mind."))  # -> The phenomenal peowr of the hamun mind.
    print(scramble_word("Mo'uSE!"))  # -> Mo'SuE!
    print(scramble_word("CoOol"))  # -> "CoOol"
    print(scramble_word("MbaE!"))  # -> Mo'SuE!
    print(scramble_word("M'baE!"))  # -> Mo'SuE!
    print(scramble_word("Mb'aE!"))  # -> Mo'SuE!
    print(scramble_word("Mba'E!"))  # -> Mo'SuE!
    print(scramble_word("MbaE"))  # -> Mo'SuE!
    print(scramble_word("M'baE"))  # -> Mo'SuE!
    print(scramble_word("Mb'aE"))  # -> Mo'SuE!
