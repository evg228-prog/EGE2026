with open(r'.\files\29341.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for line in data:
    if max(line) < sum(line) - max(line):
        a, b, c, d = line
        if a + b != c + d and a + c != b + d and c + b != a + d:
            ans += 1
print(ans)

# 2354