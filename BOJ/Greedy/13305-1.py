# 13305 : 주유소 - 58점

import sys

n = int(sys.stdin.readline())
city = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
price.pop(n-1)
result = 0

for i in range(n):
    min_price = min(price)
    min_idx = price.index(min_price)
    del price[min_idx:len(price)]

    for j in range(min_idx, len(city)):
        result += city[min_idx] * min_price
        city.pop(min_idx)

    if city==[]:
        break

print(result)
