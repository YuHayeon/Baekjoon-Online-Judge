# 16-33 : 퇴사

import sys
n = int(sys.stdin.readline().rstrip())
plan = [tuple(map(int, sys.stdin.readline().split())) for i in range((n))]
d = [0] * 17

for i in range(n):
    for j in range(i+1):
        if plan[i][0] + i > n:
            break
        elif plan[j][0] + j <= i :
            d[i] = max(d[i], d[j] + plan[i][1])
        else:
            d[i] = max(d[i], plan[i][1])

print(d)