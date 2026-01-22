def TREUG(a, b, c):
    return a + b > c and a + c > b and b + c > a

def f(A):
    for x in range(1, 1000):
        F = not ((TREUG(x, 11, 18) == (not (max(x, 5) > 68))) and TREUG(x, A, 5))
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)

###########################################################

def f(x):
    return not((TREUG(x, 11, 18) == (max(x, 5) <= 68)) and TREUG(x, A, 5))

for A in range(1, 100)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break

# 64