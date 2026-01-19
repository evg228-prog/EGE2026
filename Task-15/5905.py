from itertools import *

def f(A):
    for x, y, z in product(range(1, 1000), repeat=3):
        F = (x | 50 == x) or (y & 34 != 0) or (z | 24 != 24) or (x * y * z > (A // 8))
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)