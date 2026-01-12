from string import *
from itertools import *

cnt = 0
for val in product(printable[:25], repeat=4):
    val = ''.join(val)
    if val[0] != '0':
        if (val.count('1') + val.count('3') + val.count('5') + val.count('7') + val.count('9') + val.count('b') + val.count('d') + val.count('f') + val.count('h') + val.count('j') + val.count('l') + val.count('n')) == 1:
            if (val.count('0') + val.count('1') + val.count('2') + val.count('3')  + val.count('4') + val.count('5')) <= 2:
                cnt +=1
print(cnt)

# 95700