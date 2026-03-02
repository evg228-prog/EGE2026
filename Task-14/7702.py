from string import printable as p
ans = []
for x in range(18):
    for y in range(max(9, x + 1), 18):
        num1 = int(f'5{p[x]}{p[y]}A', 18)
        num2 = int(f'18{p[x]}7', y)
        num = num1 + num2
        ans.append(num)
print(len(set(ans)))

# 116