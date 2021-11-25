# 9012 : 괄호

import sys

n = int(sys.stdin.readline())


for _ in range(n):
    stack = sys.stdin.readline()
    stack = stack.rstrip()
    test = []
    for i in stack:
        if i == '(':
            test.append(1)
            result = "NO"
        else:
            if test == []:
                result = "NO"
                break
            else:
                test.pop()
                result = "YES"

    if test != []:
        result = "NO"

    print(result)