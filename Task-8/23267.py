from itertools import *
alph = sorted('строка')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[0] not in 'ал' and val.count('с') == 1:
        print(pos)