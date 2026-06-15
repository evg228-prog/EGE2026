from math import *

for L in range(1, 100_000):
    N = 27
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 7_564_230 > 31 * 2**20:
        print(L)
        break