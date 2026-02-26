s = {1}
for p in range(8):
    s = {x + 1 for x in s} | {x + 5 for x in s} | {x * 3 for x in s}
ans = [x for x in s if 1000 <= x <= 1024]
print(len(ans))

######################################

def f(start, cnt=0):
    if cnt == 8:
        if 1000 <= start <= 1024: return {start}
        return set()
    return f(start + 1, cnt  + 1) | f(start + 5, cnt + 1) | f(start * 3, cnt + 1)

print(len(f(1)))

# 1