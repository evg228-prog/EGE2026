with open(r'.\files\26_6641.txt') as file:
    N, M = map(int, file.readline().split())
    prices = [list(map(int, i.replace('S', '0').replace('W', '1').split())) for i in file]

prices = sorted(prices)

cnt_S = 0
bought = []
summ = 0

for price in prices:
    if summ + price[0] <= M:
        summ += price[0]
        bought.append(price)
        cnt_S += 1 if price[1] == 0 else 0

len_bought = len(bought)
for price in bought[::-1]:
    if price[1] == 1:
        for cost in prices[len_bought:]:
            len_bought += 1
            if cost[1] == 0 and summ - price[0] + cost[0] <= M:
                bought.remove(price)
                bought.append(cost)
                summ = summ - price[0] + cost[0]
                cnt_S += 1
                break
print(cnt_S, M - summ)

# 393 4