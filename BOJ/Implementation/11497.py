# 11497 : 통나무 건너뛰기

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    height_list = list(map(int, input().split()))
    height_list.sort()

    max_height = height_list.pop()

    left_height = max_height
    left_max_diff = 0
    right_height = max_height
    right_max_diff = 0

    for _ in range((n-1)//2):
        height = height_list.pop()
        right_max_diff = max(right_max_diff, right_height - height)
        right_height = height

        height = height_list.pop()
        left_max_diff = max(left_max_diff, left_height - height)
        left_height = height

    if height_list:
        height = height_list.pop()
        right_max_diff = max(right_max_diff, right_height - height)
        right_height = height

    result = max(right_max_diff, left_max_diff)
    result = max(result, right_height-left_height)

    print(result)
