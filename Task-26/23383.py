with open(r'.\files\26_23383 (1).txt') as file:
    N = int(file.readline())
    data = [tuple(map(int, i.split())) for i in file]


data = sorted(set(data), key=lambda x: (x[1], x[0]))

cnt = 1
ans = []
for men_1, men_2 in zip(data, data[1:]):
    if men_1[1] == men_2[1] and men_2[0] - men_1[0] == 1:
        cnt += 1
    else:
        cnt = 1
    ans.append([cnt, men_1[1]])
print(*max(ans, key=lambda x: (x[0], -x[1])))

# 56 30113


















###########################################################

# runners = {}
# for num, checkpoint in times:
#     if checkpoint not in runners:
#         runners[checkpoint] = {num}
#     else:
#         runners[checkpoint] |= {num}
#
# cnt = 1
# ans = 0
# best_checkpoint = []
#
# for checkpoint in runners:
#
#
# print(ans)

