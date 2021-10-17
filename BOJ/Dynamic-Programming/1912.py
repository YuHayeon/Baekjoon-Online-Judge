# 1912 : 연속합

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [0 for i in range(n)]

d[0] = a[0]

for i in range(n):
    d[i] = max(d[i-1]+a[i], a[i])

print(max(d))