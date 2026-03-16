from itertools import *

alph = sorted('аргумент')

for pos, val in enumerate(product(alph, repeat=4), start=1):
    val = ''.join(val)
    if len(val) == len(set(val)):
        if val == ''.join(sorted(val)):
            print(pos)

# 2424