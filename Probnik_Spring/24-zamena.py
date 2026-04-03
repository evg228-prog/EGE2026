with open(r'.\files\24.txt') as file:
    data = file.readline()

data = data.split('Z')
ans = 0
for i in range(len(data) - 270):
    text = 'Z'.join(data[i:i + 271])
    ans = max(ans, len(text))
print(ans)

# 1697