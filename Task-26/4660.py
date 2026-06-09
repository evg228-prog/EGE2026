with open(r'.\files\26_4660.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data)

many_check = sum(data) - sum(data[::-1][3::4]) // 2
only_check = sum(data) - sum(data[:N // 4]) // 2
print(many_check, only_check)

# 44101521 48825239