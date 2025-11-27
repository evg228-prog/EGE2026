from string import printable

for x in printable[:25]:
    num1 = int(f'A4{x}7F2', 25)
    num2 = int(f'N{x}G5{x}H', 25)
    num3 = int(f'74{x}M26', 25)
    num = num1 + num2 + num3
    if num % 24 == 0:
        print(x, num // 24)

# 16751575
