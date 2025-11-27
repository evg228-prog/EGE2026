ans = []
for N in range(1, 100000):
    R = f'{N:b}'
    if sum(map(int, R)) % 2 == 0:
        R = '11' + R[2:] + '1'
    elif R.count('0') < R.count('1'):
        R = R + '0'
    else:
        R = R + '1'
    R = int(R, 2)
    if R > 271:
        ans.append(N)
print(min(ans))

# 9
