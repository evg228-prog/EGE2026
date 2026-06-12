with open(r'.\files\26_20910.txt') as file:
    N, M, K = map(int, file.readline().split())
    places = [list(map(int, i.split())) for i in file]


seats = [M] * (K +  1)

for row, place in places:
    seats[place] = min(seats[place], row - 1)

ans = []
for i in range(1, K + 1 - 1):
    ans.append([min(seats[i], seats[i + 1]), i])

print(*max(ans))

# 21028 6660