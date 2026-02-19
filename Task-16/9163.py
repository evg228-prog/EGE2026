from functools import lru_cache

@lru_cache(None)
def F(n):
    if n >= 2025: return n
    return F(n + 1) - F(n + 2) + 7

for i in range(1, 2025)[::-1]:
    F(i)

print(F(15) - F(24))

# 4036