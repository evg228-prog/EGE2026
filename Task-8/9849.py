from itertools import *

alph = 'ABCDEF'
cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val[0] not in 'AE' and val[-1] not in 'AE':
        cnt += 1
print(cnt)

# 20736