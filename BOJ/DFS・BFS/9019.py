# 9019 : DSLR

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    graph = [0 for _ in range(10000)]
    q = deque()

    def bfs(a, b):
        q.append((a, ''))
        graph[a] = 1
        while q:
            n, d = q.popleft()
            if n == b:
                return d

            if n*2 > 9999:
                D = n*2 % 10000
            else:
                D = n*2
            if graph[D] == 0:
                graph[D] = 1
                q.append((D, d+'D'))

            if n-1 < 0:
                S = 9999
            else:
                S = n-1
            if graph[S] == 0:
                graph[S] = 1
                q.append((S, d+'S'))

            int_to_str = str(n)
            l = len(int_to_str)
            if l != 4:
                for _ in range(4-l):
                    int_to_str = '0' + int_to_str
            L = int(int_to_str[1:]+int_to_str[:1])
            R = int(int_to_str[-1:]+int_to_str[:-1])

            if graph[L] == 0:
                graph[L] = 1
                q.append((L, d+'L'))

            if graph[R] == 0:
                graph[R] = 1
                q.append((R, d+'R'))

    ans = bfs(a, b)
    print(ans)