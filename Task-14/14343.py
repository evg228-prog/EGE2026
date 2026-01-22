from string import *
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

num1 = convert(5 * 343**2031 + 4 * 49**2142 - 3 * 7**111 + 7**222, 7)
print(sum(map(int, num1)))

# 673
