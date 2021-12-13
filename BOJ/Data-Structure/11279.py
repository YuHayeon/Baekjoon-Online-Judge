# 11279 : 최대 힙

import sys
import heapq

n = int(sys.stdin.readline())
q = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if q == []:
            print(0)
        else:
            pop1, pop2 = heapq.heappop(q)
            print(pop2)
    else:
        # 최대힙을 만들어줘야 되기 때문에 우선순위의 부호를 바꿔서 저장
        heapq.heappush(q, (-x, x))
