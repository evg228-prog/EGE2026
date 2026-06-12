with open(r'.\files\26_23383 (1).txt') as file:
    N = int(file.readline())
    runners = [list(map(int, i.split())) for i in file]

runners = sorted(set(tuple(i) for i in runners))

best_id = 0
best_race = 0
cnt_sportsman = 0

cnt = 1
for i in range(len(runners) - 1):
    if runners[i][0] == runners[i + 1][0] and runners[i + 1][1] - runners[i][1] == 2:
        cnt += 1
    else:
        if cnt > best_race:
            best_race = cnt
            best_id = runners[i][0]
            cnt_sportsman = 1
        elif cnt == best_race:
            cnt_sportsman += 1
            if runners[i][0] < best_id:
                best_id = runners[i][0]
        cnt = 1

if cnt > best_race:
    best_race = cnt
    best_id = runners[-1][0]
    cnt_sportsman = 1
elif cnt == best_race:
    cnt_sportsman += 1
    if runners[-1][0] < best_id:
        best_id = runners[i][0]

print(cnt_sportsman, best_id)