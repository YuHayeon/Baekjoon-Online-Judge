# 1966 : 프린터 큐

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    q = deque(list(map(int, input().split())))
    order = 1
    
    while True:
        if q[0] != max(q):
            v = q.popleft()
            q.append(v)
            if n==0:
                n = len(q)-1
            else:
                n -= 1

        else:
            q.popleft()
            if n == 0:
                break
            else:
                order+=1
                n -= 1
    print(order)