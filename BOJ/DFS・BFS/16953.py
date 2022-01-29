import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())


def bfs(a):
    q = deque()
    q.append((a, 1))
    while q:
        x, now = q.popleft()
        if x == B:
            return now
        if x < B:
            q.append((x*2, now+1))
            q.append((int(str(x)+'1'), now+1))
    return -1


print(bfs(A))
