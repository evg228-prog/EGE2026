from re import *

with open(r'.\files\24_28943.txt') as file:
    data = file.readline()

data = data.replace('20', '#')
pattern = r'(#[^EYUIOA#]*){26}[EYUIOA]'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key=len).replace('#', '20')))

# 58