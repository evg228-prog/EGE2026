from fnmatch import *

for N in range(2123416 - 2123416 % 37, 10**8, 37):
    if fnmatch(str(N), '2*1234?6'):
        print(N, N // 37)

# 20123486 543878
# 23123446 624958
# 26123406 706038