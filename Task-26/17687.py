with open(r'.\files\26_17687.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data)
many_check = sum(data) - sum(data[::-1][8::9])
only_check = sum(data) - sum(data[- (N // 9):])

print(only_check, many_check)

# 39450073 44329073