from fnmatch import fnmatch

for N in range(123405 - 123405 % 2025, 10**8 + 1, 2025):
    if fnmatch(str(N), '12*34?5'):
        print(N, N // 2025)

# 1253475 619
# 12103425 5977
# 12593475 6219
# 12913425 6377