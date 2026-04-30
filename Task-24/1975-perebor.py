with open(r'.\files\24_1975.txt') as file:
    data = file.readline()

ans = 0
cnt = 1

for i in range(len(data) - 1):
    if data[i] == data[i + 1] == 'P':
        cnt = 1
    else:
        cnt += 1
        ans = max(ans, cnt)
ans = max(ans, cnt)
print(ans)