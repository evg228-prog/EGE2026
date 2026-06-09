with open(r'.\files\26_3586.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data)
prew_row, prew_place = data[0]
best_row = 0
best_place = 0
max_free = 0

for row, place in data[1:]:
    if row == prew_row:
        free = place - prew_place - 1
        if free > max_free:
            max_free = free
            best_row = row
            best_place = prew_place + 1
        elif free == max_free and row > best_row:
            best_row = row
            best_place = prew_place + 1
    prew_row, prew_place = row, place
print(best_row, max_free)

# 4802 7468