# 7662 : 이중 우선순위 큐

import sys
import heapq
t = int(sys.stdin.readline())
visited = [0] * 1000000

for _ in range(t):

    n = int(sys.stdin.readline())
    min_q = []
    max_q = []
    visited = [0]*10000001
    for i in range(n):
        op, num = sys.stdin.readline().split()

        if op == 'I':
            heapq.heappush(min_q, (int(num), i))
            heapq.heappush(max_q, (-int(num), i))
            visited[i] = 1
        else:
            if int(num) == -1:
                
                # min_q를 동기화 시키기
                while min_q and visited[min_q[0][1]] == 0:
                    heapq.heappop(min_q)

                if min_q:
                    visited[min_q[0][1]] = 0
                    heapq.heappop(min_q)

            elif int(num) == 1:

                # max_q를 동기화 시키기
                while max_q and visited[max_q[0][1]] == 0:
                    heapq.heappop(max_q)

                if max_q:
                    visited[max_q[0][1]] = 0
                    heapq.heappop(max_q)

    while max_q and visited[max_q[0][1]] == 0:
        heapq.heappop(max_q)
    while min_q and visited[min_q[0][1]] == 0:
        heapq.heappop(min_q)

    if min_q == []:
        print("EMPTY")
    else:
        print(-max_q[0][0], min_q[0][0])
