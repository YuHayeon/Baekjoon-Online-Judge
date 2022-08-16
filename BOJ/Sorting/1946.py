# 1946 : 신입 사원

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    record_list = []

    for _ in range(n):
        record1, record2 = map(int, input().split())
        record_list.append([record1, record2])

    record_list.sort()

    result = 1
    min_record = record_list[0][1]
    for i in range(1, n):
        if min_record > record_list[i][1]:
            min_record = record_list[i][1]
            result += 1

    print(result)
