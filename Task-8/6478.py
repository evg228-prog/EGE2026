from itertools import product

alph = 'моль'
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != 'ь' and 'ьь' not in val and 'оь' not in val:
        cnt += 1
print(cnt)

# 495
