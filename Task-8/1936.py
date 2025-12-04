from itertools import *
alph = sorted('пскаль')

cnt = 0
for pos, val in enumerate(product(alph,repeat=4 ), start=1):
    val = ''.join(val)
    if val[0] != 'ь' and 'ьь' not in val:
        cnt += 1
print(cnt)

# 1025