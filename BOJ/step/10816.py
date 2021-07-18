# 10816 : 숫자 카드 2

import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dic = {i : 0 for i in a}

for c in card:
    if c in dic.keys():
        dic[c] += 1

for i in range(m):
    if a[i] in dic.keys():
        print(dic[a[i]], end=' ')