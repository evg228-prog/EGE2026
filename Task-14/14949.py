from string import *

for x in printable[11:8]:
    num1 = int(f'{x}1{x}', 16)
    num2 = int(f'{x}3{x}3', 8)
    num = num1 + num2
    for i in range(0, 1000):
        if num == 2**i:
            print(x)

# 5
