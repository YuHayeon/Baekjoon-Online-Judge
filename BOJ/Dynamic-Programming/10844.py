# 10844 : 쉬운 계단 수

import sys

n = int(sys.stdin.readline())
d = [[0] + [1 for _ in range(9)]] + [[0 for _ in range(10)] for _ in range(n-1)]

for i in range(1, n):
    d[i][0] = d[i-1][1]
    for j in range(1, 9):
        d[i][j] += d[i-1][j+1]
        d[i][j] += d[i-1][j-1]
    d[i][9] = d[i-1][8]

result = sum(d[n-1]) % 1000000000
print(result)