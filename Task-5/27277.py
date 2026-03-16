from string import *

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

ans = []

for N in range(1, 100_000):
    R = convert(N, 3)
    if N % 3 != 0:
        R = '1' + R + R[-3:]
    else:
        R = R + convert(sum(map(int, R)) * 8, 3)
    R = int(R, 3)
    if 1500 > R > 1000:
        ans.append(R)
print(ans)

# 1205

