with open(r'.\files\17_17636.txt') as file:
    data = [int(i) for i in file]

max_3 = max(i for i in data if 100 <= abs(i) <= 999 and abs(i) % 10 == 3)

ans = []

for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = abs(num1) % 10 == 3 and 100 <= abs(num1) <= 999
    u2 = abs(num2) % 10 == 3 and 100 <= abs(num2) <= 999
    u3 = abs(num3) % 10 == 3 and 100 <= abs(num3) <= 999
    if u1 + u2 + u3 >= 1 and num1 + num2 + num3 < max_3:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))

# 147 944