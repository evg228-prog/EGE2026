from math import *

for L in range(1, 1000):
    N = 37
    i = ceil(log2(N))
    V = ceil(L * i/ 8)
    if V * 3548 > 12 * 2 ** 10:
        print(L)
        break

# 5