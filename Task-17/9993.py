from math import *

with open(r'.\files\17_9993.txt') as file:
    data = [int(i) for i in file]

def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

max_17 = max(i for i in data if i % 100 == 17)

ans = []

for nums in zip(data, data[1:]):
    u1 = sum(is_prime(i) for i in nums) == 1
    u2 = abs(sum(nums)) % abs(max_17) == 0
    if u1 and u2:
        ans.append(prod(nums))
print(len(ans), max(ans))

# 7 2446423792