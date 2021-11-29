# 2178 : 미로 탐색

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
ans = 0


def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 1+graph[x][y]


bfs(graph, 0, 0)
ans = graph[n-1][m-1]
print(ans)
