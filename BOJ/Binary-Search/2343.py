# 2343 : 기타 레슨

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lesson = list(map(int, input().split()))
start = sum(lesson) // m
end = sum(lesson)
result = end

while start <= end:
    mid = (start+end) // 2

    if mid < max(lesson):
        start = mid+1
        continue

    temp = 0
    count = 0

    for i in range(n):
        if lesson[i] > mid:
            break
        if temp + lesson[i] <= mid:
            temp += lesson[i]
        else:
            temp = lesson[i]
            count += 1

    if count <= m-1:
        end = mid-1
        result = min(result, mid)
    else:
        start = mid+1

print(result)