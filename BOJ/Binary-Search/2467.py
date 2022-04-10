# 2467 : 용액

import sys
input = sys.stdin.readline

N = int(input())
solution = list(map(int, input().split()))
result = abs(solution[0] + solution[-1])
left, right = 0, N-1
ans1, ans2 = 0, N-1

while left < right:
    if abs(solution[left]+solution[right]) < result:
        result = abs(solution[left]+solution[right])
        ans1, ans2 = left, right

    if solution[left] + solution[right] > 0:
        right -= 1
    else:
        left += 1

print(solution[ans1], solution[ans2])