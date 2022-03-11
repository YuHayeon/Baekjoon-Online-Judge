# 2468 : 안전 영역

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

height = set(sum(graph, []))
result = 1


def bfs(x, y, rain):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx = x+dx
            ny = y+dy

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] > rain and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


for h in height:
    cnt = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] > h and not visited[i][j]:
                bfs(i, j, h)
                cnt += 1
    result = max(result, cnt)

print(result)