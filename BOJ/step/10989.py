# 10989 : 수 정렬하기 3 (카운트 정렬)

import sys
n = int(sys.stdin.readline().rstrip())
count = [0] * 10001

for i in range(n):
    count[int(sys.stdin.readline())] += 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            sys.stdout.write(str(i)+'\n')