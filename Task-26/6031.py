with open(r'.\files\26_6031.txt') as file:
    N = int(file.readline())
    rings = [int(i) for i in file]

rings = sorted(rings, reverse=True)
all_rings = [rings[0]]

for ring in rings:
    if all_rings[-1] - ring >= 6:
        all_rings.append(ring)
print(len(all_rings), all_rings[-1])

# 1575 50