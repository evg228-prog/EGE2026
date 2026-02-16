from functools import lru_cache
@lru_cache(None)
def F(n):
    if n > 40: return F(n - 4) + 3020
    return 3 * (G(n - 2) - 15)

@lru_cache(None)
def G(n):
    if n >= 301208: return 10 * n + 50
    return G(n + 7) - 21

for j in range(0, 301209)[::-1]:
    G(j)
for i in range(0, 221338):
    F(i)

print(F(2026))