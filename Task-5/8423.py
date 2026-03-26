ans = []

for N in range(1, 5_000_000):
    R = f'{N:b}'
    if N % 5 == 0:
        R = R + f'{5:b}'
    else:
        R = R + '1'
    R = int(R, 2)
    if R % 7 == 0:
        R = f'{R:b}' + f'{7:b}'
    else:
        R = f'{R:b}' + '1'
    R = int(R, 2)
    if R < 1_855_663:
        ans.append(N)
print(max(ans))

# 463913