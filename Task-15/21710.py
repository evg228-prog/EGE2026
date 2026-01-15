from itertools import *
def f(x):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = A1 <= x <= A2
    return (not A) <= (B == C)

lineA = sorted([36, 75, 60, 110])
linex = [50, 69, 100]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in linex):
        ans.append(A2 - A1)
print(min(ans))

# 74