# Binary Search
# 6-2 부품 찾기

import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, input().split()))
m = int(sys.stdin.readline().rstrip())
b = list(map(int, input().split()))

def search(n,a,num):
    for j in range(n):
        if num == a[j]:
            return True
            break
    return False

for i in b:
    if search(n,a,i) == True:
        print('yes', end=' ')
    else: print('no', end=' ')