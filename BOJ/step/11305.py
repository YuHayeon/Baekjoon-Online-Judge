# 11305 : 주유소

import sys

n = int(sys.stdin.readline().rstrip())
l = list(map(int, sys.stdin.readline().split()))
p = list(map(int, sys.stdin.readline().split()))

i = 0
result = 0
while True:
    if i >= n-1:
        break
    if i == n-2:
        result += p[i]*l[i]
        break
    if p[i]*(l[i]+l[i+1]) >= (p[i]*l[i])+(p[i+1]*l[i+1]):
        result += p[i]*l[i]
        i += 1
    else:
        result += p[i]*(l[i]+l[i+1])
        i += 2

print(result)