with open(r'.\files\26_4684.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data)

only_check = sum(data) - sum(data[:N // 4]) // 2
many_check = sum(data) - sum(data[::-1][5::6]) // 2
print(many_check, only_check)

# 46201709 48825239