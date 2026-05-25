from re import *

with open(r'.\files\24_14510.txt') as file:
    data = file.readline()

pattern = r'[^AEIOUY]{2}[AEIOUY]'

data = sub(pattern, '*', data)
data = data.split('*')

ans = 10 ** 10
for i in range(1, len(data) - 498 - 1):
    line = 'SSG' + 'SSG'.join(data[i:i + 499]) + 'SSG'
    ans = min(ans, len(line))
print(ans)

# 3493