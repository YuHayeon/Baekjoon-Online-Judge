# BOJ 1932 : 정수 삼각형
# Dynamic Programming - Bottom Up

import sys

n = int(sys.stdin.readline().rstrip())
tri = []
for i in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))

d = [ [0] * n for _ in range(n) ]

print(tri)

d[0][0] = tri[0][0]
d[1][0] = tri[1][0] + tri[0][0]
d[1][1] = tri[1][1] + tri[0][0]

for i in range(2, n):
    for j in range(0, i+1):
        if j==0 :
            d[i][j] = d[i - 1][j] + tri[i][j]
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + tri[i][j]

print(max(max(d)))