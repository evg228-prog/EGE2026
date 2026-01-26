from string import *

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

for p in range(25, 37):
    num1 = int('bo', p)
    num2 = int('om', p)
    num3 = int('bl4', p)
    num4 = int('cng', p)
    if num1 + num2 + num3 == num4:
        print(p)

# 34

