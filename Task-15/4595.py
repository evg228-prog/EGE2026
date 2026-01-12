def DEL(n, m):
    return n % m == 0

def f(A):
    for x in range(1, 1000):
        F = (DEL(x, 2) <= (not DEL(x, 3))) or (x + A >= 80)
        if not F:
            return False
    return True

for A in range(1, 100):
    if f(A):
        print(A)
        break
# 74




##################

# F = ((x % 2 == 0) <= (x % 3 != 0))