from math import *

with open(r'.\files\17_3749.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if i ** 0.5 == int(i ** 0.5)) * 3

ans = []

for num in zip(data, data[1:]):
    u1 = prod(num) ** 0.5 % 1 == 0
    u2 =any(i <= maxx for i in num)
    if u1 + u2 == 2:
        ans.append(prod(num) ** 0.5)
print(len(ans), max(ans) + min(ans))

# 49 45216