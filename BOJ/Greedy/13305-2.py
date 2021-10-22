# 13305 : 주유소 - 100점

import sys

n = int(sys.stdin.readline())
city = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

low_price = price[0]
answer = low_price * city[0]

for i in range(1,n-1):
    low_price = min(low_price, price[i])
    answer += low_price * city[i]

print(answer)