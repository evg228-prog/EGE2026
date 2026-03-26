with open(r'.\files\17_15333.txt') as file:
    data = [int(i) for i in file]

max_19 = max(i for i in data if i % 19 == 0)

ans = []

for nums in zip(data, data[1:]):
    if sum(num > max_19 for num in nums) >= 1:
        ans.append(sum(nums))
print(len(ans), max(ans))

# 54 174513