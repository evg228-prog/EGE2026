with open(r'.\files\17_27629.txt') as file:
    data = [int(i) for i in file]

max_43 = max(i for i in data if abs(i) % 100 == 43 and 1000 <= abs(i) <= 9999)

ans = []

for num1, num2 in zip(data, data[1:]):
    u1 = 1000 <= abs(num1) <= 9999
    u2 = 1000 <= abs(num2) <= 9999
    if u1 + u2 >= 1 and (num1 + num2) ** 2 < max_43 ** 2:
        ans. append((num1 + num2) ** 2)
print(len(ans), max(ans))

# 1218 98843364