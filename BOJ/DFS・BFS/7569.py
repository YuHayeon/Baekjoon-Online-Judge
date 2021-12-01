# 7569 : 토마토

import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
ans = 0

# 토마토 그래프 생성
graph = []
for _ in range(h):
    graph.append([list(map(int, sys.stdin.readline().split()))
                 for _ in range(n)])
q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k))


def bfs():
    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]

            if nx < 0 or ny < 0 or nz < 0 or nx >= h or ny >= n or nz >= m:
                continue
            if graph[nx][ny][nz] == 0:
                q.append((nx, ny, nz))
                graph[nx][ny][nz] = 1+graph[x][y][z]


bfs()

for i in graph:
    for j in i:
        for k in j:
            ans = max(ans, k)
            if k == 0:
                print(-1)
                exit(0)

ans = ans-1
print(ans)
