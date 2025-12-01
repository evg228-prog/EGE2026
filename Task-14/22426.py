from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

num1 = convert(15*343**2031 + 7*49**1142 - 3*7**111 + 7**222 - 16809, 7)
num2 = abs((num1.count('0') + num1.count('2') + num1.count('4') + num1.count('6')) - (num1.count('1') + num1.count('3') + num1.count('5')))
print(num2)

# 6085