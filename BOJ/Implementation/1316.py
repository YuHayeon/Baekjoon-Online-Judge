# 1316 : 그룹 단어 체커

import sys
input = sys.stdin.readline
N = int(input())


def group(s):
    check = set()
    pre = None
    for i in s:
        if pre != i and i not in check:
            check.add(i)
            pre = i
        elif pre == i:
            continue
        else:
            return False
    return True


result = 0

for _ in range(N):
    s = input().strip()
    if group(s):
        result += 1

print(result)