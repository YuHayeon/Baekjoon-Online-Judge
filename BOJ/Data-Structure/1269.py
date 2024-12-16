# 1269 : 대칭 차집합

import sys

a_num, b_num = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

c = set(a + b)
answer = a_num + b_num - (2 * (a_num + b_num - len(c)))

print(answer)
