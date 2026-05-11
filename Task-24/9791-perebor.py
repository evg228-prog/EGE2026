from string import *

with open(r'.\files\24_9791.txt') as file:
    data = file.readline().lower()

ans = 0
checkpoint = 0
for i in range(len(data)):
    if i < checkpoint:
        continue
    if data[i] in printable[:16]:
        cnt = 0
        for j in range(i, len(data)):
            if data[j] in printable[:16]:
                cnt += 1
            else:
                checkpoint = j
                break
        ans = max(ans, cnt)
print(ans)

# 21