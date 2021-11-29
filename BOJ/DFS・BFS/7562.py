# 7562 : 나이트의 이동

import sys
from collections import deque

t = int(sys.stdin.readline())

dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, -2, 2, 1, -1, 1, -1]

for _ in range(t):

    l = int(sys.stdin.readline())
    graph = [[0]*(l) for _ in range(l)]
    ans = 0

    queue = deque()

    a1, b1 = map(int, sys.stdin.readline().split())
    a2, b2 = map(int, sys.stdin.readline().split())

    def bfs(x, y):
        graph[a1][b1] = 1
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]

                if nx < 0 or ny < 0 or nx >= l or ny >= l:
                    continue
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
                if nx == a2 and ny == b2:
                    return

    bfs(a1, b1)
    ans = graph[a2][b2]-1
    print(ans)
