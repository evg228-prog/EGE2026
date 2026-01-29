def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    d_8 = []
    for i in sorted(d):
        if i != 9 and i % 10 == 9:
            d_8 += [i]

    if d_8:
        return min(d_8)
    return 0

cnt = 0
for N in range(800_001, 10**10):
    F = f(N)
    if F:
        print(N, F)
        cnt += 1
        if cnt == 5:
            break

# 800001 309
# 800003 47059
# 800004 409
# 800006 269
# 800007 39