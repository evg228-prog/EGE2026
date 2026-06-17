with open(r'.\files\17_28938.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if abs(i) % 100 == 28)

ans = []
for nums in zip(data, data[1:], data[2:]):
    u1 = sum(1 for num in nums if 100 <= abs(num) <= 999) >= 1
    u2 = (sum(nums) / len(nums) > 0) and (sum(nums) / len(nums) < maxx)
    if u1 and u2:
        ans.append(sum(nums))
print(len(ans), max(ans))

# 1290 193483