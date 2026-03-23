with open(r'.\files\17628.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0

for line in data:
    maxx = max(line)
    minn = min(line)
    if maxx + minn <= sum(line) - maxx - minn:
        ans += 1
print(ans)

# 15115