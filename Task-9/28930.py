with open(r'.\files\28930.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for line in data:
    if line == sorted(line) and len(line) == len(set(line)):
        if max(line) + min(line) <= sum(line) - max(line) - min(line):
            ans += 1
print(ans)

# 138