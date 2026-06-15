from math import *

for N in range(1, 100_000):
    L = 172
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 356_984 * I >= 54 * 2**20:
        print(N)
        break

# 129