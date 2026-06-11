with open(r'.\files\26_17537.txt') as file:
    N, M, K = map(int, file.readline().split())
    places = [list(map(int, i.split())) for i in file]

seats = [M] * (K + 1)

for row, seat in places:
    seats[seat] = min(seats[seat], row - 1)

answer = []
for i in range(1, K + 1 - 1):
    answer.append([min(seats[i], seats[i + 1]), i + 1])

print(*max(answer))

# 9991 5643