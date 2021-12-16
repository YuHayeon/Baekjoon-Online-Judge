# 7568 : 덩치

import sys

n = int(sys.stdin.readline())
size = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
rank = [1] * n

for i in range(n):
    for j in range(n):
        if size[i][0] < size[j][0] and size[i][1] < size[j][1]:
            rank[i] += 1

for r in rank:
    print(r, end=' ')