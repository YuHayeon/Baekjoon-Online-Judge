# 2512 : 예산

import sys
input = sys.stdin.readline


def budget(money, n, total):
    for i in range(n):
        if total >= money[i]*(n-i):
            total -= money[i]
        else:
            return total // (n-i)
    return money[-1]


N = int(input())
money = list(map(int, input().split()))
total = int(input())
result = 0

if sum(money) <= total:
    result = max(money)
else:
    money.sort()
    result = budget(money, N, total)

print(result)