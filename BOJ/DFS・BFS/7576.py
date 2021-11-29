# 7576 : 토마토

import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque()

ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

print(queue)


def bfs():
    while queue:
        x, y = queue.popleft()
        print(graph)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 1 + graph[x][y]


bfs()
for i in range(n):
    for j in range(m):
        ans = max(graph[i][j], ans)
        if graph[i][j] == 0:
            print(-1)
            exit(0)
ans = ans-1
print(ans)