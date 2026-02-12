from math import *

# 1855
L = 101
N = 4090 + 10
i = ceil(log2(N)) # bit
I = ceil(L * i / 8) # byte
print((2048 * I) / 2 ** 10)

# 330

# 23749
for N in range(1, 10 ** 8):
    L = 2783
    i = ceil(log2(N)) # bit
    I = ceil(L * i / 8) # byte
    if 3_845_627 * I >= 11 * 2 ** 30:
        print(N)
        break

# 257

# 23370

for L in range(1, 10 ** 8):
    N = 10 + 17
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 7_564_230 * I > 31 * 2 ** 20:
        print(L)
        break

# 7