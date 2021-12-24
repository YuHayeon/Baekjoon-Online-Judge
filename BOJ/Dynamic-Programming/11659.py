# 11659 : 구간 합 구하기 4

import sys
n, m = map(int, sys.stdin.readline().split())
list = [0] + list(map(int, sys.stdin.readline().split()))
for i in range(1, n+1):
    list[i] += list[i-1]

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    ans = int(list[end]-list[start-1])
    print(ans)

#전체 합을 미리 구한다음에 구해야 시간 초과 안남.