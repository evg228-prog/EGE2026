from itertools import *

alph = sorted('гранит')

ans = []
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] not in 'аиг' and val.count('а') == 1:
        if pos % 2 != 0:
            ans.append(pos)
print(min(ans))

# 23589