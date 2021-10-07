# 1149 : RGB거리

import sys
n = int(sys.stdin.readline())
rgb = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
d = [[0,0,0] for i in range(n)]
d[0][0] = rgb[0][0]
d[0][1] = rgb[0][1]
d[0][2] = rgb[0][2]

for i in range(1,n):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + rgb[i][0]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + rgb[i][1]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + rgb[i][2]
    print(d)
print(min(d[n-1]))

