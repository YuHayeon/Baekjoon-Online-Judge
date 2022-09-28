# 14501 : 퇴사

import sys
input = sys.stdin.readline

n = int(input())
tasks = [list(map(int, input().split())) for _ in range(n)]
d = [0] * 17

for i in range(n-1, -1, -1):
    finish_index = i+tasks[i][0]
    if finish_index < n+1:
        d[i] = max(d[finish_index]+tasks[i][1], d[i+1])
    else:
        d[i] = max(d[i+1], d[i])

print(d[0])
