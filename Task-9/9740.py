with open(r'.\files\9740.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0

for line in data:
    cnt = [line.count(i) for i in set(line)]
    if sorted(cnt) == [1, 1, 1, 1, 3]:
        rep = [i for i in line if line.count(i) > 1]
        non_rep = [i for i in line if line.count(i) == 1]
        if sum(non_rep) / len(non_rep) <= rep[0]:
            ans += 1
print(ans)

# 36