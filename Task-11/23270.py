from math import *

for L in range(1, 100_000):
    N = 37
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 3548 * I > 12 * 2 ** 10:
        print(L)
        break