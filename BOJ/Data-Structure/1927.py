# 1927 : 최소 힙

import heapq
import sys

n = int(sys.stdin.readline())
q=[]
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if q==[]:
            print(0)
        else:
            pop = heapq.heappop(q)
            print(pop)
    else:
        heapq.heappush(q, x)