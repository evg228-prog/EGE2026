from itertools import *
alph = sorted('гондбуш')

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] != 'б' and val not in 'у' and val.count('н') >= 2:
        if pos % 2 != 0:
            print(pos)

# 117625