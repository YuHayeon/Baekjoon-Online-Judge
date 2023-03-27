#2303 : 숫자 게임

import sys
input = sys.stdin.readline

n = int(input())
results = []

for _ in range(n):
    nums = list(map(int, input().split()))
    result = 0

    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                result = max(result, (nums[i] + nums[j] + nums[k])%10)
    results.append(result)

max_num = 0
max_idx = 1
for i in range(n):
    if max_num <= results[i]:
        max_num = results[i]
        max_idx = i+1

print(max_idx)
