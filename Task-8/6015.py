from itertools import *
from string import *

cnt = 0
for val in product(printable[:9], repeat=7):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1:
        if val[0] not in '1357' and val[-1] not in '02468':
            cnt += 1
print(cnt)

# 376832