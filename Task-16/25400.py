from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 31054: return F(n + 4) + 3020
    return 3 * (G(n - 2) - 15)

@lru_cache(None)
def G(n):
    if n >= 28: return G(n - 5) - 15
    return 3 * n - 4

for j in range(0, 31055):
    G(j)
for i in range(31055, 0, -1):
    F(i)

print(F(15))

# 23156080