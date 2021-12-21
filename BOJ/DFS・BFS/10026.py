# 10026 : 적록색약

import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = deque()

normal = 0
weakness = 0


def bfs(x, y):
    visited[x][y] = 1
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = d[i][0]+x
            ny = d[i][1]+y
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            if visited[nx][ny] == 0 and graph[x][y] == graph[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            normal += 1

# 적록색약은 R과 G를 구분하지 못하므로 G를 R로 변경
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
# 방문 체크하는 배열 초기화
visited = [[0 for _ in range(n)] for _ in range(n)]

# 적록색약일때 bfs 수행. visited가 0일때마다 1씩 증가
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            weakness += 1

print(normal, weakness)
