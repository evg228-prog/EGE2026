with open(r'.\files\26_21719.txt') as file:
    N = int(file.readline())
    students = [list(map(int, i.split())) for i in file]

students = sorted(set(tuple(i) for i in students))
best_id = 0
best_solution = 0

cnt = 1
for i in range(len(students) - 1):
    if students[i][0] == students[i + 1][0] and students[i + 1][1] - students[i][1] == 2:
        cnt += 1
    else:
        if cnt > best_solution:
            best_solution = cnt
            best_id = students[i][0]
        elif cnt == best_solution and students[i][0] < best_id:
            best_id = students[i][0]

        cnt = 1

print(best_id, best_solution)

# 10135 42

