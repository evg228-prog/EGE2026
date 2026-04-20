from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_A_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_A_1 = [dot for dot in dots if dot[1] > 0.8 * dot[0] - 8]
cluster_A_2 = [dot for dot in dots if -7 < dot[1] < 0.8 * dot[0] - 8]
cluster_A_3 = [dot for dot in dots if dot[1] < -7]

center_A_1 = center(cluster_A_1)
center_A_2 = center(cluster_A_2)
center_A_3 = center(cluster_A_3)

print((center_A_1[0] + center_A_2[0] + center_A_3[0]) / 3 * 10_000, (center_A_1[1] + center_A_2[1] + center_A_3[1]) / 3 * 10_000)

# 178755 2896

with open(r'.\files\27_B_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_B_1 = [dot for dot in dots if dot[1] < -5]
cluster_B_2 = [dot for dot in dots if -5 < dot[1] < dot[0]]
cluster_B_3 = [dot for dot in dots if dot[0] < dot[1] < 12 / 7 * dot[0] + 12]
cluster_B_4 = [dot for dot in dots if 12 / 7 * dot[0] + 12 < dot[1] and dot[0] > 9]
cluster_B_5 = [dot for dot in dots if -7 / 5 * dot[0] - 84 / 5 < dot[1] and dot[0] < 9]
cluster_B_6 = [dot for dot in dots if dot[1] < -7 / 5 * dot[0] - 84 / 5]

center_B_1 = center(cluster_B_1)
center_B_2 = center(cluster_B_2)
center_B_3 = center(cluster_B_3)
center_B_4 = center(cluster_B_4)
center_B_5 = center(cluster_B_5)
center_B_6 = center(cluster_B_6)

print((center_B_1[0] + center_B_2[0] + center_B_3[0] + center_B_4[0] + center_B_5[0] + center_B_6[0]) / 6 * 10_000, (center_B_1[1] + center_B_2[1] + center_B_3[1] + center_B_4[1] + center_B_5[1] + center_B_6[1]) / 6 * 10_000)

# Не решена