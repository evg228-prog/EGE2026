with open(r'.\files\26_6759.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data)
many_check = sum(data) - sum(data[::-1][:N // 3])
only_check = sum(data) - sum(data[::-1][2::3])

print(many_check, only_check)

# 22262050 33246829