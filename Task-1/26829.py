from itertools import *

graph = 'гб бж же ев вд дг кб кг ка ае ад'.split()
matrix = '248 137 268 15 467 357 256 13'.split()

print(*range(1, 9))
for i in permutations('абвгеджк'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 43