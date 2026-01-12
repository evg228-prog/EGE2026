from itertools import *

graph = 'ab bd df fg eg ce ca bc de'.split()
matrix = '67 567 457 35 234 12 123'.split()

print(*range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 72