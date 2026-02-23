def f(start, cnt=0):
    if cnt == 15: return {start}
    return f(start + 10, cnt + 1) | f(start - 5, cnt + 1)

print(len(f(1)))

#####################################

def f(s, cnt):
    if cnt == 15:
        mn.add(s)
        return
    f(s + 10, cnt + 1)
    f(s - 5, cnt + 1)

mn = set()
f(1, 0)
print(len(mn))

#####################################

def f(p):
    a.append(p + 10)
    a.append(p - 5)

a = [1]
for i in range(15):
    b = list(a)
    a = []
    for j in b:
        f(j)
print(len(set(a)))

# 16