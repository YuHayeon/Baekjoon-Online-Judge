# 1697 : 숨바꼭질

from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())


def bfs(n, k):
    q = deque()
    visited = [False] * 100001
    q.append((n, 0))
    visited[n] = True

    while q:
        v, count = q.popleft()
        if v == k:
            return count

        for nv in (v*2, v+1, v-1):
            if nv < 0 or nv > 100000:
                continue
            if not visited[nv]:
                q.append((nv, count+1))
                visited[nv] = True


print(bfs(n, k))
