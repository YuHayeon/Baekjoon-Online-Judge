# 2638 : 치즈

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
result = 0


def bfs(x, y):
    visited = [[1 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+d[i][0]
            ny = y+d[i][1]

            if 0 <= nx < N and 0 <= ny < M:
                if cheese[nx][ny] == 0 and visited[nx][ny] == 1:
                    visited[nx][ny] = 0
                    q.append((nx, ny))
    return visited


while sum(map(sum, cheese)) != 0:

    visited = bfs(0, 0)

    for i in range(N):
        for j in range(M):
            cnt = 0
            if visited[i][j] == 1:
                for k in range(4):
                    nx = i+d[k][0]
                    ny = j+d[k][1]
                    if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                        cnt += 1
            if cnt >= 2:
                cheese[i][j] = 0
    result += 1

print(result)