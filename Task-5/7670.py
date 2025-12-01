ans = []
for N in range(151, 100000):
    R = f'{N:x}'
    R = R.replace('a', '1')
    cnt = 0
    for i in R:
        if int(i, 16) % 2 == 0:
            cnt += 1
    if cnt > 2:
        R += 'b'
    else:
        R = 'f' + R
    R = int(R, 16)
    if R == 3856:
        ans.append(N) # if R > 3500: -> min(R) = 3856
print(min(ans))

# 160