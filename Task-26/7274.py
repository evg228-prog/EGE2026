with open(r'.\files\26_7274.txt') as file:
    N = int(file.readline())
    seedings = [list(map(int, i.split())) for i in file]

seedings = sorted(seedings)
prew_row, prew_place = seedings[0]
best_row = 0
best_place = 0

for row, place in seedings[1:]:
    if row == prew_row:
        if place - prew_place == 14:
            candidate = prew_place + 1
            if row > best_row:
                best_row = row
                best_place = candidate
            elif row == best_row:
                best_place = min(best_place, candidate)
    prew_row, prew_place = row, place
print(best_row, best_place)

# 59966 50449