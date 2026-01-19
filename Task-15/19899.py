def mod(m, n):
    return m % n

def f(A):
    for x in range(1, 1000):
        F = (A + 2 * x > 400 - A) and (mod(A, 100) + mod(120, A) > 140)
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)
        break

# 221