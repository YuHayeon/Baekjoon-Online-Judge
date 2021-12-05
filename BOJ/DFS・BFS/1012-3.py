# 1012-3 : 유기농 배추 - 스터디. DFS

import sys
sys.setrecursionlimit(5000)
t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0]*n for _ in range(m)]
    stack = []

    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1


    def dfs(x, y):
        graph[x][y] = 0

        for i in range(4):
            nx = x+d[i][0]
            ny = y+d[i][1]
            if nx >= 0 and ny >= 0 and nx < m and ny < n and graph[nx][ny] == 1:
                dfs(nx, ny)


    cnt = 0
    for a in range(m):
        for b in range(n):
            if graph[a][b] == 1:
                dfs(a, b)
                cnt += 1
    print(cnt)
