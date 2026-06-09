with open(r'.\files\20899.txt') as file:
    data = [list(map(int, i.split())) for i in file]

amount = 0
for line in data:
    if max(line) < sum(line) - max(line):
        cnt = [line.count(i) for i in set(line)]
        if sorted(cnt) == [1, 1, 2]:
            amount += 1
print(amount)

# 138