with open(r'.\files\26_10107.txt') as file:
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times = sorted(times, key=lambda x: (x[1], x[0]))
events = [times[0]]

for time in times:
    if events[-1][1] <= time[0]:
        events.append(time)

events.pop()
events.append(max(times))
print(len(events), events[-1][0] - events[-2][1])

# 32 15