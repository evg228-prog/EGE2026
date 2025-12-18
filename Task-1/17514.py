from itertools import permutations

graph = 'ba ae ec cd fd fh bh ah eg gc gf'.split()
matrix = '247 148 578 126 38 47 136 235'.split()

print(*range(1, 9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 38