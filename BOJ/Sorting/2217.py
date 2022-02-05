# 2217 : 로프

import sys
input = sys.stdin.readline

N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)
result = 0

for i in range(1, N+1):
    result = max(result, rope[i-1] * i)

print(result)

