with open(r'.\files\9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    cnt = [line.count(i) for i in set(line)]
    if sorted(cnt) == [1, 1, 1, 2, 2]:
        rep = [i for i in line if line.count(i) > 1]
        non_rep = [i for i in line if line.count(i) == 1]
        if sum(rep) // len(rep) < max(non_rep):
            print(pos, line)
            break