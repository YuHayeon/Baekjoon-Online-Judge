# 1012 : 유기농 배추 - BFS

import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m, k = map(int, sys.stdin.readline().split())

    field = [[0] * m for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[x][y] = 1

    def bfs(field, a, b):
        queue = deque()
        queue.append((a, b))
        field[a][b] = 0

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                rx = x+dx[i]
                ry = y+dy[i]
                if rx >= n or rx < 0 or ry >= m or ry < 0:
                    continue
                if field[rx][ry] == 1:
                    queue.append((rx, ry))
                    field[rx][ry] = 0

    cnt = 0
    for a in range(n):
        for b in range(m):
            if field[a][b] == 1:
                bfs(field, a, b)
                cnt += 1
    print(cnt)