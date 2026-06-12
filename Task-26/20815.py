with open(r'.\files\26_20815.txt') as file:
    N, K = map(int, file.readline().split())
    data = []
    for i in file:
        num, *exs, sob = map(int, i.split())
        data.append([num, sum(exs) + sob, sob])

data = sorted(data, key=lambda x: (-x[1], -x[2], x[0]))

half_passage = data[:K]
passage_person = 0

for i in half_passage[::-1]:
    if i[1] > half_passage[-1][1]:
        passage_person = i[0]
        break

cnt = 0
for i in data[::-1]:
    if i[1] == half_passage[-1][1]:
        cnt += 1
print(passage_person, cnt)

# 45539 127