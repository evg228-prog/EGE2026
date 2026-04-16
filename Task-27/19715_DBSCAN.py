from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27.21.A_19715.txt') as file:
    dots = [list(map(float, i.split())) for i in file]

eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 30:
        clusters.append(cluster)

print([len(cluster) for cluster in clusters])
centers_X = [center(cluster)[0] for cluster in clusters]
centers_Y = [center(cluster)[1] for cluster in clusters]
print(sum(centers_X) / 2 * 10_000, sum(centers_Y) / 2 * 10_000)

# 132035 86733

with open(r'.\files\27.21.B_19715.txt') as file:
    dots = [list(map(float, i.split())) for i in file]

eps = 3
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 30:
        clusters.append(cluster)

print([len(cluster) for cluster in clusters])
centers_X = [center(cluster)[0] for cluster in clusters]
centers_Y = [center(cluster)[1] for cluster in clusters]
print(abs(sum(centers_X)) / 4 * 10_000, abs(sum(centers_Y)) / 4 * 10_000)

# 13054 128771