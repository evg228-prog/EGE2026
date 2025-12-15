from string import printable as olo


def convert(num, sys):
    res = ''
    while num:
        res += olo[num % sys]
        num //= sys
    return res[::-1]


for x in range(1, 27000):
    num1 = convert(3 * 27 ** 9 + 2 * 27 ** 6 + 27 ** 3 - x, 27)
    if num1.count('0') == 6:
        print(x)

# 27
