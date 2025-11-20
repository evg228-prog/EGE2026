from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
R = 729**8 - 3**18 + 85
new_R = convert(R, 9)
print(new_R.count('0'))