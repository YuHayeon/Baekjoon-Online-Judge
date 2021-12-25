# 1302 : 베스트셀러

import sys
input = sys.stdin.readline

n = int(input())
dict = {}

for _ in range(n):
    book = input().rstrip()
    if book in dict:
        dict[book] += 1
    else:
        dict[book] = 1

sorted_dict = sorted(dict.items(), key=lambda item: (-item[1],item[0]))
result = sorted_dict[0][0]
print(result)
