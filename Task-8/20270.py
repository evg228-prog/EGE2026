from itertools import *
from string import *

cnt = 0
for val in product(printable[:7], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        for i in '0246': val = val.replace(i, '*')
        for i in '135': val = val.replace(i, '#')
        if '**#**' in val:
            cnt += 1
print(cnt)

# 576
