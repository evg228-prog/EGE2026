from itertools import *
from string import printable

cnt = 0
for val in product(printable[:15], repeat=5):
    val = ''.join(val)
    if val.count('8') == 1 and val[0] != '0':
        if sum(1 for i in val if int(i, 15) > 9) >= 2:
            cnt += 1
print(cnt)

# 83175