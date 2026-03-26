from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 43: return G(n + 4)
    return 2 * F(n - 2) - F(n - 4) + 2

@lru_cache(None)
def G(n):
    if n < 11240: return G(n + 3) + 2
    return Q(n)

@lru_cache(None)
def Q(n):
    if n < 21: return n + 4
    return Q(n - 4) + 2

for i in range(20, 11240):
    Q(i)

for i in range(11240, 42, -1):
    G(i)

for i in range(42, 2026):
    F(i)

print(F(2026))

# 998154