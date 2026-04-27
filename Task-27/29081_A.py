from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_A_29081.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[2:].strip() == 'VII':
            target.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] > 8]
cluster_2 = [d for d in dots if d[1] < 8]

target_1 = [d for d in target if d[1] > 8]
target_2 = [d for d in target if d[1] < 8]

dist_min1 = min(dist(center(cluster_1), d) for d in target_1)
dist_min2 = min(dist(center(cluster_2), d) for d in target_2)

dist_max1 = max(dist(center(cluster_1), d) for d in target_1)
dist_max2 = max(dist(center(cluster_2), d) for d in target_2)

print(min(dist_min1, dist_min2) * 10_000, max(dist_max1, dist_max2) * 10_000)

# 1495 16955
