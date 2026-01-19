def DEL(n, m):
    return n % m == 0

def f(A):
    for x in range(1, 1000):
        B = 50 <= x <= 70
        F = DEL(x, A) or ((not DEL(x, 23)) or not B)
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)

# 69