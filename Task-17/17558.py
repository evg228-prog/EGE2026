with open(r'.\files\17_17558.txt') as file:
    data = [int(i) for i in file]

cnt = len([i for i in data if i % 32 == 0])

ans = []

for num1, num2 in zip(data, data[1:]):
    u1 = -100_000 <= num1 <= -1
    u2 = -100_000 <= num2 <= -1
    if u1 + u2 >= 1 and num1 + num2 < cnt:
        ans.append(num1 + num2)
print(len(ans), max(ans))

# 4969 299