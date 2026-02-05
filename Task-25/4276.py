def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) < 7:
        return ()
    return sorted(list(d))[-7], len(d)

cnt = 0
for N in range(400_000_001, 10**20):
    D = f(N)
    if D:
        print(*D)
        cnt += 1
        if cnt == 5:
            break

# 34 10
# 2962963 14
# 1793722 30
# 21052632 62
# 754717 14