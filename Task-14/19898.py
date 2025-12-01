from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 10000):
    num1 = convert(7**270 + 7**170 + 7**70 - x, 7)
    N = num1.count('0')
    ans.append([N, x])
print(max(ans))

# 9604
