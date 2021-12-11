# 11399 : ATM

import sys

n = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))
d.sort()

for i in range(1, n):
    d[i] = d[i]+d[i-1]

ans = sum(d)
print(ans)