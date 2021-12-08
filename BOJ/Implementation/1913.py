# 1913 : 달팽이

import sys

n = int(sys.stdin.readline())
find = int(sys.stdin.readline())

d = [[0]*n for _ in range(n)]
d[n//2][n//2] = 1
r, c = n//2, n//2

for i in range(1, n):
    if i % 2 == 1:
        for j in range(i):
            d[r-1][c] = d[r][c]+1
            r = r-1
        for j in range(i):
            d[r][c+1] = d[r][c]+1
            c = c+1
    elif i % 2 == 0:
        for j in range(i):
            d[r+1][c] = d[r][c]+1
            r = r+1
        for j in range(i):
            d[r][c-1] = d[r][c]+1
            c = c-1

for _ in range(n-1):
    d[r-1][c] = d[r][c]+1
    r = r-1

x, y = 0, 0
for i in range(n):
    for j in range(n):
        print(d[i][j], end=' ')
        if d[i][j] == find:
            x, y = i+1, j+1
    print()
print(x, y)
