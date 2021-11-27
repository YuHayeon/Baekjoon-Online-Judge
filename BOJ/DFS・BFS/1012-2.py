# 1012-2 : 유기농 배추 - DFS

import sys
sys.setrecursionlimit(10000)

t = int(sys.stdin.readline())

for _ in range(t):
    n, m, k = map(int, sys.stdin.readline().split())

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    field = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[x][y] = 1

    def dfs(field, x, y):
        field[x][y] = 0

        for i in range(4):
            rx = x+dx[i]
            ry = y+dy[i]
            if rx >= n or rx < 0 or ry >= m or ry < 0:
                continue
            if field[rx][ry] == 1:
                dfs(field, rx, ry)

    cnt = 0

    for a in range(n):
        for b in range(m):
            if field[a][b] == 1:
                dfs(field, a, b)
                cnt += 1

    print(cnt)
