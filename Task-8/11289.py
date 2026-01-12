from string import *
from itertools import *

cnt = 0
for val in product(printable[:9], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('2') == 0:
            if len(set(val)) == len(val):
                for i in '02468': val = val.replace(i, '*')
                for i in '1357': val = val.replace(i, '#')
                if '**' not in val and '##' not in val:
                    cnt += 1
print(cnt)

# 1008