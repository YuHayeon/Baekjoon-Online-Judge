# 1654 : 랜선 자르기

import sys

def cutLan(mid):
    sum = 0
    for i in a:
        sum += i // mid
        if sum > n:
            break
    return sum

k, n = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(k)]

start = 1
end = 2147483647
ans = 0

while start <= end:
    mid = (start+end)//2
    result = cutLan(mid)

    if result == n:
        ans = mid
        break
    elif result > n:
        ans = mid
        start = mid+1
    else:
        end = mid-1

print(ans)