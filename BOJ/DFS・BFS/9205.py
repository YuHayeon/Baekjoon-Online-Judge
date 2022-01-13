# 9205 : 맥주 마시면서 걸어가기

import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    graph = []
    x1, y1 = map(int, input().split())

    for _ in range(n):
        x, y = map(int, input().split())
        graph.append((x, y))
    x2, y2 = map(int, input().split())
    graph.append((x2, y2))

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited = [False for _ in range(n+1)]
        while q:
            x, y = q.popleft()
            if x == x2 and y == y2:
                print("happy")
                return
            for i in range(n+1):
                nx, ny = graph[i][0], graph[i][1]
                if not visited[i]:
                    if abs(x-nx) + abs(y-ny) <= 1000:
                        q.append((nx, ny))
                        visited[i] = True
        print('sad')
        return

    bfs(x1, y1)