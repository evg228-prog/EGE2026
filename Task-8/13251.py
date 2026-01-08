from itertools import *

cnt = 0
for val in permutations('кайф', r=4):
    val = ''.join(val)
    if 'кф' not in val and val[-1] != 'й':
        cnt += 1
print(cnt)

# 14