# 1021 : 회전하는 큐

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
want_num = deque(list(map(int, input().split())))
q = deque([i for i in range(1, N+1)])
result = 0


for n in want_num:
    while True:
        if q[0] == n:
            q.popleft()
            break

        if q.index(n) <= len(q)//2:
            while q[0] != n:
                q.append(q.popleft())
                result += 1
        else:
            while q[0] != n:
                q.appendleft(q.pop())
                result += 1


print(result)