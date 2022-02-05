# 17626 : Four Squares
# pypy3으로 통과, python은 시간초과

import math
import sys
n = int(sys.stdin.readline())
d = [0,1] + [int(1e9)] * (n-1)

for i in range(2, n+1):
    if i==int(math.sqrt(i))**2:
        d[i] = 1
    else:
        for j in range(1, int(math.sqrt(i))+1):
            d[i] = min(d[i], d[j*j] + d[i-j*j])

print(d[n])