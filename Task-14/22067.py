from string import printable as olo
def convert(num, sys):
    res = ''
    while num:
        res += olo[num % sys]
        num //= sys
    return res[::-1]
num1 = 3 * 17**777 + 15 * 17**250 - 6 * 17**100 + 2
num17 = convert(num1, 17)
ans = []
for i in num17:
    if i in '02468aceg':
        ans.append(i)
print(len(set(ans)))

# 4