# 11651 : 좌표 정렬하기 2

import sys
n = int(sys.stdin.readline().rstrip())
l = [tuple(map(int, sys.stdin.readline().split())) for i in range(n)]
l.sort(key = lambda x : (x[1],x[0]))
for i in range(n):
    sys.stdout.write(str(l[i][0])+' '+str(l[i][1])+'\n')