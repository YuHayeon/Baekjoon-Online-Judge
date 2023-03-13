# 2167 : 2차원 배열의 합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    nums[i] = [0] + list(map(int, input().split()))
    for j in range(1, m+1):
        nums[i][j] += nums[i][j-1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    answer = 0
    for a in range(i, x+1):
        answer += nums[a][y] - nums[a][j-1]
    print(answer)