for p in range(int(max('thnqul'), 36) + 1, 37):
    num1 = int('th', p)
    num2 = int('nq', p)
    num3 = int('u', p)
    num4 = int('1l7', p)
    if num1 + num2 + num3 == num4:
        print(p)

# 33