with open(r'.\files\24.txt') as file:
    data = file.readline()

ans = 0

for i in range(len(data)):
    cnt = 0
    cnt_Z = 0
    for j in range(i, len(data)):
        if data[j] == 'Z':
            cnt_Z += 1
        if cnt_Z == 271:
            break
        cnt += 1
    ans = max(ans, cnt)
print(ans)

# 1697