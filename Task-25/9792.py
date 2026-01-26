from fnmatch import fnmatch

for N in range(120076 - 120076 % 1923, 10**8, 1923):
    if fnmatch(str(N), '1*2??76'):
        print(N, N // 1923)

# 10022676 5212
# 12522576 6512
# 15022476 7812
# 17522376 9112
# 19829976 10312