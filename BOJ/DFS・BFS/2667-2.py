# 2667-1 : 단지번호붙이기 - DFS

import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

home = []
complex = 0


def bfs(graph, x, y):
    cnt = 1
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1
    return cnt


for a in range(n):
    for b in range(n):
        if graph[a][b] == 1:
            home.append(bfs(graph, a, b))
            complex += 1

home.sort()

print(complex)
for h in home:
    print(h)