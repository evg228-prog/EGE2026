from traceback import print_tb

with open(r'.\files\17_18176.txt') as file:
    data = [int(i) for i in file]

min_4 = min(i for i in data if i % 10 == 4 and str(i)[0] != '-')

ans = []

for num1, num2, num3  in zip(data, data[1:], data[2:]):
    u1 = sum(map(int, str(abs(num1))))
    u2 = sum(map(int, str(abs(num2))))
    u3 = sum(map(int, str(abs(num3))))
    if u1 + u2 + u3 == min_4:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))

# 11 180738

