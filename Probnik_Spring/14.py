for x in range(1, 9431):
    num = 39**483 * 39**2 + 39**235 * 39**1 - x * 39**0
    if str(num).count('0') > 72:
        print(str(num).count('0'))

# 72