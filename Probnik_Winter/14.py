from string import printable as olo
def convert(num, sys):
    res = ''
    while num:
        res += olo[num % sys]
        num //= sys
    return res[::-1]

ans = []
for x in range(10, 70_000):
    num1 = convert(5**2025 + 5**400 - x, 5)
    num1 = str(num1)
    ans.append([num1.count('4'), x])
print(max(ans))