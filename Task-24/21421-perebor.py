with open(r'.\files\24_21421.txt') as file:
    data = file.readline()

checkpoint = 0
ans = []
for i in range(len(data)):
    if i < checkpoint:
        continue
    if data[i] in '123456789AB':
        cnt = 0
        for j in range(i, len(data)):
            if data[j] in '0123456789AB':
                cnt += 1
            else:
                checkpoint = j
                break
            if int(data[j], 36) % 2 == 0:
                ans.append(cnt)
print(max(ans))

# 19