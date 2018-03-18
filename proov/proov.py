"""Exam and things."""


def greeting(name):
    """
    Do smth, not sure what yet.

    :param name:
    :return:
    """
    if name == "Ago":
        return None
    else:
        print("Hello, {}".format(name))

greeting("Mati")
greeting("Ago")
greeting("Malle Mai")



def formula(n):
    """
    Calulate smth, not sure what yet.

    :param n:
    :return:
    """
    overflow = n % 3
    summa = int(n / 5) - int(overflow)
    return summa

print(formula(7))
print(formula(8))
print(formula(123))


def what_meal(sleepy, food_ready):
    """
    Sleepy and fed.

    :param sleepy:
    :param food_ready:
    :return:
    """
    if sleepy and food_ready:
        return "dinner"
    if sleepy and not food_ready:
        return "breakfast"
    if not sleepy and food_ready:
        return "lunch"
    else:
        return "no food for you"

print(what_meal(True, False))
print(what_meal(False, False))
print(what_meal(True, True))


def sum_odd(n):
    """
    jhdsghjsdf hjdshjsd.

    :param n:
    :return:
    """
    sum = 0
    if n == 3:
        return 3
    if n > 3:
        for i in range(3, n+1):
            if i % 2 == 1:
                sum += i
    return sum

print(sum_odd(3))
print(sum_odd(4))
print(sum_odd(5))


def capitalize2(word):
    """
    Capitalize word.

    :param word:
    :return:
    """
    return word[0:2].upper()+word[2:]

print(capitalize2("tere"))
print(capitalize2("helloworld"))
print(capitalize2("Hi"))


def remove_middle(numbers):
    """
    jdshghsd.

    :param numbers:
    :return:
    """
    middle = int(len(numbers) / 2)
    if len(numbers) % 2 == 0:
        numbers.remove(numbers[middle-1])
    else:
        numbers.remove(numbers[middle])
    return numbers

print(remove_middle([1, 2, 3, 4, 5]))
print(remove_middle([1, 2, 3, 4]))


def replace_aa(s):
    """
    fhhjs.

    :param s:
    :return:
    """
    new = s.replace("aab", "   ")
    new2 = new.replace("aa", "x")
    new3 = new2.replace("   ", "aab")
    return new3

print(replace_aa("aac"))
print(replace_aa("aaab"))
print(replace_aa("aaaab"))
print(replace_aa("aaaaaa"))
print(replace_aa("aaaaa"))


def consecutive_number_index(numbers):
    """
    hdvhvdhvcd.

    :param numbers:
    :return:
    """
    for each in range(len(numbers)):
        if numbers[each] - numbers[each-1] == 1:
            return each-1
    return -1

print(consecutive_number_index([1, 2, 3]))
print(consecutive_number_index([1, 3, 5]))
print(consecutive_number_index([1, 3, 6, 5, 5, 6]))


def even_values_add_3(d):
    """
    jdsh.

    :param d:
    :return:
    """
    for key, value in d.items():
        if value % 2 == 0:
            d[key] = value + 3
    return d

print(even_values_add_3({"a": 12, "b": 11}))


def sum_digits(number):
    """
    fdkjsd.

    :param n:
    :return:
    """
    if number == 0:
        return 0
    else:
        return (number % 10) + sum_digits(number // 10)


print(sum_digits(100000))


def how_many_bricks(bottom_bricks):
    """
    jdhgd.

    :param bottom_bricks:
    :return:
    """

    if bottom_bricks == 1:
        return 1
    return bottom_bricks + how_many_bricks(bottom_bricks-1)


print(how_many_bricks(4))


def in_both_list(a, b):
    """
    return similarities.

    :param a:
    :param b:
    :return:
    """
    list = []
    for each in a:
        for i in b:
            if each == i:
                if each not in list:
                    list.append(each)
    return list


print(in_both_list([3, "a", 3, 5, 6, 7, 3], ["a", 3, 5, 9, 4, 0]))


def how_many_each(kids, fruits):
    """
    How many fruits each kid gets.

    :param kids:
    :param fruits:
    :return:
    """
    each = fruits // kids
    last_kid = each + fruits % kids
    return each, last_kid

print(how_many_each(3, 5))


def return_longer(long_str, short_str):
    """
    jgshj.

    :param long_str:
    :param short_str:
    :return:
    """
    a = long_str.index(short_str)
    return long_str[a:]


print(return_longer("minaoleniluskena", "ilus"))


def change_ints(dict):
    """
    Antakse ette mingi dictionary.

     mis sisaldab int ja string tüüpi väärtusi ja sa pead kõik int tüüpi väärtused korrutama kolmega.
    :param dict:
    :return:
    """
    for key, value in dict.items():
        if type(value) == int:
            dict[key] = value*3
    return dict

print(change_ints({0: 2, 1: "ter", 2: 3, 3: "hd", 4: 321.32}))


def change_list_by(list_a, number):
    """
    Antakse ette list numbritega ja arv.

    Kõik listi arvud mis on väiksemad kui arv tuleb korrutada arvuga läbi ja kõik mis on võrdsed tuleb korrutada kahega.
    :param list_a:
    :param number:
    :return:
    """
    new_list = []
    for each in list_a:
        if each < number:
            new_list.append(each*number)
        elif each == number:
            new_list.append(each*2)
        else:
            new_list.append(each)
    return new_list

print(change_list_by([2, 3, 5, 1, 6, 8, 9], 5))


def swap_sub_in_str(str, sub_str):
    """
    Kui see substring esineb stringis siis tuleb selle stringi sees see substring ümber pöörata.

    :param str:
    :param sub_str:
    :return:
    """
    if sub_str in str:
        return str[:str.index(sub_str)] + sub_str[::-1] + str[str.index(sub_str)+len(sub_str):]

print(swap_sub_in_str("tereminaolenmina", "mina"))

"""
1.	10p ülesanne oli tüütu. Funktsioon mille sisendiks on 
„Testi“ vastused „AB,C,D,DC“ (Esimese küsimuse vastused võivad 
olla A või B ning teine vastus on C kolmas D ja neljas D või C) 
ja list tudengite vastustega „ABC D“ (iga täht on üks vastus. 
    Tühik on vastamata jätmine). Iga õigesti vastatud küsimus 
annab ühe punkti ja iga valesti vastatud küsimus annab miinus 
ühe punkti. Vastamata küsimus (tühik) ei anna ega võta ära midagi. 
Tuleb välja arvutada iga tudengi vastuste protsent (kui tulemus 
on negatiivne ehk alla nullis siis tuleb panna 0%).
Nt Calculate_percentages(„AB,C,DC“, [„ACC“, „CDA“, „B D“, „AAA“]) tagastab
[„100%“, “0%“, „67%“, „0%“]
"""

def calculate_percentages(right_answers, list_of_answers):
    """
    hddshs.

    :param right_answers:
    :param list_of_answers:
    :return:
    """
    correct = right_answers.split(",")
    answers = []
    for every in list_of_answers:
        s = list(every)
        answers.append(s)
    procentage = []
    for each in answers:
        total = 0
        mitmes = 0
        for i in each:
            if i in correct[mitmes]:
                total += 1
                mitmes += 1
            elif i == " ":
                mitmes += 1
            elif i not in correct[mitmes]:
                total -= 1
                mitmes += 1
        procentage.append(total)
    final = []
    for each in procentage:
        print(each)
        if each <= 0:
            final.append("0%")
        elif each > 0:
            result = int(round((each / len(correct))*100))
            final.append("{}%".format(result))

    print(procentage, final)


calculate_percentages("AB,C,DC", ["D C", "CDA", "B D", "AAA"])


class Student:
    """
    hdsdgh.
    """

    def __init__(self, name, uniid):
        """
        Constructor.

        :param name:
        :param uniid:
        """
        self.name = name
        self.uniid = uniid

    def is_correct_uniid(self):
        """
        is uniid correct.

        :return:
        """
        allowed = ".-"
        if len(self.uniid) == 6:
            for each in self.uniid:
                if each.isalpha() or each in allowed:
                    return True
        else:
            return False

    def __str__(self):
        """
        jhgs.

        :return:
        """
        if self.is_correct_uniid():
            return "{} ({})".format(self.name, self.uniid)
        else:
            return "{} ({}) (invalid)".format(self.name, self.uniid)


student = Student("Ago", "Ag-Bos")
print(student)


def reverse_two(s):
    """
    Return string where first two letters are put into end in reverse order.
    If there are no 2 letters, return original string.

    String consists of only latin letters.
    :param s: string
    :return: string
    """
    if len(s) < 2:
        return s
    return s[2:] + s[1] + s[0]


def bigger_sum(numbers):
    """
    Find the first index where sum of elements up to that index (itself not included) is bigger than the element.

    If no such element can be found, return -1.

    :param numbers: list of non-negative ints
    :return: int
    """
    total = 0
    for each in numbers:
        if total > each:
            return numbers.index(each)
        total += each
    return -1


def first_letter_after_subword(word, subword):
    """
    Return first char after first subword in word.

    If subword is not found in the word, return "".
    If there are no characters after subword, return "".

    :param word: str
    :param subword: str, len > 0
    :return: char
    """
    if subword in word:
        index = word.index(subword) + len(subword)
        if len(word)-1 > index:
            return word[index]
    return ""


def extend_list(numbers, pos):
    """
    Extend list by adding one element.

    The pos indicates where the new element should be inserted.
    Pos also indicates which value should be inserted -
    the value of the element in the pos in the original list.
    If the pos is too high, a new 0 element is added to the end.

    extend_list([1, 2, 3], 0) => [1, 1, 2, 3]
    extend_list([1, 2, 3], 3) => [1, 2, 3, 0]
    extend_list([1, 2, 3], 312123123) => [1, 2, 3, 0]
    extend_list([1, 2], 1) => [1, 2, 2]
    :param pos: list of containing integers.
    :return: extended list
    """
    if pos <= len(numbers)-1:
        new_element = numbers[pos]
        numbers.insert(pos, new_element)
        return numbers
    numbers.append(0)
    return numbers

print(extend_list([1, 2, 3], 3))


if __name__ == '__main__':
    assert reverse_two("tere") == "reet"
    assert reverse_two("ter") == "ret"
    assert reverse_two("te") == "et"
    assert reverse_two("t") == "t"
    assert reverse_two("") == ""

    assert bigger_sum([1, 2, 3, 4]) == 3
    assert bigger_sum([1, 2, 3]) == -1
    assert bigger_sum([2, 1]) == 1
    assert bigger_sum([1, 1]) == -1
    assert bigger_sum([]) == -1

    assert first_letter_after_subword("hello", "h") == "e"
    assert first_letter_after_subword("hello", "hel") == "l"
    assert first_letter_after_subword("hello", "hello") == ""
    assert first_letter_after_subword("hello", "a") == ""
    assert first_letter_after_subword("hiho", "h") == "i"

    assert extend_list([1, 2, 3], 0) == [1, 1, 2, 3]
    assert extend_list([1, 2, 3], 1) == [1, 2, 2, 3]
    assert extend_list([1, 2, 3], 2) == [1, 2, 3, 3]
    assert extend_list([1, 2, 3], 3) == [1, 2, 3, 0]
    assert extend_list([1, 2, 3], 9) == [1, 2, 3, 0]
    assert extend_list([], 1) == [0]


def second_symbol_of_longest_str(a, b, c):
    """
    Return the second symbol of the longest string.

    If there are several strings with the same length, any one of those is correct.

    If the longest string doesn't have second symbol, return empty string.
    assert second_symbol_of_longest_str("ab", "cde", "fghi") == "g"
    assert second_symbol_of_longest_str("a", "b", "c") == ""
    :param a: str
    :param b: str
    :param c: str
    :return: str
    """
    if len(a) < 2 and len(b) < 2 and len(c) < 2:
        return ""
    longest = ""
    for each in a, b, c:
        if len(each) > len(longest):
            longest = each
    return longest[1]


def index_or_value(numbers):
    """
    Replace every element in the list with the index when index is bigger than value.
    assert index_or_value([1, 2, 3]) == [1, 2, 3]
    assert index_or_value([1, 1, 1]) == [1, 1, 2]
    assert index_or_value([1, 0, 0]) == [1, 1, 2]
    :param numbers: list of ints
    :return: list
    """
    new_list = []
    for i in range(len(numbers)):
        if i > numbers[i]:
           new_list.append(i)
        else:
            new_list.append(numbers[i])
    return new_list


def merge_strings(a, b):
    """
    Return a new string where first symbol is the first symbol of the first string,
    the second symbol is the first symbol of
    the second string, third symbol is the second symbol of the first string etc.

    If one string is finished, continue only with the other string.

    :param a: str
    :param b: str
    :return: str
    """
    new = ""
    for each in range(max(len(a), len(b))):
        if each in range(len(a)):
            new += a[each]
        if each in range(len(b)):
            new += b[each]
    return new

print(merge_strings("a", "bcd"))


def max_digit(nr):
    """
    Return the highest digit in the number.
    muuda midagi
    :param nr: int
    :return: int
    """
    max = 0
    for each in str(nr):
        if int(each) > max:
            max = int(each)
    return max



if __name__ == '__main__':
    assert second_symbol_of_longest_str("ab", "cde", "fghi") == "g"
    assert second_symbol_of_longest_str("a", "b", "c") == ""
    assert second_symbol_of_longest_str("ab", "bt", "ca") in ('b', 't', 'a')

    assert index_or_value([1, 2, 3]) == [1, 2, 3]
    assert index_or_value([1, 1, 1]) == [1, 1, 2]
    assert index_or_value([1, 0, 0]) == [1, 1, 2]

    assert merge_strings("a", "b") == "ab"
    assert merge_strings("a", "bcd") == "abcd"
    assert merge_strings("acd", "b") == "abcd"
    assert merge_strings("acd", "") == "acd"

    assert max_digit(1) == 1
    assert max_digit(10) == 1
    assert max_digit(109) == 9
    assert max_digit(0) == 0
