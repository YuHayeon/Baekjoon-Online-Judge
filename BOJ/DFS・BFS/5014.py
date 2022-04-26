# 5014 : 스타트링크

import sys
from collections import deque


def bfs(F, S, G, U, D):
    visited = [False for _ in range(F+1)]
    q = deque()
    q.append((S, 0))
    visited[S] = True

    while q:
        now, button = q.popleft()
        if now == G:
            return button

        up, down = now+U, now-D

        if up <= F and not visited[up]:
            q.append((up, button+1))
            visited[up] = True
        if down > 0 and not visited[down]:
            q.append((down, button+1))
            visited[down] = True

    return "use the stairs"


# F:전체 층 수, S:현재 층, G:목적 층
# U:위로 갈 수 있는 층 수, D:아래로 갈 수 있는 충 수
F, S, G, U, D = map(int, sys.stdin.readline().split())

print(bfs(F, S, G, U, D))