with open(r'.\files\17_23376.txt') as file:
    data = [int(i) for i in file]

max_37 = max(i for i in data if abs(i) % 100 == 37 and 10_000 <= abs(i) <= 99_999)

ans = []

for num1, num2 in zip(data, data[1:]):
    u1 = 10_000 <= abs(num1) <= 99_999
    u2 = 10_000 <= abs(num2) <= 99_999
    if u1 + u2 == 1 and (num1 + num2) ** 2 > max_37 ** 2:
        ans.append(num1 + num2)
print(len(ans), max(ans))

# 350 107294