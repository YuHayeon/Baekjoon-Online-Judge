# 12865 : 평범한 배낭

import sys

n, k = map(int, sys.stdin.readline().split())
a = [[0,0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
    w = a[i][0]
    v = a[i][1]
    for j in range(0,k+1):
        if j-w>=0:
            d[i][j] = max(d[i-1][j-w]+v, d[i-1][j])
        else:
            d[i][j] = d[i-1][j]

print(max(d[n]))




