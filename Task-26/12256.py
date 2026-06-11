with open(r'.\files\26_12256.txt') as file:
    S, N = map(int, file.readline().split())
    weights = [int(i) for i in file]

weights = sorted(weights)
truck = []

for weight in weights:
    if sum(truck) + weight <= S:
        truck.append(weight)
    elif sum(truck) - truck[-1] + weight <= S:
        truck[-1] = weight
    else:
        break
print(len(truck), truck[-1])

# 629 50