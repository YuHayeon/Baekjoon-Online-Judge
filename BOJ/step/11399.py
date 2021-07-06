# 11399 : ATM

import sys

n = int(sys.stdin.readline().rstrip())
time = list(map(int, sys.stdin.readline().split()))

time = sorted(time)

sum = 0
for i in range(0, n+1):
    for t in range(i):
        sum += time[t]

print(sum)