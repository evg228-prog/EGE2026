from itertools import *
cnt = 0
for i in range(5, 8):
    for val in product('берск', repeat=i):
        cnt += 1
print(cnt)

# 96875
