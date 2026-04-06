M = 0

for x in range(1, 9431):
    num = 39**483 + 39**235 - x
    cnt_0 = 0
    while num:
        if num % 39 == 0:
            cnt_0 += 1
        num //= 39
    M = max(M, cnt_0)
print(M)

# 250