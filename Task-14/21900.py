from string import printable as olo
def convert(num, sys):
    res = ''
    while num:
        res += olo[num % sys]
        num //= sys
    return res[::-1]

for x in range(1, 2301):
    num1 = convert(7**350 + 7**150 - x, 7)
    if num1.count('0') == 200:
        print(x)

# 2001