num = 0
for N in range(10000, 100000):
    kv = (int(min(str(N)))) + (int(min(str(N)))) ** 2
    pr = 1
    for i in str(N):
        if int(i) % 2 == 0:
            pr *= int(i)
    if kv < pr:
        num = str(pr) + str(kv)
    else:
        num = str(kv) + str(str)

    