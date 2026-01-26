def DEL(n, m):
    return n % m == 0

def f(x):
    return (DEL(x, A)) or (DEL(x, 133) <= (not DEL(x, 95)))

for A in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break

# 665