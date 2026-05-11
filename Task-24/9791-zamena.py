from string import *

with open(r'.\files\24_9791.txt') as file:
    data = file.readline().lower()

for i in printable[16:]: data = data.replace(i, ' ')
data = data.split()

print(len(max(data, key=len)))

# 21