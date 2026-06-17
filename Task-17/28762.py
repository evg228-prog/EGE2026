with open(r'.\files\17_28762.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if abs(i) % 23 == 0)

ans = []
for nums in zip(data, data[1:]):
    u1 = sum(1 for num in nums if abs(num) % minn == 0) >= 1
    if u1:
        ans.append(sum(nums))
print(len(ans), max(ans))

# 113 168437