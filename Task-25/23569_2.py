def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i * i < num + 1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 2:
        d += [num]
    if len(d) == 2 and all(str(i).count('6') == 1 for i in d):
        return max(d)
    return 0

cnt = 0
for N in range(6_086_056, 10**12):
    M = fact(N)
    if M:
        print(N, M)
        cnt += 1
        if cnt == 5:
            break

# 6086089 2467
# 6086161 3673
# 6087281 9467
# 6087317 36451
# 6087727 2683