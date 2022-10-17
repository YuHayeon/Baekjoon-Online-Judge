# 2156 : 포도주 시식

import sys
input = sys.stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]

if n == 1:
    answer = wines[0]
elif n == 2:
    answer = wines[0]+wines[1]
else:
    d = [0] * n
    d[0] = wines[0]
    d[1] = wines[0]+wines[1]
    d[2] = max(wines[0]+wines[2], wines[1]+wines[2], d[1])

    for i in range(3, n):
        d[i] = max(d[i-1], wines[i-1]+d[i-3]+wines[i], d[i-2]+wines[i])
    answer = d[n-1]

print(answer)
