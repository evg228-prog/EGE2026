def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) == 3:
        return max(d)
    return 0

cnt = 0
for i in range(int(106_732_567 ** 0.5), int(152_673_836 ** 0.5)):
    if M:= f(i ** 2):
        print(i ** 2, M)
        cnt += 1
        if cnt == 5:
            break

# 112550881 1092727
# 131079601 1225043
# 141158161 1295029