def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) > 0:
        return [i for i in d if i % 10 == 9 and i != 9]
    return 0

cnt = 0
for N in range(800_001, 10**10):
    M = f(N)
    if M:
        print(N, min(M))
        cnt += 1
        if cnt == 5:
            break

# 800001 309
# 800003 47059
# 800004 409
# 800006 269
# 800007 39