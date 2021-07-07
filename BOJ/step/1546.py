# 1546 : 평균

import sys

n = int(sys.stdin.readline().rstrip())
score = list(map(int, sys.stdin.readline().split()))
m = max(score)

for i in range(n):
    score[i] = score[i] / m * 100

result = sum(score)/n
print(result)