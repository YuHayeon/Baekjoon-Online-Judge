#11053 : 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
d = [1 for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        if num[i] < num[j]:
            d[j] = max(d[j], d[i]+1)
            
print(max(d))