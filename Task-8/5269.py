from itertools import permutations

cnt = 0
for val in set(permutations('амфибрахий')):
    val = ''.join(val)
    if val[4:6]  == 'бр':
        cnt += 1
print(cnt)

# 10080