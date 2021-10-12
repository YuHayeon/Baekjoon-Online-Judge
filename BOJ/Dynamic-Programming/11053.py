#11053 : 가장 긴 증가하는 부분 수열

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [1 for _ in range(n)]

for i in range(n):
    for j in range(0, i):
        if a[j] < a[i]:
            d[i] = max(d[i], d[j]+1)

print(max(d))