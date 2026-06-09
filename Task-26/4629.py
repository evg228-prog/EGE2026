with open(r'.\files\26_4629.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data)

expectation = sum(data) - sum(data[::-1][:N // 4]) // 2
reality = sum(data) - sum(data[:N // 4]) // 2
print(expectation, reality)

# 39434611 48825239