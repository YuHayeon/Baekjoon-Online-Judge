# 11052 : 카드 구매하기

import sys
input = sys.stdin.readline

N = int(input())
card = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(i, N+1):
        if i+j < N+1:
            card[i+j] = max(card[i+j], card[i]+card[j])

print(card[N])