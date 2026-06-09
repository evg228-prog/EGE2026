with open(r'.\files\26_3230.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data, key=lambda x: (-x[0], x[1]))

for seat1, seat2 in zip(data, data[1:]):
    if seat1[0] == seat2[0]:
        if seat2[1] - seat1[1] == 12:
            print(seat1[0], seat1[1] + 1)
            break

# 2261 5087