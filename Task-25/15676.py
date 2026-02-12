from fnmatch import fnmatch
from itertools import *

def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

ans = []
for N in range(4, 10000):
    if f(N):
        for i in range(22768, 10**8, 22768):
            if fnmatch(str(i), f'1{N}03*6*'):
                ans.append([i, N])
for i in sorted(ans):
    print(*i)

#############################################

def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

ans = []
for l1 in range(1, 5):
    for N in range(10 ** (l1 - 1), 10 ** l1):
        if f(N):
            for l2 in range(0, 4 - l1 + 1):
                for Z1 in product('0123456789', repeat=l2):
                    Z1 = ''.join(Z1)
                    for l3 in range(0, 4 - l1 - l2 + 1):
                        for Z2 in product('0123456789', repeat=l3):
                            Z2 = ''.join(Z2)
                            num = int(f'1{N}03{Z1}6{Z2}')
                            if num % 22768 == 0 and num < 10 ** 8:
                                ans.append([num, N])
for i in sorted(ans):
    print(*i)

# 12203648 22
# 14503216 45
# 15960368 596
# 18032256 8