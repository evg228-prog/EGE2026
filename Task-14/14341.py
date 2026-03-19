from string import *

for x in printable[:22]:
    num1 = int(f'56{x}C20', 22)
    num2 = int(f'89F{x}2', 22)
    num3 = int(f'H24{x}K21', 22)
    if (num1 + num2 + num3) % 21 == 0:
        print((num1 + num2 + num3) // 21)

# 93708051