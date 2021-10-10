# 1904 : 01타일

import sys

n = int(sys.stdin.readline())
d = [0 for _ in range(n+1)]

a, b = 1, 2

for i in range(3, n+1):
    a, b = b, (a+b)%15746

if n==1:
    b = 1

print(b)
