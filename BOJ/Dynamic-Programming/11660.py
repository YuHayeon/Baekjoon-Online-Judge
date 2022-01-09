# 11660 : 구간 합 구하기 5

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = [[0 for _ in range(N+1)]] + [[0]+list(map(int, input().split()))
                                 for _ in range(N)]

for i in range(1, N+1):
    for j in range(1, N+1):
        d[i][j] += d[i][j-1] + d[i-1][j]-d[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2, y2
    result = d[x2][y2]-d[x1-1][y2]-d[x2][y1-1]+d[x1-1][y1-1]
    print(result)
