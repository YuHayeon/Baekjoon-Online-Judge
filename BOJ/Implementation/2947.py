# 2947 : 나무 조각

import sys
num = list(map(int, sys.stdin.readline().split()))
i = 1

while True:

    if num[i-1] > num[i]:
        num[i-1], num[i] = num[i], num[i-1]
        print(*num)

    if num == [1, 2, 3, 4, 5]:
        break

    if i == 4:
        i = 1
    else:
        i += 1
