from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_A_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_A_1 = [dot for dot in dots if dot[0] < 5]
cluster_A_2 = [dot for dot in dots if dot[0] > 5]

center_A_1 = center(cluster_A_1)
center_A_2 = center(cluster_A_2)

print(max(center_A_1[0], center_A_2[0] * 10_000), max(center_A_1[1], center_A_2[1] * 10_000))

# 69663 192156

with open(r'.\files\27_B_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_B_1 = [dot for dot in dots if dot[0] > 9 and dot[1] < 13]
cluster_B_2 = [dot for dot in dots if dot[0] > 6 and 17 < dot[1] < 21]
cluster_B_3 = [dot for dot in dots if dot[0] > 10 and 21 < dot[1] < 25]

center_B_min = center(min(cluster_B_1, cluster_B_2, cluster_B_3, key=len))
center_B_max = center(max(cluster_B_1, cluster_B_2, cluster_B_3, key=len))

print(abs(center_B_min[0] - center_B_max[0]) * 10_000, abs(center_B_min[1] - center_B_max[1]) * 10_000)

# 867 161306