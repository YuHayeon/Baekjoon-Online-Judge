# 1697 : 숨바꼭질

import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
l = 100001
graph = [0]*l
ans = 0


def bfs():
    queue = deque()
    graph[n] = 1
    queue.append(n)

    while queue:
        x = queue.popleft()

        for i in (x+1, x-1, x*2):
            if i < 0 or i >= l:
                continue
            if graph[i] == 0:
                queue.append(i)
                graph[i] = 1+graph[x]


bfs()
ans = graph[k]-1
print(ans)