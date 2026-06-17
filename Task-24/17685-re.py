from re import *

with open(r'.\files\24_17685.txt') as file:
    data = file.readline()

num = r'(0|[1-9][0-9]*)'
pattern = fr'{num}([\+\*]{num})*'
matches = [match.group() for match in finditer(pattern, data)]

ans = 0
for num in matches:
    len_num = len(num)
    if eval(num) == 0:
        ans = max(ans, len(num))
    if len_num > ans:
        for l in range(0, len_num - 1):
            if num[l] in '+*': continue
            if num[l] == '0' and num[l + 1] not in '+*': continue
            for r in range(len_num - 1, l, -1):
                if num[r] in '*+': continue
                new_num = num[l:r + 1]
                if eval(new_num) == 0:
                    ans = max(ans, len(new_num))
                    break

print(ans)

###################################################################

num = r'(0|[1-9][0-9]*)'
zero = fr'({num}\*)*0(\*{num})*'
pattern = fr'{zero}(\+{zero})*'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))

# 169
