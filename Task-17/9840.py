with open(r'.\files\17_9840.txt') as file:
    data = [int(i) for i in file]

max_39 = max(i for i in data if 1000 <= abs(i) <= 9999 and i % 100 == 39)

ans = []

for num1, num2 in zip(data, data[1:]):
    u1 = 1000 <= abs(num1) <= 9999
    u2 = 1000 <= abs(num2) <= 9999
    if u1 + u2 == 1 and (num1 + num2) ** 2 <= max_39 ** 2:
        ans.append(num1 + num2)
print(len(ans), max(ans))

# 1591 9233