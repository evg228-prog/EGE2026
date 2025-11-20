from string import printable

for x in printable[:19]:
    num_1 = int(f'98{x}79641', 19)
    num_2 = int(f'36{x}14', 19)
    num_3 = int(f'73{x}4', 19)
    num = num_1 + num_2 + num_3
    if num % 18 == 0:
        print(x, num // 18)