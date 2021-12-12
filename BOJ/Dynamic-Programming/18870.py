# 18870 : 좌표 압축

import sys

n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
set_list = sorted(set(list))
dict ={}

for i in range(len(set_list)):
    dict[set_list[i]] = i


for n in list:
    print(dict[n], end=' ')