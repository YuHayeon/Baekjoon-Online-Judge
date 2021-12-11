# 1697 : 숨바꼭질 - 스터디

import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
end = 100000
visited = [0] * (end+1)

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        x = q.popleft()
        if x == k:
            break
        for i in (x+1, x-1, x*2):
            if i<0 or i>end:
                continue
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[x] + 1
bfs(n)
print(visited[k])