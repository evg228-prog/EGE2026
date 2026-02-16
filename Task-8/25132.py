from itertools import *

alph = sorted('сдайегэ')

ans = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if 'егэ' in val:
        ans += pos
print(ans)

# 79143659