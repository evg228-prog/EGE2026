def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    return d

def f1(num):
    d = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i): d.add(i)
            if is_prime(num // i): d.add(num // i)
    return d

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
    return d

cnt = 0
for N in range(5_200_001, 10**10):
    dels = fact(N)
    M = f(N)
    A = f1(N)
    if len(dels) == 9 and len(M) % 90 == 0:
        print(N, max(A))
        cnt += 1
        if cnt == 5:
            break

# 5207472 43
# 5208300 643
# 5209200 1447
# 5211248 23
# 5214384 739
