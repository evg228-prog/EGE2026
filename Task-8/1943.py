import re
from itertools import *
alph = 'зеркало'

cnt = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    # if (1 <= val.count('к') <= 4 and val.count('з') <= 1 and val.count('е') <= 1
    #         and val.count('р') <= 1 and val.count('а') <= 1 and val.count('л') <= 1
    #         and val.count('о') <= 1):
    if 1 <= val.count('к') <= 4:
        val = val.replace('к', '')
        if len(val) == len(set(val)):
            cnt += 1
print(cnt)

# 12570
