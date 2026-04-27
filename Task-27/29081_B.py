from math import *


def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]


with open(r'.\files\27_B_29081.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] in '89':
            target.append(dots[-1])

cluster_1 = [d for d in dots if d[1] > 22]
cluster_2 = [d for d in dots if 16 < d[1] < 22]
cluster_3 = [d for d in dots if d[0] > 22]

target_1 = [d for d in target if d[1] > 22]
target_2 = [d for d in target if 16 < d[1] < 22]
target_3 = [d for d in target if d[0] > 22]

B1 = min(
    [dist(d1, d2) for d1 in target_1 for d2 in target_2] +
    [dist(d1, d3) for d1 in target_1 for d3 in target_3] +
    [dist(d3, d2) for d3 in target_3 for d2 in target_2]
)

B2 = [dist(d1, d2) for d1 in target_1 for d2 in target_1 if d1 != d2] + \
[dist(d1, d3) for d1 in target_2 for d3 in target_2 if d1 != d3] + \
[dist(d3, d2) for d3 in target_3 for d2 in target_3 if d3 != d2]

print(B1 * 10_000, sum(B2) / len(B2) * 10_000)

# 54154 12041