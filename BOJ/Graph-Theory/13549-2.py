# 13549 : 숨바꼭질 3 - BFS

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
graph = [int(1e9) for _ in range(100001)]


def bfs(n):
    q = deque()
    q.append(n)
    graph[n] = 0
    while q:
        now = q.popleft()
        if now == k:
            break
        for x in (2*now, now-1, now+1):
            if 0 <= x < 100001 and graph[x] == int(1e9):
                if x == 2*now:
                    graph[x] = min(graph[x], graph[now])
                else:
                    graph[x] = min(graph[x], graph[now]+1)
                q.append(x)


if k <= n:
    print(n-k)
else:
    bfs(n)
    print(graph[k])