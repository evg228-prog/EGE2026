from itertools import *
from string import printable

cnt = 0
for val in product(printable[:12], repeat=7):
    val = ''.join(val)
    if val[0] != '0':

#         1-ЫЙ СПОСОБ
        for i in '0369':
            val = val.replace(i, '*')
        for i in '124578ab':
            val = val.replace(i, '+')

#         2-ОЙ СПОСОБ
        new_val = ''
        for i in val:
            if i in '0369':
                new_val += '*'
            else:
                new_val += '+'

#         3-ИЙ СПОСОБ
        val = ''.join(['*' if i in '0369' else '+' for i in val])

        if '**' not in val and '++' not in val:
            cnt += 1
print(cnt)

# 360448