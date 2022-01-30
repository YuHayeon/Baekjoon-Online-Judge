# 2304 : 창고 다각형

import sys
input = sys.stdin.readline

N = int(input())
rod = []
result = 0
max_h = 0

for _ in range(N):
    n, h = map(int, input().split())
    max_h = max(max_h, h)
    rod.append((n, h))

rod.sort()

now_n, now_h = 0, 0

for i in range(N):
    n, h = rod[i][0], rod[i][1]
    if now_h <= h:
        result += (n-now_n) * now_h
        now_n, now_h = n, h
    if h == max_h:
        v1 = now_n
        break

now_n, now_h = 0, 0

for i in range(N-1, -1, -1):
    n, h = rod[i][0], rod[i][1]
    if now_h <= h:
        result += (now_n-n) * now_h
        now_n, now_h = n, h
    if h == max_h:
        v2 = now_n+1
        break

result += (v2-v1) * max_h

print(result)