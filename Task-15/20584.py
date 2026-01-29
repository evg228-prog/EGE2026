def DEL(n, m):
    return n % m == 0

def f(A):
    for x in range(1, 1000):
        F = (DEL(405, x) <= DEL(81, x)) or (A - x > 162)
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)
        break


print('###################')

################################################

def f(x):
    return (DEL(405, x) <= DEL(81, x)) or (A - x > 162)

for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break
# 568