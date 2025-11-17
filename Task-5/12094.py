ans = []
for N in range(1, 100000):
    R = f'{N:b}'
    if N % 8 == 0:
        R = R + R[-2:]
    else:
        R = R + bin(N % 8 * 2)[2:]
    R = int(R, 2)
    if R > 3000:
        ans.append(N)
print(min(ans))



