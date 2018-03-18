"""Different exercises."""


import rsa


def get_lines(initial_line_length: float) -> tuple:
    """
    Leia lühema ja pikema lõigu pikkused (pildil y ja x - y).

    ja ümarda neid täisarvuni (kasuta lihtsalt round(): nt round(15.121212) -> 15).
    Tagastada enniku (tuple) kujul lühema lõigu pikkus, pikema lõigu pikkus.
    :param initial_line_length:
    :return:
    """
  #  initial_line_length / (initial_line_length - y) = (initial_line_length - y) / y
  #  initial_line_length*y = (initial_line_length - y)*(initial_line_length - y)
    y**2 - initial_line_length*3*y + initial_line_length*initial_line_length

    return (x, y)

print(get_lines(12))

"""
# Replace the 'X' with a number and run the code
private_key = rsa.PrivateKey(11205043368821276501164085738541636569880815545177500701989999611690504491774405591277064280887202331871750952739234209459546358927036168630891473248155077,
                             X,
                             1249811053696133958275622423192080249718918498485550607008970461898737931053796295426575931191658930367762111316721305144983323230375280961747441719469353,
                             6484029691686926333068463978243288890305224164824441508305833690895007755939365483,
                             1728098713549552126609033130920471853761401423186304421868572898161202319)

print()

mes01 = b'T\xaao\xe9?\x98\xd3.\xbf\x1aF\xdco\x06\xed"*\xa4\x8c\xbf?A\x89#\xa6\x10q\xa4\x80\x90f\xb3\x1e\xa8\xf7M\x14\xe5\xe5\xa62\x9ej\xec\x11\x1b\xea\xa1\x82P\xd6\x89\xe9\x9a~\x8b\xf8n\x0cE\x00\x1b#\xed'
mes02 = b'W\xe3\xd0\xb4!5H6\xa0\x1e\x19u\xa6\xce\x9c\xd9\x96\x84\xf7\x07b\xe8N@\x90\xbc\xa1\xd4_\x06\x96z\xf1\x18\xf2\xf3|\xe32*\x17\x81\x97P\x8c\x0f\xbe?\xbb!\xf5_\x06\xe15u\x8eX\x89\xe2\xc8U\n\xd6'

# Will print the function names to the console
print(f"EX02 FUNCTION NAME: {rsa.decrypt(mes01, private_key)}")
print(f"EX03 FUNCTION NAME: {rsa.decrypt(mes02, private_key)}")
"""


def interlude(row, col):
    """
    Find what you search.

    :param row:
    :param col:
    :return:
    """
    rows = 0
    cols = 0
    if row < 1 or col < 1:
        return None
    another_one = row
    while another_one > 0:
        rows += another_one
        another_one -= 1
    col -= 2
    while col >= 0:
        cols += col + row
        col -= 1
    return cols + rows

assert interlude(1, 2) == 2
assert interlude(1, 3) == 4
assert interlude(1, 4) == 7
assert interlude(2, 1) == 3
assert interlude(3, 1) == 6
assert interlude(4, 1) == 10
assert interlude(5, 3) == 26
assert interlude(4, 4) == 25
assert interlude(3, 5) == 24
assert interlude(15, 28) == 876
assert interlude(99, 100) == 19602
assert interlude(39132, 4923) == 970394563
