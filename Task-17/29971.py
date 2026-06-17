with open(r'.\files\17_29971.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if abs(i) % 100 == 33)

ans = []
for nums in zip(data, data[1:], data[2:]):
    u1 = sum(1 for num in nums if 10 <= abs(num) <= 99) == 2
    u2 = sum(nums) ** 2 < maxx
    if u1 and u2:
        ans.append(sum(nums))
print(len(ans), max(ans))

# 68 306