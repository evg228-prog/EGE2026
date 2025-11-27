from string import printable as olo
def convert(num, sys):
    res = ''
    while num:
        res += olo[num % sys]
        num //= sys
    return res[::-1]
ans = []
for x in range(1, 2030):
    num1 = convert(7**170 + 7**100 - x, 7)
    N = num1.count('0')
    ans.append([N, x])
print(max(ans))

