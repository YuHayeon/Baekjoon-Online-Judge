# 14503 : 로봇 청소기

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
x, y, d = map(int, input().split())
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
graph = [list(map(int, input().split())) for _ in range(N)]


def bfs(x, y, d):
    q = deque()
    graph[x][y] = 2
    q.append((x, y, d))
    cnt = 1

    while q:
        x, y, d = q.popleft()
        nd = d

        for i in range(d*(-1), d*(-1)+4):
            nx = direction[i][0]+x
            ny = direction[i][1]+y
            nd = nd-1 if 0 <= nd-1 < 4 else nd+3

            if i == d*(-1)+3 and 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 0:
                nx = direction[d*(-1)+1][0]+x
                ny = direction[d*(-1)+1][1]+y
                if graph[nx][ny] == 1:
                    return cnt
                else:
                    q.append((nx, ny, nd))
                    break

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                q.append((nx, ny, nd))
                graph[nx][ny] = 2
                cnt += 1
                break

    return cnt


result = bfs(x, y, d)
print(result)