with open(r'.\files\17_23902.txt') as file:
    data = [int(i) for i in file]

ans = []

for num in zip(data, data[1:], data[2:]):
    u1 = sum(str(i)[0] == str(i)[-1] for i in num) == 1
    u2 = sum(str(i)[1] == '2' for i in num if len(str(i)) == 4) == 2
    if u1 and u2:
        ans.append(max(num))
print(len(ans), sum(ans))

# 50 393899