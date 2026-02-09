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
for N in range(5_000_001, 10**11):
    dels = fact(N)
    if N % 100 == 12 and sum(str(dels).count('x') == 5 for x in dels) >= 1:
        print(N, min(dels))
        cnt += 1
        if cnt == 5:
            break