# 11650 : 좌표 정렬하기

import sys
n = int(sys.stdin.readline().rstrip())
l = [tuple(map(int, sys.stdin.readline().split())) for i in range(n)]
l.sort()
for i in range(n):
    sys.stdout.write(str(l[i][0])+' '+str(l[i][1])+'\n')