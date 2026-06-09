with open(r'.\files\26_1868.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data)
prew_row, prew_place = data[0]
best_row = 0
best_place = 0

for row, place in data[1:]:
    if row == prew_row:
        if place - prew_place == 3:
            candidate = prew_place + 1
            if row > best_row:
                best_row = row
                best_place = candidate
            elif row == best_row:
                best_place = min(best_place, candidate)
    prew_row, prew_place = row, place
print(best_row, best_place)

###############################################

data = sorted(data, key=lambda x: (-x[0], x[1]))

for seat1, seat2 in zip(data, data[1:]):
    if seat1[0] == seat2[0]:
        if seat2[1] - seat1[1] == 3:
            print(seat1[0], seat1[1] + 1)
            break

# 8631 7311