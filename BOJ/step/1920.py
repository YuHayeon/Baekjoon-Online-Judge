# 1920 : 수 찾기

import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().split()))
a.sort()

def binary(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return target
        elif array[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return None

for i in range(m):
    if binary(a, b[i], 0, n-1) == None:
        print("0")
    else:
        print("1")