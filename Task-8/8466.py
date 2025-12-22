from itertools import *
from string import printable

cnt = 0
for val in product(printable[:7], repeat=6):
    val = ''.join(val)
    if val[0] != '0' and val[-1] not in '0123':
        for i in '0246': val = val.replace(i, '*')
        for i in '135': val = val.replace(i, '+')
        if val.count('*') == val.count('+'):
            cnt += 1
print(cnt)

# 12672