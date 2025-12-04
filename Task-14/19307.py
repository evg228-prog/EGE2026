from string import printable as olo
def convert(num, sys):
    res = ''
    while num:
        res += olo[num % sys]
        num //= sys
    return res[::-1]
num1 = 15625**16 - 3125**3 * 25**19 + 625**4 - 2005
num2 = convert(num1, 5)[1:]
print(num2.count('0'))

# 38