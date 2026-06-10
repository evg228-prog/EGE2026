with open(r'.\files\26_9793.txt') as file:
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times = sorted(times)
details = [0] * N
best_cnt = 0
last_detail = 0

for time in times:
    if time[0] < time[1]:
        for i in range(len(details)):
            if details[i] == 0:
                details[i] = time[0]
                best_cnt = i + 1
                last_detail = time
                break
    else:
        for i in range(len(details) - 1, - 1, - 1):
            if details[i] == 0:
                details[i] = time[1]
                best_cnt = i + 1
                last_detail = time
                break
    last_detail = time
print(details.index(last_detail), best_cnt - 1)

# Не доработана

#########################################################

with open(r'.\files\26_9793.txt') as file:
    N = int(file.readline())
    pieces = []
    for pos, data in enumerate(file, start=1):
        time_1, time_2 = map(int, data.split())
        pieces.append([time_1, 's', pos])
        pieces.append([time_2, 'o', pos])

pieces = sorted(pieces)
conveyor = [0] * N

left, right = 0, N - 1
last_piece = 0
cnt = 0
for piece in pieces:
    if piece[2] in conveyor:
        continue
    if piece[1] == 's':
        conveyor[left] = piece[2]
        left += 1
        cnt += 1
    else:
        conveyor[right] = piece[2]
        right -= 1
    last_piece = piece

print(last_piece[2], cnt - 1 if last_piece[1] == 's' else 0)

#########################################################

with open(r'..\files\26_9793.txt') as file:
    N = int(file.readline())
    pieces = []
    for pos, data in enumerate(file, start=1):
        time_1, time_2 = map(int, data.split())
        if min(time_1, time_2) == time_1:
            pieces.append([time_1, 's', pos])
        else:
            pieces.append([time_2, 'o', pos])

pieces = sorted(pieces)

last_piece = pieces[-1]
cnt = sum(1 for piece in pieces if piece[1] == 's')

print(last_piece[2], cnt - 1 if last_piece[1] == 's' else 0)

# 895 488