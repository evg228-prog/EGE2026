def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and i % 100 == 11 and i != 11:
            d.add(i)
        if num % (num // i) == 0 and (num // i) % 100 == 11 and num // i != 11:
            d.add(num // i)
    return list(d)

cnt = 0

for N in range(1_350_051, 10**15):
    M = f(N)
    if M:
        print(N, M)
        cnt += 1
        if cnt == 5:
            break

# 1350051 311
# 1350055 270011
# 1350062 511
# 1350063 40911
# 1350066 225011