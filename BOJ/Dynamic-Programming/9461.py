# 9461 - 파도반 수열

import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
p = [0,1,1,1,2,2] + [0 for _ in range(max(a)-5)]

for i in range(6, max(a)+1):
    p[i] = p[i-5] + p[i-1]

for j in a:
    print(p[j])