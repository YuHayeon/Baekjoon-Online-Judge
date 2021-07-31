# BOJ 1932 : 정수 삼각형
# Dynamic Programming
# 메모이제이션 - 일차원

import sys

n = int(sys.stdin.readline().rstrip())
tri = []
for i in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))

d = [0] * n

if n == 1:
    d[0] = tri[0][0]
else:
    d[0] = tri[1][0] + tri[0][0]
    d[1] = tri[1][1] + tri[0][0]
    for i in range(2, n):
        for j in range(i,-1,-1):
            if j==0 :
                d[j] = d[j] + tri[i][j]
            else:
                d[j] = max(d[j-1], d[j]) + tri[i][j]

print(max(d))