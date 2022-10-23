# 11501 : 주식

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))

    result = 0
    max_price = prices[-1]
    for i in range(n-2, -1, -1):
        if max_price >= prices[i]:
            result += max_price-prices[i]

        else:
            max_price = prices[i]

    print(result)
