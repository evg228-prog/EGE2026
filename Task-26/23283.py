with open(r'.\files\26_23283.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times = sorted(times)

windows = [0] * K
pos = 0
cnt = 0

for time in times:
    for i in range(K):
        if windows[i] < time[0]:
            windows[i] = time[1]
            pos = i + 1
            cnt += 1
            break
print(cnt, pos)

# 793 2