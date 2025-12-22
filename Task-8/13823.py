from itertools import *

alph = sorted('мизантроп')

cnt = 0
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 == 0:
        if val[0] == 'н' and val.count('р') == 2:
            print(pos)

# 32712
