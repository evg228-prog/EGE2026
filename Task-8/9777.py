from itertools import *
alph = sorted('КОМПЬЮТЕР')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[:1] != 'Ь' and val.count('К') == 2:
        print(pos)

# 58979


