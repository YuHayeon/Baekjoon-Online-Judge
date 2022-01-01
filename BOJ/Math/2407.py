# 2407 : 조합

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = [[1, 1] for _ in range(m+1)]
result = 0

for i in range(1, m+1):
    d[i][0] = d[i-1][0] * (n-i+1)
    d[i][1] = d[i-1][1] * i

result = (d[m][0]//d[m][1])
print(result)
