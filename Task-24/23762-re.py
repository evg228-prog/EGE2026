from re import *

with open(r'.\files\24_23762.txt') as file:
    data = file.readline()

pattern = r'[^(2025)Y]*(2025){90}Y{80}[^(2025)Y]*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))