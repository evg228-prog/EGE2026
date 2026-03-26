with open(r'.\files\14251.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for line in enumerate(data, start=1):
    cnt = [line.count(i) for i in set(line)]
    if sorted(cnt) == [1, 1, 1, 2, 2]:
        rep = [i for i in line if line.count(i) != 1]
        non_chet = [i for i in line if i % 2 != 0]
        if sum(rep) <= sum(non_chet):
            print(sum(line))
            break

# 626