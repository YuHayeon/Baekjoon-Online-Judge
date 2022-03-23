# 1655 : 가운데를 말해요

import sys
import heapq
input = sys.stdin.readline

N = int(input())
leftheap, rightheap = [], []

num = int(input())
heapq.heappush(leftheap, -num)
print(-leftheap[0])

if N > 1:
    num = int(input())
    if num < -leftheap[0]:
        heapq.heappush(rightheap, -heapq.heappop(leftheap))
        heapq.heappush(leftheap, -num)
    else:
        heapq.heappush(rightheap, num)
    print(-leftheap[0])

for i in range(N-2):
    num = int(input())
    left_len, right_len = len(leftheap), len(rightheap)
    if num > rightheap[0]:
        heapq.heappush(rightheap, num)
        if len(leftheap) < len(rightheap):
            heapq.heappush(leftheap, -heapq.heappop(rightheap))

    elif num <= rightheap[0]:
        heapq.heappush(leftheap, -num)
        if right_len < left_len:
            heapq.heappush(rightheap, -heapq.heappop(leftheap))

    print(-leftheap[0])