from functools import lru_cache
@lru_cache(None)

def F(n):
    return G(n - 2)

def G(n):
    if n < 100: return n
    return F(n - 3) + 1

for i in range(1, 5000):
    F(i)

print(F(5000))

# 1078