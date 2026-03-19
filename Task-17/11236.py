from math import *

with open(r'.\files\17_11236.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if 10 <= abs(i) <= 99)
maxx = abs(max(i for i in data if 1000 <= abs(i) <= 9999 and abs(i) % 10 == 1))

ans = []

for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = num1 > minn ** 2
    u2 = num2 > minn ** 2
    u3 = num3 > minn ** 2
    if u1 + u2 + u3 == 2 and (abs(num1) * abs(num2) * abs(num3)) % maxx == 0:
        ans.append(abs(num1) + abs(num2) + abs(num3))
print(len(ans), max(ans))

###################################################

ans_1 = []

min_2 = min(i for i in data if len(str(abs(i))) == 2) ** 2
max_1 = max(i for i in data if len(str(abs(i))) == 4 and str(i)[-1] == '1')

for num in zip(data, data[1:], data[2:]):
    u1 = sum(i > min_2 for i in num) == 2
    u2 = prod(map(abs, num))% max_1 == 0
    if u1 and u2:
        ans_1.append(sum(map(abs, num)))
print(len(ans_1), max(ans_1))

# 1 118534
