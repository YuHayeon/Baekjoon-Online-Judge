# 2573 : 빙산

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
answer = 0


def bfs(x, y):

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx = x+dx
            ny = y+dy

            if 0 <= nx < N and 0 <= ny < M:
                if iceberg[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))


while True:
    visited = [[False for _ in range(M)] for _ in range(N)]

    ice = 0
    zero_cnt = 0
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] > 0 and not visited[i][j]:
                bfs(i, j)
                ice += 1
            else:
                zero_cnt += 1

    if ice > 1:
        break

    if zero_cnt == N*M:
        answer = 0
        break

    for i in range(N):
        for j in range(M):
            cnt = 0
            if visited[i][j]:
                for dx, dy in d:
                    nx = i+dx
                    ny = j+dy
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        cnt += 1
                result = iceberg[i][j] - cnt
                if result <= 0:
                    iceberg[i][j] = 0
                else:
                    iceberg[i][j] = result

    answer += 1


print(answer)