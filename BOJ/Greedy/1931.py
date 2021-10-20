# 1931 : 회의실 배정

import sys

n = int(sys.stdin.readline())
time = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
time = sorted(time, key = lambda x : (x[1], x[0]))

pre = time[0]
cnt = 1

for i in range(1,n):
    if pre[1] <= time[i][0]:
        pre = time[i]
        cnt += 1

print(cnt)