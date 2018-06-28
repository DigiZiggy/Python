"""Scramble letters in words within sentences."""


def scramble_sentence(sentence: str) -> str:
    """
    Function to change all words in sentence using scramble_word() function.

    :param sentence: sentence to scramble
    :return: scrambled sentence
    """
    if sentence == "":
        return ""
    words = sentence.split(" ")
    result = []
    for each_word in words:
        result.append(scramble_word(each_word))
    string_result = " ".join(result)
    return string_result


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
    last_letter_symbol = ""
    if word[-1] in '.,;?!"':
        last_letter_symbol = word[-1]
        word = word[0:-1]
    if len(word) <= 3:
        return word + last_letter_symbol
    if len(word) > 7:
        return word + last_letter_symbol
    astrophe_in_word = "'" in word
    if astrophe_in_word:
        astrophe_index = word.find("'")
        #taking the strophe out of the word before sorting alphabetically
        word = word[0:astrophe_index] + word[astrophe_index + 1:len(word)]
    frstletter = word[0]
    lastletter = word[-1]
    #letters to sort (first and last letter taken out)
    letters1 = list(word)[1:-1]
    letters1.sort(key=lambda s: s.lower())
    result = list(str(frstletter) + "".join(letters1) + str(lastletter) + last_letter_symbol)
    #if astrophe was present, insert it back to the same index as it was before
    if astrophe_in_word:
        result.insert(astrophe_index, "'")
    result = "".join(result)
    return result


if __name__ == '__main__':
    print(scramble_sentence("Hey, how's it going?"))  # -> Hey, how's it ginog?
    print(scramble_sentence("The phenomenal power of the human mind."))  # -> The phenomenal peowr of the hamun mind.
    print(scramble_word("Mo'uSE!"))  # -> Mo'SuE!
    print(scramble_word("CoOol"))  # -> "CoOol"
