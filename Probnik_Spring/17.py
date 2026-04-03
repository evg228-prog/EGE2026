with open(r'.\files\17.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if 10 <= i <= 99)

ans = []

for nums in zip(data, data[1:]):
    u1 = sum(10 <= num <= 99 for num in nums) == 1
    u2 = sum(nums) % maxx == 0
    if u1 and u2:
        ans.append(sum(nums))
print(len(ans), max(ans))

# 1 2970