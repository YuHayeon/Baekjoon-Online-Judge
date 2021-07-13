# 14-23 : 국영수
# BOJ 10825번 : 국영수

import sys

n = int(sys.stdin.readline().rstrip())
stu = [list(sys.stdin.readline().split()) for i in range(n)]

stu.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    sys.stdout.write(stu[i][0]+'\n')