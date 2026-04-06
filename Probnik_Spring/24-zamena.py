with open(r'.\files\24.txt') as file:
    data = file.readline()

data = data.split('Z')
ans = 10 ** 10
for i in range(len(data) - 269):
    text = 'Z'.join(data[i:i + 269])
    ans = min(ans, len(text) + 2)
print(ans)

# 1058