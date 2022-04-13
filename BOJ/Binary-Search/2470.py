# 2470 : 두 용액

import sys
input = sys.stdin.readline

N = int(input())
sol = list(map(int, input().split()))

sol.sort()
result = 2*int(1e9)+1

for i in range(N-1):
    start, end = i+1, N-1

    while start <= end:
        mid = (start+end) // 2
        temp = sol[i]+sol[mid]

        if abs(temp) < result:
            result = abs(temp)
            sol1, sol2 = i, mid

        if temp < 0:
            start = mid+1

        else:
            end = mid-1

print(sol[sol1], sol[sol2])