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
    if len(d) == 2 and all(str(i).count('5') == 1 for i in d):
        return max(d)
    return 0

cnt = 0
for N in range(1_324_728, 10**11):
    M = fact(N)
    if M:
        print(N, M)
        cnt += 1
        if cnt == 5:
            break

# 1324795 264959
# 1324801 1151
# 1324903 2543
# 1325015 265003
# 1325029 5279