from string import printable


def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]


R = 2 * 2187 ** 2020 + 729 ** 2021 - 2 * 243 ** 2022 + 81 ** 2023 - 2 * 27 ** 2024 - 6561

R_27 = convert(R, 27)
cnt = 0

for i in R_27:
    if int(i, 27) > 9:
        cnt += 1
print(cnt)

#######################################

R = 2 * 2187 ** 2020 + 729 ** 2021 - 2 * 243 ** 2022 + 81 ** 2023 - 2 * 27 ** 2024 - 6561
cnt = 0
while R :
    if R % 27 > 9:
        cnt += 1
    R //= 27
print(cnt)
