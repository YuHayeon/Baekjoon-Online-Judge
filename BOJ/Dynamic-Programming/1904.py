# 1904 : 01타일

import sys

n = int(sys.stdin.readline())
d = [0 for _ in range(n+1)]

d[1] = 1
if n > 1:
    d[2] = 2

for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]) % 15746

print(d[n])