from re import *

with open(r'.\files\24_7979.txt') as file:
    data = file.readline()

num = r'(0|[1-7][0-7]*)'
pattern = fr'(?<=F){num}([\+\*]{num})+'
matches = [match.group() for match in finditer(pattern, data)]

ans = []
for match in matches:
    match = match.replace('*', ' * ')
    match = match.replace('+', ' + ')
    match = match.split()
    match = [str(int(match[i], 8)) if i % 2 == 0 else match[i] for i in range(len(match))]
    ans.append([len(match), eval(''.join(match))])
print(max(ans))

# 142844