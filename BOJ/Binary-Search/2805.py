# 2805 : 나무 자르기

import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(a)
ans = 0

def sumWood(mid):
    sum = 0
    for i in a:
        if i-mid > 0:
            sum += i-mid
    return sum

while start <= end:
    mid = (start+end) //2
    result = sumWood(mid)

    if result >= m:
        ans = mid
        start = mid+1
    else:
        end = mid-1

print(ans)