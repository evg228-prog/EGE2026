from itertools import *
from string import *

cnt = 0

for val in product(printable[:9], repeat=4):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1:
        if sum(map(int, val[:val.index('8')])) == sum(map(int, val[val.index('8') + 1:])):
            cnt += 1
print(cnt)

############################################

ans = 0
for val in product(printable[:9], repeat=4):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1:
        val = val.split('8')
        if sum(map(int, val[0])) == sum(map(int, val[1])):
            ans += 1
print(ans)

# 64