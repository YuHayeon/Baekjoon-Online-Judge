# 1715 : 카드 정렬하기

import sys
import heapq
input = sys.stdin.readline

N = int(input())
card = []
result = 0

for _ in range(N):
    card.append(int(input()))

heapq.heapify(card)

while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    result += (a+b)
    heapq.heappush(card, a+b)

print(result)