def f(A):
    for x in range(1, 1000):
        F = (x & A == 0) <= ((x & 77 == 0) and (x & 44 == 0))
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)
        break

# 109