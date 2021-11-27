# 2667-1 : 단지번호붙이기 - DFS

import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

home = []
complex = 0


def dfs(graph, x, y):
    graph[x][y] = 0
    cnt = 1

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == 1:
            cnt += dfs(graph, nx, ny)

    return cnt


for a in range(n):
    for b in range(n):
        if graph[a][b] == 1:
            home.append(dfs(graph, a, b))
            complex += 1
home.sort()

print(complex)
for h in home:
    print(h)