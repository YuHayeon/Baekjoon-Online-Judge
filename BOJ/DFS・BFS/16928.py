# 16928 : 뱀과 사다리 게임

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [0 for _ in range(101)]
visited = [0 for _ in range(101)]

for _ in range(n):
    a, b = map(int, input().split())
    graph[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    graph[a] = b

q = deque()


def bfs(x):
    q.append(x)
    visited[x] = 1
    while q:
        x = q.popleft()
        if x == 100:
            break
        for i in range(1, 7):
            nx = x+i
            if nx > 100:
                continue
            if visited[nx] == 0 and graph[nx] == 0:
                q.append(nx)
                visited[nx] = visited[x]+1
            elif visited[nx] == 0 and graph[nx] != 0:
                q.append(graph[nx])
                visited[nx] = visited[x]+1
                if visited[graph[nx]]==0:
                    visited[graph[nx]] = visited[x]+1


bfs(1)
result = visited[100]-1
print(result)
