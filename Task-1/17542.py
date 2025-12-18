from itertools import permutations

graph = 'de ea ah hc cf gf bg db eb hg'.split()
matrix = '38 58 146 36 27 347 568 127'.split()

print(*range(1, 9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 37