with open(r'.\files\27764.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for line in data:
    if len(line) == len(set(line)):
        if (max(line) + min(line)) * 2 == sum(line) - max(line) - min(line):
            ans += 1
print(ans)

# 5019