# Binary Search
# 6-2 부품 찾기
# 이진 탐색 이용 (1) - 재귀 함수 이용

import sys

def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


n = int(sys.stdin.readline().rstrip())
a = list(map(int, input().split()))
a.sort()
m = int(sys.stdin.readline().rstrip())
b = list(map(int, input().split()))

for i in b:
    result = binary_search(a, i, 0, n-1)
    if result == None:
        print("no", end = ' ')
    else:
        print("yes", end=' ')