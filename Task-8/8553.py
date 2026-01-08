from itertools import *

alph = sorted('нормалье')

ans = []
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[:6] == 'ненорм':
        ans.append(pos)
print(min(ans))

# (154817 - 137588) - 1 = 17228

#######################################

from itertools import *

alph = sorted('нормалье')

nenorm = 0
norm = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val == 'ненорм':
        nenorm = pos
    if val[:4] == 'норм':
        norm = pos
        break
print(norm - nenorm - 1)

# 17228