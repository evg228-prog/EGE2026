from string import *

with open(r'.\files\24_21421.txt') as file:
    data = ' ' + file.readline().lower() + ' '
#
for i in printable[12:]: data = data.replace(i, ' ')
for i in printable[1:12:2]: data = data.replace(i, '1')
for i in printable[2:12:2]: data = data.replace(i, '2')

while ' 0' in data:
    data = data.replace(' 0', ' ')
while '1 ' in data:
    data = data.replace('1 ', ' ')

data = data.split()

print(len(max(data, key=len)))

################################################################

for i in printable[12:]: data = data.replace(i, ' ')

data = data.split()

ans = 0
for line in data:
    line = line.strip('0').rstrip('13579b')
    ans = max(ans, len(line))
print(ans)

# 19


