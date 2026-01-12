from re import *
with open(r'.\files\24 (1).txt') as file:
    data = file.readline()

pattern = r'([^0\-\*][\-\*]([^0][0789]))+'
matches = [match.group() for match in finditer(pattern , data)]
print(len(max(matches, key=len)))

# 24