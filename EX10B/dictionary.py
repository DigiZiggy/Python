"""GENIUS idea I had."""

import string


class Dictionary:
    """Represent a online dictionary."""

    def __init__(self, initial_data):
        """
        Klassi konstruktor, võtab ette argumendina algandmed ja loob klassi objekti.

        :param self:
        :param initial_data:
        :return:
        """
        self.initial_data = initial_data.lower()
        new_data = []
        self.words = self.initial_data.strip().replace("\n", "- ").replace("- -", "--").split("- ")
        for each in self.words:
            if each.endswith("-"):
                continue
            else:
                new_data.append(each)
        self.new_data = new_data
        self.clean_verbs = []
  #      self.clean_verbs = clean_verbs
        self.clean_adjectives = []
    #    self.clean_adjectives = clean_adjectives
        self.clean_nouns = []
  #      self.clean_nouns = clean_nouns
        print(self.clean_nouns)

        print(new_data)


    def get_definitions(self, word):
        """
        Saab ette sõna ja tagastab listi, mille sees on kõik selle sõna definitsioonid (neid saab olla mitu).

        Listis võivad definitsioonid olla suvalises järjekorras. Kui sellist sõna sõnastikus ei ole, tagastada tühi list.
        :param self:
        :param word:
        :return:
        """
        if self.is_word_noun(word) is False and self.is_word_adjective(word) is False and self.is_word_verb(word) is False:
            return []
        """
        definition_list = []
        list1 = self.words[::2]
        print(list1)

        list2 = self.words[1::2]

    #    two_lists_together = zip(list1, list2)

        dictionary = dict(zip(list1, list2))
        #dictionary.strip()

        print(dictionary)
        """


    def is_word_noun(self, word):
        """
        Saab ette sõna ja tagastab True, kui see sõna on nimisõnade hulgas.

        Muul juhul tagastab False.
        :param self:
        :param word:
        :return:
        """
        if word in self.clean_nouns:
            return True
        else:
            return False

    def is_word_verb(self, word):
        """
        Saab ette sõna ja tagastab True, kui see sõna on tegusõnade hulgas. Muul juhul tagastab False.

        :param self:
        :param word:
        :return:
        """
        if word in self.clean_verbs:
            return True
        else:
            return False

    def is_word_adjective(self, word):
        """
        Saab ette sõna ja tagastab True, kui see sõna on omadussõnade hulgas. Muul juhul tagastab False.

        :param self:
        :param word:
        :return:
        """
        if word in self.clean_adjectives:
            return True
        else:
            return False

    def get_all_nouns(self):
        """
        Tagastab listi, mille sees on kõik nimisõnad, mis on sõnastikku kantud. Kui sõnu ei ole, tagastab tühja listi.

        :param self:
        :return:
        """
        symbols = "0123456789!\" #$%&'()*+,./:;<=>?@[\\]^_`{|}~"
        nouns = []
        clean_nouns = []
        #      self.words.replace("-", ",")
        for word in self.new_data:
            if None:
                return []
            if len(word) < 4:
                continue
            if word[0] == "(" and word[1] == "n":
                word = word[3:-1]
                if word == "":
                    continue
                if " " in word:
                    continue
                else:
                    nouns.append(word)
        for each in nouns:
            if None:
                return []
            if each[0] == "-" or each[-1] == "-":
                continue
            else:
                clean_nouns.append(each)
        for each in clean_nouns:
            for i in each:
                if i in symbols:
                    clean_nouns.remove(each)
                    break
        clean_nouns = list(set(clean_nouns))
        self.clean_nouns = clean_nouns
        print(self.clean_nouns)
        return self.clean_nouns

    def get_all_verbs(self):
        """
        Tagastab listi, mille sees on kõik tegusõnad, mis on sõnastikku kantud. Kui sõnu ei ole, tagastab tühja listi.

        :param self:
        :return:
        """
        symbols = "0123456789!\"# $%&'()*+,./:;<=>?@[\\]^_`{|}~"
        verbs = []
        clean_verbs = []
        for word in self.new_data:
            if None:
                return []
            if len(word) < 4:
                continue
            if word[0] == "(" and word[1] == "v":
                word = word[3:-1]
                if word == "":
                    continue
                if " " in word:
                    continue
                else:
                    verbs.append(word)
        for each in verbs:
            if None:
                return []
            if each[0] == "-" or each[-1] == "-":
                continue
            else:
                clean_verbs.append(each)
        for each in clean_verbs:
            for i in each:
                if i in symbols:
                    clean_verbs.remove(each)
                    break
        clean_verbs = list(set(clean_verbs))
        self.clean_verbs = clean_verbs
        print(self.clean_verbs)
        return self.clean_verbs

    def get_all_adjectives(self):
        """
        Tagastab listi, mille sees on kõik omadussõnad, mis on sõnastikku kantud. Kui sõnu ei ole, tagastab tühja listi.

        :param self:
        :return:
        """
        symbols = "0123456789!\"# $%&'()*+,./:;<=>?@[\\]^_`{|}~"
        adjectives = []
        clean_adjectives = []
        for word in self.new_data:
            if None:
                return []
            if len(word) < 4:
                continue
            if word[0] == "(" and word[1] == "a":
                word = word[3:-1]
                if word == "":
                    continue
                if " " in word:
                    continue
                else:
                    adjectives.append(word)
        for each in adjectives:
            if None:
                return []
            if each[0] == "-" or each[-1] == "-":
                continue
            else:
                clean_adjectives.append(each)
        for each in clean_adjectives:
            for i in each:
                if i in symbols:
                    clean_adjectives.remove(each)
                    break
        clean_adjectives = list(set(clean_adjectives))
        self.clean_adjectives = clean_adjectives
        print(self.clean_adjectives)
        return self.clean_adjectives

    def search(self, subword, min_len, max_len):
        """
        Tagastab listi, mille sees on kõik sõnastikus olevad sõnad, milles sisaldub subword.

        Listis võivad sõnad olla suvalises järjekorras. min_len, max_len on vaikeparameeterid, mis määravad
        otsitava sõna minimaalse ja maksimaalse pikkuse.
        Kui nende väärtused pole määratud, siis otsitavate sõnade pikkus pole piiratud.
        Kui selliseid sõnu ei ole, tagastada tühi list.
        :param self:
        :param subword:
        :param min_len:
        :param max_len:
        :return:
        """


if __name__ == '__main__':
    small_dict_data = "\n".join(["(a)beautiful - very pleasing or satisfying",
                                 "(a)wise - possessed of or characterized by scholarly knowledge or learning",
                                 "(a)kind -",
                                 "(a)Warm - conserving or maintaining warmth or heat",
                                 "(v)Claim - to assert or maintain as a fact",
                                 "(n)ph one - a portable electronic telephone device",
                                 "(a)wise - having the power to judge what is true or right",
                                 "[n]place - a particular portion of space, whether of definite or indefinite exten",
                                 "(a)well-known - clearly or fully known",
                                 "(v)-create - to cause to come into being",
                                 "(n)law - the principles and regulations established in a community by some authority",
                                 "(n)injury - harm or damage that is done or sustained",
                                 "",
                                 "choice - an act or instance of selection",
                                 "(n)fire - a burning mass of material, as on a hearth or in a furnace",
                                 "(b)consume - to destroy or expend by use",
                                 "(v)consume - to eat or drink up; devour",
                                 "(v)fire - to expose to the action of fire; subject to heat",
                                 "(v)fire - to inspire"])


    small_dictionary = Dictionary(small_dict_data)

 #   assert small_dictionary.is_word_noun("fire") is True
 #   assert small_dictionary.is_word_verb("fire") is True
 #   assert small_dictionary.is_word_adjective('warm') is True
 #   assert small_dictionary.is_word_noun("place") is False

    all_nouns = small_dictionary.get_all_nouns()
    assert isinstance(all_nouns, list)

    assert len(all_nouns) == 3
    assert "law" in all_nouns
    assert "injury" in all_nouns
    assert "fire" in all_nouns

    all_verbs = small_dictionary.get_all_verbs()
    assert isinstance(all_verbs, list)

    assert len(all_verbs) == 3
    assert "consume" in all_verbs
    assert "claim" in all_verbs
    assert "fire" in all_verbs

    all_adjectives = small_dictionary.get_all_adjectives()
    assert isinstance(all_adjectives, list)

    assert len(all_adjectives) == 4
    assert "wise" in all_adjectives
    assert "warm" in all_adjectives
    assert "beautiful" in all_adjectives
    assert "well-known" in all_adjectives

    print("Ready for submission!")

"""
assert len(small_dictionary.get_definitions("kind")) == 0
assert len(small_dictionary.get_definitions("phone")) == 0
assert len(small_dictionary.get_definitions("ph one")) == 0
assert len(small_dictionary.get_definitions("choice")) == 0
assert len(small_dictionary.get_definitions("-create")) == 0
assert len(small_dictionary.get_definitions("create")) == 0
assert len(small_dictionary.get_definitions("beautiful")) == 1
assert len(small_dictionary.get_definitions("fire")) == 3
assert len(small_dictionary.get_definitions("Consume")) == 1
assert len(small_dictionary.get_definitions("wise")) == 2
assert small_dictionary.is_word_noun("fire") is True
assert small_dictionary.is_word_verb("fire") is True
assert small_dictionary.is_word_adjective('warm') is True
assert small_dictionary.is_word_noun("place") is False

all_nouns = small_dictionary.get_all_nouns()
assert isinstance(all_nouns, list)

assert len(all_nouns) == 3
assert "law" in all_nouns
assert "injury" in all_nouns
assert "fire" in all_nouns

all_verbs = small_dictionary.get_all_verbs()
assert isinstance(all_verbs, list)

assert len(all_verbs) == 3
assert "consume" in all_verbs
assert "claim" in all_verbs
assert "fire" in all_verbs

all_adjectives = small_dictionary.get_all_adjectives()
assert isinstance(all_adjectives, list)

assert len(all_adjectives) == 4
assert "wise" in all_adjectives
assert "warm" in all_adjectives
assert "beautiful" in all_adjectives
assert "well-known" in all_adjectives

search_result = small_dictionary.search("N", min_len=5, max_len=8)
assert len(search_result) == 2
assert 'consume' in search_result
assert 'injury' in search_result

print("Ready for submission!")
"""