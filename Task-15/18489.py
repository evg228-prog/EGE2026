def CIF(n, m):
    return n % 10 == m % 10

def f(A):
    for x in range(1, 1000):
        F = ((not CIF(x, 5)) and CIF(x, 4)) <= (x > A - 11)
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)

# 14