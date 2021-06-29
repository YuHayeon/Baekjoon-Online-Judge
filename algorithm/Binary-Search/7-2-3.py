# Binary Search
# 6-2 부품 찾기
# 이진 탐색 이용 (2) - 반복문 이용

import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(sys.stdin.readline().rstrip())
a = list(map(int, input().split()))
a.sort()
m = int(sys.stdin.readline().rstrip())
b = list(map(int, input().split()))

for i in b:
    result = binary_search(a, i, 0, n)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end= ' ')
