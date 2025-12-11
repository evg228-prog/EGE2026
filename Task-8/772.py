from itertools import permutations

cnt = 0
for val in set(permutations('пробник')):
    val = ''.join(val)
    for i in 'ои': val = val.replace(i, '*')
    if val[0] in 'прбнк' and val[-1] in 'прбнк' and '**' not in val:
        cnt += 1
print(cnt)

