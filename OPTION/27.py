from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_A.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1_A = [d for d in dots if d[1] < 15]
cluster_2_A = [d for d in dots if d[1] > 15]

P1 = center(cluster_1_A)[0] + center(cluster_2_A)[0]
P2 = center(cluster_1_A)[1] + center(cluster_2_A)[1]
print(P1 * 10_000, P2 * 10_000)

with open(r'.\files\27_B.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1_B = [d for d in dots if 5 < d[0] < 10]
cluster_2_B = [d for d in dots if 14 < d[0] < 19]
cluster_3_B = [d for d in dots if 19 < d[0] < 24]

Q1 = min(
    dist(center(cluster_1_B), center(cluster_2_B)),
    dist(center(cluster_1_B), center(cluster_3_B)),
    dist(center(cluster_2_B), center(cluster_3_B))
)

Q2 = max(
    dist(center(cluster_1_B), center(cluster_2_B)),
    dist(center(cluster_1_B), center(cluster_3_B)),
    dist(center(cluster_2_B), center(cluster_3_B))
)
print(Q1 * 10_000, Q2 * 10_000)

# 107002 323741
# 58778 151839