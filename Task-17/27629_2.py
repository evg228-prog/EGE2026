with open(r'.\files\17_27629.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if 1000 <= abs(i) <= 9999 and abs(i) % 100 == 43)

ans = []
for nums in zip(data, data[1:]):
    u1 = sum(1 for num in nums if 1000 <= abs(num) <= 9999) >= 1
    u2 = sum(nums) ** 2 <  maxx ** 2
    if u1 and u2:
        ans.append(sum(nums) ** 2)
print(len(ans), max(ans))

# 1218 98843364