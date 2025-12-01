from itertools import *

# product - возвращает всевозможные
# расстановки символов с повторениями длины repeat
alph_1 = '012'
for val in product(alph_1, repeat=2):
    val = ''.join(val)
    print(val)

# permutations - возвращает всевозможные перестановки символов
alph_2 = 'ab'
for val in permutations(alph_2):
    val = ''.join(val)
    print(val)

# enumerate -

alph_3 = 'miin'
res = enumerate(alph_3, start=1)
print(*res)