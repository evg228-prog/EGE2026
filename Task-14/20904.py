from string import printable as olo
def convert(num, sys):
    res = ''
    while num:
        res += olo[num % sys]
        num //= sys
    return res[::-1]

for x in range(1, 2031):
    num_10 = 3**100 - x
    num_3 = convert(num_10, 3)
    if num_3.count('0') == 1:
        print(x)

