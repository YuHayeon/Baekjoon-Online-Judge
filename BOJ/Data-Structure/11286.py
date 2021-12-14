# 11286 : 절댓값 힙

import sys
import heapq

n = int(sys.stdin.readline())
q = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x==0:
        if q:
            pop1, pop2 = heapq.heappop(q)
            print(pop2)
        else:
            print(0)
    else:
        heapq.heappush(q,(abs(x),x))