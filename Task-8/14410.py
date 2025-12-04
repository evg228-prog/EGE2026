from itertools import *
alph = sorted('солнце')

cnt = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] not in 'ео' and val.count('ц') == 2:
        if pos % 2 == 0:
            cnt += 1
print(cnt)

# 4025