def DEL(n, m):
    return n % m == 0

def f(x):
    return not ((DEL(x, 263)) <= DEL(x, A)) and DEL(x, 71)

for A in range(1, 20_000)[::-1]:
    if all(not f(x) for x in range(1, 20_000)):
        print(A)
        break

# 18673