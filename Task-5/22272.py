from string import printable as olo
def convert(num, sys):
    res = ''
    while num:
        res += olo[num % sys]
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = convert(N, 9)
    if R[0] == '7':
        R = R.replace('6', '*')
        R = R.replace('3', '6')
        R = R.replace('*', '3')
        R = '34' + R
    else:
        R = '3' + R[1:] + '45'
    R = int(R, 9)
    if R < 2876:
        ans.append([R,N])
min_R = max(ans)[0]
all_N = []
for i in ans:
    if min_R == i[0]:
        all_N.append(i[1])
print(max(all_N))

# 79