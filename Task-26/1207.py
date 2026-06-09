with open(r'.\files\26_1207.txt') as file:
    S, N = map(int, file.readline().split())
    sizes = [int(i) for i in file]

sizes = sorted(sizes)
storage = []

for size in sizes:
    if sum(storage) + size <= S:
        storage.append(size)
for size in sizes:
    if sum(storage) - storage[-1] + size <= S:
        storage[-1] = size
print(len(storage), max(storage))

# 1611 90