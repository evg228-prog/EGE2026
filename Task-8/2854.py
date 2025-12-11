from itertools import permutations

cnt = 0
for val in set(permutations('росомаха')):
    val = ''.join(val)
    for i in 'рсмх': val = val.replace(i, '*')
    for i in 'ао': val = val.replace(i, '+')
    if '**' not in val and '++' not in val:
        cnt += 1
print(cnt)

# 288