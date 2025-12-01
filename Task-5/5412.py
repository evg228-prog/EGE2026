cnt = 0
for N in range(1, 100000):
    R = f'{N:x}'
    if R.count('b') % 2 == 0:
        R = '1' + R
    else:
        R = R + '1'
    R = int(R, 16)
    if 10 <= R <= 99:
        cnt += 1
print(cnt)

# 14

