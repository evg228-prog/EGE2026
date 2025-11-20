from string import printable as klk
def convert(num, sys):
    res = ''
    while num:
        res += klk[num % sys]
        num //= sys
    return res[::-1]


ans = []
for N in range(1, 100_000):
    R = convert(N, 3)
    summ = sum(map(int, R))
    if summ % 3 == 0:
        R = R + '212'
    else:
        R = R + convert(summ * 2,3)
    R = int(R, 3)
    if R > 490:
        ans.append(R)
print(min(ans))