def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num //i}
    if len(d) > 1:
        return sum(d) // len(d)
    return 0

cnt = 0
for N in range(1, 700_000)[::-1]:
    M = f(N)
    if M % 1000 == 313:
        print(N, M)
        cnt += 1
        if cnt == 7:
            break

# 698196 43313
# 697664 31313
# 696525 22313
# 695940 33313
# 695606 31313
# 695533 18313
# 695526 28313