# 2156 : 포도주 시식

import sys
n = int(sys.stdin.readline())
a=[]
for i in range(n):
    a.append(int(sys.stdin.readline()))
d=[0 for i in range(n)]

d[0] = a[0]
if n>1:
    d[1] = a[0]+a[1]
if n>2:
    d[2] = max(a[0]+a[1], a[0]+a[2], a[1]+a[2])

for i in range(3,n):
    d[i] = max(d[i-3]+a[i-1]+a[i], d[i-2]+a[i], d[i-1])

print(d[n-1])