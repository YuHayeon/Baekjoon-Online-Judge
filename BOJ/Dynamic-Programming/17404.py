# 17404 : RGB거리 2

import sys
input = sys.stdin.readline

N = int(input())
rgb = [list(map(int, input().split())) for _ in range(N)]
d = [[0, 0, 0] for _ in range(2)]
INF = int(1e9)
res = INF


for i in range(3):
    d[0] = [INF, INF, INF]
    d[0][i] = rgb[0][i]

    for j in range(1, N):
        d[1][0] = min(d[0][1], d[0][2]) + rgb[j][0]
        d[1][1] = min(d[0][0], d[0][2]) + rgb[j][1]
        d[1][2] = min(d[0][0], d[0][1]) + rgb[j][2]

        d[0][0], d[0][1], d[0][2] = d[1][0], d[1][1], d[1][2]

    for k in range(3):
        if i != k:
            res = min(d[1][k], res)

print(res)