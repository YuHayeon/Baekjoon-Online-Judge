#11047 : 동전 0

import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))

result = 0
for i in range(n-1, -1, -1):
    if k >= coin[i]:
        result += (k // coin[i])
        k = k % coin[i]

print(result)