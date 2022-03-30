# 3020 : 개똥벌레

from cmath import inf
import sys
input = sys.stdin.readline

N, H = map(int, input().split())

up, down = [], []
for i in range(N):
    if i % 2 == 0:
        down.append(int(input()))
    else:
        up.append(int(input()))

down.sort()
up.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if array[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return start


min_cnt = int(1e9)
block_cnt = 0

for i in range(H):
    down_cnt = len(down)-binary_search(down, i+0.5, 0, len(down)-1)
    up_cnt = len(up)-binary_search(up, H-i+0.5-1, 0, len(up)-1)

    result = down_cnt+up_cnt
    if result < min_cnt:
        min_cnt = result
        block_cnt = 1
    elif result == min_cnt:
        block_cnt += 1

print(min_cnt, block_cnt)