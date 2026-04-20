from math import *

def anticenter(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return max(res)[1]

with open(r'.\files\27.17.A_19566.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

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
        clusters += [cluster]

print([len(cluster) for cluster in clusters])
anticenters_X = [anticenter(cluster)[0] for cluster in clusters]
anticenters_Y = [anticenter(cluster)[1] for cluster in clusters]
print(abs(sum(anticenters_X) / len(anticenters_X) * 10_000), abs(sum(anticenters_Y) / len(anticenters_Y) * 10_000))

# 14803 51534

with open(r'.\files\27.17.B_19566.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

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
        clusters += [cluster]

print([len(cluster) for cluster in clusters])
anticenters_X = [anticenter(cluster)[0] for cluster in clusters]
anticenters_Y = [anticenter(cluster)[1] for cluster in clusters]
print(abs(sum(anticenters_X) / len(anticenters_X) * 10_000), abs(sum(anticenters_Y) / len(anticenters_Y) * 10_000))

# 216297 43456