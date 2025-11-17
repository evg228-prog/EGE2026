from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
num1 = 4*625**9 - 25**15 + 2*5**11 - 7
convert(num1, 5)
print(convert(num1, 5).count('4'))

##############################################

num1 = 4*625**9 - 25**15 + 2*5**11 - 7

cnt_4 = 0
while num1:
    if num1 % 5 == 4:
        cnt_4 += 1
    num1 //= 5
print(cnt_4)

