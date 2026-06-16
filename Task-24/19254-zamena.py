with open(r'.\files\24_19254.txt') as file:
    data = file.readline()

data = data.replace('FSRQ', '*** ***')
data = data.split()

ans = 0
for i in range(len(data) - 80):
    line = ''.join(data[i:i + 81]).replace('******', 'FSRQ')
    ans = max(ans, len(line))
print(ans)

# 2379